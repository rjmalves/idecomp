# Imports do próprio módulo
from idecomp.config import MAX_ESTAGIOS
from idecomp.config import REES, SUBSISTEMAS
from idecomp._utils.bloco import Bloco
from idecomp._utils.registros import RegistroAn, RegistroFn, RegistroIn
from idecomp._utils.leiturablocos import LeituraBlocos
# Imports de módulos externos
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from typing import IO, List


class BlocoDadosGeraisRelato(Bloco):
    """
    Bloco com as informações de eco dos dados gerais
    utilizados na execução do caso.
    """
    str_inicio = "Relatorio  dos  Dados  Gerais"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoDadosGeraisRelato.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoDadosGeraisRelato):
            return False
        bloco: BlocoDadosGeraisRelato = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):
        pass

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoRelatorioOperacaoUHERelato(Bloco):
    """
    """
    str_inicio = "No.       Usina       Volume (% V.U.)"
    str_fim = "X----X-"

    def __init__(self):

        super().__init__(BlocoRelatorioOperacaoUHERelato.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoRelatorioOperacaoUHERelato):
            return False
        bloco: BlocoRelatorioOperacaoUHERelato = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):

        def converte_tabela_para_df() -> pd.DataFrame:
            cols = ["Volume Ini (% V.U)", "Volume Fin (% V.U)",
                    "Volume Esp. (% V.U)", "Qnat (m3/s)", "Qnat (% MLT)",
                    "Qafl (m3/s)", "Qdef (m3/s)", "Geração Pat 1",
                    "Geração Pat 2", "Geração Pat 3", "Geração Média",
                    "Vertimento Turbinável", "Vertimento Não-Turbinável",
                    "Ponta", "FPCGC"]
            df = pd.DataFrame(tabela, columns=cols)
            cols_adic = ["Código", "Usina", "Evaporação", "Tempo de Viagem",
                         "Cota Abaixo da Crista do Vert", "Def. Mínima = 0"]
            df["Código"] = numeros
            df["Usina"] = usinas
            df["Evaporação"] = evaporacao
            df["Tempo de Viagem"] = tv_afluencia
            df["Cota Abaixo da Crista do Vert"] = cota_abaixo_crista
            df["Def. Mínima = 0"] = def_minima_zero
            df = df[cols_adic + cols]
            return df

        def le_se_tem_valor(digitos: int,
                            linha: str,
                            coluna_inicio: int):
            coluna_fim = coluna_inicio + digitos
            trecho = linha[coluna_inicio:coluna_fim].strip()
            valor = None
            if len(trecho) > 0 and "---" not in trecho:
                reg = RegistroFn(digitos)
                valor = reg.le_registro(linha, coluna_inicio)
            else:
                valor = np.nan
            return valor

        # Salta duas linhas
        arq.readline()
        arq.readline()
        # Variáveis auxiliares
        reg_numero = RegistroIn(4)
        reg_usina = RegistroAn(12)
        reg_flags = RegistroAn(4)
        reg_volume = RegistroFn(5)
        reg_tabela = RegistroFn(7)
        numeros: List[int] = []
        usinas: List[str] = []
        evaporacao: List[bool] = []
        tv_afluencia: List[bool] = []
        cota_abaixo_crista: List[bool] = []
        def_minima_zero: List[bool] = []
        # Salta uma linha e extrai a semana
        tabela = np.zeros((300, 15))
        i = 0
        while True:
            linha: str = arq.readline()
            # Verifica se acabou
            if BlocoRelatorioOperacaoUHERelato.str_fim in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_para_df()
                break
            numeros.append(reg_numero.le_registro(linha, 4))
            usinas.append(reg_usina.le_registro(linha, 9))
            flags = reg_flags.le_registro(linha, 22)
            evaporacao.append("#" in flags)
            tv_afluencia.append("*" in flags)
            cota_abaixo_crista.append("@" in flags)
            def_minima_zero.append("$" in flags)
            tem_volume = len(linha[27:33].strip()) > 0
            if tem_volume:
                tabela[i, :3] = reg_volume.le_linha_tabela(linha,
                                                           27,
                                                           1,
                                                           3)
            else:
                tabela[i, :3] = np.nan
            tabela[i, 3] = le_se_tem_valor(7, linha, 45)
            tabela[i, 4] = le_se_tem_valor(6, linha, 54)
            tabela[i, 5] = le_se_tem_valor(7, linha, 63)
            tabela[i, 6:11] = reg_tabela.le_linha_tabela(linha,
                                                         72,
                                                         5,
                                                         1)
            tabela[i, 11] = le_se_tem_valor(7, linha, 112)
            tabela[i, 12] = le_se_tem_valor(7, linha, 120)
            tabela[i, 13] = le_se_tem_valor(7, linha, 128)
            tabela[i, 14] = le_se_tem_valor(7, linha, 136)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoBalancoEnergeticoRelato(Bloco):
    """
    Bloco com as informações de eco dos dados gerais
    utilizados na execução do caso.
    """
    str_inicio = "RELATORIO  DO  BALANCO  ENERGETICO"
    str_fim = "RELATORIO  DA  OPERACAO"

    def __init__(self):

        super().__init__(BlocoBalancoEnergeticoRelato.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoBalancoEnergeticoRelato):
            return False
        bloco: BlocoBalancoEnergeticoRelato = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):

        def converte_tabela_para_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["Mercado", "Bacia", "Cbomba",
                    "Ghid", "Gter", "GterAT", "Deficit",
                    "Compra", "Venda", "Itaipu50", "Itaipu60"]
            df.columns = cols
            df["Subsistema"] = subsistemas
            df = df[["Subsistema"] + cols]
            return df

        # Variáveis auxiliares
        reg_tabela = RegistroFn(7)
        str_subsis = "     Subsistema"
        str_medio = "    Medio"
        subsis = "FC"
        subsistemas = []
        # Salta uma linha e extrai a semana
        tabela = np.zeros((MAX_ESTAGIOS * len(SUBSISTEMAS), 11))
        i = 0
        while True:
            linha = arq.readline()
            # Verifica se acabou
            if BlocoBalancoEnergeticoRelato.str_fim in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_para_df()
                break
            # Senão, procura a linha que identifica o subsistema
            if str_subsis in linha:
                subsis = linha.split(str_subsis)[1][:3].strip()
            # Se está lendo um subsistema e achou a linha de valores médios
            if subsis != "FC" and str_medio in linha:
                subsistemas.append(subsis)
                tabela[i, :9] = reg_tabela.le_linha_tabela(linha,
                                                           10,
                                                           1,
                                                           9)
                # TODO - Começar a ler a interligação
                # Para o SE, lê as gerações de Itaipu50 e Itaipu60
                if subsis == "SE":
                    tabela[i, 9:] = reg_tabela.le_linha_tabela(linha,
                                                               96,
                                                               1,
                                                               2)
                # Reseta o indicador de subsistema
                subsis = "FC"
                i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoCMORelato(Bloco):
    """
    Bloco com as informações do CMO por estágio e por subsistema.
    """
    str_inicio = "CUSTO MARGINAL DE OPERACAO  ($/MWh)"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoCMORelato.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoCMORelato):
            return False
        bloco: BlocoCMORelato = o
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


