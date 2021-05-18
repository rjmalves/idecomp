# Imports do próprio módulo
from idecomp.config import MAX_SEMANAS_PRE, SUBSISTEMAS
from idecomp._utils.leitura import Leitura
from .modelos.relato import BalancoEnergeticoRelato, DadosGeraisRelato
from .modelos.relato import CMORelato
from .modelos.relato import GeracaoTermicaSubsistemaRelato
from .modelos.relato import EnergiaArmazenadaREERelato
from .modelos.relato import EnergiaArmazenadaSubsistemaRelato
from .modelos.relato import ENAPreEstudoSemanalSubsistemaRelato
from .modelos.relato import Relato
# Imports de módulos externos
import os
import numpy as np  # type: ignore
from traceback import print_exc
from typing import IO, List


class LeituraRelato(Leitura):
    """
    Realiza a leitura do arquivo relato.rvx
    existente em um diretório de saídas do DECOMP.

    Esta classe contém o conjunto de utilidades para ler
    e interpretar os campos de um arquivo relato.rvx, construindo
    um objeto `Relato` cujas informações são as mesmas do relato.rvx.

    Este objeto existe para retirar do modelo de dados a complexidade
    de iterar pelas linhas do arquivo, recortar colunas, converter
    tipos de dados, dentre outras tarefas necessárias para a leitura.

    Uma vez realizada a leitura do arquivo, as informações são guardadas
    internamente no atributo `Relato`.

    **Exemplos**

    >>> diretorio = "~/documentos/.../deck"
    >>> leitor = LeituraRelato(diretorio)
    >>> leitor.le_arquivo()
    # Ops, esqueci de pegar o objeto
    >>> relato = leitor.relato

    """
    str_inicio_dados = "Relatorio  dos  Dados  Gerais"
    str_inicio_balanco = "RELATORIO  DO  BALANCO  ENERGETICO "
    str_inicio_cmo = "CUSTO MARGINAL DE OPERACAO  ($/MWh)"
    str_inicio_gt_subsis = "GERACAO TERMICA NOS SUSBSISTEMAS (MWmed)"
    str_inicio_earm_ree = "ENERGIA ARMAZENADA NOS REEs (%"
    str_inicio_earm_subsis = "ENERGIA ARMAZENADA NOS SUBSISTEMAS (%"
    str_inicio_ena_semana_subsis = "NATURAL AFLUENTE POR SUBSISTEMA(SEMANAS"
    str_fim_balanco = "RELATORIO  DA  OPERACAO"
    str_fim_relato = "FIM DO PROCESSAMENTO"

    def __init__(self,
                 diretorio: str) -> None:
        super().__init__()
        self.diretorio = diretorio
        # Relato default, depois é substituído
        gt = GeracaoTermicaSubsistemaRelato([],
                                            np.ndarray([]))
        earm_ree = EnergiaArmazenadaREERelato([],
                                              np.ndarray([]))
        earm = EnergiaArmazenadaSubsistemaRelato([],
                                                 np.ndarray([]))
        ena_semana = ENAPreEstudoSemanalSubsistemaRelato([],
                                                         np.ndarray([]))
        balanco_energetico = BalancoEnergeticoRelato([],
                                                     np.ndarray([]))
        self.relato = Relato(DadosGeraisRelato(0),
                             CMORelato([],
                                       np.ndarray([])),
                             gt,
                             earm_ree,
                             earm,
                             ena_semana,
                             balanco_energetico)

    def le_arquivo(self,
                   relato_rev: str = "") -> Relato:
        """
        Faz a leitura do arquivo `relato.rvx`.
        """
        try:
            # Se não foi fornecido um nome de relato,
            # procura um relato no diretório
            if relato_rev == "":
                arquivos = os.listdir(self.diretorio)
                for a in arquivos:
                    if "relato.rv" in a:
                        relato_rev = a
                        break
                if len(relato_rev) == 0:
                    raise Exception("Não foi encontrado relato")
            # Lê o arquivo
            caminho = os.path.join(self.diretorio, relato_rev)
            with open(caminho, "r") as arq:
                self.relato = self._le_relato(arq)
                return self.relato
        except Exception:
            print_exc()
            return self.relato

    def _le_relato(self, arq: IO) -> Relato:
        """
        Faz a leitura do arquivo pmo.dat.
        """
        achou_dados_gerais = False
        achou_cmo = False
        achou_gt_subsis = False
        achou_earm_ree = False
        achou_earm_subsis = False
        achou_ena_semana_subsis = False
        achou_balanco_energetico = False
        linha = ""
        dados_gerais = DadosGeraisRelato(0)
        cmo = CMORelato([], np.array([]))
        gt_subsis = GeracaoTermicaSubsistemaRelato([], np.array([]))
        earm_ree = EnergiaArmazenadaREERelato([],
                                              np.ndarray([]))
        earm_subsis = EnergiaArmazenadaSubsistemaRelato([],
                                                        np.ndarray([]))
        ena_sem_subsis = ENAPreEstudoSemanalSubsistemaRelato([],
                                                             np.ndarray([]))
        tabela_bal = np.zeros((10, len(SUBSISTEMAS), 17))
        balanco_energ = BalancoEnergeticoRelato([],
                                                tabela_bal)
        balancos_lidos = 0
        while True:
            # Decide se lê uma linha nova ou usa a última lida
            linha = self._le_linha_com_backup(arq)
            if len(linha) == 0 or self._fim_arquivo(linha):
                balanco_energ.tabela = balanco_energ.tabela[:balancos_lidos,
                                                            :,
                                                            :]
                self.relato = Relato(dados_gerais,
                                     cmo,
                                     gt_subsis,
                                     earm_ree,
                                     earm_subsis,
                                     ena_sem_subsis,
                                     balanco_energ)
                break
            # Condição para iniciar uma leitura de dados
            if not achou_dados_gerais:
                achou = LeituraRelato.str_inicio_dados in linha
                achou_dados_gerais = achou
            if not achou_cmo:
                achou = LeituraRelato.str_inicio_cmo in linha
                achou_cmo = achou
            if not achou_gt_subsis:
                achou = LeituraRelato.str_inicio_gt_subsis in linha
                achou_gt_subsis = achou
            if not achou_earm_ree:
                achou = LeituraRelato.str_inicio_earm_ree in linha
                achou_earm_ree = achou
            if not achou_earm_subsis:
                achou = LeituraRelato.str_inicio_earm_subsis in linha
                achou_earm_subsis = achou
            if not achou_ena_semana_subsis:
                achou = LeituraRelato.str_inicio_ena_semana_subsis in linha
                achou_ena_semana_subsis = achou
            if not achou_balanco_energetico:
                achou = LeituraRelato.str_inicio_balanco in linha
                achou_balanco_energetico = achou
            # Quando achar, le cada parte adequadamente
            if achou_dados_gerais:
                dados_gerais = self._le_dados_gerais(arq)
                achou_dados_gerais = False
            if achou_cmo:
                cmo = self._le_cmo(arq)
                achou_cmo = False
            if achou_gt_subsis:
                gt_subsis = self._le_gt_subsistema(arq)
                achou_gt_subsis = False
            if achou_earm_ree:
                earm_ree = self._le_earm_ree(arq)
                achou_earm_ree = False
            if achou_earm_subsis:
                earm_subsis = self._le_earm_subsistema(arq)
                achou_earm_subsis = False
            if achou_ena_semana_subsis:
                ena_sem_subsis = self._le_ena_sem_subsis(arq)
                achou_ena_semana_subsis = False
            if achou_balanco_energetico:
                self._le_balanco_energetico(arq,
                                            balanco_energ)
                achou_balanco_energetico = False
                balancos_lidos += 1

        return self.relato

    def _le_dados_gerais(self,
                         arq: IO
                         ) -> DadosGeraisRelato:
        """
        """
        # Salta uma linha
        self._le_linha_com_backup(arq)
        # Descobre o número de semanas
        dados = DadosGeraisRelato(0)
        while True:
            # Confere se a leitura não acabou
            linha = self._le_linha_com_backup(arq)
            if len(linha) < 3:
                return dados
            # Senão, lê mais uma linha
            if "Numero de semanas do mes inicial" in linha:
                dados.numero_semanas_1_mes = int(linha[-3:])

    def _le_cmo(self,
                arq: IO
                ) -> CMORelato:
        """
        Lê a tabela de CMO existente no arquivo relato do DECOMP.
        """
        # Salta uma linha
        self._le_linha_com_backup(arq)
        # Descobre o número de semanas
        linha = self._le_linha_com_backup(arq)
        sems = [s for s in linha.split(" ") if (len(s) > 0
                                                and ("Sem" in s or
                                                     "Mes" in s))]
        n_semanas = len(sems)
        subsistemas: List[str] = []
        tabela = np.zeros((80, n_semanas))
        # Salta outra linha
        self._le_linha_com_backup(arq)
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = self._le_linha_com_backup(arq)
            if "X------X" in linha:
                return CMORelato(subsistemas, tabela[:i, :])
            # Senão, lê mais uma linha
            # Subsistema
            ssis = linha[4:10].strip()
            subsistemas.append(ssis)
            # Semanas
            ci = 11
            nc = 10
            for j in range(n_semanas):
                cf = ci + nc
                tabela[i, j] = float(linha[ci:cf])
                ci = cf + 1
            i += 1

    def _le_gt_subsistema(self,
                          arq: IO
                          ) -> GeracaoTermicaSubsistemaRelato:
        """
        Lê a tabela de GT por subsistema
        existente no arquivo relato do DECOMP.
        """
        # Salta uma linha
        self._le_linha_com_backup(arq)
        # Descobre o número de semanas
        linha = self._le_linha_com_backup(arq)
        sems = [s for s in linha.split(" ") if (len(s) > 0
                                                and ("Sem" in s or
                                                     "Mes" in s))]
        n_semanas = len(sems)
        subsistemas: List[str] = []
        tabela = np.zeros((20, n_semanas))
        # Salta outra linha
        self._le_linha_com_backup(arq)
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = self._le_linha_com_backup(arq)
            if "X------X" in linha:
                return GeracaoTermicaSubsistemaRelato(subsistemas,
                                                      tabela[:i, :])
            # Senão, lê mais uma linha
            # Subsistema
            ssis = linha[4:10].strip()
            subsistemas.append(ssis)
            # Semanas
            ci = 11
            nc = 10
            for j in range(n_semanas):
                cf = ci + nc
                tabela[i, j] = float(linha[ci:cf])
                ci = cf + 1
            i += 1

    def _le_earm_ree(self,
                     arq: IO
                     ) -> EnergiaArmazenadaREERelato:
        """
        Lê a tabela de EARM por REE
        existente no arquivo relato do DECOMP.
        """
        # Salta uma linha
        self._le_linha_com_backup(arq)
        # Descobre o número de semanas
        linha = self._le_linha_com_backup(arq)
        sems = [s for s in linha.split(" ") if (len(s) > 0
                                                and ("Sem" in s or
                                                     "Mes" in s))]
        n_semanas = len(sems)
        rees: List[str] = []
        tabela = np.zeros((20, n_semanas + 1))
        # Salta outra linha
        self._le_linha_com_backup(arq)
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = self._le_linha_com_backup(arq)
            if "-------" in linha:
                return EnergiaArmazenadaREERelato(rees,
                                                  tabela[:i, :])
            # Senão, lê mais uma linha
            # Subsistema
            ssis = linha[4:16].strip()
            rees.append(ssis)
            # Inicial e semanas
            ci = 28
            nc = 6
            for j in range(n_semanas + 1):
                cf = ci + nc
                tabela[i, j] = float(linha[ci:cf])
                ci = cf + 1
            i += 1

    def _le_earm_subsistema(self,
                            arq: IO
                            ) -> EnergiaArmazenadaSubsistemaRelato:
        """
        Lê a tabela de EARM por subsistema
        existente no arquivo relato do DECOMP.
        """
        # Salta uma linha
        self._le_linha_com_backup(arq)
        # Descobre o número de semanas
        linha = self._le_linha_com_backup(arq)
        sems = [s for s in linha.split(" ") if (len(s) > 0
                                                and ("Sem" in s or
                                                     "Mes" in s))]
        n_semanas = len(sems)
        subsistemas: List[str] = []
        tabela = np.zeros((20, n_semanas + 1))
        # Salta outra linha
        self._le_linha_com_backup(arq)
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = self._le_linha_com_backup(arq)
            if "-------" in linha:
                return EnergiaArmazenadaSubsistemaRelato(subsistemas,
                                                         tabela[:i, :])
            # Senão, lê mais uma linha
            # Subsistema
            ssis = linha[4:16].strip()
            subsistemas.append(ssis)
            # Inicial e semanas
            ci = 23
            nc = 6
            for j in range(n_semanas + 1):
                cf = ci + nc
                tabela[i, j] = float(linha[ci:cf])
                ci = cf + 1
            i += 1

    def _le_ena_sem_subsis(self,
                           arq: IO
                           ) -> ENAPreEstudoSemanalSubsistemaRelato:
        """
        Lê a tabela de ENA pré-estudo semanal por subsistema
        existente no arquivo relato do DECOMP.
        """
        # Salta 4 linhas
        self._le_linha_com_backup(arq)
        self._le_linha_com_backup(arq)
        self._le_linha_com_backup(arq)
        self._le_linha_com_backup(arq)
        # Cria as variáveis e inicia a leitura
        subsistemas: List[str] = []
        tabela = np.zeros((20, MAX_SEMANAS_PRE))
        i = 0
        j = 0
        while True:
            # Confere se a leitura não acabou
            linha = self._le_linha_com_backup(arq)
            if "-------" in linha:
                return ENAPreEstudoSemanalSubsistemaRelato(subsistemas,
                                                           tabela[:i, :j])
            # Senão, lê mais uma linha
            # Subsistema
            ssis = linha[4:18].strip()
            subsistemas.append(ssis)
            # Inicial e semanas
            ci = 24
            nc = 8
            for n in range(MAX_SEMANAS_PRE):
                cf = ci + nc
                ena = float(linha[ci:cf])
                if ena == 0.0:
                    j = n
                    break
                tabela[i, n] = float(linha[ci:cf])
                ci = cf + 1
            i += 1

    def _le_balanco_energetico(self,
                               arq: IO,
                               balanco: BalancoEnergeticoRelato):
        """
        """
        # Salta uma linha e extrai a semana
        self._le_linha_com_backup(arq)
        linha = self._le_linha_com_backup(arq)
        semana = int(linha.split("ESTAGIO")[1][:3].strip())
        str_subsis = "     Subsistema"
        str_medio = "    Medio"
        subsis = -1
        while True:
            linha = self._le_linha_com_backup(arq)
            # Verifica se acabou
            if LeituraRelato.str_fim_balanco in linha:
                break
            # Senão, procura a linha que identifica o subsistema
            if str_subsis in linha:
                sigla_sub = linha.split(str_subsis)[1][:3].strip()
                if sigla_sub != "FC":
                    subsis = SUBSISTEMAS.index(sigla_sub)
            # Se está lendo um subsistema e achou a linha de valores médios
            if subsis != -1 and str_medio in linha:
                nc = 7
                ci = 10
                for i in range(9):
                    cf = ci + nc
                    balanco.tabela[semana - 1,
                                   subsis,
                                   i] = float(linha[ci:cf])
                    ci = cf + 1
                # TODO - Começar a ler a interligação
                # Para o SE, lê as gerações de Itaipu50 e Itaipu60
                if subsis == 0:
                    ci = 97
                    nc = 7
                    for i in range(15, 17):
                        cf = ci + nc
                        balanco.tabela[semana - 1,
                                       subsis,
                                       i] = float(linha[ci:cf])
                        ci = cf + 1
                # Reseta o indicador de subsistema
                subsis = -1

    def _fim_arquivo(self, linha: str) -> bool:
        return LeituraRelato.str_fim_relato in linha
