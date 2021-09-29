from idecomp.decomp.modelos.postos import LeituraPostos
from idecomp._utils.arquivo import ArquivoBinario
from idecomp._utils.escritabinario import EscritaBinario
from idecomp._utils.dadosarquivo import DadosArquivoBinarios
import pandas as pd  # type: ignore


class Postos(ArquivoBinario):
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

    # Override
    @classmethod
    def le_arquivo(cls,
                   diretorio: str,
                   nome_arquivo="postos.dat") -> 'Postos':
        """
        """
        leitor = LeituraPostos(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    # Override
    def escreve_arquivo(self,
                        diretorio: str,
                        nome_arquivo: str = "postos.dat"):
        """
        """
        escritor = EscritaBinario(diretorio)
        escritor.escreve_arquivo(self._dados, nome_arquivo)

    @property
    def postos(self) -> pd.DataFrame:
        """
        """
        nome = [b.dados[0] for b in self._dados.blocos]
        ano_inicial = [b.dados[1] for b in self._dados.blocos]
        ano_final = [b.dados[2] for b in self._dados.blocos]
        df = pd.DataFrame(index=list(range(1, len(nome) + 1)))
        df["Nome"] = nome
        df["Ano Inicial Histórico"] = ano_inicial
        df["Ano Final Histórico"] = ano_final
        return df

    @postos.setter
    def postos(self, p: pd.DataFrame):
        n_postos = p.shape[0]
        n_postos_arquivo = self.postos.shape[0]
        if n_postos != n_postos_arquivo:
            raise ValueError(f"Número de postos incompatível ({n_postos})")
        for i in range(n_postos):
            self._dados.blocos[i]._dados = p.iloc[i, :].tolist()
