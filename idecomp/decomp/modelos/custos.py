# Imports do próprio módulo

# Imports de módulos externos
from cfinterface.components.block import Block
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
import pandas as pd  # type: ignore
from typing import IO, List


class BlocoRelatorioCustos(Block):
    """ """

    __slots__ = [
        "__scenario_line",
        "__dual_variables_line",
        "__fcf_line",
        "dados_cenario",
        "data",
    ]

    BEGIN_PATTERN = r" RELATORIO DAS VARIAVEIS DUAIS NO ESTAGIO"
    END_PATTERN = "X----X-"

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__scenario_line = Line([IntegerField(2, 44), IntegerField(4, 54)])
        self.__dual_variables_line = Line(
            [
                LiteralField(14, 4),
                FloatField(15, 19, 2),
            ]
        )
        self.__fcf_line = Line(
            [
                IntegerField(4, 4),
                FloatField(12, 9, 3),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoRelatorioCustos):
            return False
        bloco: BlocoRelatorioCustos = o
        if not all(
            [
                isinstance(self.data, list),
                isinstance(bloco.data, list),
            ]
        ):
            return False
        else:
            return all(
                [
                    self.data[0].equals(bloco.data[0]),
                    self.data[1].equals(bloco.data[1]),
                ]
            )

    def __read_bloco_variaveis_duais(self, file: IO):
        def converte_tabela_para_df() -> pd.DataFrame:
            cols = [
                "usina",
                "pih",
            ]
            df = pd.DataFrame(data={"usina": usinas, "pih": pihs})
            cols_adic = [
                "estagio",
                "cenario",
            ]
            df["estagio"] = [estagio] * len(usinas)
            df["cenario"] = [cenario] * len(usinas)
            df = df[cols_adic + cols]
            return df

        estagio: int = self.dados_cenario[0]
        cenario: int = self.dados_cenario[1]

        # Salta 3 linhas
        for _ in range(3):
            file.readline()

        # Variáveis auxiliares
        usinas: List[str] = []
        pihs: List[float] = []
        while True:
            linha: str = file.readline()
            # Verifica se acabou
            if "X---------------X" in linha:
                self.data.append(converte_tabela_para_df())
                break
            dados = self.__dual_variables_line.read(linha)
            usinas.append(dados[0])
            pihs.append(dados[1])

    def __read_bloco_restricoes_fcf(self, file: IO):
        def converte_tabela_para_df() -> pd.DataFrame:
            cols = [
                "indice_corte",
                "parcela_pi",
            ]
            df = pd.DataFrame(
                data={"indice_corte": indices, "parcela_pi": pis}
            )
            cols_adic = [
                "estagio",
                "cenario",
            ]
            df["estagio"] = [estagio] * len(indices)
            df["cenario"] = [cenario] * len(indices)
            df = df[cols_adic + cols]
            return df

        estagio: int = self.dados_cenario[0]
        cenario: int = self.dados_cenario[1]

        # Salta 2 linhas
        for _ in range(2):
            file.readline()

        # Variáveis auxiliares
        indices: List[int] = []
        pis: List[float] = []
        while True:
            linha: str = file.readline()
            # Verifica se acabou
            if len(linha) < 3:
                self.data.append(converte_tabela_para_df())
                break
            dados = self.__fcf_line.read(linha)
            indices.append(dados[0])
            pis.append(dados[1])

    # Override
    def read(self, file: IO, *args, **kwargs):
        str_bloco_variaveis_duais = "Aproveitamento  Bal.Hidr."
        str_bloco_restricoes_fcf = "Restricoes da FCF"

        # Extrai os dados de estágio e cenário
        self.dados_cenario = self.__scenario_line.read(file.readline())

        self.data: List[pd.DataFrame] = []
        while True:
            linha = file.readline()
            if str_bloco_variaveis_duais in linha:
                self.__read_bloco_variaveis_duais(file)
            elif str_bloco_restricoes_fcf in linha:
                self.__read_bloco_restricoes_fcf(file)
                break
