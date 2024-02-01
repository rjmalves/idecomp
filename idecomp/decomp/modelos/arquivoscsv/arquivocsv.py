from idecomp.decomp.modelos.blocos.versaomodelo import (
    VersaoModelo,
    VersaoModeloLibs,
)
from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV, TabelaCSVLibs

from cfinterface.components.block import Block
from cfinterface.files.blockfile import BlockFile
import pandas as pd  # type: ignore
from typing import List, Type, TypeVar, Optional


class ArquivoCSV(BlockFile):
    """
    Modelo de arquivo baseado em blocos específico para o formato
    dos arquivos de saída .CSV do DECOMP. Espera conter
    a implementação de dois blocos específicos:

    - Versão do modelo
    - Tabela de dados

    O primeiro é genérico, mas o segundo deve ser
    implementado para cada arquivo específico a ser lido.
    """

    BLOCKS: List[Type[Block]] = [VersaoModelo]
    ENCODING = "iso-8859-1"

    T = TypeVar("T")

    def _bloco_por_tipo(self, bloco: Type[T], indice: int) -> Optional[T]:
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
    def versao(self) -> Optional[str]:
        """
        A versão do modelo utilizada para executar o caso.

        :return: A versão do modelo
        :rtype: str | None
        """
        b = self.data.get_blocks_of_type(VersaoModelo)
        b_libs = self.data.get_blocks_of_type(VersaoModeloLibs)
        if isinstance(b, VersaoModelo):
            return b.data
        elif isinstance(b_libs, VersaoModeloLibs):
            return b_libs.data
        return None

    def _tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(TabelaCSV)
        b_libs = self.data.get_blocks_of_type(TabelaCSVLibs)
        if isinstance(b, TabelaCSV):
            return b.data
        elif isinstance(b_libs, TabelaCSVLibs):
            return b_libs.data
        return None
