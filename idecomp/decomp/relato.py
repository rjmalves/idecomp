from idecomp._utils.bloco import Bloco
# from idecomp.decomp.modelos.relato import BlocoDadosGeraisRelato
from idecomp.decomp.modelos.relato import BlocoRelatorioOperacaoUHERelato
from idecomp.decomp.modelos.relato import BlocoBalancoEnergeticoRelato
from idecomp.decomp.modelos.relato import BlocoCMORelato
from idecomp.decomp.modelos.relato import BlocoGeracaoTermicaSubsistemaRelato
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
    def relatorio_operacao_uhe(self) -> pd.DataFrame:
        """
        Tabela com o relatório de operação por UHE e por
        estágio de execução do DECOMP.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

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
        Tabela de balanço energético médio entre os patamares
        para cada estágio e subsistema.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

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
        Custo Marginal de Operação (CMO) médio por subsistema
        e por semana.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoCMORelato)
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
        b = self.__obtem_bloco(BlocoGeracaoTermicaSubsistemaRelato)
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
        b = self.__obtem_bloco(BlocoEnergiaArmazenadaREERelato)
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
        b = self.__obtem_bloco(BlocoEnergiaArmazenadaSubsistemaRelato)
        return b.dados

    @property
    def ena_pre_estudo_semanal_subsistema(self) -> pd.DataFrame:
        """
        Tabela com a ENA pré-estudo por subsistema
        e por semana.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoENAPreEstudoSemanalSubsistemaRelato)
        return b.dados

    @property
    def energia_armazenada_maxima_subsistema(self) -> pd.DataFrame:
        """
        Tabela com a EARMax (Mwmes) por subsistema.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoENAPreEstudoSemanalSubsistemaRelato)
        return b.dados[["Subsistema", "Earmax"]]

    @property
    def dias_excluidos_semana_inicial(self) -> int:
        """
        Número de dias excluídos na semana inicial de estudo.

        **Retorna**

        `int`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoDiasExcluidosSemanas)
        return b.dados[0]

    @property
    def dias_excluidos_semana_final(self) -> int:
        """
        Número de dias excluídos na semana final de estudo.

        **Retorna**

        `int`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoDiasExcluidosSemanas)
        return b.dados[1]
