import pandas as pd  # type: ignore

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_eco_discr import TabelaEcoDiscr


class DecEcoDiscr(ArquivoCSV):
    """
    Arquivo com a discretização temporal dos estágios
    e patamares do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaEcoDiscr]

    @property
    def tabela(self) -> pd.DataFrame | None:
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
