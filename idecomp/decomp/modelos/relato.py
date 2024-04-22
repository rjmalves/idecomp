# Imports do próprio módulo
from idecomp.config import (
    MAX_CENARIOS,
    MAX_ESTAGIOS,
    MAX_PATAMARES,
    MAX_SUBSISTEMAS,
    MAX_REES,
    MAX_UHES,
    MAX_UTES,
    MESES_DF,
)

# Imports de módulos externos
from cfinterface.components.block import Block
from cfinterface.components.line import Line
from cfinterface.components.field import Field
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from typing import IO, List, Tuple, Dict


class BlocoREEsSubsistemas(Block):
    """
    Bloco com as informações de relação entre os REEs e os
    Subsistemas do DECOMP no relato.rvX.
    """

    __slots__ = ["__line"]

    BEGIN_PATTERN = "Relatorio dos dados da configuracao dos Reservatorios"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__line = Line(
            [
                IntegerField(4, 4),
                LiteralField(15, 9),
                IntegerField(4, 25),
                LiteralField(6, 30),
                LiteralField(11, 38),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoREEsSubsistemas):
            return False
        bloco: BlocoREEsSubsistemas = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(
                data={
                    "codigo_ree": numeros,
                    "nome_ree": nomes,
                    "codigo_submercado": numeros_subsistema,
                    "nome_submercado": nomes_subsistema,
                    "nome_submercado_newave": nomes_newave,
                },
            )
            return df

        comecou = False
        numeros: List[int] = []
        nomes: List[str] = []
        numeros_subsistema: List[int] = []
        nomes_subsistema: List[str] = []
        nomes_newave: List[str] = []
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X----X-----" in linha:
                if not comecou:
                    comecou = True
                    continue
                else:
                    self.data = converte_tabela_em_df()
                    break
            if comecou:
                # Senão, lê mais uma linha
                dados = self.__line.read(linha)
                numeros.append(dados[0])
                nomes.append(dados[1])
                numeros_subsistema.append(dados[2])
                nomes_subsistema.append(dados[3])
                nomes_newave.append(dados[4])


class BlocoUHEsREEsSubsistemas(Block):
    """
    Bloco com as informações de relação entre os REEs e os
    Subsistemas do DECOMP no relato.rvX.
    """

    __slots__ = ["__line"]

    BEGIN_PATTERN = (
        "Relatorio dos dados de Configuracao das Usinas Hidroeletricas"
    )
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__line = Line(
            [
                IntegerField(4, 4),
                LiteralField(15, 9),
                IntegerField(4, 25),
                LiteralField(15, 30),
                IntegerField(4, 46),
                LiteralField(6, 51),
                LiteralField(11, 63),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoUHEsREEsSubsistemas):
            return False
        bloco: BlocoUHEsREEsSubsistemas = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(
                data={
                    "codigo_usina": numeros,
                    "nome_usina": nomes,
                    "codigo_ree": numeros_rees,
                    "nome_ree": nomes_rees,
                    "codigo_submercado": numeros_subsistema,
                    "nome_submercado": nomes_subsistema,
                    "nome_submercado_newave": nomes_newave,
                },
            )
            return df

        comecou = False
        numeros: List[int] = []
        nomes: List[str] = []
        numeros_rees: List[int] = []
        nomes_rees: List[str] = []
        numeros_subsistema: List[int] = []
        nomes_subsistema: List[str] = []
        nomes_newave: List[str] = []
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X----X-----" in linha:
                if not comecou:
                    comecou = True
                    continue
                else:
                    self.data = converte_tabela_em_df()
                    break
            if comecou:
                # Senão, lê mais uma linha
                dados = self.__line.read(linha)
                numeros.append(dados[0])
                nomes.append(dados[1])
                numeros_rees.append(dados[2])
                nomes_rees.append(dados[3])
                numeros_subsistema.append(dados[4])
                nomes_subsistema.append(dados[5])
                nomes_newave.append(dados[6])


class BlocoConvergenciaRelato(Block):
    """
    Bloco com as informações de convergência do DECOMP no relato.rvX.
    """

    __slots__ = ["__line"]

    BEGIN_PATTERN = "RELATORIO DE CONVERGENCIA DO PROCESSO ITERATIVO"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__line = Line(
            [
                IntegerField(4, 4),
                FloatField(12, 9, 1),
                FloatField(12, 22, 1),
                FloatField(16, 35, 7),
                LiteralField(8, 52),
                FloatField(10, 61, 0),
                FloatField(10, 72, 0),
                IntegerField(7, 85),
                FloatField(12, 93, 0),
                FloatField(12, 106, 0),
                FloatField(12, 119, 0),
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            colunas = [
                "iteracao",
                "zinf",
                "zsup",
                "gap_percentual",
                "tempo",
                "deficit_demanda_MWmed",
                "deficit_nivel_seguranca_MWmes",
                "numero_inviabilidades",
                "inviabilidades_MWmed",
                "inviabilidades_m3s",
                "inviabilidades_hm3",
            ]
            tipos = {
                "iteracao": np.int64,
                "zinf": np.float64,
                "zsup": np.float64,
                "gap_percentual": np.float64,
                "tempo": np.int64,
                "deficit_demanda_MWmed": np.float64,
                "deficit_nivel_seguranca_MWmes": np.float64,
                "numero_inviabilidades": np.int64,
                "inviabilidades_MWmed": np.float64,
                "inviabilidades_m3s": np.float64,
                "inviabilidades_hm3": np.float64,
            }
            df = pd.DataFrame(tabela, columns=colunas)
            df = df.astype(tipos)
            return df

        # Salta 9 linhas linha
        for _ in range(9):
            file.readline()

        tabela = np.zeros((999, 11))
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if len(linha) < 5:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
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


class BlocoRelatorioOperacaoRelato(Block):
    """
    Bloco com as informações do relatório da operação do DECOMP no relato.rvX.
    """

    __slots__ = ["__line", "__scenario_line", "dados_cenario"]

    BEGIN_PATTERN = r"RELATORIO  DA  OPERACAO "
    END_PATTERN = "X----X-"

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__scenario_line = Line(
            [IntegerField(2, 34), IntegerField(4, 47), FloatField(8, 67, 6)]
        )
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
        if not isinstance(o, BlocoRelatorioOperacaoRelato):
            return False
        bloco: BlocoRelatorioOperacaoRelato = o
        if not all(
            [
                isinstance(self.data, list),
                isinstance(bloco.data, list),
            ]
        ):
            return False
        else:
            return all(
                [
                    self.data[0] == bloco.data[0],
                    self.data[1].equals(bloco.data[1]),
                ]
            )

    def __read_bloco_operacao_uhe(self, file: IO):
        def converte_tabela_para_df() -> pd.DataFrame:
            cols = [
                "volume_inicial_percentual",
                "volume_final_percentual",
                "volume_espera_percentual",
                "vazao_natural_m3s",
                "vazao_natural_mlt",
                "vazao_afluente_m3s",
                "vazao_defluente_m3s",
                "geracao_patamar_1",
                "geracao_patamar_2",
                "geracao_patamar_3",
                "geracao_media",
                "vertimento_turbinavel",
                "vertimento_nao_turbinavel",
                "geracao_ponta",
                "FPCGC",
            ]
            df = pd.DataFrame(tabela, columns=cols)
            cols_adic = [
                "estagio",
                "cenario",
                "probabilidade",
                "codigo_usina",
                "nome_usina",
                "considera_evaporacao",
                "considera_tempo_viagem",
                "considera_soleira_vertedouro",
                "considera_defluencia_minima_0",
            ]
            df["estagio"] = [estagio] * len(numeros)
            df["cenario"] = [cenario] * len(numeros)
            df["probabilidade"] = [probabilidade] * len(numeros)
            df["codigo_usina"] = numeros
            df["nome_usina"] = usinas
            df["considera_evaporacao"] = evaporacao
            df["considera_tempo_viagem"] = tv_afluencia
            df["considera_soleira_vertedouro"] = cota_abaixo_crista
            df["considera_defluencia_minima_0"] = def_minima_zero
            df = df[cols_adic + cols]
            return df

        estagio: int = self.dados_cenario[0]
        cenario: int = self.dados_cenario[1]
        probabilidade: float = self.dados_cenario[2]

        # Salta 7 linhas
        for _ in range(7):
            file.readline()

        # Variáveis auxiliares
        numeros: List[int] = []
        usinas: List[str] = []
        evaporacao: List[bool] = []
        tv_afluencia: List[bool] = []
        cota_abaixo_crista: List[bool] = []
        def_minima_zero: List[bool] = []
        # Salta uma linha e extrai a semana
        tabela: np.ndarray = np.zeros((MAX_UHES, 15))
        i = 0
        while True:
            linha: str = file.readline()
            # Verifica se acabou
            if self.ends(linha):
                tabela = tabela[:i, :]
                self.data = ["UHE", converte_tabela_para_df()]
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

    def __read_bloco_operacao_geral(self, file: IO):
        def converte_tabela_para_df() -> pd.DataFrame:
            df = pd.DataFrame(
                data={
                    "estagio": estagio,
                    "cenario": cenario,
                    "probabilidade": probabilidade,
                    "custo_futuro": custo_futuro,
                    "custo_presente": custo_estagio,
                    "geracao_termica": custo_gt,
                    "violacao_desvio": custo_desvio,
                    "penalidade_vertimento_reservatorio": custo_vert_reservatorio,
                    "penalidade_vertimento_fio": custo_vert_fio,
                    "violacao_turbinamento_reservatorio": custo_turbinamento_reservatorio,
                    "violacao_turbinamento_fio": custo_turbinamento_fio,
                    "penalidade_intercambio": custo_intercambio,
                }
            )
            for subsis, cmo in cmos.items():
                df[f"cmo_{subsis}"] = cmo
            return df

        estagio: int = self.dados_cenario[0]
        cenario: int = self.dados_cenario[1]
        probabilidade: float = self.dados_cenario[2]

        linha_custo = Line([FloatField(14, 54, 2)])
        linha_custo_exp = Line([FloatField(14, 54, 2, format="E")])
        linha_custo_subsis = Line([LiteralField(2, 44), FloatField(14, 54, 2)])

        custo_futuro: list = linha_custo.read(file.readline())
        file.readline()
        file.readline()
        custo_estagio: list = linha_custo.read(file.readline())
        file.readline()
        file.readline()
        custo_gt: list = linha_custo.read(file.readline())
        file.readline()
        file.readline()
        file.readline()
        file.readline()
        custo_desvio: list = linha_custo.read(file.readline())
        custo_vert_reservatorio: list = linha_custo.read(file.readline())
        custo_vert_fio: list = linha_custo.read(file.readline())
        custo_turbinamento_reservatorio: list = linha_custo.read(
            file.readline()
        )
        custo_turbinamento_fio: list = linha_custo.read(file.readline())
        custo_intercambio: list = linha_custo_exp.read(file.readline())
        file.readline()

        cmos: Dict[str, float] = {}
        while True:
            linha = file.readline()
            if len(linha.strip()) < 4:
                self.data = ["GERAL", converte_tabela_para_df()]
                break
            dados_linha = linha_custo_subsis.read(linha)
            cmos[dados_linha[0]] = dados_linha[1]

    # Override
    def read(self, file: IO, *args, **kwargs):
        str_bloco_operacao_uhe = "# Aproveitamento(s) com evaporacao "
        str_bloco_operacao_geral = "Valor  esperado  do  custo  futuro:"
        # str_bloco_restricoes_rhe = (
        #     "Relatorio das restricoes de meta de armazenamento (MWmes) "
        # )

        # Salta duas linhas e extrai a semana
        for _ in range(2):
            file.readline()
        self.dados_cenario = self.__scenario_line.read(file.readline())

        # Salta duas linhas e extrai o tipo do bloco
        file.readline()
        linha_tipo_bloco = file.readline()
        bloco_operacao_uhe = str_bloco_operacao_uhe in linha_tipo_bloco
        bloco_operacao_geral = False
        # bloco_restricoes_rhe = str_bloco_restricoes_rhe in linha_tipo_bloco

        if not bloco_operacao_uhe:
            pos = file.tell()
            linha_tipo_bloco = file.readline()
            file.seek(pos)
            bloco_operacao_geral = str_bloco_operacao_geral in linha_tipo_bloco

        # TODO - não ignorar bloco RHE, ler
        if not (bloco_operacao_uhe or bloco_operacao_geral):
            self.data = ["RHE", pd.DataFrame()]
            return

        if bloco_operacao_uhe:
            self.__read_bloco_operacao_uhe(file)
        elif bloco_operacao_geral:
            self.__read_bloco_operacao_geral(file)


class BlocoRelatorioOperacaoUTERelato(Block):
    """
    Bloco com as informações do relatório da operação por usina térmica
    do DECOMP no relato.rvX.
    """

    __slots__ = ["__line", "__scenario_line"]

    BEGIN_PATTERN = r"RELATORIO  DA  OPERACAO  TERMICA E CONTRATOS"
    END_PATTERN = "RELATORIO  DO  BALANCO  ENERGETICO"

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__scenario_line = Line(
            [IntegerField(2, 34), IntegerField(4, 47), FloatField(8, 67, 6)]
        )
        self.__line = Line(
            [
                LiteralField(3, 4),
                LiteralField(11, 8),
                FloatField(7, 20, 2),
                FloatField(10, 28, 2),
                FloatField(10, 40, 2),
                FloatField(10, 52, 2),
                FloatField(11, 64, 2),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoRelatorioOperacaoUTERelato):
            return False
        bloco: BlocoRelatorioOperacaoUTERelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_para_df() -> pd.DataFrame:
            cols = [f"geracao_patamar{i}" for i in range(1, n_pats + 1)] + [
                "custo"
            ]
            df = pd.DataFrame(tabela, columns=cols)
            cols_adic = [
                "estagio",
                "cenario",
                "probabilidade",
                "nome_submercado",
                "nome_usina",
                "FPCGC",
            ]
            df["estagio"] = [estagio] * len(subsistemas)
            df["cenario"] = [cenario] * len(subsistemas)
            df["probabilidade"] = [probabilidade] * len(subsistemas)
            df["nome_submercado"] = subsistemas
            df["nome_usina"] = nomes_usinas
            df["FPCGC"] = fpcgcs
            df = df[cols_adic + cols]
            return df

        subsistemas = []
        nomes_usinas = []
        fpcgcs = []
        str_bloco_subsistema = " Contrato    (%) "
        str_ignorar = "X---X---------"
        str_fim_bloco = "      T o t a l  Termica"
        # Salta duas linhas e extrai a semana
        for _ in range(2):
            file.readline()
        dados = self.__scenario_line.read(file.readline())

        # Salta duas linhas e extrai o número de patamares
        for _ in range(2):
            file.readline()
        n_pats = len([s for s in file.readline().split() if "Ene_pat_" in s])

        estagio = dados[0]
        cenario = dados[1]
        probabilidade = dados[2]

        # Salta uma linha e extrai a semana
        tabela = np.zeros((MAX_UTES, n_pats + 1))
        i = 0
        while True:
            posicao_ultima_linha = file.tell()
            linha: str = file.readline()
            # Verifica se acabou
            if self.ends(linha):
                tabela = tabela[:i, :]
                file.seek(posicao_ultima_linha)
                self.data = converte_tabela_para_df()
                break
            # Verifica se começou um bloco de usinas
            if str_bloco_subsistema in linha:
                iniciou_bloco = True
            elif str_ignorar in linha:
                continue
            elif str_fim_bloco in linha:
                iniciou_bloco = False
            elif iniciou_bloco:
                # Lê o conteúdo de um bloco
                dados = self.__line.read(linha)
                subsistemas.append(dados[0])
                nomes_usinas.append(dados[1])
                fpcgcs.append(dados[2])
                tabela[i, :] = dados[3 : (3 + n_pats + 1)]
                i += 1


class BlocoBalancoEnergeticoRelato(Block):
    """
    Bloco com as informações de eco dos dados gerais
    utilizados na execução do caso.
    """

    __slots__ = [
        "__linha_cenario",
        "__linha_subsistema",
        "__linha_ear_ena",
        "__linha_balanco",
    ]

    BEGIN_PATTERN = "RELATORIO  DO  BALANCO  ENERGETICO"
    END_PATTERN = r"RELATORIO\s+DA\s+OPERACAO"  # noqa

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha_cenario = Line(
            [IntegerField(2, 34), IntegerField(4, 47), FloatField(8, 67, 6)]
        )
        self.__linha_subsistema = Line([LiteralField(3, 16)])
        self.__linha_ear_ena = Line(
            [FloatField(8, 13, 1), FloatField(8, 36, 1), FloatField(8, 63, 1)]
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

    def __define_linha_balanco(self, cabecalho: str) -> Tuple[Line, List[str]]:
        colunas = [c for c in cabecalho.split(" ") if len(c) > 2]
        colunas = [c.strip("\n") for c in colunas]
        if "Interligacao" not in colunas:
            return Line([]), []
        indice_intercambio = colunas.index("Interligacao")
        campo_patamar: List[Field] = [LiteralField(5, 4)]
        campos_balanco: List[Field] = [
            FloatField(7, 10 + 8 * i, 1) for i in range(indice_intercambio)
        ]
        campo_subsis: List[Field] = [
            LiteralField(2, 10 + 8 * indice_intercambio + 1)
        ]
        campo_interligacao: List[Field] = [
            FloatField(8, 10 + 8 * indice_intercambio + 4, 1)
        ]
        campos_apos_interligacao: List[Field] = [
            FloatField(7, 25 + 8 * indice_intercambio + 8 * i, 1)
            for i in range(2)
        ]
        return Line(
            campo_patamar
            + campos_balanco
            + campo_subsis
            + campo_interligacao
            + campos_apos_interligacao
        ), [c for c in colunas if c != "Interligacao"]

    # Override
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_para_df() -> pd.DataFrame:
            tamanho_maior_linha = max([len(lin) for lin in linhas])
            tabela = np.zeros((len(linhas), tamanho_maior_linha))
            for i, lin in enumerate(linhas):
                tabela[i, : len(lin)] = lin
            df = pd.DataFrame(tabela)
            mapa_colunas_balanco = {
                "Mercado": "mercado",
                "Bacia": "bacia",
                "Cbomba": "consumo_bombeamento",
                "Ghid": "geracao_hidraulica",
                "Gter": "geracao_termica",
                "GterAT": "geracao_termica_antecipada",
                "Geol": "geracao_eolica",
                "Deficit": "deficit",
                "Venda": "venda",
                "Compra": "compra",
                "Itaipu50": "geracao_itaipu_50hz",
                "Itaipu60": "geracao_itaipu_60hz",
            }
            colunas_balanco_mapeadas = [
                mapa_colunas_balanco.get(c, c) for c in colunas_balanco
            ]
            df.columns = colunas_balanco_mapeadas
            df["estagio"] = estagios
            df["cenario"] = cenarios
            df["probabilidade"] = probabilidades
            df["nome_submercado"] = subsistemas
            df["patamar"] = patamares
            df["energia_armazenada_inicial_MWmed"] = earms_iniciais_abs
            df["energia_armazenada_inicial_percentual"] = earms_iniciais_per
            df["energia_natural_afluente_MWmed"] = ena_abs
            df["energia_natural_afluente_percentual"] = ena_per
            df["energia_armazenada_final_MWmed"] = earms_finais_abs
            df["energia_armazenada_final_percentual"] = earms_finais_per
            cols_adic = [
                "estagio",
                "cenario",
                "probabilidade",
                "nome_submercado",
                "patamar",
                "energia_armazenada_inicial_MWmed",
                "energia_armazenada_inicial_percentual",
                "energia_natural_afluente_MWmed",
                "energia_natural_afluente_percentual",
                "energia_armazenada_final_MWmed",
                "energia_armazenada_final_percentual",
            ]
            df = df[cols_adic + colunas_balanco_mapeadas]
            return df

        # Variáveis auxiliares
        str_subsis = "     Subsistema"
        str_pat = "   Pat_"
        str_medio = "    Medio"
        subsis = "NAN"
        estagios = []
        cenarios = []
        probabilidades = []
        subsistemas = []
        patamares = []
        earms_iniciais_abs = []
        earms_iniciais_per = []
        ena_abs = []
        ena_per = []
        earms_finais_abs = []
        earms_finais_per = []
        # Salta duas linhas e extrai a semana
        file.readline()
        file.readline()
        dados = self.__linha_cenario.read(file.readline())
        estagio = dados[0]
        cenario = dados[1]
        probabilidade = dados[2]
        linhas: List[List[float]] = []
        colunas_balanco: List[str] = []
        while True:
            pos = file.tell()
            linha = file.readline()
            # Verifica se acabou
            if self.ends(linha):
                file.seek(pos)
                self.data = converte_tabela_para_df()
                break
            # Senão, procura a linha que identifica o subsistema
            if str_subsis in linha:
                subsis = self.__linha_subsistema.read(linha)[0]
                dados_ear_ena_abs = self.__linha_ear_ena.read(file.readline())
                dados_ear_ena_per = self.__linha_ear_ena.read(file.readline())
                # Ignora uma linha
                file.readline()
                self.__linha_balanco, colunas = self.__define_linha_balanco(
                    file.readline()
                )
                if len(colunas_balanco) < len(colunas):
                    colunas_balanco = colunas
            # Se está lendo um subsistema e achou a linha de valores médios
            if subsis != "FC" and (str_medio in linha or str_pat in linha):
                estagios.append(estagio)
                cenarios.append(cenario)
                probabilidades.append(probabilidade)
                subsistemas.append(subsis)
                earms_iniciais_abs.append(dados_ear_ena_abs[0])
                earms_iniciais_per.append(dados_ear_ena_per[0])
                ena_abs.append(dados_ear_ena_abs[1])
                ena_per.append(dados_ear_ena_per[1])
                earms_finais_abs.append(dados_ear_ena_abs[2])
                earms_finais_per.append(dados_ear_ena_per[2])
                dados = self.__linha_balanco.read(linha)
                patamares.append(
                    dados[0]
                    if str_pat not in linha
                    else dados[0].strip(str_pat)
                )
                indice_subsis = dados.index(
                    [d for d in dados if type(d) is str][1]
                )
                dados_antes_interligacao: List[float] = [
                    d for d in dados[1:indice_subsis] if d is not None
                ]
                dados_apos_interligacao: List[float] = [
                    d for d in dados[indice_subsis + 2 :] if d is not None
                ]
                linhas.append(
                    dados_antes_interligacao + dados_apos_interligacao
                )
                if str_medio in linha:
                    # Reseta o indicador de subsistema
                    subsis = "FC"


class BlocoCMORelato(Block):
    """
    Bloco com as informações do CMO por estágio e por subsistema.
    """

    __slots__ = ["__linha"]

    BEGIN_PATTERN = "   CUSTO MARGINAL DE OPERACAO"
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = [f"estagio_{s}" for s in range(1, num_estagios + 1)]
            patamares = (patamares_distintos + ["medio"]) * len(
                subsistemas_distintos
            )
            subsistemas = [
                [s] * (len(patamares_distintos) + 1)
                for s in subsistemas_distintos
            ]
            subsistemas = [p for s in subsistemas for p in s]
            df.columns = cols
            df["nome_submercado"] = subsistemas
            df["patamar"] = patamares
            df = df[["nome_submercado", "patamar"] + cols]
            return df

        # Salta duas linhas
        file.readline()
        file.readline()
        num_estagios = (
            len([e for e in file.readline().strip().split(" ") if len(e) > 2])
            - 1
        )
        num_estagios
        campo_subsis: List[Field] = [LiteralField(6, 4)]
        campos_cmos: List[Field] = [
            FloatField(10, 11 + i * 11, 2) for i in range(num_estagios)
        ]
        self.__linha = Line(campo_subsis + campos_cmos)
        subsistemas_distintos: list = []
        patamares_distintos: list = []
        tabela = np.zeros((MAX_SUBSISTEMAS * MAX_PATAMARES, num_estagios))
        # Salta outra linha
        file.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X------X" in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__linha.read(linha)

            pat = "Médio" if "Med" in dados[0] else dados[0].split("_")[1]
            if pat.isnumeric():
                if pat not in patamares_distintos:
                    patamares_distintos.append(pat)
            else:
                subsis = dados[0].split("_")[1]
                if subsis not in subsistemas_distintos:
                    subsistemas_distintos.append(subsis)

            tabela[i, :] = dados[1:]
            i += 1


class BlocoCustoOperacaoValorEsperadoRelato(Block):
    """
    Bloco com as informações de custo de operação
    presente e futuro por estágio.
    """

    __slots__ = ["__linha"]

    BEGIN_PATTERN = r"CUSTO DE OPERACAO E VALOR ESPERADO DO C\.FUTURO"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoCustoOperacaoValorEsperadoRelato):
            return False
        bloco: BlocoCustoOperacaoValorEsperadoRelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = [f"estagio_{s}" for s in range(1, num_estagios + 1)]
            df.columns = cols
            df["parcela"] = parcelas
            df = df[["parcela"] + cols]
            return df

        # Salta duas linhas
        file.readline()
        file.readline()
        num_estagios = len(
            [e for e in file.readline().strip().split(" ") if len(e) > 2]
        )
        campo_parcela: List[Field] = [LiteralField(6, 4)]
        campos_custos: List[Field] = [
            FloatField(12, 11 + i * 13, 1) for i in range(num_estagios)
        ]
        self.__linha = Line(campo_parcela + campos_custos)
        parcelas: list = []
        tabela = np.zeros((2, num_estagios))
        # Salta outra linha
        file.readline()
        for i in range(2):
            linha = file.readline()
            dados = self.__linha.read(linha)
            parcelas.append(dados[0])
            tabela[i, :] = dados[1:]
        self.data = converte_tabela_em_df()


class BlocoGeracaoTermicaSubsistemaRelato(Block):
    """
    Bloco com as informações de eco dos dados gerais
    utilizados na execução do caso.
    """

    __slots__ = ["__linha"]

    BEGIN_PATTERN = r"GERACAO TERMICA NOS SUSBSISTEMAS \(MWmed\)"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoGeracaoTermicaSubsistemaRelato):
            return False
        bloco: BlocoGeracaoTermicaSubsistemaRelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = [f"estagio_{s}" for s in range(1, num_estagios + 1)]
            df.columns = cols
            df["nome_submercado"] = subsistemas
            df = df[["nome_submercado"] + cols]
            return df

        # Salta duas linhas
        file.readline()
        file.readline()
        num_estagios = (
            len([e for e in file.readline().strip().split(" ") if len(e) > 2])
            - 1
        )
        campo_subsis: List[Field] = [LiteralField(6, 4)]
        campos_gt: List[Field] = [
            FloatField(10, 11 + i * 11, 1) for i in range(num_estagios)
        ]
        self.__linha = Line(campo_subsis + campos_gt)
        subsistemas: list = []
        tabela = np.zeros((MAX_SUBSISTEMAS * MAX_PATAMARES, num_estagios))
        # Salta outra linha
        file.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X------X" in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__linha.read(linha)
            subsistemas.append(dados[0])
            tabela[i, :] = dados[1:]
            i += 1


class BlocoVolumeUtilReservatorioRelato(Block):
    """
    Bloco com as informações de energia armazenada
    em percentual por REE.
    """

    __slots__ = ["__linha"]

    BEGIN_PATTERN = " VOLUME UTIL DOS RESERVATORIOS"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoVolumeUtilReservatorioRelato):
            return False
        bloco: BlocoVolumeUtilReservatorioRelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["inicial"] + [
                f"estagio_{s}" for s in range(1, num_estagios + 1)
            ]
            df.columns = cols
            df["nome_usina"] = usinas
            df["codigo_usina"] = numeros
            df = df[["codigo_usina", "nome_usina"] + cols]
            return df

        for _ in range(3):
            file.readline()

        num_estagios = (
            len([e for e in file.readline().strip().split(" ") if len(e) > 2])
            - 1
        )
        campo_usi: List[Field] = [
            IntegerField(3, 4),
            LiteralField(12, 8),
            FloatField(7, 22, 1),
        ]
        campos_vu: List[Field] = [
            FloatField(6, 30 + i * 7, 1) for i in range(num_estagios)
        ]
        self.__linha = Line(campo_usi + campos_vu)
        numeros: List[int] = []
        usinas: List[str] = []
        tabela = np.zeros((MAX_UHES, num_estagios + 1))
        # Salta outra linha
        file.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X------X" in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__linha.read(linha)
            numeros.append(dados[0])
            usinas.append(dados[1])
            tabela[i, :] = dados[2:]
            i += 1


class BlocoDadosTermicasRelato(Block):
    """
    Bloco com as informações de cadastro das térmicas existentes no estudo.
    """

    __slots__ = ["__line"]

    BEGIN_PATTERN = "Relatorio  dos  Dados  de  Usinas  Termicas"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__line = Line(
            [
                IntegerField(3, 4),
                LiteralField(10, 8),
                LiteralField(6, 19),
                IntegerField(7, 26),
                FloatField(7, 34, 2),
                FloatField(7, 42, 2),
                FloatField(7, 50, 2),
                FloatField(7, 58, 2),
                FloatField(7, 66, 2),
                FloatField(7, 74, 2),
                FloatField(7, 82, 2),
                FloatField(7, 90, 2),
                FloatField(7, 98, 2),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoDadosTermicasRelato):
            return False
        bloco: BlocoDadosTermicasRelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            cols = [
                "geracao_minima_patamar_1",
                "geracao_maxima_patamar_1",
                "custo_patamar_1",
                "geracao_minima_patamar_2",
                "geracao_maxima_patamar_2",
                "custo_patamar_2",
                "geracao_minima_patamar_3",
                "geracao_maxima_patamar_3",
                "custo_patamar_3",
            ]
            df = pd.DataFrame(tabela, columns=cols)
            df["codigo_usina"] = numeros
            df["nome_usina"] = usinas
            df["nome_submercado"] = subsistemas
            df["estagio"] = estagios
            df = df[
                ["codigo_usina", "nome_usina", "nome_submercado", "estagio"]
                + cols
            ]
            return df

        # Salta as linhas de cabeçalho
        for _ in range(5):
            file.readline()

        numeros: List[int] = []
        usinas: List[str] = []
        subsistemas: List[str] = []
        estagios: List[int] = []

        tabela = np.zeros((MAX_ESTAGIOS * MAX_UTES, 9))

        i = 0
        num_atual = 0
        usina_atual = ""
        subsis_atual = ""
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X---X----------X" in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__line.read(linha)
            # Verifica se começa uma nova UTE na linha
            if len(linha[4:7].strip()) > 0:
                num_atual = dados[0]
                usina_atual = dados[1]
                subsis_atual = dados[2]
            # Lê as propriedades existentes em todas as linhas
            numeros.append(num_atual)
            usinas.append(usina_atual)
            subsistemas.append(subsis_atual)
            estagios.append(dados[3])
            tabela[i, :] = dados[4:]
            i += 1


class BlocoDisponibilidadesTermicasRelato(Block):
    """
    Bloco com as informações de disponibilidade
    das térmicas existentes no estudo.
    """

    __slots__ = ["__linha"]

    BEGIN_PATTERN = r"Disponibilidade das Usinas Termicas \(\%\)"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoDisponibilidadesTermicasRelato):
            return False
        bloco: BlocoDisponibilidadesTermicasRelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = [f"estagio_{s}" for s in range(1, num_estagios + 1)]
            df.columns = cols
            df["nome_usina"] = usinas
            df["codigo_usina"] = numeros
            df = df[["codigo_usina", "nome_usina"] + cols]
            return df

        # Salta 4 linhas
        for _ in range(2):
            file.readline()

        num_estagios = (
            len([e for e in file.readline().strip().split(" ") if len(e) > 2])
            - 2
        )
        campo_usi: List[Field] = [
            IntegerField(3, 4),
            LiteralField(12, 8),
        ]
        campos_vu: List[Field] = [
            FloatField(6, 21 + i * 7, 1) for i in range(num_estagios)
        ]
        self.__linha = Line(campo_usi + campos_vu)
        numeros: List[int] = []
        usinas: List[str] = []
        tabela = np.zeros((MAX_UTES, num_estagios))
        # Salta outra linha
        file.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X------X" in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__linha.read(linha)
            numeros.append(dados[0])
            usinas.append(dados[1])
            tabela[i, :] = dados[2:]
            i += 1


class BlocoDadosMercadoRelato(Block):
    """
    Bloco com as informações de mercado de energia por patamar
    e por subsistema existente no :class:`Relato`.
    """

    __slots__ = ["__line"]

    BEGIN_PATTERN = "Relatorio  dos  Dados  de  Mercado"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__line = Line(
            [
                IntegerField(9, 4),
                LiteralField(6, 14),
                FloatField(9, 21, 1),
                FloatField(9, 31, 1),
                FloatField(9, 41, 1),
                FloatField(9, 51, 1),
                FloatField(9, 61, 1),
                FloatField(9, 71, 1),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoDadosMercadoRelato):
            return False
        bloco: BlocoDadosMercadoRelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            cols = [
                "patamar_1",
                "mercado_1",
                "patamar_2",
                "mercado_2",
                "patamar_3",
                "mercado_3",
            ]
            df = pd.DataFrame(tabela, columns=cols)
            df["estagio"] = estagios
            df["nome_submercado"] = subsistemas
            df = df[["estagio", "nome_submercado"] + cols]
            return df

        # Salta as linhas de cabeçalho
        for _ in range(5):
            file.readline()

        estagios: List[int] = []
        subsistemas: List[str] = []

        tabela = np.zeros((MAX_ESTAGIOS * MAX_SUBSISTEMAS, 6))

        i = 0
        estagio_atual = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X---------X------X" in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__line.read(linha)
            # Verifica se começa um novo estágio na linha
            estagio_atual = dados[0] if dados[0] is not None else estagio_atual
            # Lê as propriedades existentes em todas as linhas
            estagios.append(estagio_atual)
            subsistemas.append(dados[1])
            tabela[i, :] = dados[2:]
            i += 1


class BlocoENAAcoplamentoREERelato(Block):
    """
    Bloco com as informações de energia natural afluente para
    acoplamento com o longo prazo por REE.
    """

    __slots__ = []

    BEGIN_PATTERN = r"Afluente para Acoplamento c\/ Longo Prazo por REE"
    END_PATTERN = r"Afluente para Acoplamento c\/ Longo Prazo por Subsistema"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoENAAcoplamentoREERelato):
            return False
        bloco: BlocoENAAcoplamentoREERelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def le_tabela(linha: str) -> np.ndarray:
            indice_ree = int(linha.split("REE: ")[1].split("-")[0].strip())
            ree = linha.split("REE: ")[1].split("/")[0].split("-")[1].strip()
            subsis = linha.split("SUBSISTEMA: ")[1].split("-")[1].strip()
            # Salta uma linha para identificar o número de estágios
            file.readline()
            linha = file.readline()
            estagios = [s for s in linha.split(" ") if len(s) > 2]
            num_estagios = len(estagios) - 1
            file.readline()
            campo_cenario: List[Field] = [IntegerField(3, 4)]
            campos_enas: List[Field] = [
                FloatField(8, 8 + 9 * i, 1) for i in range(num_estagios)
            ]
            linha_tabela = Line(campo_cenario + campos_enas)
            # Começa a ler os cenários
            tab = np.zeros((MAX_CENARIOS, num_estagios + 1))
            i = 0
            while True:
                linha = file.readline()
                if len(linha) < 4:
                    tab = tab[:i, :]
                    break
                tab[i, :] = linha_tabela.read(linha)
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
            cols = ["cenario"] + [
                f"estagio_{s}" for s in range(1, n_semanas + 1)
            ]
            df.columns = cols
            df["codigo_ree"] = indices_rees
            df["nome_ree"] = rees
            df["nome_submercado"] = subsistemas
            df = df[["codigo_ree", "nome_ree", "nome_submercado"] + cols]
            df = df.astype({"cenario": np.int64})
            return df

        indices_rees: List[int] = []
        rees: List[str] = []
        subsistemas: List[str] = []
        tabela = None
        while True:
            # Confere se a leitura não acabou
            ultima_linha = file.tell()
            linha = file.readline()
            if self.ends(linha):
                self.data = converte_tabela_em_df()
                file.seek(ultima_linha)
                return linha
            if "REE: " in linha:
                tab = le_tabela(linha)
                if tabela is None:
                    tabela = tab
                else:
                    tabela = np.vstack([tabela, tab])


class BlocoEnergiaArmazenadaREERelato(Block):
    """
    Bloco com as informações de energia armazenada
    em percentual por REE.
    """

    __slots__ = ["__linha"]

    BEGIN_PATTERN = r"ENERGIA ARMAZENADA NOS REEs \(\%"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoEnergiaArmazenadaREERelato):
            return False
        bloco: BlocoEnergiaArmazenadaREERelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["inicial"] + [
                f"estagio_{s}" for s in range(1, num_estagios + 1)
            ]
            df.columns = cols
            df["nome_submercado"] = subsistemas
            df["nome_ree"] = rees
            df = df[["nome_submercado", "nome_ree"] + cols]
            return df

        # Salta 2 linhas
        for _ in range(2):
            file.readline()

        num_estagios = (
            len([e for e in file.readline().strip().split(" ") if len(e) > 2])
            - 3
        )

        campos_ree: List[Field] = [
            LiteralField(12, 4),
            IntegerField(4, 17),
            IntegerField(4, 22),
            FloatField(7, 27, 1),
        ]
        campos_vu: List[Field] = [
            FloatField(6, 35 + i * 7, 1) for i in range(num_estagios)
        ]
        self.__linha = Line(campos_ree + campos_vu)
        rees: List[str] = []
        numeros: List[int] = []
        subsistemas: List[int] = []
        tabela = np.zeros((MAX_REES, num_estagios + 1))
        # Salta outra linha
        file.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X------------X" in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__linha.read(linha)
            rees.append(dados[0])
            numeros.append(dados[1])
            subsistemas.append(dados[2])
            tabela[i, :] = dados[3:]
            i += 1


class BlocoEnergiaArmazenadaSubsistemaRelato(Block):
    """
    Bloco com as informações de energia armazenada
    em percentual por REE.
    """

    __slots__ = ["__linha"]

    BEGIN_PATTERN = r"ENERGIA ARMAZENADA NOS SUBSISTEMAS \(\%"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoEnergiaArmazenadaSubsistemaRelato):
            return False
        bloco: BlocoEnergiaArmazenadaSubsistemaRelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["inicial"] + [
                f"estagio_{s}" for s in range(1, num_estagios + 1)
            ]
            df.columns = cols
            df["nome_submercado"] = subsistemas
            df = df[["nome_submercado"] + cols]
            return df

        # Salta 2 linhas
        for _ in range(2):
            file.readline()

        num_estagios = (
            len([e for e in file.readline().strip().split(" ") if len(e) > 2])
            - 2
        )

        campos_ree: List[Field] = [
            LiteralField(12, 4),
            IntegerField(4, 17),
            FloatField(7, 22, 1),
        ]
        campos_vu: List[Field] = [
            FloatField(6, 30 + i * 7, 1) for i in range(num_estagios)
        ]
        self.__linha = Line(campos_ree + campos_vu)
        subsistemas: List[int] = []
        numeros: List[int] = []
        tabela = np.zeros((MAX_REES, num_estagios + 1))
        # Salta outra linha
        file.readline()
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X------------X" in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__linha.read(linha)
            subsistemas.append(dados[0])
            numeros.append(dados[1])
            tabela[i, :] = dados[2:]
            i += 1


class BlocoENAPreEstudoMensalREERelato(Block):
    """
    Bloco com as informações da ENA pré estudo mensal do caso
    por REE.
    """

    __slots__ = ["__line"]

    BEGIN_PATTERN = r"ENERGIA NATURAL AFLUENTE POR REE \(MESES"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        campos_ree: List[Field] = [
            LiteralField(14, 4),
            IntegerField(4, 19),
            IntegerField(4, 24),
            FloatField(8, 29, 1),
        ]
        campos_ena: List[Field] = [
            FloatField(8, 38 + i * 9, 1) for i in range(len(MESES_DF) - 1)
        ]
        self.__line = Line(campos_ree + campos_ena)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoENAPreEstudoMensalREERelato):
            return False
        bloco: BlocoENAPreEstudoMensalREERelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["energia_armazenada_maxima"] + [
                f"estagio_pre_{s}" for s in range(1, 12)
            ]
            df.columns = cols
            df["nome_ree"] = rees
            df = df[["nome_ree"] + cols]
            return df

        # Salta 5 linhas
        for _ in range(5):
            file.readline()

        rees: List[str] = []
        tabela = np.zeros((MAX_REES, len(MESES_DF)))
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X--------------X" in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e REE
            dados = self.__line.read(linha)
            rees.append(dados[0])
            # Semanas
            tabela[i, :] = dados[3:]
            i += 1


