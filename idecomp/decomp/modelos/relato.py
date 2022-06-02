# Imports do próprio módulo
from idecomp.config import (
    MAX_ESTAGIOS,
    MAX_PATAMARES,
    MAX_SUBSISTEMAS,
    MAX_REES,
)
from idecomp.config import SUBSISTEMAS
from idecomp._utils.bloco import Bloco
from idecomp._utils.registros import RegistroAn, RegistroFn, RegistroIn
from idecomp._utils.leiturablocos import LeituraBlocos

# Imports de módulos externos
from cfinterface.components.block import Block
from cfinterface.components.line import Line
from cfinterface.components.field import Field
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from typing import IO, List


class BlocoConvergenciaRelato(Block):
    """
    Bloco com as informações de convergência do DECOMP no relato.rvX.
    """

    BEGIN_PATTERN = "RELATORIO DE CONVERGENCIA DO PROCESSO ITERATIVO"
    END_PATTERN = ""

    def __init__(self, state=..., previous=None, next=None, data=None) -> None:
        super().__init__(state, previous, next, data)
        self.__line = Line(
            [
                IntegerField(4, 4),
                FloatField(12, 9, 1),
                FloatField(12, 22, 1),
                FloatField(16, 35, 7),
                LiteralField(8, 52),
                FloatField(61),
                FloatField(72),
                IntegerField(85),
                FloatField(93),
                FloatField(106),
                FloatField(119),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoConvergenciaRelato):
            return False
        bloco: BlocoConvergenciaRelato = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

    # Override
    def read(self, arq: IO):
        def converte_tabela_em_df() -> pd.DataFrame:
            colunas = [
                "Iteração",
                "Zinf",
                "Zsup",
                "Gap (%)",
                "Tempo (s)",
                "Tot. Def. Demanda (MWmed)",
                "Tot. Def. Niv. Seg. (MWmes)",
                "Num. Inviab",
                "Tot. Inviab (MWmed)",
                "Tot. Inviab (m3/s)",
                "Tot. Inviab (Hm3)",
            ]
            tipos = {
                "Iteração": np.int64,
                "Zinf": np.float64,
                "Zsup": np.float64,
                "Gap (%)": np.float64,
                "Tempo (s)": np.int64,
                "Tot. Def. Demanda (MWmed)": np.float64,
                "Tot. Def. Niv. Seg. (MWmes)": np.float64,
                "Num. Inviab": np.int64,
                "Tot. Inviab (MWmed)": np.float64,
                "Tot. Inviab (m3/s)": np.float64,
                "Tot. Inviab (Hm3)": np.float64,
            }
            df = pd.DataFrame(tabela, columns=colunas)
            df = df.astype(tipos)
            return df

        # Salta 9 linhas linha
        for _ in range(9):
            arq.readline()

        tabela = np.zeros((999, 11))
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if len(linha) < 5:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_em_df()
                break
            if "----" in linha:
                continue
            dados = self.__line.read(linha)
            # Senão, lê mais uma linha
            tabela[i, 0:4] = dados[0:4]
            parcelas = dados[4].split(":")
            segundos = (
                int(parcelas[0]) * 3600
                + int(parcelas[1]) * 60
                + int(parcelas[2])
            )
            tabela[i, 4] = segundos
            tabela[i, 5:11] = dados[5:11]
            i += 1


class BlocoRelatorioOperacaoUHERelato(Block):
    """ """

    BEGIN_PATTERN = "No.       Usina       Volume (% V.U.)"
    END_PATTERN = "X----X-"

    def __init__(self, state=..., previous=None, next=None, data=None) -> None:
        super().__init__(state, previous, next, data)
        self.__line = Line(
            [
                IntegerField(4, 4),
                LiteralField(12, 9),
                LiteralField(5, 21),
                FloatField(5, 27, 1),
                FloatField(5, 33, 1),
                FloatField(5, 39, 1),
                FloatField(7, 45, 1),
                FloatField(6, 54, 1),
                FloatField(8, 62, 1),
                FloatField(8, 71, 1),
                FloatField(7, 80, 1),
                FloatField(7, 88, 1),
                FloatField(7, 96, 1),
                FloatField(7, 104, 1),
                FloatField(7, 112, 1),
                FloatField(7, 120, 1),
                FloatField(7, 128, 1),
                FloatField(7, 136, 1),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoRelatorioOperacaoUHERelato):
            return False
        bloco: BlocoRelatorioOperacaoUHERelato = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

    # Override
    def le(self, arq: IO):
        def converte_tabela_para_df() -> pd.DataFrame:
            cols = [
                "Volume Ini (% V.U)",
                "Volume Fin (% V.U)",
                "Volume Esp. (% V.U)",
                "Qnat (m3/s)",
                "Qnat (% MLT)",
                "Qafl (m3/s)",
                "Qdef (m3/s)",
                "Geração Pat 1",
                "Geração Pat 2",
                "Geração Pat 3",
                "Geração Média",
                "Vertimento Turbinável",
                "Vertimento Não-Turbinável",
                "Ponta",
                "FPCGC",
            ]
            df = pd.DataFrame(tabela, columns=cols)
            cols_adic = [
                "Código",
                "Usina",
                "Evaporação",
                "Tempo de Viagem",
                "Cota Abaixo da Crista do Vert",
                "Def. Mínima = 0",
            ]
            df["Código"] = numeros
            df["Usina"] = usinas
            df["Evaporação"] = evaporacao
            df["Tempo de Viagem"] = tv_afluencia
            df["Cota Abaixo da Crista do Vert"] = cota_abaixo_crista
            df["Def. Mínima = 0"] = def_minima_zero
            df = df[cols_adic + cols]
            return df

        # Salta duas linhas
        arq.readline()
        arq.readline()

        # Variáveis auxiliares
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
            if self.ends(linha):
                tabela = tabela[:i, :]
                self._dados = converte_tabela_para_df()
                break
            dados = self.__line.read(linha)
            numeros.append(dados[0])
            usinas.append(dados[1])
            flags = dados[2]
            evaporacao.append("#" in flags)
            tv_afluencia.append("*" in flags)
            cota_abaixo_crista.append("@" in flags)
            def_minima_zero.append("$" in flags)
            tabela[i, :] = dados[3:]
            i += 1


class BlocoBalancoEnergeticoRelato(Block):
    """
    Bloco com as informações de eco dos dados gerais
    utilizados na execução do caso.
    """

    BEGIN_PATTERN = "RELATORIO  DO  BALANCO  ENERGETICO"
    END_PATTERN = "RELATORIO  DA  OPERACAO"

    def __init__(self, state=..., previous=None, next=None, data=None) -> None:
        super().__init__(state, previous, next, data)
        self.__linha_cenario = Line(
            [IntegerField(2, 34), IntegerField(3, 48), FloatField(8, 67, 6)]
        )
        self.__linha_subsistema = Line([LiteralField(3, 16)])
        self.__linha_ear_ena = Line(
            [FloatField(8, 13, 1), FloatField(8, 36, 1), FloatField(8, 63, 1)]
        )
        self.__linha_balanco = Line(
            [
                LiteralField(5, 4),
                FloatField(7, 10, 1),
                FloatField(7, 18, 1),
                FloatField(7, 26, 1),
                FloatField(7, 34, 1),
                FloatField(7, 42, 1),
                FloatField(7, 50, 1),
                FloatField(7, 58, 1),
                FloatField(7, 66, 1),
                FloatField(7, 74, 1),
                LiteralField(2, 83),
                FloatField(8, 86, 1),
                FloatField(7, 97, 1),
                FloatField(7, 105, 1),
            ]
        )
        # self.__linha_intercambio = Line(
        #     [
        #         LiteralField(2, 83),
        #         FloatField(8, 86, 1),
        #     ]
        # )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoBalancoEnergeticoRelato):
            return False
        bloco: BlocoBalancoEnergeticoRelato = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

    # Override
    def read(self, arq: IO):
        # Por retrocompatibilidade só lê valores médios.
        # TODO - Ler tudo. As linhas já estão modeladas.
        def converte_tabela_para_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = [
                "Mercado",
                "Bacia",
                "Cbomba",
                "Ghid",
                "Gter",
                "GterAT",
                "Deficit",
                "Compra",
                "Venda",
                "Itaipu50",
                "Itaipu60",
            ]
            df.columns = cols
            df["Subsistema"] = subsistemas
            df = df[["Subsistema"] + cols]
            return df

        # Variáveis auxiliares
        str_subsis = "     Subsistema"
        str_medio = "    Medio"
        subsis = "FC"
        estagios = []
        cenarios = []
        probabilidades = []
        subsistemas = []
        earms_iniciais_abs = []
        earms_iniciais_per = []
        ena_abs = []
        earms_finais_abs = []
        earms_finais_per = []
        # Salta duas linhas e extrai a semana
        arq.readline()
        arq.readline()
        dados = self.__linha_cenario(arq.readline())
        estagio = dados[0]
        cenario = dados[1]
        probabilidade = dados[2]
        tabela = np.zeros((MAX_ESTAGIOS * MAX_SUBSISTEMAS, 11))
        i = 0
        while True:
            linha = arq.readline()
            # Verifica se acabou
            if self.ends(linha):
                tabela = tabela[:i, :]
                self._dados = converte_tabela_para_df()
                break
            # Senão, procura a linha que identifica o subsistema
            if str_subsis in linha:
                subsis = self.__linha_subsistema.read(linha)[0]
                dados_ear_ena_abs = self.__linha_ear_ena.read(arq.readline())
                dados_ear_ena_per = self.__linha_ear_ena.read(arq.readline())
                earms_iniciais_abs.append(dados_ear_ena_abs[0])
                earms_iniciais_per.append(dados_ear_ena_per[0])
                ena_abs.append(dados_ear_ena_abs[1])
                earms_finais_abs.append(dados_ear_ena_abs[2])
                earms_finais_per.append(dados_ear_ena_per[2])
            # Se está lendo um subsistema e achou a linha de valores médios
            if subsis != "FC" and str_medio in linha:
                estagios.append(estagio)
                cenarios.append(cenario)
                probabilidades.append(probabilidade)
                subsistemas.append(subsis)
                dados = self.__linha_balanco.read(linha)
                tabela[i, :] = dados[1:10] + dados[11:]
                # Reseta o indicador de subsistema
                subsis = "FC"
                i += 1


class BlocoCMORelato(Block):
    """
    Bloco com as informações do CMO por estágio e por subsistema.
    """

    BEEGIN_PATTERN = "CUSTO MARGINAL DE OPERACAO  ($/MWh)"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoCMORelato):
            return False
        bloco: BlocoCMORelato = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

    # Override
    def read(self, arq: IO):
        def gera_coluna_patamares_subsistemas():
            n_patamares = len(patamares_distintos)
            n_subsistemas = len(subsistemas_distintos)
            col_subsistemas: List[str] = []

            pass

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
        arq.readline()
        num_estagios = (
            len([e for e in arq.readline().strip().split(" ") if len(e) > 0])
            - 1
        )
        campo_subsis: List[Field] = [LiteralField(6, 4)]
        campos_cmos: List[Field] = [
            FloatField(10, 11 + i * 11, 2) for i in range(num_estagios)
        ]
        self.__linha = Line(campo_subsis + campos_cmos)
        # Descobre o número de semanas
        subsistemas_distintos: list = []
        patamares_distintos: list = []
        tabela = np.zeros((MAX_SUBSISTEMAS * MAX_PATAMARES, num_estagios))
        # Salta outra linha
        arq.readline()
        i = 0
        # TODO - refazer: ler todos os patamares antes de fazer as colunas
        # separadas de subsistemas e patamares.
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X------X" in linha:
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__linha.read(linha)

            pat = "Médio" if "Med" in dados[0] else dados[0].split("_")[1]
            if pat.isnumeric():
                if pat not in subsistemas_distintos:
                    subsistemas_distintos.append(pat)
            else:
                if pat not in patamares_distintos:
                    patamares_distintos.append(pat)

            tabela[i, :] = dados[1:]
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

        super().__init__(
            BlocoGeracaoTermicaSubsistemaRelato.str_inicio, "", True
        )

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
        sems = [
            s
            for s in linha.split(" ")
            if (len(s) > 0 and ("Sem" in s or "Mes" in s))
        ]
        reg_ssis = RegistroAn(6)
        reg_gt = RegistroFn(10)
        n_semanas = len(sems)
        subsistemas: List[str] = []
        tabela = np.zeros((MAX_SUBSISTEMAS, n_semanas))
        # Salta outra linha
        arq.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X------X" in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e patamar
            ssis = reg_ssis.le_registro(linha, 4)
            subsistemas.append(ssis)
            # Semanas
            tabela[i, :] = reg_gt.le_linha_tabela(linha, 11, 1, n_semanas)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoVolumeUtilReservatorioRelato(Bloco):
    """
    Bloco com as informações de energia armazenada
    em percentual por REE.
    """

    str_inicio = " VOLUME UTIL DOS RESERVATORIOS"
    str_fim = ""

    def __init__(self):

        super().__init__(
            BlocoVolumeUtilReservatorioRelato.str_inicio, "", True
        )

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoVolumeUtilReservatorioRelato):
            return False
        bloco: BlocoVolumeUtilReservatorioRelato = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["Inicial"] + [
                f"Estágio {s}" for s in range(1, n_semanas + 1)
            ]
            df.columns = cols
            df["Usina"] = usinas
            df["Número"] = numeros
            df = df[["Número", "Usina"] + cols]
            return df

        # Salta duas linhas
        arq.readline()
        arq.readline()
        # Descobre o número de semanas
        linha = arq.readline()
        sems = [
            s
            for s in linha.split(" ")
            if (len(s) > 0 and ("Sem" in s or "Mes" in s))
        ]
        reg_usina = RegistroAn(12)
        reg_numero = RegistroIn(4)
        reg_vol = RegistroFn(6)
        n_semanas = len(sems)
        usinas: List[str] = []
        numeros: List[int] = []
        tabela = np.zeros((300, n_semanas + 1))
        # Salta outra linha
        arq.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X-------X" in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e REE
            numero = reg_numero.le_registro(linha, 4)
            usina = reg_usina.le_registro(linha, 9)
            numeros.append(numero)
            usinas.append(usina)
            # Semanas
            tabela[i, :] = reg_vol.le_linha_tabela(linha, 23, 1, n_semanas + 1)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoDadosTermicasRelato(Bloco):
    """
    Bloco com as informações de cadastro das térmicas existentes no estudo.
    """

    str_inicio = "Relatorio  dos  Dados  de  Usinas  Termicas"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoDadosTermicasRelato.str_inicio, "", True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoDadosTermicasRelato):
            return False
        bloco: BlocoDadosTermicasRelato = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):
        def converte_tabela_em_df() -> pd.DataFrame:
            cols = [
                "GT Min Pat. 1",
                "GT Max Pat. 1",
                "Custo Pat. 1",
                "GT Min Pat. 2",
                "GT Max Pat. 2",
                "Custo Pat. 2",
                "GT Min Pat. 3",
                "GT Max Pat. 3",
                "Custo Pat. 3",
            ]
            df = pd.DataFrame(tabela, columns=cols)
            df["Código"] = numeros
            df["Usina"] = usinas
            df["Subsistema"] = subsistemas
            df["Estágio"] = estagios
            df = df[["Código", "Usina", "Subsistema", "Estágio"] + cols]
            return df

        # Salta as linhas de cabeçalho
        for _ in range(4):
            arq.readline()

        reg_num = RegistroIn(3)
        reg_usina = RegistroAn(10)
        reg_subsis = RegistroAn(6)
        reg_estagio = RegistroIn(7)
        reg_valores = RegistroFn(7)
        numeros: List[int] = []
        usinas: List[str] = []
        subsistemas: List[str] = []
        estagios: List[int] = []

        tabela = np.zeros((5000, 9))

        i = 0
        num_atual = 0
        usina_atual = ""
        subsis_atual = ""
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X---X----------X" in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Verifica se começa uma nova UTE na linha
            if len(linha[4:7].strip()) > 0:
                num_atual = reg_num.le_registro(linha, 4)
                usina_atual = reg_usina.le_registro(linha, 8)
                subsis_atual = reg_subsis.le_registro(linha, 19)
            # Lê as propriedades existentes em todas as linhas
            numeros.append(num_atual)
            usinas.append(usina_atual)
            subsistemas.append(subsis_atual)
            estagios.append(reg_estagio.le_registro(linha, 26))
            tabela[i, :] = reg_valores.le_linha_tabela(linha, 34, 1, 9)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoDisponibilidadesTermicasRelato(Bloco):
    """
    Bloco com as informações de disponibilidade
    das térmicas existentes no estudo.
    """

    str_inicio = "Disponibilidade das Usinas Termicas (%)"
    str_fim = ""

    def __init__(self):

        super().__init__(
            BlocoDisponibilidadesTermicasRelato.str_inicio, "", True
        )

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoDisponibilidadesTermicasRelato):
            return False
        bloco: BlocoDisponibilidadesTermicasRelato = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):
        def converte_tabela_em_df() -> pd.DataFrame:
            cols = [f"Estágio {i}" for i in range(1, n_semanas + 1)]
            df = pd.DataFrame(tabela, columns=cols)
            df["Código"] = numeros
            df["Usina"] = usinas
            df = df[["Código", "Usina"] + cols]
            return df

        # Salta uma linha
        arq.readline()

        # Descobre o número de estágios
        linha = arq.readline()
        sems = [
            s
            for s in linha.split(" ")
            if (len(s) > 0 and ("Sem" in s or "Mes" in s))
        ]
        n_semanas = len(sems)

        reg_num = RegistroIn(3)
        reg_usina = RegistroAn(12)
        reg_valores = RegistroFn(6)
        numeros: List[int] = []
        usinas: List[str] = []
        tabela = np.zeros((300, n_semanas))

        # Salta outra linha
        arq.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X---X------------X" in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            numeros.append(reg_num.le_registro(linha, 4))
            usinas.append(reg_usina.le_registro(linha, 8))
            tabela[i, :] = reg_valores.le_linha_tabela(linha, 21, 1, n_semanas)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoDadosMercadoRelato(Bloco):
    """
    Bloco com as informações de mercado de energia por patamar
    e por subsistema existente no :class:`Relato`.
    """

    str_inicio = "Relatorio  dos  Dados  de  Mercado"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoDadosMercadoRelato.str_inicio, "", True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoDadosMercadoRelato):
            return False
        bloco: BlocoDadosMercadoRelato = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):
        def converte_tabela_em_df() -> pd.DataFrame:
            cols = [
                "Patamar 1",
                "Mercado 1",
                "Patamar 2",
                "Mercado 2",
                "Patamar 3",
                "Mercado 3",
            ]
            df = pd.DataFrame(tabela, columns=cols)
            df["Estágio"] = estagios
            df["Subsistema"] = subsistemas
            df = df[["Estágio", "Subsistema"] + cols]
            return df

        # Salta as linhas de cabeçalho
        for _ in range(4):
            arq.readline()

        reg_estagio = RegistroIn(9)
        reg_subsis = RegistroAn(6)
        reg_valores = RegistroFn(9)
        estagios: List[int] = []
        subsistemas: List[str] = []

        tabela = np.zeros((100, 6))

        i = 0
        estagio_atual = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X---------X------X" in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Verifica se começa um novo estágio na linha
            if len(linha[4:13].strip()) > 0:
                estagio_atual = reg_estagio.le_registro(linha, 4)
            # Lê as propriedades existentes em todas as linhas
            estagios.append(estagio_atual)
            subsistemas.append(reg_subsis.le_registro(linha, 14))
            tabela[i, :] = reg_valores.le_linha_tabela(linha, 21, 1, 6)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoENAAcoplamentoREERelato(Bloco):
    """
    Bloco com as informações de energia natural afluente para
    acoplamento com o longo prazo por REE.
    """

    str_inicio = "Afluente para Acoplamento c/ Longo Prazo por REE"
    str_fim = "Afluente para Acoplamento c/ Longo Prazo por Subsistema"

    def __init__(self):

        super().__init__(BlocoENAAcoplamentoREERelato.str_inicio, "", True)

        self._dados: pd.DataFrame = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoENAAcoplamentoREERelato):
            return False
        bloco: BlocoENAAcoplamentoREERelato = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):
        def le_tabela(linha: str) -> np.ndarray:
            indice_ree = int(linha.split("REE: ")[1].split("-")[0].strip())
            ree = linha.split("REE: ")[1].split("/")[0].split("-")[1].strip()
            subsis = linha.split("SUBSISTEMA: ")[1].split("-")[1].strip()
            # Salta uma linha para identificar o número de estágios
            arq.readline()
            lin = arq.readline()
            sems = [
                s
                for s in lin.split(" ")
                if (len(s) > 0 and ("Sem" in s or "Mes" in s))
            ]
            n_semanas = len(sems)
            arq.readline()
            # Começa a ler os cenários
            reg_cen = RegistroIn(3)
            reg_ena = RegistroFn(8)
            tab = np.zeros((1000, n_semanas + 1))
            i = 0
            while True:
                lin = arq.readline()
                if len(lin) < 4:
                    tab = tab[:i, :]
                    break
                tab[i, 0] = reg_cen.le_registro(lin, 4)
                tab[i, 1:] = reg_ena.le_linha_tabela(lin, 8, 1, n_semanas)
                indices_rees.append(indice_ree)
                rees.append(ree)
                subsistemas.append(subsis)
                i += 1
            return tab

        def converte_tabela_em_df() -> pd.DataFrame:
            if isinstance(tabela, np.ndarray):
                df = pd.DataFrame(tabela)
                n_semanas = tabela.shape[1] - 1
            else:
                raise TypeError("Erro na leitura das ENAs para acoplamento")
            cols = ["Cenário"] + [
                f"Estágio {s}" for s in range(1, n_semanas + 1)
            ]
            df.columns = cols
            df["Índice"] = indices_rees
            df["REE"] = rees
            df["Subsistema"] = subsistemas
            df = df[["Índice", "REE", "Subsistema"] + cols]
            df = df.astype({"Cenário": np.int64})
            return df

        indices_rees: List[int] = []
        rees: List[str] = []
        subsistemas: List[str] = []
        tabela = None
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if BlocoENAAcoplamentoREERelato.str_fim in linha:
                self._dados = converte_tabela_em_df()
                return linha
            if "REE: " in linha:
                tab = le_tabela(linha)
                if tabela is None:
                    tabela = tab
                else:
                    tabela = np.vstack([tabela, tab])

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

        super().__init__(BlocoEnergiaArmazenadaREERelato.str_inicio, "", True)

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
            cols = ["Inicial"] + [
                f"Estágio {s}" for s in range(1, n_semanas + 1)
            ]
            df.columns = cols
            df["Subsistema"] = subsistemas
            df["REE"] = rees
            df = df[["Subsistema", "REE"] + cols]
            return df

        # Salta uma linha
        arq.readline()
        # Descobre o número de semanas
        linha = arq.readline()
        sems = [
            s
            for s in linha.split(" ")
            if (len(s) > 0 and ("Sem" in s or "Mes" in s))
        ]
        reg_ree = RegistroAn(12)
        reg_ssis = RegistroIn(4)
        n_semanas = len(sems)
        rees: List[str] = []
        subsistemas: List[int] = []
        tabela = np.zeros((MAX_REES, n_semanas + 1))
        # Salta outra linha
        arq.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X------X" in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e REE
            ree = reg_ree.le_registro(linha, 4)
            ssis = reg_ssis.le_registro(linha, 22) - 1
            rees.append(ree)
            subsistemas.append(ssis)
            # Semanas
            ci = 28
            for col in range(n_semanas + 1):
                cf = ci + 6
                conteudo = linha[ci:cf].strip()
                if not conteudo.replace(".", "0").isnumeric():
                    tabela[i, col] = np.nan
                else:
                    tabela[i, col] = float(conteudo)
                ci = cf + 1
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

        super().__init__(
            BlocoEnergiaArmazenadaSubsistemaRelato.str_inicio, "", True
        )

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
            cols = ["Inicial"] + [
                f"Estágio {s}" for s in range(1, n_semanas + 1)
            ]
            df.columns = cols
            df["Subsistema"] = subsistemas
            df = df[["Subsistema"] + cols]
            return df

        # Salta uma linha
        arq.readline()
        # Descobre o número de semanas
        linha = arq.readline()
        sems = [
            s
            for s in linha.split(" ")
            if (len(s) > 0 and ("Sem" in s or "Mes" in s))
        ]
        reg_ssis = RegistroAn(12)
        reg_earm = RegistroFn(6)
        n_semanas = len(sems)
        subsistemas: List[str] = []
        tabela = np.zeros((MAX_SUBSISTEMAS, n_semanas + 1))
        # Salta outra linha
        arq.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X------------X" in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e REE
            ssis = reg_ssis.le_registro(linha, 4)
            subsistemas.append(ssis)
            # Semanas
            tabela[i, :] = reg_earm.le_linha_tabela(
                linha, 23, 1, n_semanas + 1
            )
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoENAPreEstudoMensalREERelato(Bloco):
    """
    Bloco com as informações da ENA pré estudo mensal do caso
    por REE.
    """

    str_inicio = "ENERGIA NATURAL AFLUENTE POR REE (MESES"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoENAPreEstudoMensalREERelato.str_inicio, "", True)

        self._dados = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoENAPreEstudoMensalREERelato):
            return False
        bloco: BlocoENAPreEstudoMensalREERelato = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["Earmax"] + [f"Estágio Pré {s}" for s in range(1, 12)]
            df.columns = cols
            df["REE"] = rees
            df = df[["REE"] + cols]
            return df

        # Salta 4 linhas
        for _ in range(4):
            arq.readline()
        reg_ree = RegistroAn(14)
        reg_ena = RegistroFn(8)
        rees: List[str] = []
        tabela = np.zeros((20, 12))
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X--------------X" in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e REE
            ssis = reg_ree.le_registro(linha, 4)
            rees.append(ssis)
            # Semanas
            tabela[i, :] = reg_ena.le_linha_tabela(linha, 29, 1, 12)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoENAPreEstudoMensalSubsistemaRelato(Bloco):
    """
    Bloco com as informações da ENA pré estudo mensal do caso
    por Subsistema.
    """

    str_inicio = "ENERGIA NATURAL AFLUENTE POR SUBSISTEMA (MESES"
    str_fim = ""

    def __init__(self):

        super().__init__(
            BlocoENAPreEstudoMensalSubsistemaRelato.str_inicio, "", True
        )

        self._dados = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoENAPreEstudoMensalSubsistemaRelato):
            return False
        bloco: BlocoENAPreEstudoMensalSubsistemaRelato = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["Earmax"] + [f"Estágio Pré {s}" for s in range(1, 12)]
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
        tabela = np.zeros((MAX_SUBSISTEMAS, 12))
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X--------------X" in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e REE
            ssis = reg_ssis.le_registro(linha, 4)
            subsistemas.append(ssis)
            # Semanas
            tabela[i, :] = reg_ena.le_linha_tabela(linha, 24, 1, 12)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoENAPreEstudoSemanalREERelato(Bloco):
    """
    Bloco com as informações da ENA pré estudo semanal do caso
    por REE.
    """

    str_inicio = "DADOS DE ENERGIA NATURAL AFLUENTE POR REE (SEMANAS"
    str_fim = ""

    def __init__(self):

        super().__init__(
            BlocoENAPreEstudoSemanalREERelato.str_inicio, "", True
        )

        self._dados = pd.DataFrame()

    def __eq__(self, o: object):
        if not isinstance(o, BlocoENAPreEstudoSemanalREERelato):
            return False
        bloco: BlocoENAPreEstudoSemanalREERelato = o
        return self._dados.equals(bloco._dados)

    # Override
    def le(self, arq: IO):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["Earmax"] + [f"Estágio Pré {s}" for s in range(1, 6)]
            df.columns = cols
            df["REE"] = rees
            df = df[["REE"] + cols]
            # Remove as colunas preenchidas com 0
            for c in cols:
                if df[c].max() == 0:
                    df.drop(columns=[c], inplace=True)
            return df

        # Salta 4 linhas
        for _ in range(4):
            arq.readline()
        reg_ree = RegistroAn(14)
        reg_ena = RegistroFn(8)
        rees: List[str] = []
        tabela = np.zeros((20, 6))
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X--------------X" in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e REE
            ssis = reg_ree.le_registro(linha, 4)
            rees.append(ssis)
            # Semanas
            tabela[i, :] = reg_ena.le_linha_tabela(linha, 29, 1, 6)
            i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class BlocoENAPreEstudoSemanalSubsistemaRelato(Bloco):
    """
    Bloco com as informações da ENA pré estudo semanal do caso
    por Subsistema.
    """

    str_inicio = "NATURAL AFLUENTE POR SUBSISTEMA(SEMANAS"
    str_fim = ""

    def __init__(self):

        super().__init__(
            BlocoENAPreEstudoSemanalSubsistemaRelato.str_inicio, "", True
        )

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
            cols = ["Earmax"] + [f"Estágio Pré {s}" for s in range(1, 6)]
            df.columns = cols
            df["Subsistema"] = subsistemas
            df = df[["Subsistema"] + cols]
            # Remove as colunas preenchidas com 0
            for c in cols:
                if df[c].max() == 0:
                    df.drop(columns=c, inplace=True)
            return df

        # Salta 4 linhas
        for _ in range(4):
            arq.readline()
        reg_ssis = RegistroAn(14)
        reg_ena = RegistroFn(8)
        subsistemas: List[str] = []
        tabela = np.zeros((MAX_SUBSISTEMAS, 6))
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = arq.readline()
            if "X--------------X" in linha:
                tabela = tabela[:i, :]
                self._dados = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e REE
            ssis = reg_ssis.le_registro(linha, 4)
            subsistemas.append(ssis)
            # Semanas
            tabela[i, :] = reg_ena.le_linha_tabela(linha, 24, 1, 6)
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

        super().__init__(BlocoDiasExcluidosSemanas.str_inicio, "", True)

        self._dados = [0, 0]

    def __eq__(self, o: object):
        if not isinstance(o, BlocoDiasExcluidosSemanas):
            return False
        bloco: BlocoDiasExcluidosSemanas = o
        return all(
            [
                self._dados[0] == bloco._dados[0],
                self._dados[1] == bloco._dados[1],
            ]
        )

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

    def __init__(self, diretorio: str):
        super().__init__(diretorio)

    # Override
    def _cria_blocos_leitura(self) -> List[Bloco]:
        """
        Cria a lista de blocos a serem lidos no arquivo adterm.dat.
        """
        relat_uhe: List[Bloco] = [
            BlocoRelatorioOperacaoUHERelato() for _ in range(10)
        ]
        balanc_energ: List[Bloco] = [
            BlocoBalancoEnergeticoRelato() for _ in range(10)
        ]
        return (
            [
                BlocoDadosGeraisRelato(),
                BlocoConvergenciaRelato(),
                BlocoCMORelato(),
                BlocoVolumeUtilReservatorioRelato(),
                BlocoDadosTermicasRelato(),
                BlocoDisponibilidadesTermicasRelato(),
                BlocoDadosMercadoRelato(),
                BlocoENAAcoplamentoREERelato(),
                BlocoEnergiaArmazenadaREERelato(),
                BlocoEnergiaArmazenadaSubsistemaRelato(),
                BlocoENAPreEstudoMensalREERelato(),
                BlocoENAPreEstudoMensalSubsistemaRelato(),
                BlocoENAPreEstudoSemanalREERelato(),
                BlocoENAPreEstudoSemanalSubsistemaRelato(),
                BlocoGeracaoTermicaSubsistemaRelato(),
                BlocoDiasExcluidosSemanas(),
            ]
            + relat_uhe
            + balanc_energ
        )
