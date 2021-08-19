from idecomp._utils.bloco import Bloco
# from idecomp.decomp.modelos.relato import BlocoDadosGeraisRelato
from idecomp.decomp.modelos.relgnl import BlocoDadosUsinasRelGNL
from idecomp.decomp.modelos.relgnl import BlocoComandosUsinasAjustesTGRelGNL
from idecomp.decomp.modelos.relgnl import BlocoComandosUsinasAjustesRERelGNL
from idecomp.decomp.modelos.relgnl import LeituraRelGNL
from idecomp._utils.arquivo import ArquivoBlocos
from idecomp._utils.dadosarquivo import DadosArquivoBlocos
from typing import Type
import pandas as pd  # type: ignore


class RelGNL(ArquivoBlocos):
    """
    Armazena os dados de saída do DECOMP referentes às térmicas de
    despacho antecipado (GNL).

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP e reproduzidas no `relgnl.rvx`, bem como as saídas finais
    da execução.

    """
    def __init__(self,
                 dados: DadosArquivoBlocos) -> None:
        super().__init__(dados)

    # Override
    @classmethod
    def le_arquivo(cls,
                   diretorio: str,
                   nome_arquivo="relgnl.rv0") -> 'RelGNL':
        """
        """
        leitor = LeituraRelGNL(diretorio)
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
    def usinas_termicas(self) -> pd.DataFrame:
        """
        Tabela de informações das usinas térmicas GNL.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoDadosUsinasRelGNL)
        return b.dados

    @property
    def comandos_usinas_registros_tg(self) -> pd.DataFrame:
        """
        Tabela de comandos das usinas térmicas GNL com ajustes
        devido aos registros TG.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoComandosUsinasAjustesTGRelGNL)
        return b.dados

    @property
    def comandos_usinas_restricoes_eletricas(self) -> pd.DataFrame:
        """
        Tabela de comandos das usinas térmicas GNL com ajustes
        devido a restrições elétricas especiais.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoComandosUsinasAjustesRERelGNL)
        return b.dados
