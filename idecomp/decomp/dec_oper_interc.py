from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_interc import TabelaOperInterc

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecOperInterc(ArquivoCSV):
    """
    Arquivo com a operação dos intercâmbios do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperInterc]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - periodo (`int`)
        - no (`int`)
        - cenario (`int`)
        - patamar (`int`)
        - indiceSubmercadoDe (`int`)
        - nomeSubmercadoDe (`str`)
        - indiceSubmercadoPara (`int`)
        - nomeSubmercadoPara (`str`)
        - intercambioOrigemMW (`float`)
        - intercambioDestinoMW (`float`)
        - perdasMW (`float`)
        - fatorPerdas (`float`)
        - capacidadeMW (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