class BlocoENAPreEstudoMensalSubsistemaRelato(Block):
    """
    Bloco com as informações da ENA pré estudo mensal do caso
    por Subsistema.
    """

    __slots__ = ["__line"]

    BEGIN_PATTERN = r"ENERGIA NATURAL AFLUENTE POR SUBSISTEMA \(MESES"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        campos_subsis: List[Field] = [
            LiteralField(14, 4),
            IntegerField(4, 19),
            FloatField(8, 24, 1),
        ]
        campos_ena: List[Field] = [
            FloatField(8, 33 + i * 9, 1) for i in range(len(MESES_DF) - 1)
        ]
        self.__line = Line(campos_subsis + campos_ena)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoENAPreEstudoMensalSubsistemaRelato):
            return False
        bloco: BlocoENAPreEstudoMensalSubsistemaRelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["energia_armazenada_maxima"] + [
                f"estagio_pre_{s}" for s in range(1, 12)
            ]
            df.columns = cols
            df["nome_submercado"] = subsistemas
            df = df[["nome_submercado"] + cols]
            return df

        # Salta 5 linhas
        for _ in range(5):
            file.readline()

        subsistemas: List[str] = []
        tabela = np.zeros((MAX_SUBSISTEMAS, len(MESES_DF)))
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X--------------X" in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            # Subsistema e REE
            dados = self.__line.read(linha)
            subsistemas.append(dados[0])
            # Semanas
            tabela[i, :] = dados[2:]
            i += 1


