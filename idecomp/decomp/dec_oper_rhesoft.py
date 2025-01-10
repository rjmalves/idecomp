from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_rhesoft import (
    TabelaOperRheSoftv31,
    TabelaOperRheSoft,
)

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecOperRheSoft(ArquivoCSV):
    """
    Arquivo com os resultados de atendimento das restrições de energia
    armazenada mínima (RHE) modeladas com tratamento soft do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperRheSoft]
    VERSIONS = {
        "31.0.2": [VersaoModelo, TabelaOperRheSoftv31],
        "31.1.2": [VersaoModelo, TabelaOperRheSoft],
    }

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - no (`int`)
        - cenario (`int`)
        - codigo_restricao (`int`)
        - limite_MW (`float`)
        - valor_MW (`float`)
        - violacao_absoluta_MW (`float`)
        - violacao_percentual (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
