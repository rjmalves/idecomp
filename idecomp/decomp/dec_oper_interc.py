from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_interc import (
    TabelaOperInterc,
    TabelaOperIntercv31,
)

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecOperInterc(ArquivoCSV):
    """
    Arquivo com a operação dos intercâmbios do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperInterc]
    VERSIONS = {
        "31.0.2": [VersaoModelo, TabelaOperIntercv31],
        "31.1.2": [VersaoModelo, TabelaOperInterc],
    }

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - no (`int`)
        - cenario (`int`)
        - patamar (`int`)
        - codigo_submercado_de (`int`)
        - nome_submercado_de (`str`)
        - codigo_submercado_para (`int`)
        - nome_submercado_para (`str`)
        - intercambio_origem_MW (`float`)
        - intercambio_destino_MW (`float`)
        - perdas_MW (`float`)
        - fator_perdas (`float`)
        - capacidade_MW (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
