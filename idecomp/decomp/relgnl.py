from idecomp.decomp.modelos.relgnl import BlocoDadosUsinasRelgnl
from idecomp.decomp.modelos.relgnl import BlocoComandosUsinasAjustesTGRelgnl
from idecomp.decomp.modelos.relgnl import BlocoComandosUsinasAjustesRERelgnl
from idecomp.decomp.modelos.relgnl import BlocoRelatorioOperacaoRelgnl
from cfinterface.components.block import Block
from cfinterface.files.blockfile import BlockFile
from typing import Type, List, TypeVar, Optional
import pandas as pd  # type: ignore


class Relgnl(BlockFile):
    """
    Armazena os dados de saída do DECOMP referentes às térmicas de
    despacho antecipado (GNL).

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP e reproduzidas no `relgnl.rvx`, bem como as saídas finais
    da execução.

    """

    T = TypeVar("T")

    BLOCKS = [
        BlocoDadosUsinasRelgnl,
        BlocoComandosUsinasAjustesTGRelgnl,
        BlocoComandosUsinasAjustesRERelgnl,
        BlocoRelatorioOperacaoRelgnl,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)
        self.__relatorio_operacao_gnl = None

    def __concatena_blocos(self, bloco: Type[T]) -> Optional[pd.DataFrame]:
        """
        Adiciona uma coluna com os estágios de cada amostra e outra
        com o estágio de cada uma, assumindo
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
    def usinas_termicas(self) -> Optional[pd.DataFrame]:
        """
        Tabela de informações das usinas térmicas GNL.

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
        b = self.data.get_blocks_of_type(BlocoDadosUsinasRelgnl)
        if isinstance(b, BlocoDadosUsinasRelgnl):
            return b.data
        return None

    @property
    def comandos_usinas_registros_tg(self) -> Optional[pd.DataFrame]:
        """
        Tabela de comandos das usinas térmicas GNL com ajustes
        devido aos registros TG.

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - lag (`int`)
        - nome_submercado (`str`)
        - semana (`int`)
        - patamar_1 (`float`)
        - patamar_2 (`float`)
        - patamar_3 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoComandosUsinasAjustesTGRelgnl)
        if isinstance(b, BlocoComandosUsinasAjustesTGRelgnl):
            return b.data
        return None

    @property
    def comandos_usinas_restricoes_eletricas(self) -> Optional[pd.DataFrame]:
        """
        Tabela de comandos das usinas térmicas GNL com ajustes
        devido a restrições elétricas especiais.

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - lag (`int`)
        - nome_submercado (`str`)
        - semana (`int`)
        - patamar_1 (`float`)
        - patamar_2 (`float`)
        - patamar_3 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoComandosUsinasAjustesRERelgnl)
        if isinstance(b, BlocoComandosUsinasAjustesRERelgnl):
            return b.data
        return None

    @property
    def relatorio_operacao_termica(self) -> Optional[pd.DataFrame]:
        """
        Tabela com o relatório do despacho sinalizado para as usinas
        térmicas GNL.

        - estagio (`int`)
        - cenario (`int`)
        - probabilidade (`float`)
        - nome_submercado (`str`)
        - nome_usina (`str`)
        - lag (`int`)
        - semana (`int`)
        - data_inicio_semana (`str`)
        - geracao_patamar_1 (`float`)
        - duracao_patamar_1 (`float`)
        - geracao_patamar_2 (`float`)
        - duracao_patamar_2 (`float`)
        - geracao_patamar_3 (`float`)
        - duracao_patamar_3 (`float`)
        - custo (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """

        if self.__relatorio_operacao_gnl is None:
            self.__relatorio_operacao_gnl = self.__concatena_blocos(
                BlocoRelatorioOperacaoRelgnl
            )
        return self.__relatorio_operacao_gnl
