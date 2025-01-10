from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.eco_fpha import TabelaEcoFpha

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class EcoFpha(ArquivoCSV):
    """
    Arquivo com o eco dos dados para modelagem da
    função de produção para as usinas hidrelétricas.
    """

    BLOCKS = [VersaoModelo, TabelaEcoFpha]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - codigo_usina (`int`)
        - estagio (`int`)
        - nome_usina (`str`)
        - tipo (`int`)
        - conv (`int`)
        - alfa (`int`)
        - rems (`int`)
        - numero_pontos_vazao_turbinada (`int`)
        - vazao_turbinada_minima (`float`)
        - vazao_turbinada_maxima (`float`)
        - numero_pontos_volume_armazenado (`int`)
        - volume_armazenado_minimo (`float`)
        - volume_armazenado_maximo (`float`)
        - geracao_minima (`float`)
        - geracao_maxima (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
