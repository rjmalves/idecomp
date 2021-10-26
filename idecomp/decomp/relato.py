from idecomp._utils.bloco import Bloco
# from idecomp.decomp.modelos.relato import BlocoDadosGeraisRelato
from idecomp.decomp.modelos.relato import BlocoConvergenciaRelato
from idecomp.decomp.modelos.relato import BlocoRelatorioOperacaoUHERelato
from idecomp.decomp.modelos.relato import BlocoBalancoEnergeticoRelato
from idecomp.decomp.modelos.relato import BlocoCMORelato
from idecomp.decomp.modelos.relato import BlocoGeracaoTermicaSubsistemaRelato
from idecomp.decomp.modelos.relato import BlocoVolumeUtilReservatorioRelato
from idecomp.decomp.modelos.relato import BlocoEnergiaArmazenadaREERelato
from idecomp.decomp.modelos.relato import BlocoEnergiaArmazenadaSubsistemaRelato  # noqa
from idecomp.decomp.modelos.relato import BlocoENAPreEstudoSemanalSubsistemaRelato  # noqa
from idecomp.decomp.modelos.relato import BlocoDiasExcluidosSemanas
from idecomp.decomp.modelos.relato import LeituraRelato
from idecomp._utils.arquivo import ArquivoBlocos
from idecomp._utils.dadosarquivo import DadosArquivoBlocos
from typing import Type, List
import pandas as pd  # type: ignore


