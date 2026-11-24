from cfinterface.components.integerfield import IntegerField


class FortranIntegerField(IntegerField):
    """
    Campo inteiro lido como o DECOMP lê o formato ``Iw`` do Fortran:
    os brancos do campo são ignorados, e ``1 2`` é lido como 12.

    O valor é escrito alinhado à direita no campo. Quando
    ``preferred_size`` é informado e o valor cabe nas primeiras
    ``preferred_size`` colunas do campo, ele é escrito alinhado à
    direita nelas, como nos decks em que um campo ``I4`` do manual
    é preenchido nas três primeiras colunas. Um valor que não cabe no
    campo não é escrito.
    """

    __slots__ = ["__preferred_size"]

    def __init__(
        self,
        size: int = 8,
        starting_position: int = 0,
        value: int | None = None,
        preferred_size: int | None = None,
    ) -> None:
        super().__init__(size, starting_position, value)
        self.__preferred_size = preferred_size

    def _textual_read(self, line: str) -> int:
        return int(
            "".join(
                line[self._starting_position : self._ending_position].split()
            )
        )

    def _textual_write(self) -> str:
        escrito = super()._textual_write()
        texto = escrito.strip()
        if len(texto) > self.size:
            raise ValueError(
                f"O valor {self.value} não cabe em {self.size} colunas"
            )
        if (
            texto
            and self.__preferred_size is not None
            and len(texto) <= self.__preferred_size
        ):
            return texto.rjust(self.__preferred_size).ljust(self.size)
        return escrito
