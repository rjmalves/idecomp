from cfinterface.components.integerfield import IntegerField


class FortranIntegerField(IntegerField):
    """
    Campo inteiro lido como o DECOMP lê o formato ``Iw`` do Fortran:
    os brancos do campo são ignorados, e ``1 2`` é lido como 12.

    O valor é escrito alinhado à direita no campo. Um valor que não
    cabe no campo não é escrito.
    """

    __slots__: list[str] = []

    def _textual_read(self, line: str) -> int:
        return int(
            "".join(
                line[self._starting_position : self._ending_position].split()
            )
        )

    def _textual_write(self) -> str:
        escrito = super()._textual_write()
        if len(escrito.strip()) > self.size:
            raise ValueError(
                f"O valor {self.value} não cabe em {self.size} colunas"
            )
        return escrito
