from idecomp.decomp.modelos.dec_estatfpha import (
    BlocoDesvios,
)
from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from cfinterface.files.blockfile import BlockFile
from typing import Optional, Type, TypeVar
import pandas as pd  # type: ignore


class DecEstatFpha(BlockFile):
    """
    Arquivo com os dados referentes a estatísticas da função de produção do DECOMP.

    """

    BLOCKS = [
        VersaoModelo,
        BlocoDesvios,
    ]
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
        b = self._bloco_por_tipo(VersaoModelo, 0)
        if b is not None:
            return b.data
        return None

    @property
    def estatisticas_desvios(self) -> pd.DataFrame:
        """
        Obtém tabela com informações referentes às estatísticas
        de desvios da função de produção.

        - variaveis (`str`)
        - valor (`float`)

        :return: As variáveis como um dataframe
        :rtype: pd.DataFrame | None
        """
        b = self._bloco_por_tipo(BlocoDesvios, 0)
        if b is not None:
            return b.data
        return None
