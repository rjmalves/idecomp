from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_evap import (
    TabelaOperEvapv31,
    TabelaOperEvap,
)

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecOperEvap(ArquivoCSV):
    """
    Arquivo com a operação de evaporação por usina hidroelétrica do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperEvap]
    VERSIONS = {
        "31.0.2": [VersaoModelo, TabelaOperEvapv31],
        "31.1.2": [VersaoModelo, TabelaOperEvap],
    }

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - no (`int`)
        - cenario (`int`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - codigo_submercado (`int`)
        - codigo_ree (`int`)
        - volume_util_inicial_hm3 (`float`)
        - volume_util_inicial_percentual (`float`)
        - volume_util_final_hm3 (`float`)
        - volume_util_final_percentual (`float`)
        - evaporacao_modelo_hm3 (`float`)
        - evaporacao_calculada_hm3 (`float`)
        - desvio_absoluto_hm3 (`float`)
        - desvio_percentual (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
