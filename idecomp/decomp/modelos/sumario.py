# Imports do próprio módulo
from idecomp.config import REES, SUBSISTEMAS
from idecomp._utils.bloco import Bloco
from idecomp._utils.registros import RegistroAn, RegistroFn, RegistroIn
from idecomp._utils.leiturablocos import LeituraBlocos
# Imports de módulos externos
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from typing import IO, List


class BlocoCMOSumario(Bloco):
    """
    Bloco com as informações do CMO por estágio e por subsistema.
    """
    str_inicio = "CUSTO MARGINAL DE OPERACAO  ($/MWh)"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoCMOSumario.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoCMOSumario):
            return False
        bloco: BlocoCMOSumario = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):

        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = [f"Estágio {s}" for s in range(1, n_semanas + 1)]
            df.columns = cols
            df["Subsistema"] = subsistemas
            df["Patamar"] = patamares
            df = df[["Subsistema", "Patamar"] + cols]
            return df

        # Salta uma linha
        arq.readline()
        # Descobre o número de semanas
        linha = arq.readline()
        sems = [s for s in linha.split(" ") if (len(s) > 0
                                                and ("Sem" in s or
                                                     "Mes" in s))]
        reg_pat = RegistroAn(6)
        reg_cmo = RegistroFn(10)
        n_semanas = len(sems)
        subsistemas: List[str] = []
        patamares: List[str] = []
        tabela = np.zeros((4 * len(SUBSISTEMAS),
                           n_semanas))
        # Salta outra linha
        arq.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X------X" in linha:
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e patamar
            ssis = SUBSISTEMAS[int(i / 4)]
            str_pat = reg_pat.le_registro(linha, 4)
            pat = "Médio" if "Med" in str_pat else str_pat.split("_")[1]
            subsistemas.append(ssis)
            patamares.append(pat)
            # Semanas
            tabela[i, :] = reg_cmo.le_linha_tabela(linha,
                                                   11,
                                                   1,
                                                   n_semanas)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoGeracaoTermicaSubsistemaSumario(Bloco):
    """
    Bloco com as informações de eco dos dados gerais
    utilizados na execução do caso.
    """
    str_inicio = "GERACAO TERMICA NOS SUSBSISTEMAS (MWmed)"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoGeracaoTermicaSubsistemaSumario.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoGeracaoTermicaSubsistemaSumario):
            return False
        bloco: BlocoGeracaoTermicaSubsistemaSumario = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):

        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = [f"Estágio {s}" for s in range(1, n_semanas + 1)]
            df.columns = cols
            df["Subsistema"] = subsistemas
            df = df[["Subsistema"] + cols]
            return df

        # Salta uma linha
        arq.readline()
        # Descobre o número de semanas
        linha = arq.readline()
        sems = [s for s in linha.split(" ") if (len(s) > 0
                                                and ("Sem" in s or
                                                     "Mes" in s))]
        reg_ssis = RegistroAn(6)
        reg_gt = RegistroFn(10)
        n_semanas = len(sems)
        subsistemas: List[str] = []
        tabela = np.zeros((len(SUBSISTEMAS),
                           n_semanas))
        # Salta outra linha
        arq.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X------X" in linha:
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e patamar
            ssis = reg_ssis.le_registro(linha, 4)
            subsistemas.append(ssis)
            # Semanas
            tabela[i, :] = reg_gt.le_linha_tabela(linha,
                                                  11,
                                                  1,
                                                  n_semanas)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoEnergiaArmazenadaREESumario(Bloco):
    """
    Bloco com as informações de energia armazenada
    em percentual por REE.
    """
    str_inicio = "ENERGIA ARMAZENADA NOS REEs (%"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoEnergiaArmazenadaREESumario.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoEnergiaArmazenadaREESumario):
            return False
        bloco: BlocoEnergiaArmazenadaREESumario = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):

        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["Inicial"] + [f"Estágio {s}"
                                  for s in range(1, n_semanas + 1)]
            df.columns = cols
            df["Subsistema"] = subsistemas
            df["REE"] = rees
            df = df[["Subsistema", "REE"] + cols]
            return df

        # Salta uma linha
        arq.readline()
        # Descobre o número de semanas
        linha = arq.readline()
        sems = [s for s in linha.split(" ") if (len(s) > 0
                                                and ("Sem" in s or
                                                     "Mes" in s))]
        reg_ree = RegistroAn(12)
        reg_ssis = RegistroIn(4)
        reg_earm = RegistroFn(6)
        n_semanas = len(sems)
        rees: List[str] = []
        subsistemas: List[str] = []
        tabela = np.zeros((len(REES),
                           n_semanas + 1))
        # Salta outra linha
        arq.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X------X" in linha:
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e REE
            ree = reg_ree.le_registro(linha, 4)
            ssis = SUBSISTEMAS[reg_ssis.le_registro(linha, 22) - 1]
            rees.append(ree)
            subsistemas.append(ssis)
            # Semanas
            tabela[i, :] = reg_earm.le_linha_tabela(linha,
                                                    28,
                                                    1,
                                                    n_semanas + 1)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoEnergiaArmazenadaSubsistemaSumario(Bloco):
    """
    Bloco com as informações de energia armazenada
    em percentual por REE.
    """
    str_inicio = "ENERGIA ARMAZENADA NOS SUBSISTEMAS (%"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoEnergiaArmazenadaSubsistemaSumario.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoEnergiaArmazenadaSubsistemaSumario):
            return False
        bloco: BlocoEnergiaArmazenadaSubsistemaSumario = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):

        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["Inicial"] + [f"Estágio {s}"
                                  for s in range(1, n_semanas + 1)]
            df.columns = cols
            df["Subsistema"] = subsistemas
            df = df[["Subsistema"] + cols]
            return df

        # Salta uma linha
        arq.readline()
        # Descobre o número de semanas
        linha = arq.readline()
        sems = [s for s in linha.split(" ") if (len(s) > 0
                                                and ("Sem" in s or
                                                     "Mes" in s))]
        reg_ssis = RegistroAn(12)
        reg_earm = RegistroFn(6)
        n_semanas = len(sems)
        subsistemas: List[str] = []
        tabela = np.zeros((len(SUBSISTEMAS) - 1,
                           n_semanas + 1))
        # Salta outra linha
        arq.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X------------X" in linha:
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e REE
            ssis = reg_ssis.le_registro(linha, 4)
            subsistemas.append(ssis)
            # Semanas
            tabela[i, :] = reg_earm.le_linha_tabela(linha,
                                                    23,
                                                    1,
                                                    n_semanas + 1)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class LeituraSumario(LeituraBlocos):
    """
    Realiza a leitura do arquivo sumario.rvx
    existente em um diretório de saídas do DECOMP.

    Esta classe contém o conjunto de utilidades para ler
    e interpretar os campos de um arquivo sumario.rvx, construindo
    um objeto `Sumario` cujas informações são as mesmas do sumario.rvx.

    Este objeto existe para retirar do modelo de dados a complexidade
    de iterar pelas linhas do arquivo, recortar colunas, converter
    tipos de dados, dentre outras tarefas necessárias para a leitura.

    """
    def __init__(self,
                 diretorio: str):
        super().__init__(diretorio)

    # Override
    def _cria_blocos_leitura(self) -> List[Bloco]:
        """
        Cria a lista de blocos a serem lidos no arquivo sumario.rvx.
        """
        return ([BlocoCMOSumario(),
                 BlocoEnergiaArmazenadaREESumario(),
                 BlocoEnergiaArmazenadaSubsistemaSumario(),
                 BlocoGeracaoTermicaSubsistemaSumario()])
