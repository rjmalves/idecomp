from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModeloLibs
from idecomp.decomp.modelos.oper_disp_usih_ree import TabelaOperDispUsihRee

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class OperDispUsihRee(ArquivoCSV):
    """
    Arquivo com a disponibilidade das usinas hidroelétricas do DECOMP,
    por REE.
    """

    BLOCKS = [VersaoModeloLibs, TabelaOperDispUsihRee]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - cenario (`int`)
        - patamar (`int`)
        - codigo_ree (`int`)
        - nome_ree (`str`)
        - geracao_hidraulica_maxima_pl (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
