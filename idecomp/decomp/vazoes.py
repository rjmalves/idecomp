from idecomp.decomp.modelos.vazoes import LeituraVazoes
from idecomp._utils.arquivo import ArquivoBinario
from idecomp._utils.escritabinario import EscritaBinario
from idecomp._utils.dadosarquivo import DadosArquivoBinarios
import pandas as pd  # type: ignore
import numpy as np  # type: ignore


class Vazoes(ArquivoBinario):
    """
    Armazena os dados de saída do DECOMP referentes às térmicas de
    despacho antecipado (GNL).

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP e reproduzidas no `relgnl.rvx`, bem como as saídas finais
    da execução.

    """
    def __init__(self,
                 dados: DadosArquivoBinarios) -> None:
        super().__init__(dados)
        self.__df = None

    # Override
    @classmethod
    def le_arquivo(cls,
                   diretorio: str,
                   nome_arquivo="vazoes.dat") -> 'Vazoes':
        """
        """
        leitor = LeituraVazoes(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    # Override
    def escreve_arquivo(self,
                        diretorio: str,
                        nome_arquivo: str = "vazoes.dat"):
        """
        """
        escritor = EscritaBinario(diretorio)
        escritor.escreve_arquivo(self._dados, nome_arquivo)

    def __calcula_df(self):
        tabela_dados = np.zeros((12000, 600), dtype="int32")
        i = 0
        for b in self._blocos:
            tabela_dados[i, :] = np.array(b._dados)
            i += 1
        tabela_dados = tabela_dados[:i, :]
        colunas = [f"Posto {i}" for i in
                   range(1, tabela_dados.shape[1] + 1)]
        self.__df = pd.DataFrame(tabela_dados,
                                 columns=colunas)

    @property
    def vazoes(self) -> pd.DataFrame:
        """
        """
        if self.__df is None:
            self.__calcula_df()
        return self.__df

    @vazoes.setter
    def vazoes(self, df: pd.DataFrame):
        nova_tabela = df.to_numpy()
        for i, b in enumerate(self._blocos):
            b._dados = list(nova_tabela[i, :])
        self.__df = None
