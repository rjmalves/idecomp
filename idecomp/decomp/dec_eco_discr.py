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

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_eco_discr.csv"
    ) -> "DecEcoDiscr":
        return cls.read(diretorio, arquivo)

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - periodo (`int`)
        - patamar (`int`)
        - duracao (`float`)
        - numeroPatamares (`int`)
        - numeroAberturas (`int`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
