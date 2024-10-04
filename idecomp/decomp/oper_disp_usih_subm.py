from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModeloLibs
from idecomp.decomp.modelos.oper_disp_usih_subm import TabelaOperDispUsihSubm

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class OperDispUsihSubm(ArquivoCSV):
    """
    Arquivo com a disponibilidade das usinas hidroelétricas do DECOMP,
    por submercado.
    """

    BLOCKS = [VersaoModeloLibs, TabelaOperDispUsihSubm]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - cenario (`int`)
        - patamar (`int`)
        - codigo_submercado (`int`)
        - nome_submercado (`str`)
        - geracao_hidraulica_maxima_pl (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
