from idecomp.decomp.modelos.relato import BlocoREEsSubsistemas
from idecomp.decomp.modelos.relato import BlocoUHEsREEsSubsistemas
from idecomp.decomp.modelos.relato import BlocoConvergenciaRelato
from idecomp.decomp.modelos.relato import BlocoRelatorioOperacaoRelato
from idecomp.decomp.modelos.relato import BlocoRelatorioOperacaoUTERelato
from idecomp.decomp.modelos.relato import BlocoBalancoEnergeticoRelato
from idecomp.decomp.modelos.relato import BlocoCMORelato
from idecomp.decomp.modelos.relato import BlocoGeracaoTermicaSubsistemaRelato
from idecomp.decomp.modelos.relato import BlocoCustoOperacaoValorEsperadoRelato
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
from typing import Union, List, TypeVar, Optional
import pandas as pd  # type: ignore


class Relato(BlockFile):
    """
    Armazena os dados de saída do DECOMP referentes ao
    acompanhamento do programa.

    Esta classe lida com as informações de entrada D ao
    DECOMP e reproduzidas no `relato.rvx`, bem como as saídas finais
    da execução: custos de operação, despacho de térmicas, etc.

    """

    T = TypeVar("T", bound=Block)

    BLOCKS = [
        BlocoREEsSubsistemas,
        BlocoUHEsREEsSubsistemas,
        BlocoConvergenciaRelato,
        BlocoRelatorioOperacaoUTERelato,
        BlocoRelatorioOperacaoRelato,
        BlocoBalancoEnergeticoRelato,
        BlocoCMORelato,
        BlocoGeracaoTermicaSubsistemaRelato,
        BlocoCustoOperacaoValorEsperadoRelato,
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
        self.__relatorios_operacao_ute = None
        self.__relatorios_operacao_uhe = None
        self.__relatorios_operacao_custos = None
        self.__balanco_energetico = None

    def __concatena_blocos(
        self, blocos: Union[T, List[T]], indice_data=None
    ) -> Optional[pd.DataFrame]:
        df = None
        if not isinstance(blocos, list):
            blocos = [blocos]
        for b in blocos:
            df_estagio = b.data if indice_data is None else b.data[indice_data]
            if df is None:
                df = df_estagio
            else:
                df = pd.concat([df, df_estagio], ignore_index=True)
        if df is not None:
            return df
        return None

    @property
    def rees_submercados(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de relação entre os REEs e os submercados do
        DECOMP existente no :class:`Relato`

        - codigo_ree (`int`)
        - nome_ree (`str`)
        - codigo_submercado (`int`)
        - nome_submercado (`str`)
        - nome_submercado_newave (`str`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None.
        """
        b = self.data.get_blocks_of_type(BlocoREEsSubsistemas)
        if isinstance(b, BlocoREEsSubsistemas):
            return b.data
        return None

    @property
    def uhes_rees_submercados(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de relação entre as UHEs, REEs e os submercados do
        DECOMP existente no :class:`Relato`

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - codigo_ree (`int`)
        - nome_ree (`str`)
        - codigo_submercado (`int`)
        - nome_submercado (`str`)
        - nome_submercado_newave (`str`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None.
        """
        b = self.data.get_blocks_of_type(BlocoUHEsREEsSubsistemas)
        if isinstance(b, BlocoUHEsREEsSubsistemas):
            return b.data
        return None

    @property
    def convergencia(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de convergência do DECOMP existente no
        :class:`Relato`

        - iteracao (`int`)
        - zinf (`float`)
        - zsup (`float`)
        - gap_percentual (`float`)
        - tempo (`int`)
        - deficit_demanda_MWmed (`float`)
        - deficit_nivel_seguranca_MWmes (`float`)
        - numero_inviabilidades (`int`)
        - inviabilidades_MWmed (`float`)
        - inviabilidades_m3s (`float`)
        - inviabilidades_hm3 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None.
        """
        b = self.data.get_blocks_of_type(BlocoConvergenciaRelato)
        if isinstance(b, BlocoConvergenciaRelato):
            return b.data
        return None

    @property
    def relatorio_operacao_custos(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de operação de cada UHE por estágio do DECOMP
        existente no :class:`Relato`

        - estagio (`int`)
        - cenario (`int`)
        - probabilidade (`float`)
        - custo_futuro (`float`)
        - custo_presente (`float`)
        - geracao_termica (`float`)
        - violacao_desvio (`float`)
        - penalidade_vertimento_reservatorio (`float`)
        - penalidade_vertimento_fio (`float`)
        - violacao_turbinamento_reservatorio (`float`)
        - violacao_turbinamento_fio (`float`)
        - penalidade_intercambio (`float`)
        - cmo_<sbm1> (`float`)
        - ...
        - cmo_<sbmN> (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        if self.__relatorios_operacao_custos is None:
            blocos_custos: List[BlocoRelatorioOperacaoRelato] = []
            for b in self.data.of_type(BlocoRelatorioOperacaoRelato):
                if b.data[0] == "GERAL":
                    blocos_custos.append(b)
            self.__relatorios_operacao_custos = self.__concatena_blocos(
                blocos_custos, 1
            )
        return self.__relatorios_operacao_custos

    @property
    def relatorio_operacao_uhe(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de operação de cada UHE por estágio do DECOMP
        existente no :class:`Relato`

        - estagio (`int`)
        - cenario (`int`)
        - probabilidade (`float`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - considera_evaporacao (`bool`)
        - considera_tempo_viagem (`bool`)
        - considera_soleira_vertedouro (`bool`)
        - considera_defluencia_minima_0 (`bool`)
        - volume_inicial_percentual (`float`)
        - volume_final_percentual (`float`)
        - volume_espera_percentual (`float`)
        - vazao_natural_m3s (`float`)
        - vazao_natural_mlt (`float`)
        - vazao_afluente_m3s (`float`)
        - vazao_defluente_m3s (`float`)
        - geracao_patamar_1 (`float`)
        - geracao_patamar_2 (`float`)
        - geracao_patamar_3 (`float`)
        - geracao_media (`float`)
        - vertimento_turbinavel (`float`)
        - vertimento_nao_turbinavel (`float`)
        - geracao_ponta (`float`)
        - FPCGC (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        if self.__relatorios_operacao_uhe is None:
            blocos_uhe: List[BlocoRelatorioOperacaoRelato] = []
            for b in self.data.of_type(BlocoRelatorioOperacaoRelato):
                if b.data[0] == "UHE":
                    blocos_uhe.append(b)
            self.__relatorios_operacao_uhe = self.__concatena_blocos(
                blocos_uhe, 1
            )
        return self.__relatorios_operacao_uhe

    @property
    def relatorio_operacao_ute(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de operação de cada UTE por estágio do DECOMP
        existente no :class:`Relato`

        - estagio (`int`)
        - cenario (`int`)
        - probabilidade (`float`)
        - nome_submercado (`str`)
        - nome_usina (`str`)
        - FPCGC (`float`)
        - geracao_patamar_1 (`float`)
        - ...
        - geracao_patamar_N (`float`)
        - custo (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        if self.__relatorios_operacao_ute is None:
            blocos = self.data.get_blocks_of_type(
                BlocoRelatorioOperacaoUTERelato
            )
            if blocos is not None:
                self.__relatorios_operacao_ute = self.__concatena_blocos(
                    blocos
                )
        return self.__relatorios_operacao_ute

    @property
    def balanco_energetico(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de balanço energético entre os patamares para
        cada estágio do DECOMP existente no :class:`Relato`

        - estagio (`int`)
        - cenario (`int`)
        - probabilidade (`float`)
        - nome_submercado (`str`)
        - patamar (`str`)
        - energia_armazenada_inicial_MWmed (`float`)
        - energia_armazenada_inicial_percentual (`float`)
        - energia_natural_afluente_MWmed (`float`)
        - energia_natural_afluente_percentual (`float`)
        - energia_armazenada_final_MWmed (`float`)
        - energia_armazenada_final_percentual (`float`)
        - mercado (`float`)
        - bacia (`float`)
        - consumo_bombeamento (`float`)
        - geracao_hidraulica (`float`)
        - geracao_termica (`float`)
        - geracao_termica_antecipada (`float`)
        - geracao_eolica (`float`)
        - deficit (`float`)
        - compra (`float`)
        - venda (`float`)
        - geracao_itaipu_50hz (`float`)
        - geracao_itaipu_60hz (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        if self.__balanco_energetico is None:
            blocos = self.data.get_blocks_of_type(BlocoBalancoEnergeticoRelato)
            if blocos is not None:
                self.__balanco_energetico = self.__concatena_blocos(blocos)
        return self.__balanco_energetico

    @property
    def cmo_medio_submercado(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de CMO existente no :class:`Relato`

        - nome_submercado (`str`)
        - patamar (`str`)
        - estagio_1 (`float`)
        - estagio_2 (`float`)
        - ...
        - estagio_N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoCMORelato)
        if isinstance(b, BlocoCMORelato):
            return b.data
        return None

    @property
    def geracao_termica_submercado(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Geração Térmica existente no :class:`Relato`

        - nome_submercado (`str`)
        - estagio_1 (`float`)
        - estagio_2 (`float`)
        - ...
        - estagio_N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoGeracaoTermicaSubsistemaRelato)
        if isinstance(b, BlocoGeracaoTermicaSubsistemaRelato):
            return b.data
        return None

    @property
    def custo_operacao_valor_esperado(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Custo de Operação existente no :class:`Relato`

        - parcela (`str`)
        - estagio_1 (`float`)
        - estagio_2 (`float`)
        - ...
        - estagio_N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoCustoOperacaoValorEsperadoRelato)
        if isinstance(b, BlocoCustoOperacaoValorEsperadoRelato):
            return b.data
        return None

    @property
    def energia_armazenada_ree(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Energia Armazenada por REE (em %)
        existente no :class:`Relato`

        - nome_submercado (`str`)
        - nome_ree (`str`)
        - inicial (`float`)
        - estagio_1 (`float`)
        - estagio_2 (`float`)
        - ...
        - estagio_N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoEnergiaArmazenadaREERelato)
        if isinstance(b, BlocoEnergiaArmazenadaREERelato):
            return b.data
        return None

    @property
    def energia_armazenada_submercado(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Energia Armazenada por Submercado (em %)
        existente no :class:`Relato`

        - nome_submercado (`str`)
        - inicial (`float`)
        - estagio_1 (`float`)
        - estagio_2 (`float`)
        - ...
        - estagio_N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(
            BlocoEnergiaArmazenadaSubsistemaRelato
        )
        if isinstance(b, BlocoEnergiaArmazenadaSubsistemaRelato):
            return b.data
        return None

    @property
    def volume_util_reservatorios(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Volumes Úteis por reservatório (em %)
        existente no :class:`Relato`

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - inicial (`float`)
        - estagio_1 (`float`)
        - estagio_2 (`float`)
        - ...
        - estagio_N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoVolumeUtilReservatorioRelato)
        if isinstance(b, BlocoVolumeUtilReservatorioRelato):
            return b.data
        return None

    @property
    def dados_termicas(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de dados cadastrais das usinas térmicas
        existente no :class:`Relato`.

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - nome_submercado (`str`)
        - estagio (`int`)
        - geracao_minima_patamar_1 (`float`)
        - geracao_maxima_patamar_1 (`float`)
        - custo_patamar_1 (`float`)
        - geracao_minima_patamar_2 (`float`)
        - geracao_maxima_patamar_2 (`float`)
        - custo_patamar_2 (`float`)
        - geracao_minima_patamar_3 (`float`)
        - geracao_maxima_patamar_3 (`float`)
        - custo_patamar_3 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoDadosTermicasRelato)
        if isinstance(b, BlocoDadosTermicasRelato):
            return b.data
        return None

    @property
    def disponibilidades_termicas(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de disponibilidades das usinas térmicas
        existente no :class:`Relato`.

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - estagio_1 (`float`)
        - estagio_2 (`float`)
        - ...
        - estagio_N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoDisponibilidadesTermicasRelato)
        if isinstance(b, BlocoDisponibilidadesTermicasRelato):
            return b.data
        return None

    @property
    def dados_mercado(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de dados do mercado de energia
        existente no :class:`Relato`.

        - estagio (`int`)
        - nome_submercado (`str`)
        - patamar_1 (`float`)
        - mercado_1 (`float`)
        - ...
        - patamar_N (`float`)
        - mercado_N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoDadosMercadoRelato)
        if isinstance(b, BlocoDadosMercadoRelato):
            return b.data
        return None

    @property
    def ena_acoplamento_ree(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de ENA para acoplamento com o longo prazo
        (em MWmed) existente no :class:`Relato`

        - codigo_ree (`int`)
        - nome_ree (`str`)
        - nome_submercado (`str`)
        - estagio_1 (`float`)
        - estagio_2 (`float`)
        - ...
        - estagio_N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoENAAcoplamentoREERelato)
        if isinstance(b, BlocoENAAcoplamentoREERelato):
            return b.data
        return None

    @property
    def ena_pre_estudo_mensal_ree(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de ENA Pré-Estudo Mensal por REE
        existente no :class:`Relato`

        - nome_ree (`str`)
        - estagio_pre_1 (`float`)
        - estagio_pre_2 (`float`)
        - ...
        - estagio_pre_11 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoENAPreEstudoMensalREERelato)
        if isinstance(b, BlocoENAPreEstudoMensalREERelato):
            df: pd.DataFrame = b.data.copy()
            df.drop(columns=["energia_armazenada_maxima"], inplace=True)
            return df
        return None

    @property
    def ena_pre_estudo_mensal_submercado(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de ENA Pré-Estudo Mensal por Submercado
        existente no :class:`Relato`

        - nome_submercado (`str`)
        - estagio_pre_1 (`float`)
        - estagio_pre_2 (`float`)
        - ...
        - estagio_pre_11 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(
            BlocoENAPreEstudoMensalSubsistemaRelato
        )
        if isinstance(b, BlocoENAPreEstudoMensalSubsistemaRelato):
            df: pd.DataFrame = b.data.copy()
            df.drop(columns=["energia_armazenada_maxima"], inplace=True)
            return df
        return None

    @property
    def ena_pre_estudo_semanal_ree(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de ENA Pré-Estudo Semanal por REE
        existente no :class:`Relato`

        - nome_ree (`str`)
        - estagio_pre_1 (`float`)
        - estagio_pre_2 (`float`)
        - ...
        - estagio_pre_5 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoENAPreEstudoSemanalREERelato)
        if isinstance(b, BlocoENAPreEstudoSemanalREERelato):
            df: pd.DataFrame = b.data.copy()
            df.drop(columns=["energia_armazenada_maxima"], inplace=True)
            return df
        return None

    @property
    def ena_pre_estudo_semanal_submercado(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de ENA Pré-Estudo Semanal por Submercado
        existente no :class:`Relato`

        - nome_submercado (`str`)
        - estagio_pre_1 (`float`)
        - estagio_pre_2 (`float`)
        - ...
        - estagio_pre_5 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(
            BlocoENAPreEstudoSemanalSubsistemaRelato
        )
        if isinstance(b, BlocoENAPreEstudoSemanalSubsistemaRelato):
            df: pd.DataFrame = b.data.copy()
            df.drop(columns=["energia_armazenada_maxima"], inplace=True)
            return df
        return None

    @property
    def energia_armazenada_maxima_submercado(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Energia Armazenada Máxima (EARMax) em MWmes
        por submercado existente no :class:`Relato`

        - nome_submercado (`str`)
        - energia_armazenada_maxima (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(
            BlocoENAPreEstudoSemanalSubsistemaRelato
        )
        if isinstance(b, BlocoENAPreEstudoSemanalSubsistemaRelato):
            df: pd.DataFrame = b.data.copy()
            return df[["nome_submercado", "energia_armazenada_maxima"]]
        return None

    @property
    def dias_excluidos_semana_inicial(self) -> Optional[int]:
        """
        Obtém o número de dias excluídos da semana inicial.

        :return: O número de dias
        :rtype: int | None
        """
        b = self.data.get_blocks_of_type(BlocoDiasExcluidosSemanas)
        if isinstance(b, BlocoDiasExcluidosSemanas):
            return b.data[0]
        return None

    @property
    def dias_excluidos_semana_final(self) -> Optional[int]:
        """
        Obtém o número de dias excluídos da semana final.

        :return: O número de dias
        :rtype: int | None
        """
        b = self.data.get_blocks_of_type(BlocoDiasExcluidosSemanas)
        if isinstance(b, BlocoDiasExcluidosSemanas):
            return b.data[1]
        return None
