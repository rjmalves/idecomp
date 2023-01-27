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

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_eco_cotajus.csv"
    ) -> "DecEcoCotajus":
        return cls.read(diretorio, arquivo)

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - indiceUsina (`int`)
        - nomeUsina (`str`)
        - indiceCurvaJusante (`int`)
        - alturaReferenciaUsinaJusante (`float`)
        - indicePolinomio (`int`)
        - vazaoMinima (`float`)
        - vazaoMaxima (`float`)
        - a0 (`float`)
        - a1 (`float`)
        - a2 (`float`)
        - a3 (`float`)
        - a4 (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
