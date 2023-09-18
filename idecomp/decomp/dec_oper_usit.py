from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_usit import (
    TabelaOperUsit,
    TabelaOperUsitv31,
)

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class DecOperUsit(ArquivoCSV):
    """
    Arquivo com a operação por usina termoelétrica do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperUsit]
    VERSIONS = {
        "31.0.2": [VersaoModelo, TabelaOperUsitv31],
        "31.1.2": [VersaoModelo, TabelaOperUsit],
    }

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_oper_usit.csv"
    ) -> "DecOperUsit":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, arquivo))

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - periodo (`int`)
        - no (`int`)
        - cenario (`int`)
        - patamar (`int`)
        - duracao (`float`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - codigo_submercado (`int`)
        - nome_submercado (`str`)
        - custo_incremental (`float`)
        - geracao_minima_MW (`float`)
        - geracao_MW (`float`)
        - fator_manutencao (`float`)
        - geracao_maxima_MW (`float`)
        - custo_geracao (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
