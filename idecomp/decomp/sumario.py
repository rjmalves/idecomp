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
        Realiza a leitura de um arquivo "sumario.rvx" existente em
        um diretório.

        :param diretorio: O caminho relativo ou completo para o diretório
            onde se encontra o arquivo
        :type diretorio: str
        :param nome_arquivo: Nome do arquivo a ser lido, potencialmente
            especificando a revisão. Tem como valor default "sumario.rv0"
        :type nome_arquivo: str, optional
        :return: Um objeto :class:`Sumario` com informações do arquivo lido
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
        Obtém a tabela de CMO existente no :class:`Sumario`

        :return: A tabela de CMO como um `pd.DataFrame`.
        """
        b = self.__obtem_bloco(BlocoCMOSumario)
        return b.dados

    @property
    def geracao_termica_subsistema(self) -> pd.DataFrame:
        """
        Obtém a tabela de Geração Térmica existente no :class:`Sumario`

        :return: A tabela de Geração Térmica como um `pd.DataFrame`.
        """
        b = self.__obtem_bloco(BlocoGeracaoTermicaSubsistemaSumario)
        return b.dados

    @property
    def energia_armazenada_ree(self) -> pd.DataFrame:
        """
        Obtém a tabela de Energia Armazenada por REE (em %)
        existente no :class:`Sumario`

        :return: A tabela de EARM como um `pd.DataFrame`.
        """
        b = self.__obtem_bloco(BlocoEnergiaArmazenadaREESumario)
        return b.dados

    @property
    def energia_armazenada_subsistema(self) -> pd.DataFrame:
        """
        Obtém a tabela de Energia Armazenada por Subsistema (em %)
        existente no :class:`Sumario`

        :return: A tabela de EARM como um `pd.DataFrame`.
        """
        b = self.__obtem_bloco(BlocoEnergiaArmazenadaSubsistemaSumario)
        return b.dados
