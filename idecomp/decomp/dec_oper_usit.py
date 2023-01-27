from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_usit import TabelaOperUsit

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecOperUsit(ArquivoCSV):
    """
    Arquivo com a operação por usina termoelétrica do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperUsit]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_oper_usit.csv"
    ) -> "DecOperUsit":
        return cls.read(diretorio, arquivo)

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - periodo (`int`)
        - no (`int`)
        - cenario (`int`)
        - patamar (`int`)
        - duracao (`float`)
        - indiceUsina (`int`)
        - nomeUsina (`str`)
        - indiceSubmercado (`int`)
        - nomeSubmercado (`str`)
        - custoIncremental (`float`)
        - geracaoMinimaMW (`float`)
        - geracaoMW (`float`)
        - fatorManutencao (`float`)
        - geracaoMaximaMW (`float`)
        - custoGeracao (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
