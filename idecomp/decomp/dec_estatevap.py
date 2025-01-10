from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_estatevap import TabelaEstatEvap

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecEstatEvap(ArquivoCSV):
    """
    Arquivo com as estatísticas de desvios de modelagem da evaporação da usinas
     hidrelétricas do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaEstatEvap]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - numero_usinas_evaporacao (`int`)
        - numero_usinas_total (`int`)
        - evaporacao_modelo_hm3 (`float`)
        - evaporacao_calculada_hm3 (`float`)
        - desvio_absoluto_positivo_hm3 (`float`)
        - desvio_absoluto_negativo_hm3 (`float`)
        - evaporacao_modelo_m3s (`float`)
        - evaporacao_calculada_m3s (`float`)
        - desvio_absoluto_positivo_m3s (`float`)
        - desvio_absoluto_negativo_m3s (`float`)
        - desvio_percentual (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
