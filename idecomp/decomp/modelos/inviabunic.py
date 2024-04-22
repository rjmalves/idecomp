from cfinterface.components.block import Block
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.literalfield import LiteralField
from typing import List, IO
import pandas as pd  # type: ignore


class BlocoInviabilidadesIteracoes(Block):
    """
    Bloco com as informações das inviabilidades visitadas
    pelo DECOMP durante o processo iterativo.
    """

    __slots__ = ["__linha"]

    BEGIN_PATTERN = "RELATORIO DE VIOLACOES DAS RESTRICOES"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                IntegerField(9, 4),
                LiteralField(14, 14),
                IntegerField(8, 29),
                IntegerField(8, 38),
                LiteralField(51, 47),
                FloatField(16, 99, 8),
                LiteralField(5, 116),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoInviabilidadesIteracoes):
            return False
        bloco: BlocoInviabilidadesIteracoes = o
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
            df = pd.DataFrame()
            df["iteracao"] = iteracoes
            df["etapa"] = fwds_bwds
            df["estagio"] = estagios
            df["cenario"] = cenarios
            df["restricao"] = restricoes
            df["violacao"] = violacoes
            df["unidade"] = unidades
            return df

        # Salta linhas de cabeçalho
        for _ in range(4):
            file.readline()
        iteracoes: List[int] = []
        fwds_bwds: List[int] = []
        estagios: List[int] = []
        cenarios: List[int] = []
        restricoes: List[str] = []
        violacoes: List[float] = []
        unidades: List[str] = []
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if len(linha.strip()) < 5:
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__linha.read(linha)
            iteracoes.append(dados[0])
            fwds_bwds.append(dados[1])
            estagios.append(dados[2])
            cenarios.append(dados[3])
            restricoes.append(dados[4])
            violacoes.append(dados[5])
            unidades.append(dados[6])


class BlocoInviabilidadesSimFinal(Block):
    """
    Bloco com as informações das inviabilidades visitadas
    pelo DECOMP durante a simulação final.
    """

    __slots__ = ["__linha"]

    BEGIN_PATTERN = "SIMULACAO FINAL:"
    END_PATTERN = ""

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [
                IntegerField(8, 4),
                IntegerField(8, 13),
                LiteralField(76, 22),
                FloatField(16, 99, 8),
                LiteralField(5, 116),
            ]
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoInviabilidadesSimFinal):
            return False
        bloco: BlocoInviabilidadesSimFinal = o
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
            df = pd.DataFrame()
            df["estagio"] = estagios
            df["cenario"] = cenarios
            df["restricao"] = restricoes
            df["violacao"] = violacoes
            df["unidade"] = unidades
            return df

        # Salta linhas de cabeçalho
        for _ in range(4):
            file.readline()

        estagios: List[int] = []
        cenarios: List[int] = []
        restricoes: List[str] = []
        violacoes: List[float] = []
        unidades: List[str] = []
        while True:
            # Confere se a leitura não acabou
            linha = file.readline()
            if len(linha.strip()) < 5:
                self.data = converte_tabela_em_df()
                break
            # Senão, lê mais uma linha
            dados = self.__linha.read(linha)
            estagios.append(dados[0])
            cenarios.append(dados[1])
            restricoes.append(dados[2])
            violacoes.append(dados[3])
            unidades.append(dados[4])
