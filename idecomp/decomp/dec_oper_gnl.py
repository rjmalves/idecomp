from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_gnl import TabelaOperGnl

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecOperGnl(ArquivoCSV):
    """
    Arquivo com a operação das usinas térmicas de despacho
    antecipado do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperGnl]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_oper_gnl.csv"
    ) -> "DecOperGnl":
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
        - indiceUsina (`float`)
        - nomeUsina (`str`)
        - indiceSubmercado (`float`)
        - nomeSubmercado (`str`)
        - lag (`int`)
        - custoIncremental (`float`)
        - beneficioGNL (`float`)
        - geracaoMinimaMW (`float`)
        - geracaoComandadaMW (`float`)
        - geracaoSinalizadaMW (`float`)
        - geracaoMW (`float`)
        - geracaoMaximaMW (`float`)
        - fatorManutencao (`float`)
        - custoGeracao (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
