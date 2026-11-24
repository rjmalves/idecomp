import re
from decimal import Decimal

from cfinterface.components.floatfield import FloatField

# Sinal, mantissa e expoente opcional de um campo real de entrada do
# Fortran. O expoente é introduzido por uma letra ou apenas pelo sinal.
_NUMERO = re.compile(
    r"(?P<sinal>[+-]?)(?P<inteira>\d*)(?:\.(?P<fracao>\d*))?"
    r"(?:[EeDd](?P<expoente>[+-]?\d+)|(?P<expoente_sinal>[+-]\d+))?"
)

# Maior número de dígitos significativos de um float.
_DIGITOS_SIGNIFICATIVOS = 17


class FortranFloatField(FloatField):
    """
    Campo real lido como o DECOMP lê os formatos ``Fw.d`` e ``Ew.d``
    do Fortran. Um valor escrito sem ponto decimal tem seus últimos
    ``implied_decimals`` dígitos tomados como a parte fracionária: em
    ``F10.2``, ``299`` é lido como 2.99. Um valor escrito com ponto
    decimal é lido como escrito, e os brancos do campo são ignorados.

    ``implied_decimals`` é o ``d`` do formato do campo no manual do
    usuário, independente de ``decimal_digits``, que é a precisão
    preferida para a escrita. O valor é escrito com essa precisão
    quando ela o reproduz e cabe no campo. Senão, é escrito com o
    menor texto que o reproduz e cabe no campo, em ponto fixo ou, se
    não houver um, em notação exponencial. Quando nenhum texto que
    caiba no campo reproduz o valor, é escrito o que mais se aproxima
    dele. Um texto sem ponto decimal só é escrito quando é lido como o
    valor, de modo que o valor não é reescalado na leitura.
    """

    __slots__ = ["__format", "__implied_decimals", "__sep"]

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
        self.__format = format
        self.__implied_decimals = implied_decimals
        self.__sep = sep

    def __le_texto(self, texto: str) -> float:
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

    def _textual_read(self, line: str) -> float:
        return self.__le_texto(
            "".join(
                line[self._starting_position : self._ending_position].split()
            ).replace(self.__sep, ".")
        )

    def __releitura(self, texto: str) -> float | None:
        if len(texto) > self.size:
            return None
        try:
            return self.__le_texto(texto.replace(self.__sep, "."))
        except ValueError:
            return None

    def __exponencial(self, valor: float, precisao: int) -> str:
        letra = "D" if self.__format.lower() == "d" else "E"
        mantissa, expoente = f"{valor:.{precisao}E}".split("E")
        if "." not in mantissa:
            mantissa += "."
        return f"{mantissa}{letra}{int(expoente):+d}".replace(".", self.__sep)

    def __ponto_fixo(self, valor: float, precisao: int) -> list[str]:
        texto = f"{valor:.{precisao}f}"
        if "." not in texto:
            texto += "."
        textos = [texto]
        sem_zero = re.sub(r"^(-?)0\.", r"\1.", texto)
        if sem_zero != texto:
            textos.append(sem_zero)
        return [t.replace(".", self.__sep) for t in textos]

    def __candidatos_exatos(self, valor: float) -> list[str]:
        textos: list[str] = []
        if self.__format.lower() == "f":
            texto = format(Decimal(repr(valor)), "f")
            if "." in texto:
                texto = texto.rstrip("0")
            else:
                texto += "."
            textos.append(texto.replace(".", self.__sep))
            sem_zero = re.sub(r"^(-?)0\.", r"\1.", texto)
            if sem_zero != texto:
                textos.append(sem_zero.replace(".", self.__sep))
        textos += [
            self.__exponencial(valor, p) for p in range(_DIGITOS_SIGNIFICATIVOS)
        ]
        return textos

    def __candidatos_aproximados(self, valor: float) -> list[str]:
        textos: list[str] = []
        if self.__format.lower() == "f":
            for p in range(self.size, -1, -1):
                textos += self.__ponto_fixo(valor, p)
        textos += [
            self.__exponencial(valor, p)
            for p in range(_DIGITOS_SIGNIFICATIVOS - 1, -1, -1)
        ]
        return textos

    def _textual_write(self) -> str:
        preferido = super()._textual_write()
        if not preferido.strip():
            return preferido
        assert self.value is not None
        valor = float(self.value)
        preferido = preferido.strip()
        for texto in [preferido] + self.__candidatos_exatos(valor):
            if self.__releitura(texto) == valor:
                return texto.rjust(self.size)
        aproximados = [
            (abs(lido - valor), texto)
            for texto in [preferido] + self.__candidatos_aproximados(valor)
            if (lido := self.__releitura(texto)) is not None
        ]
        if not aproximados:
            raise ValueError(
                f"O valor {self.value} não cabe em {self.size} colunas"
            )
        return min(aproximados, key=lambda a: a[0])[1].rjust(self.size)
