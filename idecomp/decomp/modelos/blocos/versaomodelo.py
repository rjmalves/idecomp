from cfinterface.components.block import Block

from typing import Any, IO


class VersaoModelo(Block):
    """
    Bloco para ler a versão utilizada do modelo a partir da linha de
    título do arquivo.
    """

    __slots__ = []

    BEGIN_PATTERN = r"CEPEL: DECOMP"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, VersaoModelo):
            return False
        else:
            if not all([type(self.data) is str, type(o.data) is str]):
                return False
            return self.data == o.data

    def read(self, file: IO[Any], *args: Any, **kwargs: Any) -> None:  # type: ignore[override]  # cfinterface base returns bool
        linha = file.readline()
        self.data = linha.split("Versao")[1].strip().split("-")[0].strip()


class VersaoModeloLibs(Block):
    """
    Bloco para ler a versão utilizada do modelo a partir da linha de
    título do arquivo.
    """

    __slots__ = []

    BEGIN_PATTERN = r"Nome do Modelo: DECOMP Versão:"
    END_PATTERN = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, VersaoModeloLibs):
            return False
        else:
            if not all([type(self.data) is str, type(o.data) is str]):
                return False
            return self.data == o.data

    def read(self, file: IO[Any], *args: Any, **kwargs: Any) -> None:  # type: ignore[override]  # cfinterface base returns bool
        linha = file.readline()
        self.data = linha.split("Versão:")[1].strip()
