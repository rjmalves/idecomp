from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_usih import (
    TabelaOperUsihv31,
    TabelaOperUsih,
)

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class DecOperUsih(ArquivoCSV):
    """
    Arquivo com a operação por usina hidroelétrica do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperUsih]
    VERSIONS = {
        "31.0.2": [VersaoModelo, TabelaOperUsihv31],
        "31.1.2": [VersaoModelo, TabelaOperUsih],
    }

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_oper_usih.csv"
    ) -> "DecOperUsih":
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
        - nome_submercado (`str`)
        - volume_util_maximo_hm3 (`float`)
        - volume_util_inicial_hm3 (`float`)
        - volume_util_inicial_percentual (`float`)
        - volume_util_final_hm3 (`float`)
        - volume_util_final_percentual (`float`)
        - geracao_MW (`float`)
        - potencia_instalada_MW (`float`)
        - potencia_disponivel_MW (`float`)
        - vazao_natural_m3s (`float`)
        - vazao_natural_mlt (`float`)
        - vazao_incremental_m3s (`float`)
        - vazao_montante_m3s (`float`)
        - vazao_montante_tv_m3s (`float`)
        - vazao_afluente_m3s (`float`)
        - vazao_defluente_m3s (`float`)
        - vazao_turbinada_m3s (`float`)
        - vazao_vertida_m3s (`float`)
        - vazao_desviada_m3s (`float`)
        - vazao_recebida_bombeamento_m3s (`float`)
        - vazao_retirada_bombeamento_m3s (`float`)
        - vazao_retirada_m3s (`float`)
        - vazao_retorno_m3s (`float`)
        - vazao_evaporada_m3s (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
