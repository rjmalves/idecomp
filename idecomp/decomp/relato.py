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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
        """
        if self.__balanco_energetico is None:
            self.__balanco_energetico = (
                self.__blocos_adicionando_coluna_estagios(
                    BlocoBalancoEnergeticoRelato
                )
            )
        return self.__balanco_energetico

    @property
    def cmo_medio_subsistema(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de CMO existente no :class:`Relato`

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
        """
        b = self.__bloco_por_tipo(BlocoCMORelato, 0)
        if b is not None:
            return b.data
        return None

    @property
    def geracao_termica_subsistema(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Geração Térmica existente no :class:`Relato`

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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

        :return: O DataFrame com os valores
        :rtype: Optional[pd.DataFrame]
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
        :rtype: Optional[int]
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
        :rtype: Optional[int]
        """
        b = self.__bloco_por_tipo(BlocoDiasExcluidosSemanas, 0)
        if b is not None:
            return b.data[1]
        return None
