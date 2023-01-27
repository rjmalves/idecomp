from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_sist import TabelaOperSist

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecOperSist(ArquivoCSV):
    """
    Arquivo com a operação por submercado do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperSist]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_oper_sist.csv"
    ) -> "DecOperSist":
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
        - indiceSubmercado (`int`)
        - nomeSubmercado (`str`)
        - demandaMW (`float`)
        - geracaoPequenasUsinasMW (`float`)
        - geracaoTermicaMW (`float`)
        - geracaoTermicaAntecipadaMW (`float`)
        - geracaoHidroeletricaMW (`float`)
        - geracaoEolicaMW (`float`)
        - energiaBombeamentoMW (`float`)
        - energiaImportadaMW (`float`)
        - energiaExportadaMW (`float`)
        - intercambioLiquidoMW (`float`)
        - itaipu50MW (`float`)
        - itaipu60MW (`float`)
        - deficitMW (`float`)
        - enaMWmes (`float`)
        - earmInicialMWmes (`float`)
        - earmInicialPercentual (`float`)
        - earmFinalMWmes (`float`)
        - earmFinalPercentual (`float`)
        - cmo (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
