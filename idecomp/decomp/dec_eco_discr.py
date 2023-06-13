from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_eco_discr import TabelaEcoDiscr

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


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
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, arquivo))

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - periodo (`int`)
        - patamar (`int`)
        - duracao (`float`)
        - numero_patamares (`int`)
        - numero_aberturas (`int`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
