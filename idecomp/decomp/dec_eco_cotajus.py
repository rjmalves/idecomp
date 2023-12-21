from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_eco_cotajus import TabelaEcoCotajus

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecEcoCotajus(ArquivoCSV):
    """
    Arquivo com o eco dos polinômios por partes das
    curvas de jusante do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaEcoCotajus]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - codigo_usina (`int`)
        - nome_usina (`str`)
        - indice_curva_jusante (`int`)
        - altura_referencia_usina_jusante (`float`)
        - indice_polinomio (`int`)
        - vazao_minima (`float`)
        - vazao_maxima (`float`)
        - a0 (`float`)
        - a1 (`float`)
        - a2 (`float`)
        - a3 (`float`)
        - a4 (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
