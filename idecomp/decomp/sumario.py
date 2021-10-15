from idecomp._utils.bloco import Bloco
from idecomp.decomp.modelos.sumario import BlocoCMOSumario
from idecomp.decomp.modelos.sumario import BlocoGeracaoTermicaSubsistemaSumario
from idecomp.decomp.modelos.sumario import BlocoEnergiaArmazenadaREESumario
from idecomp.decomp.modelos.sumario import BlocoEnergiaArmazenadaSubsistemaSumario  # noqa
from idecomp.decomp.modelos.sumario import LeituraSumario
from idecomp._utils.arquivo import ArquivoBlocos
from idecomp._utils.dadosarquivo import DadosArquivoBlocos
from typing import Type
import pandas as pd  # type: ignore


class Sumario(ArquivoBlocos):
    """
    Armazena os dados de saída do DECOMP referentes ao
    acompanhamento do programa.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP e reproduzidas no `sumario.rvx`, bem como as saídas finais
    da execução: custos de operação, despacho de térmicas, etc.

    """
    def __init__(self,
                 dados: DadosArquivoBlocos) -> None:
        super().__init__(dados)

    # Override
    @classmethod
    def le_arquivo(cls,
                   diretorio: str,
                   nome_arquivo="sumario.rv0") -> 'Sumario':
        """
        """
        leitor = LeituraSumario(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    def __obtem_bloco(self, tipo: Type[Bloco]) -> Bloco:
        """
        """
        for b in self._blocos:
            if isinstance(b, tipo):
                return b
        raise ValueError(f"Não foi encontrado um bloco do tipo {tipo}")

    @property
    def cmo_medio_subsistema(self) -> pd.DataFrame:
        """
        Custo Marginal de Operação (CMO) médio por subsistema
        e por semana.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoCMOSumario)
        return b.dados

    @property
    def geracao_termica_subsistema(self) -> pd.DataFrame:
        """
        Tabela com a Geração Térmica por subsistema
        e por semana.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoGeracaoTermicaSubsistemaSumario)
        return b.dados

    @property
    def energia_armazenada_ree(self) -> pd.DataFrame:
        """
        Tabela com a Energia Armazenada (%) por REE
        e por semana.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoEnergiaArmazenadaREESumario)
        return b.dados

    @property
    def energia_armazenada_subsistema(self) -> pd.DataFrame:
        """
        Tabela com a Energia Armazenada (%) por subsistema
        e por semana.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoEnergiaArmazenadaSubsistemaSumario)
        return b.dados
