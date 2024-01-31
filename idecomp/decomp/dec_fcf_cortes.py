from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_fcf_cortes import TabelaFcfCortes

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecFcfCortes(ArquivoCSV):
    """
    Arquivo com os cortes da FCF geradas pelo DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaFcfCortes]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - indice_iteracao (`int`)
        - tipo_entidade (`str`)
        - indice_entidade (`int`)
        - nome_entidade (`str`)
        - tipo_coeficiente (`str`)
        - indice_lag (`int`)
        - indice_patamar (`int`)
        - valor_coeficiente (`float`)
        - unidade_coeficiente (`str`)
        - ponto_consultado (`float`)
        - unidade_ponto_consultado (`str`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