class Relato(ArquivoBlocos):
    """
    Armazena os dados de saída do DECOMP referentes ao
    acompanhamento do programa.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP e reproduzidas no `relato.rvx`, bem como as saídas finais
    da execução: custos de operação, despacho de térmicas, etc.

    """
    def __init__(self,
                 dados: DadosArquivoBlocos) -> None:
        super().__init__(dados)

    # Override
    @classmethod
    def le_arquivo(cls,
                   diretorio: str,
                   nome_arquivo="relato.rv0") -> 'Relato':
        """
        Realiza a leitura de um arquivo "relato.rvx" existente em
        um diretório.

        :param diretorio: O caminho relativo ou completo para o diretório
            onde se encontra o arquivo
        :type diretorio: str
        :param nome_arquivo: Nome do arquivo a ser lido, potencialmente
            especificando a revisão. Tem como valor default "relato.rv0"
        :type nome_arquivo: str, optional
        :return: Um objeto :class:`Relato` com informações do arquivo lido
        """
        leitor = LeituraRelato(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    def __obtem_bloco(self, tipo: Type[Bloco]) -> Bloco:
        """
        """
        for b in self._blocos:
            if isinstance(b, tipo):
                return b
        raise ValueError(f"Não foi encontrado um bloco do tipo {tipo}")

    def __obtem_blocos(self, tipo: Type[Bloco]) -> List[Bloco]:
        """
        """
        blocos = []
        for b in self._blocos:
            if isinstance(b, tipo):
                blocos.append(b)
        if len(blocos) == 0:
            raise ValueError(f"Não foi encontrado um bloco do tipo {tipo}")
        return blocos

    @property
    def convergencia(self) -> pd.DataFrame:
        """
        Obtém a tabela de convergência do DECOMP existente no
        :class:`Relato`

        :return: A tabela de convergência como um `pd.DataFrame`.
        """
        b = self.__obtem_bloco(BlocoConvergenciaRelato)
        return b.dados

    @property
    def relatorio_operacao_uhe(self) -> pd.DataFrame:
        """
        Obtém a tabela de operação de cada UHE por estágio do DECOMP
        existente no :class:`Relato`

        :return: O relatório de operação como um `pd.DataFrame`.
        """
        relatorios = self.__obtem_blocos(BlocoRelatorioOperacaoUHERelato)
        relat_final = None
        for i, r in enumerate(relatorios):
            df_r: pd.DataFrame = r.dados.copy()
            cols_sem_estagio = list(df_r.columns)
            df_r["Estágio"] = i + 1
            df_r = df_r[["Estágio"] + cols_sem_estagio]
            if relat_final is None:
                relat_final = df_r
            else:
                relat_final = pd.concat([relat_final, df_r], ignore_index=True)
        return relat_final

    @property
    def balanco_energetico(self) -> pd.DataFrame:
        """
        Obtém a tabela de balanço energético entre os patamares para
        cada estágio do DECOMP existente no :class:`Relato`

        :return: O relatório de balanço energético como um `pd.DataFrame`.
        """
        balancos = self.__obtem_blocos(BlocoBalancoEnergeticoRelato)
        balanc_final = None
        for i, r in enumerate(balancos):
            df_r: pd.DataFrame = r.dados.copy()
            cols_sem_estagio = list(df_r.columns)
            df_r["Estágio"] = i + 1
            df_r = df_r[["Estágio"] + cols_sem_estagio]
            if balanc_final is None:
                balanc_final = df_r
            else:
                balanc_final = pd.concat([balanc_final, df_r],
                                         ignore_index=True)
        return balanc_final

    @property
    def cmo_medio_subsistema(self) -> pd.DataFrame:
        """
        Obtém a tabela de CMO existente no :class:`Relato`

        :return: A tabela de CMO como um `pd.DataFrame`.
        """
        b = self.__obtem_bloco(BlocoCMORelato)
        return b.dados

    @property
    def geracao_termica_subsistema(self) -> pd.DataFrame:
        """
        Obtém a tabela de Geração Térmica existente no :class:`Relato`

        :return: A tabela de Geração Térmica como um `pd.DataFrame`.
        """
        b = self.__obtem_bloco(BlocoGeracaoTermicaSubsistemaRelato)
        return b.dados

    @property
    def energia_armazenada_ree(self) -> pd.DataFrame:
        """
        Obtém a tabela de Energia Armazenada por REE (em %)
        existente no :class:`Relato`

        :return: A tabela de EARM como um `pd.DataFrame`.
        """
        b = self.__obtem_bloco(BlocoEnergiaArmazenadaREERelato)
        return b.dados

    @property
    def energia_armazenada_subsistema(self) -> pd.DataFrame:
        """
        Obtém a tabela de Energia Armazenada por Subsistema (em %)
        existente no :class:`Relato`

        :return: A tabela de EARM como um `pd.DataFrame`.
        """
        b = self.__obtem_bloco(BlocoEnergiaArmazenadaSubsistemaRelato)
        return b.dados

    @property
    def volume_util_reservatorios(self) -> pd.DataFrame:
        """
        Obtém a tabela de Volumes Úteis por reservatório (em %)
        existente no :class:`Relato`

        :return: A tabela de volumes como um `pd.DataFrame`.
        """
        b = self.__obtem_bloco(BlocoVolumeUtilReservatorioRelato)
        return b.dados

    @property
    def ena_pre_estudo_semanal_subsistema(self) -> pd.DataFrame:
        """
        Obtém a tabela de ENA Pré-Estudo Semanal
        existente no :class:`Relato`

        :return: A tabela de ENA como um `pd.DataFrame`.
        """
        b = self.__obtem_bloco(BlocoENAPreEstudoSemanalSubsistemaRelato)
        return b.dados

    @property
    def energia_armazenada_maxima_subsistema(self) -> pd.DataFrame:
        """
        Obtém a tabela de Energia Armazenada Máxima (EARMax) em MWmes
        por subsistema existente no :class:`Relato`

        :return: A tabela de EARMax como um `pd.DataFrame`.
        """
        b = self.__obtem_bloco(BlocoENAPreEstudoSemanalSubsistemaRelato)
        return b.dados[["Subsistema", "Earmax"]]

    @property
    def dias_excluidos_semana_inicial(self) -> int:
        """
        Obtém o número de dias excluídos da semana inicial.

        :return: O número de dias como um `int`.
        """
        b = self.__obtem_bloco(BlocoDiasExcluidosSemanas)
        return b.dados[0]

    @property
    def dias_excluidos_semana_final(self) -> int:
        """
        Obtém o número de dias excluídos da semana final.

        :return: O número de dias como um `int`.
        """
        b = self.__obtem_bloco(BlocoDiasExcluidosSemanas)
        return b.dados[1]
