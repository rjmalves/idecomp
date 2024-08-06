from cfinterface.components.section import Section
from typing import IO, List
import numpy as np  # type: ignore
import pandas as pd


class SecaoDadosCortdeco(Section):
    """
    Registro com os cortes da FCF.
    """

    __slots__ = [
        "__tabela_int",
        "__tabela_float",
        "__numero_coeficientes",
        "__numero_coeficientes_rhs",
        "__numero_coeficientes_varm",
        "__numero_coeficientes_tviagem",
        "__numero_coeficientes_gnl",
        "__tamanho_registro",
        "__numero_total_cortes",
        "__codigos_uhes",
        "__codigos_uhes_tempo_viagem",
        "__numero_patamares_carga",
        "__numero_estagios",
        "__codigos_submercados",
        "__lag_maximo_tempo_viagem",
    ]

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, SecaoDadosCortdeco):
            return False
        bloco: SecaoDadosCortdeco = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

    def __inicializa_variaveis(self):
        self.__tabela_int = np.zeros(
            (self.__numero_total_cortes, 1), dtype=np.int32
        )
        self.__numero_coeficientes_rhs = 1
        self.__numero_coeficientes_varm = int(len(self.__codigos_uhes))
        self.__numero_coeficientes_tviagem = int(
            len(self.__codigos_uhes_tempo_viagem)
            * self.__lag_maximo_tempo_viagem
        )
        self.__numero_coeficientes_gnl = int(
            len(self.__codigos_submercados)
            * self.__numero_estagios
            * self.__numero_patamares_carga
        )
        self.__numero_coeficientes = (
            self.__numero_coeficientes_rhs
            + self.__numero_coeficientes_varm
            + self.__numero_coeficientes_tviagem
            + self.__numero_coeficientes_gnl
        )
        self.__tabela_float = np.zeros(
            (self.__numero_total_cortes, self.__numero_coeficientes),
            dtype=np.float64,
        )

    def __le_e_atribui_int(
        self, file: IO, destino: np.ndarray, tamanho: int, indice: int
    ):
        destino[indice, :] = np.frombuffer(
            file.read(tamanho * 4),
            dtype=np.int32,
            count=tamanho,
        )

    def __le_e_atribui_float(
        self, file: IO, destino: np.ndarray, tamanho: int, indice: int
    ):
        destino[indice, :] = np.frombuffer(
            file.read(tamanho * 8),
            dtype=np.float64,
            count=tamanho,
        )

    def __le_registro(
        self,
        file: IO,
        offset: int,
        indice: int,
    ) -> int:
        file.seek(offset)
        self.__le_e_atribui_int(file, self.__tabela_int, 1, indice)
        self.__le_e_atribui_float(
            file, self.__tabela_float, self.__numero_coeficientes, indice
        )
        indice_proximo_corte = self.__tabela_int[indice, 0]
        self.__tabela_int[indice, 0] = indice
        return indice_proximo_corte

    def __converte_array_em_dataframe(self):
        df_int = pd.DataFrame(
            self.__tabela_int,
            columns=[
                "indice_corte",
            ],
        )
        # Para transformar no índice do corte em si, soma 1
        # Depois, inverte a indexação
        df_int["indice_corte"] += 1
        df_int["indice_corte"] = df_int["indice_corte"].to_numpy()[::-1]

        cols_varm = [f"pi_varm_uhe{i}" for i in self.__codigos_uhes]
        cols_tviagem = [
            f"pi_qdefp_uhe{i}_lag{j}"
            for j in range(self.__lag_maximo_tempo_viagem)
            for i in self.__codigos_uhes_tempo_viagem
        ]
        cols_gnl = [
            f"pi_gnl_sbm{i}_pat{j}_lag{k}"
            for i in self.__codigos_submercados
            for k in range(1, self.__numero_estagios + 1)
            for j in range(1, self.__numero_patamares_carga + 1)
        ]
        df_float = pd.DataFrame(
            self.__tabela_float[:, 0 : (self.__numero_coeficientes)],
            columns=["rhs"] + cols_varm + cols_tviagem + cols_gnl,
        )

        df = pd.concat([df_int, df_float], axis=1)
        return df.sort_values(by="indice_corte").reset_index(drop=True)

    def read(
        self,
        file: IO,
        tamanho_registro: int,
        indice_ultimo_corte: int,
        numero_total_cortes: int,
        numero_patamares_carga: int,
        numero_estagios: int,
        codigos_uhes: List[int],
        codigos_uhes_tempo_viagem: List[int],
        codigos_submercados: List[int],
        lag_maximo_tempo_viagem: int,
        *args,
        **kwargs,
    ):
        # Atribui variáveis locais
        self.__tamanho_registro = tamanho_registro
        self.__numero_total_cortes = numero_total_cortes
        self.__numero_patamares_carga = numero_patamares_carga
        self.__numero_estagios = numero_estagios
        self.__codigos_uhes = codigos_uhes
        self.__codigos_uhes_tempo_viagem = codigos_uhes_tempo_viagem
        self.__codigos_submercados = codigos_submercados
        self.__lag_maximo_tempo_viagem = lag_maximo_tempo_viagem
        # Realiza leitura
        self.__inicializa_variaveis()
        indice_proximo_corte = self.__le_registro(
            file, (indice_ultimo_corte - 1) * self.__tamanho_registro, 0
        )
        cortes_lidos = 1
        while (indice_proximo_corte != 0) and (
            cortes_lidos < numero_total_cortes
        ):
            indice_proximo_corte = self.__le_registro(
                file,
                tamanho_registro * (indice_proximo_corte - 1),
                cortes_lidos,
            )
            cortes_lidos += 1
        df_cortes_completo = self.__converte_array_em_dataframe()
        self.data = df_cortes_completo
