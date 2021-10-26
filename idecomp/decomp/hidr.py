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
        Realiza a leitura de um arquivo "hidr.dat" existente em
        um diretório.

        :param diretorio: O caminho relativo ou completo para o diretório
            onde se encontra o arquivo
        :type diretorio: str
        :param nome_arquivo: Nome do arquivo a ser lido.
            Tem como valor default "hidr.dat"
        :type nome_arquivo: str, optional
        :return: Um objeto :class:`Hidr` com informações do arquivo lido
        """
        leitor = LeituraHidr(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    # Override
    def escreve_arquivo(self,
                        diretorio: str,
                        nome_arquivo: str = "hidr.dat"):
        """
        Realiza a escrita de um arquivo com as informações do
        objeto :class:`Hidr`

        :param diretorio: O caminho relativo ou completo para o diretório
            onde será escrito o arquivo.
        :type diretorio: str
        :param nome_arquivo: Nome do arquivo a ser escrito.Tem como valor
            default "hidr.dat"
        :type nome_arquivo: str, optional
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

        blocos = self._dados.blocos
        dados = {}
        for i, c in enumerate(colunas):
            dados_coluna = [b.dados[i] for b in blocos]
            dados[c] = dados_coluna

        df = pd.DataFrame(data=dados)
        df.index = list(range(1, len(list(df.index)) + 1))
        self.__df = df.copy()

    @property
    def tabela(self) -> pd.DataFrame:
        """
        A tabela com as informações contidas no arquivo `hidr.dat` é um
        DataFrame com o número delinhas igual ao número de postos e 192
        colunas.
        O índice é a numeração das usinas em ordem crescente, iniciando
        em 1.
        As colunas são:

        - Nome (`str`): nome da usina (12 caracteres)
        - Posto (`int`): posto de vazão natural da usina
        - Posto BDH [1 - 8] (`int`): TODO
        - Subsistema (`str`): subsistema da usina
        - Empresa (`str`): agente responsável pela usina
        - Posto Jusante (`int`): posto à jusante da usina
        - Desvio (`float`): TODO
        - Volume Mínimo (`float`): volume mínimo da usina (hm3)
        - Volume Máximo (`float`): volume máximo da usina (hm3)
        - Volume Vertedouro (`float`): volume do vertedouro da usina (hm3)
        - Volume Desvio (`float`): TODO
        - Cota Mínima (`float`): cota mínima da usina (m)
        - Cota Máxima (`float`): cota máxima da usina (m)
        - C[1-5] CV (`float`): coeficientes do polinômio cota-volume
        - C[1-5] CA (`float`): coeficientes do polinômio cota-área
        - Evaporação Mês [1-12] (`float`): coeficientes de evaporação (mm)
        - Num Conjunto Máquinas (`int`): número de conjuntos de máquinas
        - Num Máquinas Conjunto [1-5] (`int`): máquinas por conjunto
        - Pot. Conjunto [1-5] (`float`): potência das máquinas (MWmed)
        - Ingorado [1-75]: campos ignorados
        - H Nominal [1-5]: alturas nominais de queda por conjunto (m)
        - Q Nominal [1-5]: vazões nominais por conjunto (m3/s)
        - Produtibilidade Específica (`float`): produtibilidade específica
        - Perdas (`float`): perdas da usina (% ?)
        - Número Pol. Jusante (`int`): número de polinômios de jusante
        - C[1-5] PJUS[1-6] (`float`): coeficientes de cada polinjus
        - C[1-5] PJUSREF (`float`): coeficientes do polinjus de referência
        - Canal de Fuga Médio (`float`): cota média do canal de fuga (m)
        - Influencia Vert. Cfuga (`int`): TODO (0 ou 1)
        - Fator Carga Max. (`float`): TODO (%)
        - Fator Carga Min. (`float`): TODO (%)
        - Vazão Mínima (`float`): vazão mínima da usina (m3/s)
        - Num. Unidades Base (`int`): TODO (0 = X, 1 = Y, 2 = Z)
        - Tipo Turbina (`int`): TODO (0 = X, 1 = Y, 2 = Z)
        - Representação Conjunto (`int`): TODO (0 = X, 1 = Y, 2 = Z)
        - Taxa Indisp. Forçada (`float`): TODO (%)
        - Taxa Indisp. Programada (`float`): TODO (%)
        - Tipo de Perda (`int`): TODO (0 = X, 1 = Y, 2 = Z)
        - Data (`str`): TODO (DD/MM/AA)
        - Observação (`str`): observação qualquer sobre a usina
        - Volume de Referência (`float`): TODO (hm3)
        - Tipo de Regulação (`str`): TODO (D, S ou M)

        :return: Tabela com as informações contidas no arquivo `hidr.dat`
        :rtype: pd.DataFrame
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
