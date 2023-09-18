from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_sist import (
    TabelaOperSist,
    TabelaOperSistv31,
)

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class DecOperSist(ArquivoCSV):
    """
    Arquivo com a operação por submercado do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperSist]
    VERSIONS = {
        "31.0.2": [VersaoModelo, TabelaOperSistv31],
        "31.1.2": [VersaoModelo, TabelaOperSist],
    }

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_oper_sist.csv"
    ) -> "DecOperSist":
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
        - codigo_submercado (`int`)
        - nome_submercado (`str`)
        - demanda_MW (`float`)
        - geracao_pequenas_usinas_MW (`float`)
        - geracao_termica_MW (`float`)
        - geracao_termica_antecipada_MW (`float`)
        - geracao_hidroeletrica_MW (`float`)
        - geracao_eolica_MW (`float`)
        - energia_bombeamento_MW (`float`)
        - energia_importada_MW (`float`)
        - energia_exportada_MW (`float`)
        - intercambio_liquido_MW (`float`)
        - itaipu_50MW (`float`)
        - itaipu_60MW (`float`)
        - deficit_MW (`float`)
        - ena_MWmes (`float`)
        - earm_inicial_MWmes (`float`)
        - earm_inicial_percentual (`float`)
        - earm_final_MWmes (`float`)
        - earm_final_percentual (`float`)
        - cmo (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
