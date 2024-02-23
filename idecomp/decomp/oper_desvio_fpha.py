from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModeloLibs
from idecomp.decomp.modelos.oper_desvio_fpha import TabelaOperDesvioFpha

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class OperDesvioFpha(ArquivoCSV):
    """
    Arquivo com os desvios da função de produção por usina hidroelétrica do DECOMP.
    """

    BLOCKS = [VersaoModeloLibs, TabelaOperDesvioFpha]

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - estagio (`int`)
        - cenario (`int`)
        - patamar (`int`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - vazao_turbinada_m3s (`float`)
        - vazao_vertida_m3s (`float`)
        - volume_inicial_hm3 (`float`)
        - volume_final_hm3 (`float`)
        - volume_medio_hm3 (`float`)
        - altura_montante (`float`)
        - vazao_lateral_usina_m3s (`float`)
        - vazao_lateral_posto_m3s (`float`)
        - vazao_jusante_m3s (`float`)
        - altura_jusante (`float`)
        - altura_liquida (`float`)
        - perdas_hidraulicas (`float`)
        - produtibilidade_especifica (`float`)
        - geracao_hidraulica_pl (`float`)
        - geracao_hidraulica_fpha (`float`)
        - geracao_hidraulica_fph (`float`)
        - desvio_absoluto_pl_fph (`float`)
        - desvio_percentual_pl_fph (`float`)
        - desvio_absoluto_pl_fpha (`float`)
        - desvio_percentual_pl_fpha (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