class BlocoGeracaoTermicaSubsistemaRelato(Bloco):
    """
    Bloco com as informações de eco dos dados gerais
    utilizados na execução do caso.
    """
    str_inicio = "GERACAO TERMICA NOS SUSBSISTEMAS (MWmed)"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoGeracaoTermicaSubsistemaRelato.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoGeracaoTermicaSubsistemaRelato):
            return False
        bloco: BlocoGeracaoTermicaSubsistemaRelato = o
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


class BlocoEnergiaArmazenadaREERelato(Bloco):
    """
    Bloco com as informações de energia armazenada
    em percentual por REE.
    """
    str_inicio = "ENERGIA ARMAZENADA NOS REEs (%"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoEnergiaArmazenadaREERelato.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoEnergiaArmazenadaREERelato):
            return False
        bloco: BlocoEnergiaArmazenadaREERelato = o
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


class BlocoEnergiaArmazenadaSubsistemaRelato(Bloco):
    """
    Bloco com as informações de energia armazenada
    em percentual por REE.
    """
    str_inicio = "ENERGIA ARMAZENADA NOS SUBSISTEMAS (%"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoEnergiaArmazenadaSubsistemaRelato.str_inicio,
                         "",
                         True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoEnergiaArmazenadaSubsistemaRelato):
            return False
        bloco: BlocoEnergiaArmazenadaSubsistemaRelato = o
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


