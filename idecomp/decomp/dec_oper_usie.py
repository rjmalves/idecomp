from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_usie import TabelaOperUsie

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecOperUsie(ArquivoCSV):
    """
    Arquivo com a operação por estação elevatória do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperUsie]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_oper_usit.csv"
    ) -> "DecOperUsie":
        return cls.read(diretorio, arquivo)

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - periodo (`int`)
        - no (`int`)
        - cenario (`int`)
        - patamar (`int`)
        - duracao (`int`)
        - indice_usina (`int`)
        - nome_usina (`str`)
        - indice_submercado (`int`)
        - nome_submercado (`str`)
        - indice_usina_jusante (`int`)
        - indice_usina_montante (`int`)
        - vazao_bombeada_m3s (`float`)
        - energia_bombeamento_MW (`float`)
        - vazao_bombeada_minima_m3s (`float`)
        - vazao_bombeada_maxima_m3s (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
