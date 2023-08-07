from idecomp.decomp.modelos.decomptim import BlocoTemposEtapas

from cfinterface.files.blockfile import BlockFile
from typing import TypeVar, Optional
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


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
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def tempos_etapas(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela dos tempos de execução do DECOMP existente no
        :class:`DecompTim`

        - etapa (`str`)
        - tempo (`timedelta`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None.
        """
        b = self.data.get_blocks_of_type(BlocoTemposEtapas)
        if isinstance(b, BlocoTemposEtapas):
            return b.data
        return None
