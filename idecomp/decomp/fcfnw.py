from idecomp.decomp.modelos.fcfnw import BlocoCortesFCF

from cfinterface.files.blockfile import BlockFile
from typing import TypeVar, Optional
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


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
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

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
        b = self.data.get_blocks_of_type(BlocoCortesFCF)
        if isinstance(b, BlocoCortesFCF):
            return b.data
        return None
