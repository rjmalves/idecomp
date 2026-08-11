from cfinterface.components.floatfield import FloatField
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.register import Register
from cfinterface.storage import StorageType


def _quantidade_campos(linha: str | bytes) -> int:
    """
    Conta o número de campos de dados (após o identificador) de uma
    linha delimitada por ``;``, ignorando o token do identificador.

    :param linha: a linha lida do arquivo
    :type linha: str | bytes
    :return: a quantidade de campos de dados
    :rtype: int
    """
    if isinstance(linha, bytes):
        return len(linha.split(b";")) - 1
    return len(linha.split(";")) - 1


class PEECadastro(Register):
    """ """

    __slots__ = []

    IDENTIFIER = "PEE-CAD"
    IDENTIFIER_DIGITS = 8
    LINE = Line(
        [
            IntegerField(),
            LiteralField(),
        ],
        delimiter=";",
    )

    @property
    def codigo_pee(self) -> int | None:
        """
        O código do parque eólico equivalente.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_pee.setter
    def codigo_pee(self, c: int) -> None:
        self.data[0] = c

    @property
    def nome_pee(self) -> str | None:
        """
        O nome do parque eólico equivalente.

        :return: O nome
        :rtype: str | None
        """
        return self.data[1]

    @nome_pee.setter
    def nome_pee(self, n: str) -> None:
        self.data[1] = n


class PEESubmercado(Register):
    """ """

    __slots__ = []

    IDENTIFIER = "PEE-SUBM"
    IDENTIFIER_DIGITS = 9
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
        ],
        delimiter=";",
    )

    @property
    def codigo_pee(self) -> int | None:
        """
        O código do parque eólico equivalente.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_pee.setter
    def codigo_pee(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_submercado(self) -> int | None:
        """
        O código do submercado do parque eólico equivalente.

        :return: O código
        :rtype: int | None
        """
        return self.data[1]

    @codigo_submercado.setter
    def codigo_submercado(self, c: int) -> None:
        self.data[1] = c


class PEEConfiguracaoPeriodo(Register):
    """ """

    __slots__ = []

    IDENTIFIER = "PEE-CONFIG-PER"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            LiteralField(),
        ],
        delimiter=";",
    )

    @property
    def codigo_pee(self) -> int | None:
        """
        O código do parque eólico equivalente.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_pee.setter
    def codigo_pee(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio_inicial(self) -> int | None:
        """
        O estágio inicial de validade do estado de operação.

        :return: O estágio
        :rtype: int | None
        """
        return self.data[1]

    @estagio_inicial.setter
    def estagio_inicial(self, e: int) -> None:
        self.data[1] = e

    @property
    def estagio_final(self) -> int | None:
        """
        O estágio final de validade do estado de operação.

        :return: O estágio
        :rtype: int | None
        """
        return self.data[2]

    @estagio_final.setter
    def estagio_final(self, e: int) -> None:
        self.data[2] = e

    @property
    def estado_operacao(self) -> str | None:
        """
        O estado de operação do parque eólico equivalente.

        :return: O estado
        :rtype: str | None
        """
        return self.data[3]

    @estado_operacao.setter
    def estado_operacao(self, e: str) -> None:
        self.data[3] = e


class PEEPotenciaInstaladaPeriodo(Register):
    """ """

    __slots__ = []

    IDENTIFIER = "PEE-POT-INST-PER"
    IDENTIFIER_DIGITS = 17
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=3),
        ],
        delimiter=";",
    )

    @property
    def codigo_pee(self) -> int | None:
        """
        O código do parque eólico equivalente.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_pee.setter
    def codigo_pee(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio_inicial(self) -> int | None:
        """
        O estágio inicial de validade da potência instalada.

        :return: O estágio
        :rtype: int | None
        """
        return self.data[1]

    @estagio_inicial.setter
    def estagio_inicial(self, e: int) -> None:
        self.data[1] = e

    @property
    def estagio_final(self) -> int | None:
        """
        O estágio final de validade da potência instalada.

        :return: O estágio
        :rtype: int | None
        """
        return self.data[2]

    @estagio_final.setter
    def estagio_final(self, e: int) -> None:
        self.data[2] = e

    @property
    def potencia_instalada(self) -> float | None:
        """
        A potência instalada do parque eólico equivalente.

        :return: A potência em MW
        :rtype: float | None
        """
        return self.data[3]

    @potencia_instalada.setter
    def potencia_instalada(self, p: float) -> None:
        self.data[3] = p


class PEEGeracaoPeriodoPatamarCenario(Register):
    """ """

    __slots__ = []

    IDENTIFIER = "PEE-GER-PER-PAT-CEN"
    IDENTIFIER_DIGITS = 20
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=4),
        ],
        delimiter=";",
    )

    @classmethod
    def matches(
        cls, line: str | bytes, storage: str | StorageType = ""
    ) -> bool:
        """
        Casa apenas as linhas do card com 5 campos (período único,
        sem ``PerFin``). O layout com 6 campos é tratado por
        :class:`PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal`.
        """
        return super().matches(line, storage) and _quantidade_campos(line) == 5

    @property
    def codigo_pee(self) -> int | None:
        """
        O código do parque eólico equivalente.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_pee.setter
    def codigo_pee(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio(self) -> int | None:
        """
        O estágio (período) de validade da geração.

        :return: O estágio
        :rtype: int | None
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, e: int) -> None:
        self.data[1] = e

    @property
    def patamar(self) -> int | None:
        """
        O índice do patamar de carga.

        :return: O patamar
        :rtype: int | None
        """
        return self.data[2]

    @patamar.setter
    def patamar(self, p: int) -> None:
        self.data[2] = p

    @property
    def cenario(self) -> int | None:
        """
        O índice do cenário.

        :return: O cenário
        :rtype: int | None
        """
        return self.data[3]

    @cenario.setter
    def cenario(self, c: int) -> None:
        self.data[3] = c

    @property
    def geracao(self) -> float | None:
        """
        A geração do parque eólico equivalente.

        :return: A geração em MW
        :rtype: float | None
        """
        return self.data[4]

    @geracao.setter
    def geracao(self, g: float) -> None:
        self.data[4] = g


class PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal(Register):
    """
    Variante do registro ``PEE-GER-PER-PAT-CEN`` com 6 campos, em que o
    período é informado por um intervalo (``PerIni`` e ``PerFin``) em vez de
    um único período. Expõe as mesmas propriedades da variante de período
    único, acrescida de ``estagio_final``.
    """

    __slots__ = []

    IDENTIFIER = "PEE-GER-PER-PAT-CEN"
    IDENTIFIER_DIGITS = 20
    LINE = Line(
        [
            IntegerField(),
            IntegerField(),
            IntegerField(),
            IntegerField(),
            IntegerField(),
            FloatField(decimal_digits=4),
        ],
        delimiter=";",
    )

    @classmethod
    def matches(
        cls, line: str | bytes, storage: str | StorageType = ""
    ) -> bool:
        """
        Casa apenas as linhas do card com 6 campos (intervalo de períodos,
        com ``PerFin``). O layout com 5 campos é tratado por
        :class:`PEEGeracaoPeriodoPatamarCenario`.
        """
        return super().matches(line, storage) and _quantidade_campos(line) == 6

    @property
    def codigo_pee(self) -> int | None:
        """
        O código do parque eólico equivalente.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_pee.setter
    def codigo_pee(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio(self) -> int | None:
        """
        O estágio (período) inicial de validade da geração.

        :return: O estágio
        :rtype: int | None
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, e: int) -> None:
        self.data[1] = e

    @property
    def estagio_final(self) -> int | None:
        """
        O estágio (período) final de validade da geração.

        :return: O estágio
        :rtype: int | None
        """
        return self.data[2]

    @estagio_final.setter
    def estagio_final(self, e: int) -> None:
        self.data[2] = e

    @property
    def patamar(self) -> int | None:
        """
        O índice do patamar de carga.

        :return: O patamar
        :rtype: int | None
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, p: int) -> None:
        self.data[3] = p

    @property
    def cenario(self) -> int | None:
        """
        O índice do cenário.

        :return: O cenário
        :rtype: int | None
        """
        return self.data[4]

    @cenario.setter
    def cenario(self, c: int) -> None:
        self.data[4] = c

    @property
    def geracao(self) -> float | None:
        """
        A geração do parque eólico equivalente.

        :return: A geração em MW
        :rtype: float | None
        """
        return self.data[5]

    @geracao.setter
    def geracao(self, g: float) -> None:
        self.data[5] = g
