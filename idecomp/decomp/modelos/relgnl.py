# Imports do próprio módulo
from idecomp.config import MAX_ESTAGIOS, MAX_UTES

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


class BlocoDadosUsinasRelgnl(Block):
    """
    Bloco com as informações de eco dos dados gerais
    utilizados na execução do caso.
    """

    __slots__ = ["__line"]

    BEGIN_PATTERN = "Relatorio  dos  Dados  de  Usinas  Termicas GNL"
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
        if not isinstance(o, BlocoDadosUsinasRelgnl):
            return False
        bloco: BlocoDadosUsinasRelgnl = o
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


class BlocoComandosUsinasAjustesTGRelgnl(Block):
    """
    Bloco com as informações de eco dos dados gerais
    utilizados na execução do caso.
    """

    __slots__ = ["__linha"]

    BEGIN_PATTERN = "usinas GNL com possiveis ajustes devido a registros TG"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoComandosUsinasAjustesTGRelgnl):
            return False
        bloco: BlocoComandosUsinasAjustesTGRelgnl = o
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
            colunas = ["patamar_1", "patamar_2", "patamar_3"]
            df = pd.DataFrame(tabela, columns=colunas)
            df["codigo_usina"] = numeros
            df["nome_usina"] = usinas
            df["lag"] = lags
            df["nome_submercado"] = subsistemas
            df["semana"] = semanas
            df = df[
                [
                    "codigo_usina",
                    "nome_usina",
                    "lag",
                    "nome_submercado",
                    "semana",
                ]
                + colunas
            ]
            return df

        file.readline()
        file.readline()
        num_estagios = len(
            [e for e in file.readline().strip().split(" ") if len(e) > 2]
        )
        file.readline()
        file.readline()
        campo_usi: List[Field] = [
            IntegerField(3, 3),
            LiteralField(11, 8),
            IntegerField(3, 20),
            LiteralField(6, 24),
            LiteralField(11, 31),
        ]
        campos_cmos: List[Field] = [
            FloatField(11, 43 + i * 11, 2) for i in range(num_estagios)
        ]
        self.__linha = Line(campo_usi + campos_cmos)
        numeros: List[int] = []
        usinas: List[str] = []
        lags: List[int] = []
        subsistemas: List[str] = []
        semanas: List[str] = []
        tabela = np.zeros((MAX_UTES * MAX_ESTAGIOS, num_estagios))
        i = 0
        while True:
            linha: str = file.readline()
            if len(linha) < 3:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            dados = self.__linha.read(linha)
            numeros.append(dados[0])
            usinas.append(dados[1])
            lags.append(dados[2])
            subsistemas.append(dados[3])
            semanas.append(dados[4])
            tabela[i, :] = dados[5:]
            i += 1


class BlocoComandosUsinasAjustesRERelgnl(Block):
    """
    Bloco com as informações de eco dos dados gerais
    utilizados na execução do caso.
    """

    __slots__ = ["__linha"]

    BEGIN_PATTERN = "ajustes devido a Restricoes Eletricas Especiais"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoComandosUsinasAjustesRERelgnl):
            return False
        bloco: BlocoComandosUsinasAjustesRERelgnl = o
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
            colunas = ["patamar_1", "patamar_2", "patamar_3"]
            df = pd.DataFrame(tabela, columns=colunas)
            df["codigo_usina"] = numeros
            df["nome_usina"] = usinas
            df["lag"] = lags
            df["nome_submercado"] = subsistemas
            df["estagio"] = semanas
            df = df[
                [
                    "codigo_usina",
                    "nome_usina",
                    "lag",
                    "nome_submercado",
                    "estagio",
                ]
                + colunas
            ]
            return df

        # Salta duas linhas
        file.readline()
        file.readline()
        num_estagios = len(
            [e for e in file.readline().strip().split(" ") if len(e) > 2]
        )
        file.readline()
        file.readline()
        campo_usi: List[Field] = [
            IntegerField(3, 3),
            LiteralField(11, 8),
            IntegerField(3, 20),
            LiteralField(6, 24),
            IntegerField(9, 31),
        ]
        campos_cmos: List[Field] = [
            FloatField(11, 41 + i * 11, 2) for i in range(num_estagios)
        ]
        self.__linha = Line(campo_usi + campos_cmos)
        numeros: List[int] = []
        usinas: List[str] = []
        lags: List[int] = []
        subsistemas: List[str] = []
        semanas: List[str] = []
        tabela = np.zeros((MAX_UTES * MAX_ESTAGIOS, num_estagios))
        i = 0
        while True:
            linha: str = file.readline()
            if len(linha) < 3:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            dados = self.__linha.read(linha)
            numeros.append(dados[0])
            usinas.append(dados[1])
            lags.append(dados[2])
            subsistemas.append(dados[3])
            semanas.append(dados[4])
            tabela[i, :] = dados[5:]
            i += 1


