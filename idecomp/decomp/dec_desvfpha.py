from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_desvfpha import TabelaDesvFpha

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class DecDesvFpha(ArquivoCSV):
    """
    Arquivo com os desvios da função de produção por usina hidroelétrica do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaDesvFpha]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_desvfpha.csv"
    ) -> "DecDesvFpha":
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

        - codigo_usina (`int`)
        - periodo (`int`)
        - no (`int`)
        - patamar (`int`)
        - nome_usina (`str`)
        - volume_total_hm3 (`float`)
        - volume_util_percentual (`float`)
        - vazao_turbinada_m3s (`float`)
        - vazao_vertida_m3s (`float`)
        - vazao_jusante_m3s (`float`)
        - vazao_lateral_usina_m3s (`float`)
        - vazao_lateral_posto_m3s (`float`)
        - altura_jusante (`float`)
        - altura_montante (`float`)
        - produtibilidade_especifica (`float`)
        - perdas_hidraulicas (`float`)
        - afogamento (`int`)
        - geracao_hidraulica_fph (`float`)
        - geracao_hidraulica_fpha (`float`)
        - desvio_absoluto_MW (`float`)
        - desvio_percentual (`float`)
        - influencia_vertimento_canal_fuga (`int`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
