from cfinterface.components.section import Section
from typing import IO, List
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from datetime import datetime


class SecaoDadosMapcut(Section):
    """
    Registro com os dados da execução do caso existente no
    arquivo mapcut.
    """

    __slots__ = ["__contador_registro"]

    REGISTER_SIZE = 48020

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.data = {
            "dados_gerais": [],  # registro 1
            "dados_caso": [],  # registro 2
            "dados_uhes": [],  # registro 3
            "dados_uhes_topologia": [],  # registro 4
            "dados_arvore": [],  # registro 5
            "dados_estagios": [],  # registro 6
            "dados_tempo_viagem": [],  # registros 7 e 8
            "dados_gnl": [],  # registros 9
            "dados_custos": [],  # registros 10
        }
        self.__contador_registro = 1

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, SecaoDadosMapcut):
            return False
        bloco: SecaoDadosMapcut = o
        if not all(
            [
                isinstance(self.data, dict),
                isinstance(o.data, dict),
            ]
        ):
            return False
        else:
            return self.data == bloco.data

    def read(self, file: IO, *args, **kwargs):
        # Leitura do primeiro registro (dados gerais)
        self.__le_primeiro_registro(file)
        # Leitura do segundo registro (dados do caso)
        self.__le_segundo_registro(file)
        # Leitura do terceiro registro (códigos UHEs)
        self.__le_terceiro_registro(file)
        # Leitura do quarto registro (dados cascatas UHEs)
        self.__le_quarto_registro(file)
        # Leitura do quinto registro (dados da árvore de cenários)
        self.__le_quinto_registro(file)
        # Leitura do sexto registro (dados gerais dos estágios)
        self.__le_sexto_registro(file)
        # Leitura do sétimo e oitavo registro (dados de tempo de viagem)
        self.__le_setimo_oitavo_registros(file)
        # Leitura do nono e décimo registro (dados de usinas gnl)
        self.__le_nono_decimo_registros(file)

    def __le_primeiro_registro(self, file: IO):
        tamanho_primeiro_bloco = 5
        dados_primeiro_bloco = np.frombuffer(
            file.read(tamanho_primeiro_bloco * 4),
            dtype=np.int32,
            count=tamanho_primeiro_bloco,
        )
        ncen = list(dados_primeiro_bloco)[-1]
        tamanho_segundo_bloco = ncen
        dados_segundo_bloco = np.frombuffer(
            file.read(tamanho_segundo_bloco * 4),
            dtype=np.int32,
            count=tamanho_segundo_bloco,
        )
        dados = list(dados_primeiro_bloco) + list(dados_segundo_bloco)
        self.data["dados_gerais"] = list(dados)

    def __le_segundo_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho = 4
        dados = np.frombuffer(
            file.read(tamanho * 4),
            dtype=np.int32,
            count=tamanho,
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_caso"] = list(dados)

    def __le_terceiro_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho = self.numero_uhes
        dados = np.frombuffer(
            file.read(tamanho * 4),
            dtype=np.int32,
            count=tamanho,
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_uhes"] = list(dados)

    def __le_quarto_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho = self.numero_uhes
        dados = np.frombuffer(
            file.read(tamanho * 4),
            dtype=np.float32,
            count=tamanho,
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_uhes_topologia"] = list(dados)

    def __le_quinto_registro(self, file: IO):
        self.__contador_registro = self.__contador_registro + 14
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho = self.numero_cenarios
        dados = np.frombuffer(
            file.read(tamanho * 4),
            dtype=np.int32,
            count=tamanho,
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_arvore"] = list(dados)

    def __le_sexto_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho_primeiro_bloco = 5
        dados_primeiro_bloco = np.frombuffer(
            file.read(tamanho_primeiro_bloco * 4),
            dtype=np.int32,
            count=tamanho_primeiro_bloco,
        )
        nper = list(dados_primeiro_bloco)[1]
        nutv = list(dados_primeiro_bloco)[-2]
        tamanho_segundo_bloco = 2 * nper
        dados_segundo_bloco = np.frombuffer(
            file.read(tamanho_segundo_bloco * 4),
            dtype=np.int32,
            count=tamanho_segundo_bloco,
        )
        tamanho_terceiro_bloco = nutv * nper
        dados_terceiro_bloco = np.frombuffer(
            file.read(tamanho_terceiro_bloco * 4),
            dtype=np.int32,
            count=tamanho_terceiro_bloco,
        )
        dados = (
            list(dados_primeiro_bloco)
            + list(dados_segundo_bloco)
            + list(dados_terceiro_bloco)
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_estagios"] = list(dados)

    def __le_setimo_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho_primeiro_bloco = 3
        tamanho_segundo_bloco = 1
        dados_primeiro_bloco = np.frombuffer(
            file.read(tamanho_primeiro_bloco * 4),
            dtype=np.int32,
            count=tamanho_primeiro_bloco,
        )
        dados_segundo_bloco = np.frombuffer(
            file.read(tamanho_segundo_bloco * 8),
            dtype=np.float64,
            count=tamanho_segundo_bloco,
        )
        dados = list(dados_primeiro_bloco) + list(dados_segundo_bloco)
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_tempo_viagem"] += list(dados)

    def __le_oitavo_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho = 1
        dados_primeiro_bloco = np.frombuffer(
            file.read(tamanho * 4),
            dtype=np.int32,
            count=tamanho,
        )
        dados_segundo_bloco = np.frombuffer(
            file.read(tamanho * 8),
            dtype=np.float64,
            count=tamanho,
        )
        dados = list(dados_primeiro_bloco) + list(dados_segundo_bloco)
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_tempo_viagem"] += list(dados)

    def __le_setimo_oitavo_registros(self, file: IO):
        for uhe in range(1, self.numero_uhes_tempo_viagem + 1, 1):
            for est in range(1, self.numero_estagios + 1, 1):
                lags = self.lag_tempo_viagem_por_uhe[(uhe * est) - 1]
                for lag in range(0, lags + 1, 1):
                    if (est == 1) & (lag == 0):
                        self.__le_setimo_registro(file)
                    else:
                        self.__le_oitavo_registro(file)

    def __le_nono_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho_primeiro_bloco = 1
        dados_primeiro_bloco = np.frombuffer(
            file.read(tamanho_primeiro_bloco * 4),
            dtype=np.int32,
            count=tamanho_primeiro_bloco,
        )
        ngnl = list(dados_primeiro_bloco)[0]
        tamanho_segundo_bloco = 3 * ngnl
        dados_segundo_bloco = np.frombuffer(
            file.read(tamanho_segundo_bloco * 4),
            dtype=np.int32,
            count=tamanho_segundo_bloco,
        )
        tamanho_terceiro_bloco = len(self.patamares_por_estagio) * ngnl
        dados_terceiro_bloco = np.frombuffer(
            file.read(tamanho_terceiro_bloco * 8),
            dtype=np.float64,
            count=tamanho_terceiro_bloco,
        )
        dados = (
            list(dados_primeiro_bloco)
            + list(dados_segundo_bloco)
            + list(dados_terceiro_bloco)
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_gnl"] += list(dados)

    def __le_decimo_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho = 6
        dados = np.frombuffer(
            file.read(tamanho * 8),
            dtype=np.float64,
            count=tamanho,
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_custos"] += list(dados)

    def __le_nono_decimo_registros(self, file: IO):
        for _ in range(self.numero_estagios):
            self.__le_nono_registro(file)
            self.__le_decimo_registro(file)

    @property
    def numero_iteracoes(self) -> int:
        return self.data["dados_gerais"][0]

    @property
    def numero_cortes(self) -> int:
        return self.data["dados_gerais"][1]

    @property
    def numero_submercados(self) -> int:
        return self.data["dados_gerais"][2]

    @property
    def numero_uhes(self) -> int:
        return self.data["dados_gerais"][3]

    @property
    def numero_cenarios(self) -> int:
        return self.data["dados_gerais"][4]

    @property
    def registro_ultimo_corte_no(self) -> pd.DataFrame:
        lista_estagios: List[int] = []
        estagio = 1
        for no in range(1, self.numero_cenarios + 1):
            if no in self.indice_primeiro_no_estagio:
                index = self.indice_primeiro_no_estagio.index(no)
                estagio = self.indice_primeiro_no_estagio[index]
            lista_estagios = lista_estagios + [estagio]

        df_registro_ultimo_corte_no = pd.DataFrame(
            data={
                "no": list(range(1, self.numero_cenarios + 1)),
                "estagio": lista_estagios,
                "indice_ultimo_corte": self.data["dados_gerais"][
                    -self.numero_cenarios :
                ],
            }
        )
        return df_registro_ultimo_corte_no

    @property
    def tamanho_corte(self) -> int:
        return self.data["dados_caso"][0]

    @property
    def data_inicio(self) -> datetime:
        dia = self.data["dados_caso"][1]
        mes = self.data["dados_caso"][2]
        ano = self.data["dados_caso"][3]
        return datetime(year=ano, month=mes, day=dia)

    @property
    def codigos_uhes(self) -> list:
        return self.data["dados_uhes"]

    @property
    def codigos_uhes_jusante(self) -> list:
        return self.data["dados_uhes_topologia"]

    @property
    def indice_no_arvore(self) -> list:
        return self.data["dados_arvore"]

    @property
    def numero_estagios(self) -> int:
        return self.data["dados_estagios"][1]

    @property
    def numero_semanas(self) -> int:
        return self.data["dados_estagios"][2]

    @property
    def numero_uhes_tempo_viagem(self) -> int:
        return self.data["dados_estagios"][3]

    @property
    def maximo_lag_tempo_viagem(self) -> int:
        return self.data["dados_estagios"][4]

    @property
    def indice_primeiro_no_estagio(self) -> list:
        offset = 5
        return self.data["dados_estagios"][
            offset : (offset + self.numero_estagios)
        ]

    @property
    def patamares_por_estagio(self) -> list:
        offset = 4 + self.numero_estagios + 1
        patamares_estagio = self.data["dados_estagios"][
            offset : (offset + self.numero_estagios)
        ]
        return patamares_estagio

    @property
    def lag_tempo_viagem_por_uhe(self) -> list:
        return self.data["dados_estagios"][
            -(self.numero_uhes_tempo_viagem * self.numero_estagios) :
        ]

    @property
    def dados_tempo_viagem(self) -> pd.DataFrame:
        offset = 0
        lags_tempo_vigem = []
        coef_amortecimento = []
        df_tempo_viagem = pd.DataFrame()

        for u in range(self.numero_uhes_tempo_viagem):
            # Pega informações do registro de dados de tempo de viagem
            usina = self.data["dados_tempo_viagem"][offset]
            lags_usina = self.lag_tempo_viagem_por_uhe[
                u * (self.numero_estagios) : (u + 1) * self.numero_estagios
            ]
            horas_tempo_viagem = self.data["dados_tempo_viagem"][offset + 1]

            idx_lag = offset + 2
            idx_coef = offset + 3

            # offset
            offset = 2 * (sum(lags_usina) + self.numero_estagios) + 2

            lags_tempo_vigem += [
                self.data["dados_tempo_viagem"][i]
                for i in list(range(idx_lag, idx_lag + offset - 2, 2))
            ]
            coef_amortecimento += [
                self.data["dados_tempo_viagem"][i]
                for i in list(range(idx_coef, idx_coef + offset - 2, 2))
            ]
            dados_tempo_viagem = {
                "codigo_usina": np.repeat(usina, len(lags_tempo_vigem)),
                "numero_horas": np.repeat(
                    horas_tempo_viagem, len(lags_tempo_vigem)
                ),
                "estagio": np.repeat(
                    list(range(1, self.numero_estagios + 1)),
                    int(len(lags_tempo_vigem) / self.numero_estagios),
                ),
                "indice_lag": lags_tempo_vigem,
                "coeficiente_amortecimento": coef_amortecimento,
            }
            df_tempo_viagem = pd.concat(
                [df_tempo_viagem, pd.DataFrame(dados_tempo_viagem)]
            )
        return df_tempo_viagem.reset_index(drop=True)

    @property
    def codigos_uhes_tempo_viagem(self) -> list:
        return self.dados_tempo_viagem["codigo_usina"].unique().tolist()

    @property
    def codigos_submercados_gnl(self) -> list:
        codigos_submercados = (
            self.dados_gnl["codigo_submercado"].unique().tolist()
        )
        return codigos_submercados

    @property
    def dados_gnl(self) -> pd.DataFrame:
        offset = 0
        df_dados_gnl = pd.DataFrame()
        for est in range(self.numero_estagios):
            numero_utes_gnl = int(self.data["dados_gnl"][offset])
            codigos_submercados = self.data["dados_gnl"][
                (offset + 1) : (offset + numero_utes_gnl + 1)
            ]
            lags_meses = self.data["dados_gnl"][
                (offset + numero_utes_gnl + 1) : (
                    offset + numero_utes_gnl + 1 + numero_utes_gnl
                )
            ]
            numero_patamares = self.data["dados_gnl"][
                (offset + 2 * numero_utes_gnl + 1) : (
                    offset + 3 * numero_utes_gnl + 1
                )
            ]
            offset = offset + int(
                1 + 4 * numero_utes_gnl + sum(numero_patamares)
            )

            dados = {
                "estagio": np.repeat(est + 1, len(codigos_submercados)),
                "numero_utes_gnl": np.repeat(
                    numero_utes_gnl, len(codigos_submercados)
                ),
                "codigo_submercado": codigos_submercados,
                "indice_lag": lags_meses,
                "numero_patamares": numero_patamares,
            }

            df_dados_gnl = pd.concat([df_dados_gnl, pd.DataFrame(dados)])

        return df_dados_gnl.reset_index(drop=True)

    @property
    def dados_custos(self) -> pd.DataFrame:
        offset = 0
        df_custos = pd.DataFrame()
        for est in range(self.numero_estagios):
            dados_custos = {
                "estagio": [est + 1],
                "taxa_desconto": [self.data["dados_custos"][offset]],
                "parcela_custo_geracao_termica_minima": [
                    self.data["dados_custos"][offset + 1]
                ],
                "parcela_custo_contrato_importacao_minimo": [
                    self.data["dados_custos"][offset + 2]
                ],
                "parcela_custo_contrato_exportacao_minimo": [
                    self.data["dados_custos"][offset + 3]
                ],
                "geracao_termica_minima_sinalizada_gnl": [
                    self.data["dados_custos"][offset + 4]
                ],
                "geracao_termica_minima_gerada_gnl": [
                    self.data["dados_custos"][offset + 5]
                ],
            }
            offset = offset + 6
            df_custos = pd.concat([df_custos, pd.DataFrame(dados_custos)])
        return df_custos.reset_index(drop=True)