class BlocoENAPreEstudoSemanalREERelato(Block):
    """
    Bloco com as informações da ENA pré estudo semanal do caso
    por REE.
    """

    __slots__ = ["__line"]

    BEGIN_PATTERN = r"DADOS DE ENERGIA NATURAL AFLUENTE POR REE \(SEMANAS"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        campos_ree: List[Field] = [
            LiteralField(14, 4),
            IntegerField(4, 19),
            IntegerField(4, 24),
            FloatField(8, 29, 1),
        ]
        campos_ena: List[Field] = [
            FloatField(8, 38 + i * 9, 1) for i in range(5)
        ]
        self.__line = Line(campos_ree + campos_ena)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoENAPreEstudoSemanalREERelato):
            return False
        bloco: BlocoENAPreEstudoSemanalREERelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["energia_armazenada_maxima"] + [
                f"estagio_pre_{s}" for s in range(1, 6)
            ]
            df.columns = cols
            df["nome_ree"] = rees
            df = df[["nome_ree"] + cols]
            # Remove as colunas preenchidas com 0
            for c in cols:
                if df[c].max() == 0:
                    df.drop(columns=[c], inplace=True)
            return df

        # Salta 5 linhas
        for _ in range(5):
            file.readline()

        rees: List[str] = []
        tabela = np.zeros((MAX_REES, 6))
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X--------------X" in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__line.read(linha)
            # REE
            rees.append(dados[0])
            # Semanas
            tabela[i, :] = dados[3:]
            i += 1


