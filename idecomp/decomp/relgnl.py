from idecomp.decomp.modelos.relgnl import BlocoDadosUsinasRelGNL
from idecomp.decomp.modelos.relgnl import BlocoComandosUsinasAjustesTGRelGNL
from idecomp.decomp.modelos.relgnl import BlocoComandosUsinasAjustesRERelGNL
from idecomp.decomp.modelos.relgnl import BlocoRelatorioOperacaoRelGNL
from cfinterface.components.block import Block
from cfinterface.files.blockfile import BlockFile
from typing import Type, List, TypeVar, Optional
import pandas as pd  # type: ignore


class RelGNL(BlockFile):
    """
    Armazena os dados de saída do DECOMP referentes às térmicas de
    despacho antecipado (GNL).

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP e reproduzidas no `relgnl.rvx`, bem como as saídas finais
    da execução.

    """

    T = TypeVar("T")

    BLOCKS = [
        BlocoDadosUsinasRelGNL,
        BlocoComandosUsinasAjustesTGRelGNL,
        BlocoComandosUsinasAjustesRERelGNL,
        BlocoRelatorioOperacaoRelGNL,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)
        self.__relatorio_operacao_gnl = None

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="relgnl.rv0") -> "RelGNL":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="relgnl.rv0"):
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
        b = self.__bloco_por_tipo(BlocoDadosUsinasRelGNL, 0)
        if b is not None:
            return b.data
        return None

    @property
    def comandos_usinas_registros_tg(self) -> Optional[pd.DataFrame]:
        """
        Tabela de comandos das usinas térmicas GNL com ajustes
        devido aos registros TG.

        - Código (`int`)
        - Usina (`str`)
        - Lag (`int`)
        - Subsistema (`str`)
        - Semana (`int`)
        - Pat 1 (`float`)
        - Pat 2 (`float`)
        - Pat 3 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoComandosUsinasAjustesTGRelGNL, 0)
        if b is not None:
            return b.data
        return None

    @property
    def comandos_usinas_restricoes_eletricas(self) -> Optional[pd.DataFrame]:
        """
        Tabela de comandos das usinas térmicas GNL com ajustes
        devido a restrições elétricas especiais.

        - Código (`int`)
        - Usina (`str`)
        - Lag (`int`)
        - Subsistema (`str`)
        - Semana (`int`)
        - Pat 1 (`float`)
        - Pat 2 (`float`)
        - Pat 3 (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoComandosUsinasAjustesRERelGNL, 0)
        if b is not None:
            return b.data
        return None

    @property
    def relatorio_operacao_termica(self) -> Optional[pd.DataFrame]:
        """
        Tabela com o relatório do despacho sinalizado para as usinas
        térmicas GNL.

        - Período (`int`)
        - Cenário (`int`)
        - Probabilidade (`float`)
        - Subsistema (`str`)
        - Usina (`str`)
        - Lag (`int`)
        - Estágio (`int`)
        - Início Semana (`str`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """

        if self.__relatorio_operacao_gnl is None:
            self.__relatorio_operacao_gnl = self.__concatena_blocos(
                BlocoRelatorioOperacaoRelGNL
            )
        return self.__relatorio_operacao_gnl
