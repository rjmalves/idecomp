from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_gnl import TabelaOperGnl, TabelaOperGnlv31

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecOperGnl(ArquivoCSV):
    """
    Arquivo com a operação das usinas térmicas de despacho
    antecipado do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperGnl]
    VERSIONS = {
        "31.0.2": [VersaoModelo, TabelaOperGnlv31],
        "31.1.2": [VersaoModelo, TabelaOperGnl],
    }

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - no (`int`)
        - cenario (`int`)
        - patamar (`int`)
        - duracao (`float`)
        - codigo_usina (`float`)
        - nome_usina (`str`)
        - codigo_submercado (`float`)
        - nome_submercado (`str`)
        - lag (`int`)
        - custo_incremental (`float`)
        - beneficio_gnl (`float`)
        - geracao_minima_MW (`float`)
        - geracao_comandada_MW (`float`)
        - geracao_sinalizada_MW (`float`)
        - geracao_MW (`float`)
        - geracao_maxima_MW (`float`)
        - fator_manutencao (`float`)
        - custo_geracao (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
