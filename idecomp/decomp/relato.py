from idecomp.decomp.modelos.relato import BlocoConvergenciaRelato
from idecomp.decomp.modelos.relato import BlocoRelatorioOperacaoUHERelato
from idecomp.decomp.modelos.relato import BlocoBalancoEnergeticoRelato
from idecomp.decomp.modelos.relato import BlocoCMORelato
from idecomp.decomp.modelos.relato import BlocoGeracaoTermicaSubsistemaRelato
from idecomp.decomp.modelos.relato import BlocoENAAcoplamentoREERelato
from idecomp.decomp.modelos.relato import BlocoVolumeUtilReservatorioRelato
from idecomp.decomp.modelos.relato import BlocoDadosTermicasRelato
from idecomp.decomp.modelos.relato import BlocoDisponibilidadesTermicasRelato
from idecomp.decomp.modelos.relato import BlocoDadosMercadoRelato
from idecomp.decomp.modelos.relato import BlocoEnergiaArmazenadaREERelato
from idecomp.decomp.modelos.relato import (
    BlocoEnergiaArmazenadaSubsistemaRelato,
)  # noqa
from idecomp.decomp.modelos.relato import BlocoENAPreEstudoMensalREERelato
from idecomp.decomp.modelos.relato import (
    BlocoENAPreEstudoMensalSubsistemaRelato,
)  # noqa
from idecomp.decomp.modelos.relato import BlocoENAPreEstudoSemanalREERelato
from idecomp.decomp.modelos.relato import (
    BlocoENAPreEstudoSemanalSubsistemaRelato,
)  # noqa
from idecomp.decomp.modelos.relato import BlocoDiasExcluidosSemanas

from cfinterface.components.block import Block
from cfinterface.files.blockfile import BlockFile
from typing import Type, List, TypeVar, Optional
import pandas as pd  # type: ignore


