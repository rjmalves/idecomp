from idecomp.decomp.modelos.fcfnw import BlocoCortesFCF

from cfinterface.files.blockfile import BlockFile
from typing import Type, TypeVar, Optional
import pandas as pd  # type: ignore


class Fcfnw(BlockFile):
    """
    Armazena os dados de saída do DECOMP referentes ao
    acoplamento realizado com a FCF do NEWAVE.

    Esta classe lida com as informações de entrada ao
    DECOMP e reproduzidas no `fcfnwX.rvx`.

    """

    T = TypeVar("T")

    BLOCKS = [BlocoCortesFCF]

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="fcfnwn.rv0") -> "Fcfnw":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="fcfnwn.rv0"):
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
    def cortes(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela de cortes do NEWAVE existente no
        :class:`Fcfnw`.

        Os nomes da colunas podem variar de acordo com o
        período de acoplamento (NEWAVE REE ou individualizado).

        Caso REE:

        - corte (`int`)
        - RHS (`float`)
        - REE (`int`)
        - coef_earm (`float`)
        - coef_eafl_1 (`float`)
        - ...
        - coef_eafl_N (`float`)
        - coef_GNL_pat1_lag1 (`float`)
        - coef_GNL_pat1_lag2 (`float`)
        - ...
        - coef_GNL_patK_lag1 (`float`)
        - coef_GNL_patK_lag2 (`float`)
        - coef_vminop_max (`float`)

        Caso individualizado:

        - corte (`int`)
        - RHS (`float`)
        - UHE (`int`)
        - coef_varm (`float`)
        - coef_afl_1 (`float`)
        - ...
        - coef_afl_N (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None.
        """
        b = self.__bloco_por_tipo(BlocoCortesFCF, 0)
        if b is not None:
            return b.data
        return None
