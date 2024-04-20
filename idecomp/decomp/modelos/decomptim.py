# Imports de módulos externos
from cfinterface.components.block import Block
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
import pandas as pd  # type: ignore
from typing import IO
from datetime import timedelta


class BlocoTemposEtapas(Block):
    """
    Bloco com as informações de tempo de execução existentes no arquivo
    decomp.tim.
    """

    __slots__ = ["__line"]

    BEGIN_PATTERN = "RELATORIO DE CONVERGENCIA DO PROCESSO ITERATIVO"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__line = Line(
            [
                IntegerField(3, 35),
                IntegerField(2, 40),
                IntegerField(2, 46),
            ]
        )

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
            return self.data.equals(bloco.data)

    def read_line_time(self, linha: str) -> timedelta:
        data = self.__line.read(linha)
        return timedelta(hours=data[0], minutes=data[1], seconds=data[2])

    # Override
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:

            df = pd.DataFrame(
                data={
                    "Etapa": [
                        str_leitura_dados,
                        "Convergencia",
                        str_impressao,
                        str_tempo_total,
                    ],
                    "Tempo": [
                        tempo_leitura_dados,
                        tempo_convergencia,
                        tempo_impressao,
                        tempo_total,
                    ],
                }
            )
            return df

        # Salta 9 linhas linha
        str_leitura_dados = "Leitura de Dados"
        str_envio_variaveis = "Envio de Variaveis:"
        str_impressao = "Impressao"
        str_total = "Total"
        str_tempo_total = "Tempo Total"
        iniciou_convergencia = False
        iniciou_impressao = False
        tempo_leitura_dados = timedelta(seconds=0.0)
        tempo_convergencia = timedelta(seconds=0.0)
        tempo_impressao = timedelta(seconds=0.0)
        tempo_total = timedelta(seconds=0.0)
        while True:
            linha = file.readline()
            if len(linha) == 0:
                self.data = converte_tabela_em_df()
                break
            if str_tempo_total in linha:
                tempo_total = self.read_line_time(linha)
            elif iniciou_impressao and str_total in linha:
                tempo_impressao = self.read_line_time(linha)
            elif iniciou_convergencia and str_total in linha:
                tempo_convergencia += self.read_line_time(linha)
            elif str_impressao in linha:
                iniciou_impressao = True
            elif str_leitura_dados in linha:
                tempo_leitura_dados = self.read_line_time(linha)
            elif str_envio_variaveis in linha and not iniciou_convergencia:
                iniciou_convergencia = True
                tempo_convergencia += self.read_line_time(linha)
