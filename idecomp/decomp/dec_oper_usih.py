from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_oper_usih import TabelaOperUsih

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecOperUsih(ArquivoCSV):
    """
    Arquivo com a operação por usina hidroelétrica do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaOperUsih]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_oper_usih.csv"
    ) -> "DecOperUsih":
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
        - nomeSubmercado (`str`)
        - volumeUtilMaximoHm3 (`float`)
        - volumeUtilInicialHm3 (`float`)
        - volumeUtilInicialPercentual (`float`)
        - volumeUtilFinalHm3 (`float`)
        - volumeUtilFinalPercentual (`float`)
        - geracaoMW (`float`)
        - potenciaInstaladaMW (`float`)
        - potenciaDisponivelMW (`float`)
        - vazaoNaturalM3S (`float`)
        - vazaoNaturalMLT (`float`)
        - vazaoIncrementalM3S (`float`)
        - vazaoMontanteM3S (`float`)
        - vazaoMontanteTVM3S (`float`)
        - vazaoAfluenteM3S (`float`)
        - vazaoDefluenteM3S (`float`)
        - vazaoTurbinadaM3S (`float`)
        - vazaoVertidaM3S (`float`)
        - vazaoDesviadaM3S (`float`)
        - vazaoRecebidaBombeamentoM3S (`float`)
        - vazaoRetiradaBombeamentoM3S (`float`)
        - vazaoRetiradaM3S (`float`)
        - vazaoRetornoM3S (`float`)
        - vazaoEvaporadaM3S (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
