from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_cortes_evap import TabelaCortesEvap

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecAvlEvap(ArquivoCSV):
    """
    Arquivo com os cortes da evaporação linear do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaCortesEvap]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - periodo (`int`)
        - codigoUsina (`int`)
        - nomeUsina (`str`)
        - submercado (`int`)
        - ree (`int`)
        - derivadaCotaArea (`float`)
        - derivadaVolumeCota (`float`)
        - volumeReferenciaHm3 (`float`)
        - evaporacaoReferenciaHm3 (`float`)
        - coeficienteVolume (`float`)
        - rhsVolume (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
