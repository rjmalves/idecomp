from idecomp._utils.bloco import Bloco
from idecomp.decomp.modelos.inviabunic import BlocoInviabilidadesIteracoes
from idecomp.decomp.modelos.inviabunic import BlocoInviabilidadesSimFinal
from idecomp.decomp.modelos.inviabunic import LeituraInviabUnic
from idecomp._utils.arquivo import ArquivoBlocos
from idecomp._utils.dadosarquivo import DadosArquivoBlocos
from typing import Type
import pandas as pd  # type: ignore


class InviabUnic(ArquivoBlocos):
    """
    Armazena os dados de saída do DECOMP referentes às inviabilidades
    ocorridas durante o processo de execução.

    Esta classe lida com as informações de saída fornecidas pelo
    DECOMP e reproduzidas no `inviab_unic.rvx`.

    """
    def __init__(self,
                 dados: DadosArquivoBlocos) -> None:
        super().__init__(dados)

    # Override
    @classmethod
    def le_arquivo(cls,
                   diretorio: str,
                   nome_arquivo="inviab_unic.rv0") -> 'InviabUnic':
        """
        Realiza a leitura de um arquivo "inviab_unic.rvx" existente em
        um diretório.

        :param diretorio: O caminho relativo ou completo para o diretório
            onde se encontra o arquivo
        :type diretorio: str
        :param nome_arquivo: Nome do arquivo a ser lido, potencialmente
            especificando a revisão. Tem como valor default "inviab_unic.rv0"
        :type nome_arquivo: str, optional
        :return: Um objeto :class:`InviabUnic` com informações do arquivo lido
        """
        leitor = LeituraInviabUnic(diretorio)
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
    def inviabilidades_iteracoes(self) -> pd.DataFrame:
        """
        Tabela das inviabilidades visitadas pelo modelo durante
        as iterações. As colunas são:

        - Iteração (`int`): iteração de ocorrência da inviabilidade
        - FWD/BWD (`int`): momento de ocorrência da inviabilidade (0/1)
        - Estágio (`int`): estágio da ocorrência da inviabilidade
        - Cenário (`int`): cenário da ocorrência da inviabilidade
        - Restrição (`str`): mensagem da restrição como no arquivo
        - Violação (`float`): quantidade de violação da restrição
        - Unidade (`str`): unidade de medição da restrição violada

        :return: Tabela das inviabilidades no mesmo formato do
            arquivo `inviab_unic.rvX`.
        :rtype: pd.DataFrame
        """
        b = self.__obtem_bloco(BlocoInviabilidadesIteracoes)
        return b.dados

    @property
    def inviabilidades_simulacao_final(self) -> pd.DataFrame:
        """
        Tabela das inviabilidades visitadas pelo modelo durante
        a simulação final. As colunas são:

        - Estágio (`int`): estágio da ocorrência da inviabilidade
        - Cenário (`int`): cenário da ocorrência da inviabilidade
        - Restrição (`str`): mensagem da restrição como impressa
        - Violação (`float`): quantidade de violação da restrição
        - Unidade (`str`): unidade de medição da restrição violada

        :return: Tabela das inviabilidades no mesmo formato do
            arquivo `inviab_unic.rvX`.
        :rtype: pd.DataFrame
        """
        b = self.__obtem_bloco(BlocoInviabilidadesSimFinal)
        return b.dados
