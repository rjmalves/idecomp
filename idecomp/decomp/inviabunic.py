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
                   nome_arquivo="inviab_unic.rv0") -> 'InviabUnic':
        """
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
        o processo iterativo.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoInviabilidadesIteracoes)
        return b.dados

    @property
    def inviabilidades_simulacao_final(self) -> pd.DataFrame:
        """
        Tabela das inviabilidades visitadas pelo modelo durante
        a simulação final.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b = self.__obtem_bloco(BlocoInviabilidadesSimFinal)
        return b.dados