class BlocoRelatorioOperacaoRelgnl(Block):
    """
    Bloco com as informações de eco dos dados gerais
    utilizados na execução do caso.
    """

    __slots__ = ["__linha_cenario", "__linha_operacao"]

    BEGIN_PATTERN = "RELATORIO  DA  OPERACAO  TERMICA E CONTRATOS"
    END_PATTERN = "RELATORIO  DA  OPERACAO  TERMICA E CONTRATOS"

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha_cenario = Line(
            [IntegerField(2, 34), IntegerField(4, 47), FloatField(8, 67, 6)]
        )
        self.__linha_operacao = Line(
            [
                LiteralField(3, 4),
                LiteralField(11, 8),
                IntegerField(7, 20),
                LiteralField(7, 28),
                FloatField(8, 36, 2),
                FloatField(7, 45, 2),
                FloatField(8, 53, 2),
                FloatField(7, 62, 2),
                FloatField(8, 70, 2),
                FloatField(7, 79, 2),
                FloatField(10, 87, 2),
                LiteralField(12, 98),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoRelatorioOperacaoRelgnl):
            return False
        bloco: BlocoRelatorioOperacaoRelgnl = o
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
            df = pd.DataFrame(tabela)
            cols = [
                "geracao_patamar_1",
                "duracao_patamar_1",
                "geracao_patamar_2",
                "duracao_patamar_2",
                "geracao_patamar_3",
                "duracao_patamar_3",
                "custo",
            ]
            df.columns = cols
            df["estagio"] = periodo
            df["cenario"] = cenario
            df["probabilidade"] = probabilidade
            df["nome_submercado"] = subsistemas
            df["nome_usina"] = usinas
            df["lag"] = lags
            df["semana"] = estagios
            df["data_inicio_semana"] = inicio_semanas
            df = df[
                [
                    "estagio",
                    "cenario",
                    "probabilidade",
                    "nome_submercado",
                    "nome_usina",
                    "lag",
                    "semana",
                    "data_inicio_semana",
                ]
                + cols
            ]
            return df

        # Variáveis auxiliares
        str_tabela = "Sinalizacao de Despacho antecipado em k meses"

        subsistemas: List[str] = []
        usinas: List[str] = []
        lags: List[int] = []
        estagios: List[str] = []
        inicio_semanas: List[str] = []

        # Salta duas linhas e extrai o estágio / cenário
        file.readline()
        file.readline()
        dados = self.__linha_cenario.read(file.readline())
        periodo: int = dados[0]
        cenario: int = dados[1]
        probabilidade: float = dados[2]

        tabela = np.zeros((MAX_ESTAGIOS * MAX_UTES, 7))
        i = 0
        achou_tabela = False
        while True:
            ultima_linha = file.tell()
            linha = file.readline()
            # Verifica se acabou
            if self.ends(linha) or len(linha) == 0:
                file.seek(ultima_linha)
                tabela = tabela[:i, :]
                self.data = converte_tabela_para_df()
                break
            # Senão, procura a linha que identifica o subsistema
            if str_tabela in linha:
                achou_tabela = True
                # Salta 4 linhas
                for _ in range(4):
                    file.readline()
            elif len(linha) < 5:
                achou_tabela = False
            # Se está lendo um subsistema e achou a linha de valores médios
            elif achou_tabela:
                dados = self.__linha_operacao.read(linha)
                subsistemas.append(dados[0])
                usinas.append(dados[1])
                lags.append(dados[2])
                estagios.append(dados[3])
                tabela[i, :] = dados[4:11]
                inicio_semanas.append(dados[11])
                i += 1
