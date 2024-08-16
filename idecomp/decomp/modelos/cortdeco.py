from cfinterface.components.section import Section
from typing import IO, List
import numpy as np  # type: ignore
import pandas as pd  # type: ignore


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
        "__numero_bytes_nulos",
        "__tamanho_registro",
        "__numero_total_cortes",
        "__numero_cortes_por_estagio",
        "__codigos_uhes",
        "__codigos_uhes_tempo_viagem",
        "__numero_patamares_carga",
        "__numero_estagios",
        "__codigos_submercados",
        "__lag_maximo_tempo_viagem",
        "__registro_ultimo_corte_no",
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

    def __inicializa_variaveis(self, numero_total_cortes):

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
        self.__numero_bytes_nulos = self.__tamanho_registro - (
            8 * (self.__numero_coeficientes) + 4
        )
        # Tabela para armazenar leitura dos campos do tipo int (relacionados aos
        # indices de registros)
        self.__tabela_int = np.zeros((numero_total_cortes, 2), dtype=np.int32)
        # Tabela para armazenar leitura dos campos do tipo float (relacionados aos
        # coeficientes da FCF)
        self.__tabela_float = np.zeros(
            (numero_total_cortes, self.__numero_coeficientes),
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

    def __converte_array_em_dataframe(self, no: int, estagio: int):
        df_int = pd.DataFrame(
            self.__tabela_int[:, 0],
            columns=[
                "indice_corte",
            ],
        )
        # Para transformar no índice do corte em si, soma 1
        # Depois, inverte a indexação
        df_int["indice_corte"] += 1
        df_int["indice_corte"] = df_int["indice_corte"].to_numpy()[::-1]
        df_int["no"] = no
        df_int["estagio"] = estagio
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
        return df.sort_values(
            by=["estagio", "no", "indice_corte"]
        ).reset_index(drop=True)

    def __le_arquivo(
        self,
        file: IO,
    ):
        df_cortes_completo = pd.DataFrame()
        # Realiza leitura para cada no que constroi corte
        for _, row in self.__registro_ultimo_corte_no.iterrows():
            # Identifica indice do ultimo corte do no
            estagio = row["estagio"]
            no = row["no"]
            indice_ultimo_corte = row["indice_ultimo_corte"]
            # Caso seja o ultimo estagio que constroi corte (penultimo estagio do caso),
            # faz um shift no indice do ultimo corte para englobar o ultimo corte impresso
            # pelo Cepel
            if estagio == (self.__numero_estagios - 1):
                incremento_offset = self.__registro_ultimo_corte_no.loc[
                    self.__registro_ultimo_corte_no["estagio"]
                    != max(self.__registro_ultimo_corte_no["estagio"])
                ].shape[0]
                indice_ultimo_corte = indice_ultimo_corte + incremento_offset
            # Caso o indice do ultimo corte seja 0, indica que acabou a leitura
            if indice_ultimo_corte == 0:
                self.data = df_cortes_completo.reset_index(drop=True)
                return
            # Identifica o numero total de cortes para o estagio
            numero_total_cortes = self.__numero_cortes_por_estagio.loc[
                self.__numero_cortes_por_estagio["estagio"] == estagio,
                "numero_total_cortes",
            ].iloc[0]

            # Inicializa variaveis para a leitura dos cortes do no
            self.__inicializa_variaveis(numero_total_cortes)
            # Faz a leitura dos registros
            indice_proximo_corte = self.__le_registro(
                file, (indice_ultimo_corte - 1) * self.__tamanho_registro, 0
            )
            cortes_lidos = 1
            while (indice_proximo_corte != 0) and (
                cortes_lidos < numero_total_cortes
            ):
                indice_proximo_corte = self.__le_registro(
                    file,
                    self.__tamanho_registro * (indice_proximo_corte - 1),
                    cortes_lidos,
                )
                cortes_lidos += 1
            df_cortes_no = self.__converte_array_em_dataframe(no, estagio)
            # Concatena com informacoes dos cortes do no/estagio
            df_cortes_completo = pd.concat([df_cortes_completo, df_cortes_no])

    def __identifica_numero_cortes_estagio(self) -> pd.DataFrame:
        # Adiciona um corte a mais para o ultimo estagio,
        # devido metodologia de impressão adotada pelo Cepel
        df = self.__registro_ultimo_corte_no.loc[
            self.__registro_ultimo_corte_no["estagio"]
            != max(self.__registro_ultimo_corte_no["estagio"])
        ][["estagio"]]
        df["numero_total_cortes"] = self.__numero_total_cortes
        df.loc[df["estagio"] == df["estagio"].max(), "numero_total_cortes"] = (
            self.__numero_total_cortes + 1
        )
        return df

    def __identifica_indices_registros(
        self, df_registro_ultimo_corte_no: pd.DataFrame
    ) -> pd.DataFrame:
        # Copia e ordena df dos cortes
        df_cortes = self.data.copy()
        df_cortes.sort_values(
            by=["indice_corte", "no"], inplace=True, ascending=[False, True]
        )
        df_cortes["indice_registro"] = 0
        df_cortes["indice_proximo_registro"] = 0
        # Calcula offset dos registros de acordo com o numero de nos (o ultimo
        # estagio nao constroi cortes)
        incremento_offset = df_registro_ultimo_corte_no.loc[
            df_registro_ultimo_corte_no["estagio"]
            != max(df_registro_ultimo_corte_no["estagio"])
        ].shape[0]
        # Identifica dados relativos aos nos e itera nos nos
        df_nos = df_registro_ultimo_corte_no.loc[
            df_registro_ultimo_corte_no["indice_ultimo_corte"] != 0
        ]
        for _, row in df_nos.iterrows():
            indice_registro = row["indice_ultimo_corte"]
            # Realiza offset caso seja o ultimo estagio para compatibilizar
            # com a impressão de um corte adicional feita pelo CEPEL
            if row["estagio"] == max(df_nos["estagio"]):
                indice_registro = indice_registro + incremento_offset
            # Itera sobre os cortes daquele no e armazena informacoes de
            # indice do registro e indice do proximo registro
            for _, row_cortes in df_cortes.loc[
                (df_cortes["no"] == row["no"])
            ].iterrows():
                indice_corte = row_cortes["indice_corte"]
                df_cortes.loc[
                    (df_cortes["no"] == row["no"])
                    & (df_cortes["indice_corte"] == indice_corte),
                    "indice_registro",
                ] = indice_registro
                df_cortes.loc[
                    (df_cortes["no"] == row["no"])
                    & (df_cortes["indice_corte"] == indice_corte),
                    "indice_proximo_registro",
                ] = max(0, indice_registro - incremento_offset)
                indice_registro = max(0, indice_registro - incremento_offset)
        # return df_cortes
        return df_cortes.sort_values(by=["indice_registro"])

    def __atualiza_registros(
        self, file: IO, df_registro_ultimo_corte_no: pd.DataFrame
    ):
        df_cortes = self.__identifica_indices_registros(
            df_registro_ultimo_corte_no
        )
        for _, row in df_cortes.iterrows():
            # Vai para a posicao do registro
            # file.seek(
            #     int(row["indice_registro"] - 1) * self.__tamanho_registro
            # )
            # Escreve primeiro campo (inteiro)
            file.write(
                np.array(
                    row["indice_proximo_registro"], dtype=np.int32
                ).tobytes()
            )
            # Escreve campos relativos aos coeficientes (float)
            file.write(
                np.array(row.to_numpy()[3:-2], dtype=np.float64).tobytes()
            )
            file.write(
                np.array(
                    [0] * (self.__numero_bytes_nulos // 4), dtype=np.int32
                ).tobytes()
            )

    def read(
        self,
        file: IO,
        tamanho_registro: int,
        registro_ultimo_corte_no: pd.DataFrame,
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
        self.__registro_ultimo_corte_no = registro_ultimo_corte_no
        self.__numero_cortes_por_estagio = (
            self.__identifica_numero_cortes_estagio()
        )

        self.__le_arquivo(file)
        # Ignore bytes restantes
        _ = file.read()

    def write(
        self,
        file: IO,
        *args,
        **kwargs,
    ):
        df_registro_ultimo_corte_no = kwargs["df_registro_ultimo_corte_no"]
        self.__atualiza_registros(file, df_registro_ultimo_corte_no)
