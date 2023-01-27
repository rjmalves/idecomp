from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_ree import TabelaOperRee

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecOperRee(ArquivoCSV):
    """
    Arquivo com a operação por REE do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperRee]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_oper_ree.csv"
    ) -> "DecOperRee":
        return cls.read(diretorio, arquivo)

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - periodo (`int`)
        - no (`int`)
        - cenario (`int`)
        - indiceRee (`int`)
        - nomeRee (`str`)
        - indiceSubmercado (`int`)
        - nomeSubmercado (`str`)
        - enaMWmes (`float`)
        - earmInicialMWmes (`float`)
        - earmInicialPercentual (`float`)
        - earmFinalMWmes (`float`)
        - earmFinalPercentual (`float`)
        - earmMaximoMWmes (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
