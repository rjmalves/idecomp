from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.avl_cortesfpha_dec import TabelaCortesFpha

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class AvlCortesFpha(ArquivoCSV):
    """
    Arquivo com os cortes da função de produção hidráulica aproximada do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaCortesFpha]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - codigo_usina (`int`)
        - estagio (`int`)
        - nome_usina (`str`)
        - segmento_fpha (`int`)
        - fator_correcao (`float`)
        - rhs (`float`)
        - coeficiente_volume_util (`float`)
        - coeficiente_vazao_turbinada (`float`)
        - coeficiente_vazao_vertida (`float`)
        - coeficiente_vazao_lateral (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
