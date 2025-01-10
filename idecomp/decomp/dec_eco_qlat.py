from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_eco_qlat import TabelaEcoQlat

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecEcoQlat(ArquivoCSV):
    """
    Arquivo com o eco dos dados para cálculo
    da vazão de jusante das usinas hidrelétricas.
    """

    BLOCKS = [VersaoModelo, TabelaEcoQlat]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - fator_participacao_usina (`float`)
        - tipo_entidade_jusante (`str`)
        - codigo_entidade_jusante (`int`)
        - fator_participacao_entidade (`float`)
        - vazao_incremental_media_m3s (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
