from idecomp.decomp.modelos.decomptim import BlocoTemposEtapas

from cfinterface.files.blockfile import BlockFile
from typing import TypeVar, Optional
import pandas as pd  # type: ignore


class Decomptim(BlockFile):
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

    @property
    def tempos_etapas(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela dos tempos de execução do DECOMP existente no
        :class:`Decomptim`

        - etapa (`str`)
        - tempo (`timedelta`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None.
        """
        b = self.data.get_blocks_of_type(BlocoTemposEtapas)
        if isinstance(b, BlocoTemposEtapas):
            return b.data
        return None