class BlocoENAPreEstudoSemanalSubsistemaRelato(Block):
    """
    Bloco com as informações da ENA pré estudo semanal do caso
    por Subsistema.
    """

    __slots__ = ["__line"]

    BEGIN_PATTERN = r"NATURAL AFLUENTE POR SUBSISTEMA\(SEMANAS"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        campos_subsis: List[Field] = [
            LiteralField(14, 4),
            IntegerField(4, 19),
            FloatField(8, 24, 1),
        ]
        campos_ena: List[Field] = [
            FloatField(8, 33 + i * 9, 1) for i in range(5)
        ]
        self.__line = Line(campos_subsis + campos_ena)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoENAPreEstudoSemanalSubsistemaRelato):
            return False
        bloco: BlocoENAPreEstudoSemanalSubsistemaRelato = o
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
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            cols = ["energia_armazenada_maxima"] + [
                f"estagio_pre_{s}" for s in range(1, 6)
            ]
            df.columns = cols
            df["nome_submercado"] = subsistemas
            df = df[["nome_submercado"] + cols]
            # Remove as colunas preenchidas com 0
            for c in cols:
                if df[c].max() == 0:
                    df.drop(columns=[c], inplace=True)
            return df

        # Salta 5 linhas
        for _ in range(5):
            file.readline()

        subsistemas: List[str] = []
        tabela = np.zeros((MAX_SUBSISTEMAS, 6))
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if "X--------------X" in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__line.read(linha)
            # Subsistema
            subsistemas.append(dados[0])
            # Semanas
            tabela[i, :] = dados[2:]
            i += 1


class BlocoDiasExcluidosSemanas(Block):
    """
    Bloco com as informações de dias excluídos das semanas
    inicial e final do estudo.
    """

    __slots__ = ["__line"]

    BEGIN_PATTERN = " Mes inicial do periodo de estudos"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)

        self.__line = Line([IntegerField(2, 53)])

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoDiasExcluidosSemanas):
            return False
        bloco: BlocoDiasExcluidosSemanas = o
        if not all(
            [
                isinstance(self.data, list),
                isinstance(o.data, list),
            ]
        ):
            return False
        else:
            return self.data == bloco.data

    # Override
    def read(self, file: IO, *args, **kwargs):
        file.readline()
        dias_semana_inicial = self.__line.read(file.readline())[0]
        dias_semana_final = self.__line.read(file.readline())[0]
        self.data = [dias_semana_inicial, dias_semana_final]
