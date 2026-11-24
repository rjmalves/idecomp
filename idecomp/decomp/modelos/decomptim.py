# Imports de módulos externos
import re
from datetime import date, time, timedelta
from typing import IO, Any, ClassVar, Final, Literal

import pandas as pd  # type: ignore[import-untyped]
from cfinterface.components.block import Block

_TEMPO: Final = re.compile(r"(\d+)h\s*(\d+)min\s*([\d.]+)s")
_LEITURA_DADOS: Final = re.compile(r"^Leitura de Dados:")
_ENVIO_INICIAL: Final = re.compile(r"^Envio de Variaveis:")
_GRUPO_ITERACAO: Final = re.compile(
    r"^Iteracao\s+(\d+)\s+-\s+Envio de Variaveis:"
)
_GRUPO_FINAL: Final = re.compile(
    r"^(Impressao|Sim\. Final)\s+-\s+Envio de Variaveis:"
)
_DESCIDA_1A_PARTE: Final = re.compile(r"^\s+Descida 1a Parte:")
_DESCIDA_2A_PARTE: Final = re.compile(r"^\s+Descida 2a Parte:")
_RETORNO: Final = re.compile(r"^\s+Retorno:")
_TOTAL_GRUPO: Final = re.compile(r"^\s+Total:")
_IMPRESSAO: Final = re.compile(r"^Tempo de Impressao:")
_TEMPO_TOTAL: Final = re.compile(r"^Tempo Total:")
_COLUNAS_ITERACOES: Final = [
    "iteracao",
    "envio_variaveis",
    "descida_1a_parte",
    "descida_2a_parte",
    "retorno",
    "total",
]


def _tempo(linha: str, etapa: str) -> timedelta:
    m = _TEMPO.search(linha)
    if m is None:
        raise ValueError(f"Tempo não encontrado na linha de {etapa}: {linha!r}")
    return timedelta(hours=int(m[1]), minutes=int(m[2]), seconds=float(m[3]))


class _BlocoCabecalho(Block):
    """
    Bloco base para as linhas do cabeçalho do arquivo decomp.tim, em que
    o valor é lido da própria linha de início do bloco.
    """

    __slots__ = []

    END_PATTERN = ""
    CAMPO: ClassVar[str]
    VALOR: ClassVar[re.Pattern[str]]

    @staticmethod
    def converte(m: re.Match[str]) -> Any:
        return m[1]

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, _BlocoCabecalho) or type(o) is not type(self):
            return False
        return self.data is not None and self.data == o.data

    # Override
    def read(self, file: IO[Any], *args: Any, **kwargs: Any) -> bool:
        linha = file.readline()
        m = self.VALOR.search(linha)
        if m is None:
            raise ValueError(
                f"Valor não encontrado na linha de {self.CAMPO}: {linha!r}"
            )
        try:
            self.data = self.converte(m)
        except ValueError as e:
            raise ValueError(
                f"Valor inválido na linha de {self.CAMPO}: {linha!r}"
            ) from e
        return True


class BlocoVersaoModelo(_BlocoCabecalho):
    """
    Bloco com a versão do DECOMP existente no cabeçalho do arquivo
    decomp.tim, isto é, o primeiro termo após `Versao`.
    """

    __slots__ = []

    BEGIN_PATTERN = r"^Versao "
    CAMPO = "versao_modelo"
    VALOR = re.compile(r"^Versao\s+(\S+)")


class BlocoCaso(_BlocoCabecalho):
    """
    Bloco com o nome do caso existente no cabeçalho do arquivo decomp.tim.
    """

    __slots__ = []

    BEGIN_PATTERN = r"^Caso:"
    CAMPO = "caso"
    VALOR = re.compile(r"^Caso:\s*(\S.*?)\s*$")


class BlocoData(_BlocoCabecalho):
    """
    Bloco com a data de início da execução existente no cabeçalho do
    arquivo decomp.tim.
    """

    __slots__ = []

    BEGIN_PATTERN = r"^Data:"
    CAMPO = "data_hora_inicio (linha Data)"
    VALOR = re.compile(r"^Data:\s*(\d{2})-(\d{2})-(\d{4})")

    @staticmethod
    def converte(m: re.Match[str]) -> date:
        return date(int(m[3]), int(m[2]), int(m[1]))


class BlocoHora(_BlocoCabecalho):
    """
    Bloco com a hora de início da execução existente no cabeçalho do
    arquivo decomp.tim, com os segundos fracionários.
    """

    __slots__ = []

    BEGIN_PATTERN = r"^Hora:"
    CAMPO = "data_hora_inicio (linha Hora)"
    VALOR = re.compile(r"^Hora:\s*(\d+)h\s*(\d+)min\s*(\d+)\.(\d{1,6})sec")

    @staticmethod
    def converte(m: re.Match[str]) -> time:
        return time(int(m[1]), int(m[2]), int(m[3]), int(m[4].ljust(6, "0")))


class BlocoNumeroProcessadores(_BlocoCabecalho):
    """
    Bloco com o número de processadores existente no cabeçalho do
    arquivo decomp.tim.
    """

    __slots__ = []

    BEGIN_PATTERN = r"^Numero de Processadores:"
    CAMPO = "numero_processadores"
    VALOR = re.compile(r"^Numero de Processadores:\s*(\d+)")

    @staticmethod
    def converte(m: re.Match[str]) -> int:
        return int(m[1])


