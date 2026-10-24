import re

from cfinterface.components.floatfield import FloatField

# Sinal, mantissa e expoente opcional de um campo real de entrada do
# Fortran. O expoente é introduzido por uma letra ou apenas pelo sinal.
_NUMERO = re.compile(
    r"(?P<sinal>[+-]?)(?P<inteira>\d*)(?:\.(?P<fracao>\d*))?"
    r"(?:[EeDd](?P<expoente>[+-]?\d+)|(?P<expoente_sinal>[+-]\d+))?"
)

_MANTISSA = re.compile(r"[+-]?\d+")


class FortranFloatField(FloatField):
    """
    Campo real lido como o DECOMP lê os formatos ``Fw.d`` e ``Ew.d``
    do Fortran. Um valor escrito sem ponto decimal tem seus últimos
    ``implied_decimals`` dígitos tomados como a parte fracionária: em
    ``F10.2``, ``299`` é lido como 2.99. Um valor escrito com ponto
    decimal é lido como escrito, e os brancos do campo são ignorados.

    ``implied_decimals`` é o ``d`` do formato do campo no manual do
    usuário, independente de ``decimal_digits``, que é a precisão de
    escrita. A escrita sempre contém o ponto decimal, para que o valor
    não seja reescalado na leitura.
    """

    __slots__ = ["__implied_decimals", "__sep"]

    def __init__(
        self,
        size: int = 8,
        starting_position: int = 0,
        decimal_digits: int = 4,
        format: str = "F",
        sep: str = ".",
        value: float | None = None,
        compact: bool = False,
        implied_decimals: int = 0,
    ) -> None:
        super().__init__(
            size,
            starting_position,
            decimal_digits,
            format,
            sep,
            value,
            compact,
        )
        self.__implied_decimals = implied_decimals
        self.__sep = sep

    def _textual_read(self, line: str) -> float:
        texto = "".join(
            line[self._starting_position : self._ending_position].split()
        ).replace(self.__sep, ".")
        numero = _NUMERO.fullmatch(texto)
        if numero is None or not (numero["inteira"] or numero["fracao"]):
            raise ValueError(f"Campo real inválido: '{texto}'")
        expoente = int(numero["expoente"] or numero["expoente_sinal"] or 0)
        if numero["fracao"] is None:
            return float(
                f"{numero['sinal']}{numero['inteira']}"
                + f"e{expoente - self.__implied_decimals}"
            )
        return float(
            f"{numero['sinal']}{numero['inteira']}.{numero['fracao']}"
            + f"e{expoente}"
        )

    def _textual_write(self) -> str:
        valor = super()._textual_write()
        if self.__implied_decimals == 0 or "." in valor or not valor.strip():
            return valor
        # A precisão foi reduzida a zero para o valor caber no campo.
        texto = valor.strip()
        mantissa = _MANTISSA.match(texto)
        if mantissa is not None:
            texto = texto[: mantissa.end()] + "." + texto[mantissa.end() :]
        if mantissa is None or len(texto) > self.size:
            raise ValueError(
                f"O valor {self.value} não cabe em {self.size} colunas"
                + " com ponto decimal"
            )
        return texto.rjust(self.size)
