from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_gnl import TabelaOperGnl, TabelaOperGnlv31

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class DecOperGnl(ArquivoCSV):
    """
    Arquivo com a operação das usinas térmicas de despacho
    antecipado do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperGnl]
    VERSIONS = {
        "31.0.2": [VersaoModelo, TabelaOperGnlv31],
        "31.1.2": [VersaoModelo, TabelaOperGnl],
    }

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_oper_gnl.csv"
    ) -> "DecOperGnl":
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
        - codigo_usina (`float`)
        - nome_usina (`str`)
        - codigo_submercado (`float`)
        - nome_submercado (`str`)
        - lag (`int`)
        - custo_incremental (`float`)
        - beneficio_gnl (`float`)
        - geracao_minima_MW (`float`)
        - geracao_comandada_MW (`float`)
        - geracao_sinalizada_MW (`float`)
        - geracao_MW (`float`)
        - geracao_maxima_MW (`float`)
        - fator_manutencao (`float`)
        - custo_geracao (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
