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

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - periodo (`int`)
        - no (`int`)
        - cenario (`int`)
        - patamar (`int`)
        - duracao (`int`)
        - indiceUsina (`int`)
        - nomeUsina (`str`)
        - indiceSubmercado (`int`)
        - nomeSubmercado (`str`)
        - indiceUsinaJusante (`int`)
        - indiceUsinaMontante (`int`)
        - vazaoBombeadaM3S (`float`)
        - energiaBombeamentoMW (`float`)
        - vazaoBombeadaMinimaM3S (`float`)
        - vazaoBombeadaMaximaM3S (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