class BlocoENAPreEstudoSemanalSubsistemaRelato(Bloco):
    """
    Bloco com as informações de eco dos dados gerais
    utilizados na execução do caso.
    """
    str_inicio = "NATURAL AFLUENTE POR SUBSISTEMA(SEMANAS"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoENAPreEstudoSemanalSubsistemaRelato.str_inicio,
                         "",
                         True)

        self._dados = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoENAPreEstudoSemanalSubsistemaRelato):
            return False
        bloco: BlocoENAPreEstudoSemanalSubsistemaRelato = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):

        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["Earmax"] + [f"Estágio Pré {s}"
                                 for s in range(1, 6)]
            df.columns = cols
            df["Subsistema"] = subsistemas
            df = df[["Subsistema"] + cols]
            return df

        # Salta 4 linhas
        for _ in range(4):
            arq.readline()
        reg_ssis = RegistroAn(14)
        reg_ena = RegistroFn(8)
        subsistemas: List[str] = []
        tabela = np.zeros((len(SUBSISTEMAS) - 1,
                           6))
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X--------------X" in linha:
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e REE
            ssis = reg_ssis.le_registro(linha, 4)
            subsistemas.append(ssis)
            # Semanas
            tabela[i, :] = reg_ena.le_linha_tabela(linha,
                                                   24,
                                                   1,
                                                   6)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoDiasExcluidosSemanas(Bloco):
    """
    Bloco com as informações de dias excluídos das semanas
    inicial e final do estudo.
    """
    str_inicio = " Mes inicial do periodo de estudos"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoDiasExcluidosSemanas.str_inicio,
                         "",
                         True)

        self._dados = [0, 0]

    def __eq__(self, o: object):
        if not isinstance(o, BlocoDiasExcluidosSemanas):
            return False
        bloco: BlocoDiasExcluidosSemanas = o
        return all([
                    self._dados[0] == bloco._dados[0],
                    self._dados[1] == bloco._dados[1]
                   ])

    # Override
    def le(self, arq: IO):
        reg_dias = RegistroIn(1)
        self._dados[0] = reg_dias.le_registro(arq.readline(), 54)
        self._dados[1] = reg_dias.le_registro(arq.readline(), 54)

    # Override
    def escreve(self, arq: IO):
        pass


class LeituraRelato(LeituraBlocos):
    """
    Realiza a leitura do arquivo relato.rvx
    existente em um diretório de saídas do DECOMP.

    Esta classe contém o conjunto de utilidades para ler
    e interpretar os campos de um arquivo relato.rvx, construindo
    um objeto `Relato` cujas informações são as mesmas do relato.rvx.

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
        Cria a lista de blocos a serem lidos no arquivo adterm.dat.
        """
        relat_uhe: List[Bloco] = [BlocoRelatorioOperacaoUHERelato()
                                  for _ in range(10)]
        balanc_energ: List[Bloco] = [BlocoBalancoEnergeticoRelato()
                                     for _ in range(10)]
        return ([BlocoDadosGeraisRelato(),
                 BlocoCMORelato(),
                 BlocoEnergiaArmazenadaREERelato(),
                 BlocoEnergiaArmazenadaSubsistemaRelato(),
                 BlocoENAPreEstudoSemanalSubsistemaRelato(),
                 BlocoGeracaoTermicaSubsistemaRelato(),
                 BlocoDiasExcluidosSemanas()] +
                relat_uhe +
                balanc_energ)
