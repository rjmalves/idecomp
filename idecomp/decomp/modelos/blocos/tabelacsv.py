from typing import IO, Any

import pandas as pd  # type: ignore[import-untyped]
from cfinterface.components.block import Block
from cfinterface.components.line import Line


class TabelaCSV(Block):
    """
    Bloco para ler uma tabela com separadores CSV fornecidos
    a partir de um modelo de linha, para arquivos de saída do DECOMP.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;------;"
    LINE_MODEL = Line([])
    COLUMN_NAMES: list[str] = []
    END_PATTERN = ""

    def _monta_df(self, dados: dict[str, Any]) -> pd.DataFrame:
        return pd.DataFrame(data=dados, columns=self.__class__.COLUMN_NAMES)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, TabelaCSV):
            return False
        else:
            if not all(
                [type(self.data) is pd.DataFrame, type(o.data) is pd.DataFrame]
            ):
                return False
            else:
                return self.data.equals(o.data)

    def read(self, file: IO[Any], *args: Any, **kwargs: Any) -> None:  # type: ignore[override]
        if len(self.__class__.LINE_MODEL.fields) != len(
            self.__class__.COLUMN_NAMES
        ):
            n_linha = len(self.__class__.LINE_MODEL.fields)
            n_cols = len(self.__class__.COLUMN_NAMES)
            raise RuntimeError(
                f"Número de colunas ({n_cols}) diferente do"
                + f" número de campos da linha ({n_linha})"
            )
        # Espera o fim do cabeçalho
        linha = file.readline()
        while True:
            linha = file.readline()
            if self.__class__.BEGIN_PATTERN in linha:
                break
            elif len(linha) < 3:
                return
        # Lê a tabela
        dados: dict[str, list[Any]] = {
            c: [] for c in self.__class__.COLUMN_NAMES
        }
        while True:
            linha = file.readline()
            if len(linha) < 3:
                self.data = self._monta_df(dados)
                return
            dados_linha = self.__class__.LINE_MODEL.read(linha)
            for i, c in enumerate(self.__class__.COLUMN_NAMES):
                dados[c].append(dados_linha[i])


class TabelaCSVLibs(Block):
    """
    Bloco para ler uma tabela com separadores CSV fornecidos
    a partir de um modelo de linha, para arquivos de saída do DECOMP.
    """

    __slots__ = []

    BEGIN_PATTERN = "&IIIIIII;IIIIIII;"
    LINE_MODEL = Line([])
    COLUMN_NAMES: list[str] = []
    END_PATTERN = ""

    def _monta_df(self, dados: dict[str, Any]) -> pd.DataFrame:
        return pd.DataFrame(data=dados, columns=self.__class__.COLUMN_NAMES)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, TabelaCSVLibs):
            return False
        else:
            if not all(
                [type(self.data) is pd.DataFrame, type(o.data) is pd.DataFrame]
            ):
                return False
            else:
                return self.data.equals(o.data)

    def read(self, file: IO[Any], *args: Any, **kwargs: Any) -> None:  # type: ignore[override]
        if len(self.__class__.LINE_MODEL.fields) != len(
            self.__class__.COLUMN_NAMES
        ):
            n_linha = len(self.__class__.LINE_MODEL.fields)
            n_cols = len(self.__class__.COLUMN_NAMES)
            raise RuntimeError(
                f"Número de colunas ({n_cols}) diferente do"
                + f" número de campos da linha ({n_linha})"
            )

        # Lê a tabela
        linha = file.readline()
        dados: dict[str, list[Any]] = {
            c: [] for c in self.__class__.COLUMN_NAMES
        }
        while True:
            linha = file.readline()
            if len(linha) < 3:
                self.data = self._monta_df(dados)
                return
            dados_linha = self.__class__.LINE_MODEL.read(linha)
            for i, c in enumerate(self.__class__.COLUMN_NAMES):
                dados[c].append(dados_linha[i])
