from typing import Optional

import pandas as pd  # type: ignore

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from idecomp.decomp.modelos.avl_turb_max import TabelaAvlTurbMax


class AvlTurbMax(ArquivoCSV):
    """
    Arquivo com avaliação do turbinamento máximo das usinas hidrelétricas do DECOMP.
    """

    BLOCKS = [TabelaAvlTurbMax]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - observacao (`str`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - volume_util_inicial_hm3 (`float`)
        - volume_util_final_hm3 (`float`)
        - vazao_turbinada_m3s (`float`)
        - vazao_turbinada_maxima_pl_m3s (`float`)
        - engolimento_maximo_priori_m3s (`float`)
        - engolimento_maximo_posteriori_m3s (`float`)
        - vazao_turbinada_maxima_gerador_m3s (`float`)
        - altura_queda (`float`)
        - altura_efetiva (`float`)
        - altura_montante (`float`)
        - altura_jusante (`float`)
        - violacao_turbinamento_m3s (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
