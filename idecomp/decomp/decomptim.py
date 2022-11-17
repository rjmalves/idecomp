from idecomp.decomp.modelos.decomptim import BlocoTemposEtapas

from cfinterface.files.blockfile import BlockFile
from typing import Type, TypeVar, Optional
import pandas as pd  # type: ignore


class DecompTim(BlockFile):
    """
    Armazena os dados de saída do DECOMP referentes ao
    tempo de execução das etapas do programa.

    Esta classe lida com as informações de saída do
    DECOMP e reproduzidas no `decomp.tim`.

    """

    T = TypeVar("T")

    BLOCKS = [
        BlocoTemposEtapas,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="decomp.tim"
    ) -> "DecompTim":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="decomp.tim"):
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
    def tempos_etapas(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela dos tempos de execução do DECOMP existente no
        :class:`DecompTim`

        - Etapa (`str`)
        - Tempo (`timedelta`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None.
        """
        b = self.__bloco_por_tipo(BlocoTemposEtapas, 0)
        if b is not None:
            return b.data
        return None
