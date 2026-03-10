import pandas as pd  # type: ignore

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_avl_evap import TabelaAvlEvap


class DecAvlEvap(ArquivoCSV):
    """
    Arquivo com a avaliação da evaporação linear do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaAvlEvap]

    @property
    def tabela(self) -> pd.DataFrame | None:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - codigo_submercado (`int`)
        - codigo_ree (`int`)
        - volume_armazenado_hm3 (`float`)
        - evaporacao_calculada_hm3 (`float`)
        - evaporacao_modelo_hm3 (`float`)
        - desvio_absoluto_hm3 (`float`)
        - desvio_percentual (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
