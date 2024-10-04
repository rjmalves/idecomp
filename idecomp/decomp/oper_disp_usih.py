from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModeloLibs
from idecomp.decomp.modelos.oper_disp_usih import TabelaOperDispUsih

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class OperDispUsih(ArquivoCSV):
    """
    Arquivo com a disponibilidade das usinas hidroelétricas do DECOMP.
    """

    BLOCKS = [VersaoModeloLibs, TabelaOperDispUsih]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - cenario (`int`)
        - patamar (`int`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - codigo_submercado (`int`)
        - nome_submercado (`str`)
        - volume_inicial_hm3 (`float`)
        - volume_final_hm3 (`float`)
        - vazao_vertida_m3s (`float`)
        - vazao_turbinada_m3s (`float`)
        - vazao_turbinada_maxima_m3s (`float`)
        - geracao_hidraulica (`float`)
        - geracao_hidraulica_maxima (`float`)
        - geracao_hidraulica_maxima_pl (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
