from idecomp.decomp.modelos.relato import BlocoCMORelato
from idecomp.decomp.modelos.relato import BlocoGeracaoTermicaSubsistemaRelato
from idecomp.decomp.modelos.relato import BlocoCustoOperacaoValorEsperadoRelato
from idecomp.decomp.modelos.relato import BlocoVolumeUtilReservatorioRelato
from idecomp.decomp.modelos.relato import BlocoEnergiaArmazenadaREERelato
from idecomp.decomp.modelos.relato import (
    BlocoEnergiaArmazenadaSubsistemaRelato,
)
from cfinterface.files.blockfile import BlockFile
from typing import Type, TypeVar, Optional
import pandas as pd  # type: ignore


class Sumario(BlockFile):
    """
    Armazena os dados de saída do DECOMP referentes ao
    acompanhamento do programa.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP e reproduzidas no `sumario.rvx`, bem como as saídas finais
    da execução: custos de operação, despacho de térmicas, etc.

    """

    T = TypeVar("T")

    BLOCKS = [
        BlocoCMORelato,
        BlocoGeracaoTermicaSubsistemaRelato,
        BlocoCustoOperacaoValorEsperadoRelato,
        BlocoVolumeUtilReservatorioRelato,
        BlocoEnergiaArmazenadaREERelato,
        BlocoEnergiaArmazenadaSubsistemaRelato,
    ]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="sumario.rv0"
    ) -> "Sumario":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="sumario.rv0"):
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

    @property
    def cmo_medio_subsistema(self) -> pd.DataFrame:
        """
        Obtém a tabela de CMO existente no :class:`Sumario`

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
    def geracao_termica_subsistema(self) -> pd.DataFrame:
        """
        Obtém a tabela de Geração Térmica existente no :class:`Sumario`

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
    def volume_util_reservatorios(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de Volumes Úteis por reservatório (em %)
        existente no :class:`Sumario`

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
    def energia_armazenada_ree(self) -> pd.DataFrame:
        """
        Obtém a tabela de Energia Armazenada por REE (em %)
        existente no :class:`Sumario`

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
    def energia_armazenada_subsistema(self) -> pd.DataFrame:
        """
        Obtém a tabela de Energia Armazenada por Subsistema (em %)
        existente no :class:`Sumario`

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
