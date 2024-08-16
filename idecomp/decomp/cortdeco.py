from cfinterface.files.sectionfile import SectionFile
from idecomp.decomp.modelos.cortdeco import SecaoDadosCortdeco

import pandas as pd  # type: ignore
from typing import TypeVar, Optional, Union, List, IO


class Cortdeco(SectionFile):
    """
    Armazena os dados de saída do DECOMP referentes aos
    cortes de Benders.
    """

    T = TypeVar("T")

    SECTIONS = [SecaoDadosCortdeco]
    STORAGE = "BINARY"

    def __obtem_secao_cortdeco(self) -> Optional[pd.DataFrame]:
        s = self.data.get_sections_of_type(SecaoDadosCortdeco)
        return s.data if not isinstance(s, list) and s is not None else None

    @classmethod
    def read(
        cls,
        content: Union[str, bytes],
        tamanho_registro: int = 0,
        registro_ultimo_corte_no: pd.DataFrame = pd.DataFrame(),
        numero_total_cortes: int = 0,
        numero_patamares_carga: int = 3,
        numero_estagios: int = 0,
        codigos_uhes: List[int] = [],
        codigos_uhes_tempo_viagem: List[int] = [],
        codigos_submercados: List[int] = [],
        lag_maximo_tempo_viagem: int = 3,
        *args,
        **kwargs
    ) -> "Cortdeco":
        a = super().read(
            content,
            tamanho_registro=tamanho_registro,
            registro_ultimo_corte_no=registro_ultimo_corte_no,
            numero_total_cortes=numero_total_cortes,
            numero_patamares_carga=numero_patamares_carga,
            numero_estagios=numero_estagios,
            codigos_uhes=codigos_uhes,
            codigos_uhes_tempo_viagem=codigos_uhes_tempo_viagem,
            codigos_submercados=codigos_submercados,
            lag_maximo_tempo_viagem=lag_maximo_tempo_viagem,
            *args,
            **kwargs
        )
        return a

    def write(
        self,
        to: Union[str, IO],
        df_registro_ultimo_corte_no: pd.DataFrame = pd.DataFrame(),
        *args,
        **kwargs
    ):
        super().write(
            to,
            df_registro_ultimo_corte_no=df_registro_ultimo_corte_no,
            *args,
            **kwargs
        )

    @property
    def cortes(self) -> Optional[pd.DataFrame]:
        """
        Retorna o conjunto dos cortes de Benders construídos
        durante o cálculo da política
        (leitura e escrita).

        - indice_corte (`int`)
        - no (`int`)
        - estagio (`int`)
        - pi_varm_uhe1 (`float`)
        - ...
        - pi_varm_uheU (`float`)
        - pi_qdefp_uheU_lag1 (`float`)
        - ...
        - pi_qdefp_uheU_lagL (`float`)
        - pi_gnl_sbm1_pat1_lag1 (`float`)
        - ...
        - pi_gnl_sbmS_patP_lagL (`float`)

        R é o número de REEs.
        U é o número de UHEs.
        S é o número de submercados.
        P é o número de patamares de carga.
        L é o lag máximo.

        :return: Os coeficientes dos cortes em uma tabela.
        :rtype: pd.DataFrame | None
        """

        return self.__obtem_secao_cortdeco()

    @cortes.setter
    def cortes(self, df: pd.DataFrame):
        dados = self.__obtem_secao_cortdeco()
        if dados is not None:
            dados = df

    @property
    def coeficientes_volume_armazenado(self) -> Optional[pd.DataFrame]:
        """
        Retorna o conjunto dos coeficientes dos cortes de Benders construídos
        durante o cálculo da política para os eixos de volume armazenado
        (apenas leitura).

        - indice_corte (`int`)
        - no (`int`)
        - estagio (`int`)
        - codigo_usina (`int`)
        - valor (`float`)

        :return: Os coeficientes de volume armazenado dos cortes
         em uma tabela.
        :rtype: pd.DataFrame | None
        """

        def __cria_data_frame(df_cortes: pd.DataFrame) -> pd.DataFrame:
            varm_cols = [col for col in df_cortes.columns if "varm" in col]
            df_melted = pd.melt(
                df_cortes,
                id_vars=["indice_corte", "no", "estagio"],
                value_vars=varm_cols,
            )
            df_melted["codigo_usina"] = (
                df_melted["variable"]
                .str.split("uhe", expand=True)[1]
                .astype(int)
            )
            df_melted = df_melted.drop(["variable"], axis=1)
            df_melted.rename(
                columns={
                    "value": "valor",
                },
                inplace=True,
            )
            df_melted = df_melted[
                [
                    "indice_corte",
                    "no",
                    "estagio",
                    "codigo_usina",
                    "valor",
                ]
            ]
            return df_melted

        df = self.__obtem_secao_cortdeco()
        if df is not None:
            return __cria_data_frame(df)
        else:
            return None

    @property
    def coeficientes_defluencia_tempo_viagem(self) -> Optional[pd.DataFrame]:
        """
        Retorna o conjunto dos coeficientes dos cortes de Benders construídos
        durante o cálculo da política para os eixos de vazão defluente passada
        por tempo de viagem (apenas leitura).

        - indice_corte (`int`)
        - no (`int`)
        - estagio (`int`)
        - codigo_usina (`int`)
        - lag (`int`)
        - valor (`float`)

        :return: Os coeficientes de defluência por tempo de viagem dos cortes
         em uma tabela.
        :rtype: pd.DataFrame | None
        """

        def __cria_data_frame(df_cortes: pd.DataFrame) -> pd.DataFrame:
            qdefp_cols = [col for col in df_cortes.columns if "qdefp" in col]
            df_melted = pd.melt(
                df_cortes,
                id_vars=["indice_corte", "no", "estagio"],
                value_vars=qdefp_cols,
            )
            df_melted["variable"] = df_melted["variable"].str.split(
                "uhe", expand=True
            )[1]
            df_melted["codigo_usina"] = (
                df_melted["variable"]
                .str.split("_", expand=True)[0]
                .astype(int)
            )
            df_melted["lag"] = (
                df_melted["variable"]
                .str.split("lag", expand=True)[1]
                .astype(int)
            )
            df_melted = df_melted.drop(["variable"], axis=1)
            df_melted.rename(
                columns={
                    "value": "valor",
                },
                inplace=True,
            )
            df_melted = df_melted[
                [
                    "indice_corte",
                    "codigo_usina",
                    "no",
                    "estagio",
                    "lag",
                    "valor",
                ]
            ]
            return df_melted

        df = self.__obtem_secao_cortdeco()
        if df is not None:
            return __cria_data_frame(df)
        else:
            return None

    @property
    def coeficientes_geracao_gnl(self) -> Optional[pd.DataFrame]:
        """
        Retorna o conjunto dos coeficientes dos cortes de Benders construídos
        durante o cálculo da política para os eixos de geração térmica
        futura para usinas com antecipacao de despacho (GNL) (apenas leitura).

        - indice_corte (`int`)
        - no (`int`)
        - estagio (`int`)
        - codigo_usina (`int`)
        - lag (`int`)
        - valor (`float`)

        :return: Os coeficientes de geração antecipada
         em uma tabela.
        :rtype: pd.DataFrame | None
        """

        def __cria_data_frame(df_cortes: pd.DataFrame) -> pd.DataFrame:
            gnl_cols = [col for col in df_cortes.columns if "sbm" in col]
            df_melted = pd.melt(
                df_cortes,
                id_vars=["indice_corte", "no", "estagio"],
                value_vars=gnl_cols,
            )
            df_melted["variable"].str.split("sbm", expand=True)
            df_melted["codigo_submercado"] = (
                df_melted["variable"]
                .str.split("sbm", expand=True)[1]
                .str.split("_", expand=True)[0]
            ).astype(int)
            df_melted["lag"] = (
                df_melted["variable"]
                .str.split("pat", expand=True)[1]
                .str.split("_", expand=True)[0]
            ).astype(int)
            df_melted = df_melted.drop(["variable"], axis=1)
            df_melted.rename(
                columns={
                    "value": "valor",
                },
                inplace=True,
            )
            df_melted = df_melted[
                [
                    "indice_corte",
                    "no",
                    "estagio",
                    "codigo_submercado",
                    "lag",
                    "valor",
                ]
            ]
            return df_melted

        df = self.__obtem_secao_cortdeco()
        if df is not None:
            return __cria_data_frame(df)
        else:
            return None
