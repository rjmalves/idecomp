from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_usie import (
    TabelaOperUsie,
    TabelaOperUsiev31,
)

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecOperUsie(ArquivoCSV):
    """
    Arquivo com a operação por estação elevatória do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperUsie]
    VERSIONS = {
        "31.0.2": [VersaoModelo, TabelaOperUsiev31],
        "31.1.2": [VersaoModelo, TabelaOperUsie],
    }

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - no (`int`)
        - cenario (`int`)
        - patamar (`int`)
        - duracao (`int`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - codigo_submercado (`int`)
        - nome_submercado (`str`)
        - codigo_usina_jusante (`int`)
        - codigo_usina_montante (`int`)
        - vazao_bombeada_m3s (`float`)
        - energia_bombeamento_MW (`float`)
        - vazao_bombeada_minima_m3s (`float`)
        - vazao_bombeada_maxima_m3s (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