class Relato(BlockFile):
    """
    Armazena os dados de saída do DECOMP referentes ao
    acompanhamento do programa.

    Esta classe lida com as informações de entrada D ao
    DECOMP e reproduzidas no `relato.rvx`, bem como as saídas finais
    da execução: custos de operação, despacho de térmicas, etc.

    """

    T = TypeVar("T")

    BLOCKS = [
        BlocoConvergenciaRelato,
        BlocoRelatorioOperacaoUHERelato,
        BlocoBalancoEnergeticoRelato,
        BlocoCMORelato,
        BlocoGeracaoTermicaSubsistemaRelato,
        BlocoENAAcoplamentoREERelato,
        BlocoVolumeUtilReservatorioRelato,
        BlocoDadosTermicasRelato,
        BlocoDisponibilidadesTermicasRelato,
        BlocoDadosMercadoRelato,
        BlocoEnergiaArmazenadaREERelato,
        BlocoEnergiaArmazenadaSubsistemaRelato,
        BlocoENAPreEstudoMensalREERelato,
        BlocoENAPreEstudoMensalSubsistemaRelato,
        BlocoENAPreEstudoSemanalREERelato,
        BlocoENAPreEstudoSemanalSubsistemaRelato,
        BlocoDiasExcluidosSemanas,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)
        self.__relatorios_operacao_uhe = None
        self.__balanco_energetico = None

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="relato.rv0") -> "Relato":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="relato.rv0"):
        self.write(diretorio, nome_arquivo)

    def __bloco_por_tipo(self, bloco: Type[T], indice: int) -> Optional[T]:
        """
        Obtém um gerador de blocos de um tipo, se houver algum no arquivo.
        :param bloco: Um tipo de bloco para ser lido
        :type bloco: T
        :param indice: O índice do bloco a ser acessado, dentre os do tipo
        :type indice: int
        :return: O gerador de blocos, se houver
        :rtype: Optional[Generator[T], None, None]
        """
        try:
            return next(
                b
                for i, b in enumerate(self.data.of_type(bloco))
                if i == indice
            )
        except StopIteration:
            return None

    def __concatena_blocos(self, bloco: Type[T]) -> Optional[pd.DataFrame]:
        """
        Adiciona uma coluna com o estágio de cada bloco, assumindo
        a mesma ordem das séries de energia.
        :param bloco: O tipo de bloco
        :type bloco: Type[T]
        :return: O DataFrame com os estágios
        :rtype: pd.DataFrame
        """
        df = None
        for i, b in enumerate(self.data.of_type(bloco)):
            if not isinstance(b, Block):
                continue
            df_estagio = b.data
            if df is None:
                df = df_estagio
            else:
                df = pd.concat([df, df_estagio], ignore_index=True)
        if df is not None:
            return df
        return None

    def __blocos_adicionando_coluna_estagios(
        self, bloco: Type[T]
    ) -> Optional[pd.DataFrame]:
        """
        Adiciona uma coluna com o estágio de cada bloco, assumindo
        a mesma ordem das séries de energia.
        :param bloco: O tipo de bloco
        :type bloco: Type[T]
        :return: O DataFrame com os estágios
        :rtype: pd.DataFrame
        """

        col_estagio: List[int] = []
        df = None
        for i, b in enumerate(self.data.of_type(bloco)):
            if not isinstance(b, Block):
                continue
            df_estagio = b.data.copy()
            col_estagio += [i + 1] * df_estagio.shape[0]
            if df is None:
                df = df_estagio
            else:
                df = pd.concat([df, df_estagio], ignore_index=True)
        if df is not None:
            cols = list(df.columns)
            df["Estágio"] = col_estagio
            return df[["Estágio"] + cols]
        return None

    @property
    def convergencia(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de convergência do DECOMP existente no
        :class:`Relato`

        - Iteração (`int`)
        - Zinf (`float`)
        - Zsup (`float`)
        - Gap (%) (`float`)
        - Tempo (s) (`int`)
        - Tot. Def. Demanda (MWmed) (`float`)
        - Tot. Def. Niv. Seg. (MWmes) (`float`)
        - Num. Inviab" (`int`)
        - Tot. Inviab (MWmed) (`float`)
        - Tot. Inviab (m3/s) (`float`)
        - Tot. Inviab (Hm3) (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None.
        """
        b = self.__bloco_por_tipo(BlocoConvergenciaRelato, 0)
        if b is not None:
            return b.data
        return None

    @property
    def relatorio_operacao_uhe(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de operação de cada UHE por estágio do DECOMP
        existente no :class:`Relato`

        - Estágio (`int`)
        - Código (`int`)
        - Usina (`str`)
        - Evaporação (`bool`)
        - Tempo de Viagem (`bool`)
        - Cota Abaixo da Crista do Vert (`bool`)
        - Def. Mínima = 0 (`bool`)
        - Volume Ini (% V.U) (`float`)
        - Volume Fin (% V.U) (`float`)
        - Volume Esp. (% V.U) (`float`)
        - Qnat (m3/s) (`float`)
        - Qnat (% MLT) (`float`)
        - Qafl (m3/s) (`float`)
        - Qdef (m3/s) (`float`)
        - Geração Pat 1 (`float`)
        - Geração Pat 2 (`float`)
        - Geração Pat 3 (`float`)
        - Geração Média (`float`)
        - Vertimento Turbinável (`float`)
        - Vertimento Não-Turbinável (`float`)
        - Ponta (`float`)
        - FPCGC (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        if self.__relatorios_operacao_uhe is None:
            self.__relatorios_operacao_uhe = (
                self.__blocos_adicionando_coluna_estagios(
                    BlocoRelatorioOperacaoUHERelato
                )
            )
        return self.__relatorios_operacao_uhe

    @property
    def balanco_energetico(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de balanço energético entre os patamares para
        cada estágio do DECOMP existente no :class:`Relato`

        - Estágio (`int`)
        - Cenário (`int`)
        - Probabilidade (`float`)
        - Subsistema (`str`)
        - Earm Inicial Absoluto (`float`)
        - Earm Inicial Percentual (`float`)
        - ENA Absoluta (`float`)
        - ENA Percentual (`float`)
        - Earm Final Absoluto (`float`)
        - Earm Final Percentual (`float`)
        - Mercado (`float`)
        - Bacia (`float`)
        - Cbomba (`float`)
        - Ghid (`float`)
        - Gter (`float`)
        - GterAT (`float`)
        - Geol (`float`)
        - Deficit (`float`)
        - Compra (`float`)
        - Venda (`float`)
        - Itaipu50 (`float`)
        - Itaipu60 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        if self.__balanco_energetico is None:
            self.__balanco_energetico = self.__concatena_blocos(
                BlocoBalancoEnergeticoRelato
            )
        return self.__balanco_energetico

    @property
    def cmo_medio_subsistema(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de CMO existente no :class:`Relato`

        - Subsistema (`str`)
        - Patamar (`str`)
        - Estágio 1 (`float`)
        - Estágio 2 (`float`)
        - ...
        - Estágio N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoCMORelato, 0)
        if b is not None:
            return b.data
        return None

    @property
    def geracao_termica_subsistema(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Geração Térmica existente no :class:`Relato`

        - Subsistema (`str`)
        - Estágio 1 (`float`)
        - Estágio 2 (`float`)
        - ...
        - Estágio N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoGeracaoTermicaSubsistemaRelato, 0)
        if b is not None:
            return b.data
        return None

    @property
    def energia_armazenada_ree(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Energia Armazenada por REE (em %)
        existente no :class:`Relato`

        - Subsistema (`str`)
        - REE (`str`)
        - Inicial (`float`)
        - Estágio 1 (`float`)
        - Estágio 2 (`float`)
        - ...
        - Estágio N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoEnergiaArmazenadaREERelato, 0)
        if b is not None:
            return b.data
        return None

    @property
    def energia_armazenada_subsistema(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Energia Armazenada por Subsistema (em %)
        existente no :class:`Relato`

        - Subsistema (`str`)
        - Inicial (`float`)
        - Estágio 1 (`float`)
        - Estágio 2 (`float`)
        - ...
        - Estágio N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoEnergiaArmazenadaSubsistemaRelato, 0)
        if b is not None:
            return b.data
        return None

    @property
    def volume_util_reservatorios(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Volumes Úteis por reservatório (em %)
        existente no :class:`Relato`

        - Número (`int`)
        - Usina (`str`)
        - Inicial (`float`)
        - Estágio 1 (`float`)
        - Estágio 2 (`float`)
        - ...
        - Estágio N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoVolumeUtilReservatorioRelato, 0)
        if b is not None:
            return b.data
        return None

    @property
    def dados_termicas(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de dados cadastrais das usinas térmicas
        existente no :class:`Relato`.

        - Código (`int`)
        - Usina (`str`)
        - Subsistema (`str`)
        - Estágio (`int`)
        - GT Min Pat. 1 (`float`)
        - GT Max Pat. 1 (`float`)
        - Custo Pat. 1 (`float`)
        - GT Min Pat. 2 (`float`)
        - GT Max Pat. 2 (`float`)
        - Custo Pat. 2 (`float`)
        - GT Min Pat. 3 (`float`)
        - GT Max Pat. 3 (`float`)
        - Custo Pat. 3 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoDadosTermicasRelato, 0)
        if b is not None:
            return b.data
        return None

    @property
    def disponibilidades_termicas(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de disponibilidades das usinas térmicas
        existente no :class:`Relato`.

        - Número (`int`)
        - Usina (`str`)
        - Estágio 1 (`float`)
        - Estágio 2 (`float`)
        - ...
        - Estágio N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoDisponibilidadesTermicasRelato, 0)
        if b is not None:
            return b.data
        return None

    @property
    def dados_mercado(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de dados do mercado de energia
        existente no :class:`Relato`.

        - Estágio (`int`)
        - Subsistema (`str`)
        - Patamar 1 (`float`)
        - Mercado 1 (`float`)
        - ...
        - Patamar N (`float`)
        - Mercado N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoDadosMercadoRelato, 0)
        if b is not None:
            return b.data
        return None

    @property
    def ena_acoplamento_ree(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de ENA para acoplamento com o longo prazo
        (em MWmed) existente no :class:`Relato`

        - Índice (`int`)
        - REE (`str`)
        - Subsistema (`str`)
        - Estágio 1 (`float`)
        - Estágio 2 (`float`)
        - ...
        - Estágio N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoENAAcoplamentoREERelato, 0)
        if b is not None:
            return b.data
        return None

    @property
    def ena_pre_estudo_mensal_ree(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de ENA Pré-Estudo Mensal por REE
        existente no :class:`Relato`

        - REE (`str`)
        - Earmax (`float`)
        - Estágio Pré 1 (`float`)
        - Estágio Pré 2 (`float`)
        - ...
        - Estágio Pré 11 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoENAPreEstudoMensalREERelato, 0)
        if b is not None:
            df: pd.DataFrame = b.data.copy()
            df.drop(columns=["Earmax"], inplace=True)
            return df
        return None

    @property
    def ena_pre_estudo_mensal_subsistema(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de ENA Pré-Estudo Mensal por Subsistema
        existente no :class:`Relato`

        - Subsistema (`str`)
        - Earmax (`float`)
        - Estágio Pré 1 (`float`)
        - Estágio Pré 2 (`float`)
        - ...
        - Estágio Pré 11 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoENAPreEstudoMensalSubsistemaRelato, 0)
        if b is not None:
            df: pd.DataFrame = b.data.copy()
            df.drop(columns=["Earmax"], inplace=True)
            return df
        return None

    @property
    def ena_pre_estudo_semanal_ree(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de ENA Pré-Estudo Semanal por REE
        existente no :class:`Relato`

        - REE (`str`)
        - Earmax (`float`)
        - Estágio Pré 1 (`float`)
        - Estágio Pré 2 (`float`)
        - ...
        - Estágio Pré 5 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoENAPreEstudoSemanalREERelato, 0)
        if b is not None:
            df: pd.DataFrame = b.data.copy()
            df.drop(columns=["Earmax"], inplace=True)
            return df
        return None

    @property
    def ena_pre_estudo_semanal_subsistema(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de ENA Pré-Estudo Semanal por Subsistema
        existente no :class:`Relato`

        - Subsistema (`str`)
        - Earmax (`float`)
        - Estágio Pré 1 (`float`)
        - Estágio Pré 2 (`float`)
        - ...
        - Estágio Pré 5 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoENAPreEstudoSemanalSubsistemaRelato, 0)
        if b is not None:
            df: pd.DataFrame = b.data.copy()
            df.drop(columns=["Earmax"], inplace=True)
            return df
        return None

    @property
    def energia_armazenada_maxima_subsistema(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Energia Armazenada Máxima (EARMax) em MWmes
        por subsistema existente no :class:`Relato`

        - Subsistema (`str`)
        - Earmax (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoENAPreEstudoSemanalSubsistemaRelato, 0)
        if b is not None:
            return b.data[["Subsistema", "Earmax"]]
        return None

    @property
    def dias_excluidos_semana_inicial(self) -> Optional[int]:
        """
        Obtém o número de dias excluídos da semana inicial.

        :return: O número de dias
        :rtype: int | None
        """
        b = self.__bloco_por_tipo(BlocoDiasExcluidosSemanas, 0)
        if b is not None:
            return b.data[0]
        return None

    @property
    def dias_excluidos_semana_final(self) -> Optional[int]:
        """
        Obtém o número de dias excluídos da semana final.

        :return: O número de dias
        :rtype: int | None
        """
        b = self.__bloco_por_tipo(BlocoDiasExcluidosSemanas, 0)
        if b is not None:
            return b.data[1]
        return None
