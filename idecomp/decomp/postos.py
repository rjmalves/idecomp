from idecomp.decomp.modelos.postos import LeituraPostos
from idecomp._utils.arquivo import ArquivoBinario
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

    @property
    def postos(self) -> pd.DataFrame:
        """
        """
        nome = [b.dados[0] for b in self._dados.blocos]
        ano_inicial = [b.dados[1] for b in self._dados.blocos]
        ano_final = [b.dados[2] for b in self._dados.blocos]
        df = pd.DataFrame(index=range(1, len(nome) + 1))
        df["Nome"] = nome
        df["Ano Inicial Histórico"] = ano_inicial
        df["Ano Final Histórico"] = ano_final
        return df
