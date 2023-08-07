from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_cortes_evap import TabelaCortesEvap

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class DecCortesEvap(ArquivoCSV):
    """
    Arquivo com os cortes da evaporação linear do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaCortesEvap]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_cortes_evap.csv"
    ) -> "DecCortesEvap":
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
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - codigo_submercado (`int`)
        - codigo_ree (`int`)
        - derivada_cota_area (`float`)
        - derivada_volume_cota (`float`)
        - volume_referencia_hm3 (`float`)
        - evaporacao_referencia_hm3 (`float`)
        - coeficiente_volume (`float`)
        - rhs_volume (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
