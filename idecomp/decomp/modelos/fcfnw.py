# Imports do próprio módulo

# Imports de módulos externos
from cfinterface.components.block import Block
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.floatfield import FloatField
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from typing import IO


class BlocoCortesFCF(Block):
    """
    Bloco com as informações da função de custo futuro utilizada
    no acoplamento.
    """

    __slots__ = []

    BEGIN_PATTERN = "Restricao     RHS"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoCortesFCF):
            return False
        bloco: BlocoCortesFCF = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

    # Override
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            if ree:
                colunas = ["corte", "RHS", "REE", "coef_earm"] + [
                    f"coef_eafl_{i}" for i in range(1, num_elementos_afl + 1)
                ]
                if gnl:
                    colunas += [
                        f"coef_GNL_pat{p}_lag{la}"
                        for p in range(1, n_patamares + 1)
                        for la in [1, 2]
                    ]
                if vminop_max:
                    colunas += ["coef_vminop_max"]
                tipos = {
                    "corte": np.int64,
                    "REE": np.int64,
                }
            else:
                colunas = ["corte", "RHS", "UHE", "coef_varm"] + [
                    f"coef_afl_{i}" for i in range(1, num_elementos_afl + 1)
                ]
                tipos = {
                    "corte": np.int64,
                    "UHE": np.int64,
                }
            df = pd.DataFrame(tabela, columns=colunas)
            df = df.astype(tipos)
            return df

        linha_inicial = file.readline()
        ree = "REE" in linha_inicial
        uhe = "Usi" in linha_inicial
        gnl = "Pat" in linha_inicial
        n_patamares = linha_inicial.count("Pat") if gnl else 0
        vminop_max = "Coef.Vminop-Max" in linha_inicial

        # Salta 2 linhas
        for _ in range(2):
            file.readline()

        # Lê a primeira linha da tabelapara descobrir o número de termos
        pos = file.tell()
        primeira_linha = file.readline()
        file.seek(pos)
        num_elementos = (
            len([e for e in primeira_linha.split(" ") if len(e) > 0]) - 4
        )
        num_elementos_afl = (
            num_elementos - int(ree) - 6 * int(gnl) - int(vminop_max)
        )
        # Sempre considera 2 lags máximos GNL
        num_elementos_gnl = n_patamares * 2

        # Constroi a linha para leitura
        campos_linha = [
            IntegerField(9, 4),
            FloatField(11, 14, decimal_digits=1),
            IntegerField(6, 26),
            FloatField(20, 32, decimal_digits=10),
        ] + [
            FloatField(20, 53 + int(uhe) + 20 * i, decimal_digits=10)
            for i in range(num_elementos_afl)
        ]
        if gnl:
            col_inicial_gnl = 53 + 20 * num_elementos_afl + 1
            campos_linha += [
                FloatField(20, col_inicial_gnl + 20 * i, decimal_digits=10)
                for i in range(num_elementos_gnl)
            ]
        if vminop_max:
            col_inicial_vminop = 54 + 20 * (
                num_elementos_afl + num_elementos_gnl
            )
            campos_linha += [
                FloatField(23, col_inicial_vminop, decimal_digits=10)
            ]
        line = Line(campos_linha)

        # Faz a leitura
        corte_atual = 0
        rhs_atual = 0
        tabela = np.zeros((4950000, num_elementos + 3 + int(uhe)))
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if len(linha) < 5:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break

            dados = line.read(linha)
            corte_atual = dados[0] if not pd.isna(dados[0]) else corte_atual
            rhs_atual = dados[1] if not pd.isna(dados[1]) else rhs_atual
            tabela[i, 0] = corte_atual
            tabela[i, 1] = rhs_atual
            tabela[i, 2:] = dados[2:]
            i += 1
