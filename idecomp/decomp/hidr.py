from idecomp.decomp.modelos.hidr import LeituraHidr
from idecomp._utils.arquivo import ArquivoBinario
from idecomp._utils.escritabinario import EscritaBinario
from idecomp._utils.dadosarquivo import DadosArquivoBinarios
import pandas as pd  # type: ignore


class Hidr(ArquivoBinario):
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
        self.__df: pd.DataFrame = None

    # Override
    @classmethod
    def le_arquivo(cls,
                   diretorio: str,
                   nome_arquivo="hidr.dat") -> 'Hidr':
        """
        """
        leitor = LeituraHidr(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    # Override
    def escreve_arquivo(self,
                        diretorio: str,
                        nome_arquivo: str = "hidr.dat"):
        """
        """
        escritor = EscritaBinario(diretorio)
        escritor.escreve_arquivo(self._dados, nome_arquivo)

    def __calcula_df(self):

        colunas = [
                   "Nome",
                   "Posto",
                   *[f"Posto BDH {i}" for i in range(1, 9)],
                   "Subsistema",
                   "Empresa",
                   "Posto Jusante",
                   "Desvio",
                   "Volume Mínimo",
                   "Volume Máximo",
                   "Volume Vertedouro",
                   "Volume Desvio",
                   "Cota Mínima",
                   "Cota Máxima",
                   *[f"C{i} CV" for i in range(1, 6)],
                   *[f"C{i} CA" for i in range(1, 6)],
                   *[f"Evaporação Mês {i}" for i in range(1, 13)],
                   "Num. Conjuntos Máquinas",
                   *[f"Num. Máquinas Conjunto {i}" for i in range(1, 6)],
                   *[f"Pot. Conjunto {i}" for i in range(1, 6)],
                   *[f"Ignorado {i}" for i in range(1, 76)],
                   *[f"H Nominal {i}" for i in range(1, 6)],
                   *[f"Q Nominal {i}" for i in range(1, 6)],
                   "Produtibilidade Específica",
                   "Perdas",
                   "Número Pol. Jusante",
                   *[f"C{i} PJUS1" for i in range(1, 6)],
                   *[f"C{i} PJUS2" for i in range(1, 6)],
                   *[f"C{i} PJUS3" for i in range(1, 6)],
                   *[f"C{i} PJUS4" for i in range(1, 6)],
                   *[f"C{i} PJUS5" for i in range(1, 6)],
                   *[f"C{i} PJUS6" for i in range(1, 6)],
                   *[f"C{i} PJUSREF" for i in range(1, 7)],
                   "Canal de Fuga Médio",
                   "Influencia Vert. Cfuga",
                   "Fator Carga Max.",
                   "Fator Carga Min.",
                   "Vazão Mínima",
                   "Num. Unidades Base",
                   "Tipo Turbina",
                   "Representação Conjunto",
                   "Taxa Indisp. Forçada",
                   "Taxa Indisp. Programada",
                   "Tipo de Perda",
                   "Data",
                   "Observação",
                   "Volume de Referência",
                   "Tipo de Regulação"
                  ]

        df = pd.DataFrame(index=list(range(1, 601)))
        blocos = self._dados.blocos
        for i, c in enumerate(colunas):
            dados_coluna = [b.dados[i] for b in blocos]
            df[c] = dados_coluna
        self.__df = df.copy()

    @property
    def tabela(self) -> pd.DataFrame:
        """
        """
        if self.__df is None:
            self.__calcula_df()
        return self.__df

    @tabela.setter
    def tabela(self, df: pd.DataFrame):
        n_postos = df.shape[0]
        n_postos_arquivo = self.tabela.shape[0]
        if n_postos != n_postos_arquivo:
            raise ValueError(f"Número de postos incompatível ({n_postos})")
        for i in range(n_postos):
            self._dados.blocos[i]._dados = df.iloc[i, :].tolist()
