from typing import IO, Any

from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.section import Section


class NomeCaso(Section):
    """
    Bloco com o nome do caso do arquivo de
    entrada do DECOMP `caso.dat`.
    """

    __slots__ = ["__linha"]

    def __init__(
        self, previous: Any = None, next: Any = None, data: Any = None
    ) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line([LiteralField(80, 0)])

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, NomeCaso):
            return False
        bloco: NomeCaso = o
        if not all(
            [
                isinstance(self.data, str),
                isinstance(o.data, str),
            ]
        ):
            return False
        else:
            return self.data == bloco.data

    # Override
    def read(self, file: IO[Any], *args: Any, **kwargs: Any) -> None:  # type: ignore[override]
        self.data = self.__linha.read(file.readline())[0]

    # Override
    def write(self, file: IO[Any], *args: Any, **kwargs: Any) -> None:  # type: ignore[override]
        file.write(self.__linha.write([self.data]))