class BlocoPlataforma(_BlocoCabecalho):
    """
    Bloco com a plataforma do executável existente no cabeçalho do
    arquivo decomp.tim.
    """

    __slots__ = []

    BEGIN_PATTERN = r"^\s+PLATAFORMA_+:"
    CAMPO = "plataforma"
    VALOR = re.compile(r"^\s+PLATAFORMA_+:\s*(\S.*?)\s*$")


class BlocoPacoteOtimizacao(_BlocoCabecalho):
    """
    Bloco com o pacote de otimização existente no cabeçalho do arquivo
    decomp.tim.
    """

    __slots__ = []

    BEGIN_PATTERN = r"^\s+PACOTE DE OTIMIZACAO:"
    CAMPO = "pacote_otimizacao"
    VALOR = re.compile(r"^\s+PACOTE DE OTIMIZACAO:\s*(\S.*?)\s*$")


class BlocoTemposEtapas(Block):
    """
    Bloco com as informações de tempo de execução existentes no arquivo
    decomp.tim.
    """

    __slots__ = ["__tempos_iteracoes"]

    BEGIN_PATTERN = "RELATORIO DE CONVERGENCIA DO PROCESSO ITERATIVO"
    END_PATTERN = ""

    def __init__(
        self, previous: Any = None, next: Any = None, data: Any = None
    ) -> None:
        super().__init__(previous, next, data)
        self.__tempos_iteracoes = pd.DataFrame(columns=_COLUNAS_ITERACOES)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoTemposEtapas):
            return False
        bloco: BlocoTemposEtapas = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return all(
                [
                    self.data.equals(bloco.data),
                    self.tempos_iteracoes.equals(bloco.tempos_iteracoes),
                ]
            )

    @property
    def tempos_iteracoes(self) -> pd.DataFrame:
        """
        Tabela com uma linha por iteração concluída do processo iterativo.

        :return: O DataFrame com os tempos de cada iteração
        :rtype: pd.DataFrame
        """
        return self.__tempos_iteracoes

    # Override
    def read(self, file: IO[Any], *args: Any, **kwargs: Any) -> None:  # type: ignore[override]
        grupo: Literal["nenhum", "iteracao", "final"] = "nenhum"
        tempo_leitura_dados = timedelta(0)
        tempo_envio_inicial = timedelta(0)
        tempo_iteracoes = timedelta(0)
        iteracao: dict[str, Any] = {}
        linhas_iteracoes: list[dict[str, Any]] = []
        tempo_simulacao_final = timedelta(0)
        tempo_impressao = timedelta(0)
        tempo_total = timedelta(0)
        while len(linha := file.readline()) > 0:
            if _LEITURA_DADOS.search(linha):
                tempo_leitura_dados = _tempo(linha, "Leitura de Dados")
            elif _ENVIO_INICIAL.search(linha):
                tempo_envio_inicial = _tempo(linha, "Envio de Variaveis")
            elif m := _GRUPO_ITERACAO.search(linha):
                grupo = "iteracao"
                iteracao = dict.fromkeys(_COLUNAS_ITERACOES, timedelta(0))
                iteracao["iteracao"] = int(m[1])
                iteracao["envio_variaveis"] = _tempo(
                    linha, "Envio de Variaveis da iteracao"
                )
            elif _GRUPO_FINAL.search(linha):
                grupo = "final"
            elif grupo == "iteracao" and _DESCIDA_1A_PARTE.search(linha):
                iteracao["descida_1a_parte"] = _tempo(linha, "Descida 1a Parte")
            elif grupo == "iteracao" and _DESCIDA_2A_PARTE.search(linha):
                iteracao["descida_2a_parte"] = _tempo(linha, "Descida 2a Parte")
            elif grupo == "iteracao" and _RETORNO.search(linha):
                iteracao["retorno"] = _tempo(linha, "Retorno")
            elif _TOTAL_GRUPO.search(linha):
                if grupo == "iteracao":
                    iteracao["total"] = _tempo(linha, "Total da iteracao")
                    tempo_iteracoes += iteracao["total"]
                    linhas_iteracoes.append(iteracao)
                elif grupo == "final":
                    tempo_simulacao_final = _tempo(linha, "Simulacao Final")
                grupo = "nenhum"
            elif _IMPRESSAO.search(linha):
                tempo_impressao = _tempo(linha, "Impressao")
            elif _TEMPO_TOTAL.search(linha):
                tempo_total = _tempo(linha, "Tempo Total")
        self.__tempos_iteracoes = pd.DataFrame(
            linhas_iteracoes, columns=_COLUNAS_ITERACOES
        ).astype({"iteracao": int})
        self.data = pd.DataFrame(
            data={
                "Etapa": [
                    "Leitura de Dados",
                    "Convergencia",
                    "Simulacao Final",
                    "Impressao",
                    "Tempo Total",
                ],
                "Tempo": [
                    tempo_leitura_dados,
                    tempo_envio_inicial + tempo_iteracoes,
                    tempo_simulacao_final,
                    tempo_impressao,
                    tempo_total,
                ],
            }
        )
