# Imports de módulos externos
import re
from datetime import timedelta
from typing import IO, Any, Final, Literal

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
