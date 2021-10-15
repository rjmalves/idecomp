from idecomp._utils.bloco import Bloco
from idecomp._utils.registros import RegistroAn, RegistroIn
from idecomp._utils.leiturablocos import LeituraBlocos
# Imports de módulos externos
import pandas as pd  # type: ignore
from typing import IO, List


class BlocoInviabilidadesIteracoes(Bloco):
    """
    Bloco com as informações das inviabilidades visitadas
    pelo DECOMP durante o processo iterativo.
    """
    str_inicio = "TERACAO  FWD(1)/BWD(0)  ESTAGIO  CENARIO"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoInviabilidadesIteracoes.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoInviabilidadesIteracoes):
            return False
        bloco: BlocoInviabilidadesIteracoes = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):

        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame()
            df["Iteração"] = iteracoes
            df["FWD/BWD"] = fwds_bwds
            df["Estágio"] = estagios
            df["Cenário"] = cenarios
            df["Restrição"] = restricoes
            df["Violação"] = violacoes
            df["Unidade"] = unidades
            return df

        # Salta uma linha
        arq.readline()
        reg_iter = RegistroIn(9)
        reg_fwdbwd = RegistroIn(14)
        reg_estagio = RegistroIn(8)
        reg_cenario = RegistroIn(8)
        reg_restricao = RegistroAn(51)
        reg_violacao = RegistroAn(22)
        iteracoes: List[int] = []
        fwds_bwds: List[int] = []
        estagios: List[int] = []
        cenarios: List[int] = []
        restricoes: List[str] = []
        violacoes: List[float] = []
        unidades: List[str] = []
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if len(linha.strip()) < 5:
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            iteracoes.append(reg_iter.le_registro(linha, 4))
            fwds_bwds.append(reg_fwdbwd.le_registro(linha, 14))
            estagios.append(reg_estagio.le_registro(linha, 29))
            cenarios.append(reg_cenario.le_registro(linha, 38))
            restricoes.append(reg_restricao.le_registro(linha, 47))
            viol = reg_violacao.le_registro(linha, 99)
            violacao = float(viol.strip().split(" ")[0])
            unidade = viol.strip().split(" ")[1]
            violacoes.append(violacao)
            unidades.append(unidade)

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoInviabilidadesSimFinal(Bloco):
    """
    Bloco com as informações das inviabilidades visitadas
    pelo DECOMP durante a simulação final.
    """
    str_inicio = "    ESTAGIO  CENARIO         RESTRICAO"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoInviabilidadesSimFinal.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoInviabilidadesSimFinal):
            return False
        bloco: BlocoInviabilidadesSimFinal = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):

        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame()
            df["Estágio"] = estagios
            df["Cenário"] = cenarios
            df["Restrição"] = restricoes
            df["Violação"] = violacoes
            df["Unidade"] = unidades
            return df

        # Salta uma linha
        arq.readline()
        reg_estagio = RegistroIn(8)
        reg_cenario = RegistroIn(8)
        reg_restricao = RegistroAn(76)
        reg_violacao = RegistroAn(22)
        estagios: List[int] = []
        cenarios: List[int] = []
        restricoes: List[str] = []
        violacoes: List[float] = []
        unidades: List[str] = []
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if len(linha.strip()) < 5:
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            estagios.append(reg_estagio.le_registro(linha, 4))
            cenarios.append(reg_cenario.le_registro(linha, 13))
            restricoes.append(reg_restricao.le_registro(linha, 22))
            viol = reg_violacao.le_registro(linha, 99)
            violacao = float(viol.strip().split(" ")[0])
            unidade = viol.strip().split(" ")[1]
            violacoes.append(violacao)
            unidades.append(unidade)

    # Override
    def escreve(self, arq: IO):
        pass


class LeituraInviabUnic(LeituraBlocos):
    """
    Realiza a leitura do arquivo inviab_unic.rvx
    existente em um diretório de saídas do DECOMP.

    Esta classe contém o conjunto de utilidades para ler
    e interpretar os campos de um arquivo inviab_unic.rvx, construindo
    um objeto `InviabUnic` cujas informações são as mesmas do sumario.rvx.

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
        Cria a lista de blocos a serem lidos no arquivo inviab_unic.rvx.
        """
        return ([BlocoInviabilidadesIteracoes(),
                 BlocoInviabilidadesSimFinal()])
