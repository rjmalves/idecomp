from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_eco_evap import TabelaEcoEvap

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecEcoEvap(ArquivoCSV):
    """
    Arquivo com o eco dos dados da consideração da evaporação
    das usinas hidrelétricas.
    """

    BLOCKS = [VersaoModelo, TabelaEcoEvap]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - nome_submercado (`str`)
        - codigo_ree (`int`)
        - volume_referencia_hm3 (`float`)
        - evaporacao_referencia_hm3 (`float`)
        - coeficiente_evaporacao_mensal (`int`)
        - considera_evaporacao (`bool`)
        - considera_evaporacao_linear (`bool`)
        - flag_tipo_volume_referencia (`bool`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
