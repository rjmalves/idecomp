from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_eco_discr import TabelaEcoDiscr

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecEcoDiscr(ArquivoCSV):
    """
    Arquivo com a discretização temporal dos estágios
    e patamares do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaEcoDiscr]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - patamar (`int`)
        - duracao (`float`)
        - numero_patamares (`int`)
        - numero_aberturas (`int`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
