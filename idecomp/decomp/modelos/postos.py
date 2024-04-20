from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.integerfield import IntegerField
from typing import List


class RegistroPostos(Register):
    """
    Registro com os dados associados às informações dos postos.
    """

    __slots__ = []

    POSTOS = 320

    LINE = Line(
        [
            LiteralField(size=12, starting_position=0),
            IntegerField(size=4, starting_position=12),
            IntegerField(size=4, starting_position=16),
        ],
        storage="BINARY",
    )

    @classmethod
    def set_postos(cls, postos: int):
        cls.POSTOS = postos
        cls.LINE = Line(
            [
                LiteralField(size=12, starting_position=0),
                IntegerField(size=4, starting_position=12),
                IntegerField(size=4, starting_position=16),
            ],
            storage="BINARY",
        )

    @property
    def postos(self) -> List[int]:
        return self.data

    @postos.setter
    def postos(self, v: List[int]):
        self.data = v
