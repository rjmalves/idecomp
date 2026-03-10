from datetime import datetime

from cfinterface.components.datetimefield import DatetimeField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.register import Register

from idecomp.config import FORMATO_CAMPOS_DATA_LIBS


class RegistroRestricaoEletricaHorizontePeriodo(Register):
    """
    Registro que contém o cadastro do horizonte de validade
    da restrição RE, através de um horizonte de período,
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "RESTRICAO-ELETRICA-HORIZONTE-PERIODO"
    IDENTIFIER_DIGITS = 36
    LINE = Line(
        [
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio_inicio(self) -> int | None:
        """
        O estágio de início da validade da restrição.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicio.setter
    def estagio_inicio(self, c: int) -> None:
        self.data[1] = c

    @property
    def estagio_fim(self) -> int | None:
        """
        O estágio de fim da validade da restrição.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_fim.setter
    def estagio_fim(self, n: int) -> None:
        self.data[2] = n


class RegistroRestricaoEletricaHorizonteData(Register):
    """
    Registro que contém o cadastro do horizonte de validade
    da restrição RE, através de um intervalo de datas,
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "RESTRICAO-ELETRICA-HORIZONTE-DATA"
    IDENTIFIER_DIGITS = 33
    LINE = Line(
        [
            IntegerField(size=20),
            DatetimeField(format=FORMATO_CAMPOS_DATA_LIBS),
            DatetimeField(format=FORMATO_CAMPOS_DATA_LIBS),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def data_inicio(self) -> datetime | None:
        """
        A data de início da validade da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[1]

    @data_inicio.setter
    def data_inicio(self, c: datetime) -> None:
        self.data[1] = c

    @property
    def data_fim(self) -> datetime | None:
        """
        A data de fim da validade da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[2]

    @data_fim.setter
    def data_fim(self, n: datetime) -> None:
        self.data[2] = n


class RegistroRestricaoEletricaFormula(Register):
    """
    Registro que contém um cadastro de restrição elétrica (RE),
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "RESTRICAO-ELETRICA-FORMULA"
    IDENTIFIER_DIGITS = 26
    LINE = Line(
        [
            IntegerField(size=20),
            LiteralField(size=200),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def formula(self) -> str | None:
        """
        A fórmula da restrição.

        :return: A fórmula
        :rtype: Optional[str]
        """
        return self.data[1]

    @formula.setter
    def formula(self, n: str) -> None:
        self.data[1] = n


class RegistroRestricaoEletricaFormulaPeriodoPatamar(Register):
    """
    Registro que contém um cadastro de restrição elétrica (RE)
    que varia ao longo do tempo, informada por intervalo de estágios,
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "RESTRICAO-ELETRICA-FORMULA-PERIODO-PATAMAR"
    IDENTIFIER_DIGITS = 42
    LINE = Line(
        [
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            LiteralField(size=200),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio_inicio(self) -> int | None:
        """
        O estágio de início da restrição.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicio.setter
    def estagio_inicio(self, c: int) -> None:
        self.data[1] = c

    @property
    def estagio_fim(self) -> int | None:
        """
        O estágio de fim da restrição.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_fim.setter
    def estagio_fim(self, c: int) -> None:
        self.data[2] = c

    @property
    def patamar(self) -> int | None:
        """
        O índice do patamar de carga.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, c: int) -> None:
        self.data[3] = c

    @property
    def formula(self) -> str | None:
        """
        A fórmula da restrição.

        :return: A fórmula
        :rtype: Optional[str]
        """
        return self.data[4]

    @formula.setter
    def formula(self, n: str) -> None:
        self.data[4] = n


class RegistroRestricaoEletricaFormulaDataPatamar(Register):
    """
    Registro que contém um cadastro de restrição elétrica (RE)
    que variam ao longo do tempo, informada por intervalo de data,
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "RESTRICAO-ELETRICA-FORMULA-DATA-PATAMAR"
    IDENTIFIER_DIGITS = 39
    LINE = Line(
        [
            IntegerField(size=20),
            DatetimeField(format=FORMATO_CAMPOS_DATA_LIBS),
            DatetimeField(format=FORMATO_CAMPOS_DATA_LIBS),
            IntegerField(size=20),
            LiteralField(size=200),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def data_inicio(self) -> datetime | None:
        """
        A data de início da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[1]

    @data_inicio.setter
    def data_inicio(self, c: datetime) -> None:
        self.data[1] = c

    @property
    def data_fim(self) -> datetime | None:
        """
        A data de fim da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[2]

    @data_fim.setter
    def data_fim(self, c: datetime) -> None:
        self.data[2] = c

    @property
    def patamar(self) -> int | None:
        """
        O índice do patamar de carga.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, c: int) -> None:
        self.data[3] = c

    @property
    def formula(self) -> str | None:
        """
        A fórmula da restrição.

        :return: A fórmula
        :rtype: Optional[str]
        """
        return self.data[4]

    @formula.setter
    def formula(self, n: str) -> None:
        self.data[4] = n


class RegistroRestricaoEletricaLimitesFormulaPeriodoPatamar(Register):
    """
    Registro que contém os limites de cada restrição
    RE por período e patamar,
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "RESTRICAO-ELETRICA-LIMITES-FORMULA-PERIODO-PATAMAR"
    IDENTIFIER_DIGITS = 50
    LINE = Line(
        [
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            FloatField(size=20),
            FloatField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio_inicio(self) -> int | None:
        """
        O estágio de início da validade dos limites da restrição.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicio.setter
    def estagio_inicio(self, c: int) -> None:
        self.data[1] = c

    @property
    def estagio_fim(self) -> int | None:
        """
        O estágio de fim da validade dos limites da restrição.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_fim.setter
    def estagio_fim(self, v: int) -> None:
        self.data[2] = v

    @property
    def patamar(self) -> int | None:
        """
        O índice do patamar para os limites.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, v: int) -> None:
        self.data[3] = v

    @property
    def limite_inferior(self) -> str | None:
        """
        A equação que da o limite inferior da restrição.

        :return: A equação
        :rtype: Optional[str]
        """
        return self.data[4]

    @limite_inferior.setter
    def limite_inferior(self, v: str) -> None:
        self.data[4] = v

    @property
    def limite_superior(self) -> str | None:
        """
        A equação que da o limite superior da restrição.

        :return: A equação
        :rtype: Optional[str]
        """
        return self.data[5]

    @limite_superior.setter
    def limite_superior(self, v: str) -> None:
        self.data[5] = v


class RegistroRestricaoEletricaLimitesFormulaDataPatamar(Register):
    """
    Registro que contém os limites de cada restrição
    RE por intervalo de data e patamar,
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "RESTRICAO-ELETRICA-LIMITES-FORMULA-DATA-PATAMAR"
    IDENTIFIER_DIGITS = 47
    LINE = Line(
        [
            IntegerField(size=20),
            DatetimeField(format=FORMATO_CAMPOS_DATA_LIBS),
            DatetimeField(format=FORMATO_CAMPOS_DATA_LIBS),
            IntegerField(size=20),
            FloatField(size=20),
            FloatField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def data_inicio(self) -> datetime | None:
        """
        A data de início da validade dos limites da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[1]

    @data_inicio.setter
    def data_inicio(self, c: datetime) -> None:
        self.data[1] = c

    @property
    def data_fim(self) -> datetime | None:
        """
        A data de fim da validade dos limites da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[2]

    @data_fim.setter
    def data_fim(self, v: datetime) -> None:
        self.data[2] = v

    @property
    def patamar(self) -> int | None:
        """
        O índice do patamar para os limites.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, v: int) -> None:
        self.data[3] = v

    @property
    def limite_inferior(self) -> str | None:
        """
        A equação que da o limite inferior da restrição.

        :return: A equação
        :rtype: Optional[str]
        """
        return self.data[4]

    @limite_inferior.setter
    def limite_inferior(self, v: str) -> None:
        self.data[4] = v

    @property
    def limite_superior(self) -> str | None:
        """
        A equação que da o limite superior da restrição.

        :return: A equação
        :rtype: Optional[str]
        """
        return self.data[5]

    @limite_superior.setter
    def limite_superior(self, v: str) -> None:
        self.data[5] = v


class RegistroAliasEletrico(Register):
    """
    Registro que contém um cadastro alias elétrico,
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "ALIAS-ELETRICO"
    IDENTIFIER_DIGITS = 14
    LINE = Line(
        [
            IntegerField(size=20),
            LiteralField(size=200),
        ],
        delimiter=";",
    )

    @property
    def codigo_alias(self) -> int | None:
        """
        O código do alias.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_alias.setter
    def codigo_alias(self, c: int) -> None:
        self.data[0] = c

    @property
    def identificador_alias(self) -> str | None:
        """
        O identificador do alias elétrico personalizado.

        :return: O identificador
        :rtype: Optional[str]
        """
        return self.data[1]

    @identificador_alias.setter
    def identificador_alias(self, n: str) -> None:
        self.data[1] = n


class RegistroAliasEletricoValorPeriodoPatamar(Register):
    """
    Registro que contém os valores assumidos pelo alias
    para cada período e patamar,
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "ALIAS-ELETRICO-VALOR-PERIODO-PATAMAR"
    IDENTIFIER_DIGITS = 36
    LINE = Line(
        [
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            FloatField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_alias(self) -> int | None:
        """
        O código do alias.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_alias.setter
    def codigo_alias(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio_inicio(self) -> int | None:
        """
        O estágio de início da validade do dado.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicio.setter
    def estagio_inicio(self, c: int) -> None:
        self.data[1] = c

    @property
    def estagio_fim(self) -> int | None:
        """
        O estágio de fim da validade do dado.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_fim.setter
    def estagio_fim(self, v: int) -> None:
        self.data[2] = v

    @property
    def patamar(self) -> int | None:
        """
        O índice do patamar.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, v: int) -> None:
        self.data[3] = v

    @property
    def valor(self) -> float | None:
        """
        O valor do alias elétrico.

        :return: O valor
        :rtype: Optional[float]
        """
        return self.data[4]

    @valor.setter
    def valor(self, v: float) -> None:
        self.data[4] = v


class RegistroRestricaoEletricaRegraAtivacao(Register):
    """
    Registro que define uma regra para ativação e desativação das
    restrições,
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "RESTRICAO-ELETRICA-REGRA-ATIVACAO"
    IDENTIFIER_DIGITS = 33
    LINE = Line(
        [
            IntegerField(size=20),
            LiteralField(size=200),
        ],
        delimiter=";",
    )

    @property
    def codigo_regra_ativacao(self) -> int | None:
        """
        O código da regra de ativação.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_regra_ativacao.setter
    def codigo_regra_ativacao(self, c: int) -> None:
        self.data[0] = c

    @property
    def regra_ativacao(self) -> str | None:
        """
        A regra condicional para ativação.

        :return: A regra
        :rtype: Optional[str]
        """
        return self.data[1]

    @regra_ativacao.setter
    def regra_ativacao(self, n: str) -> None:
        self.data[1] = n


class RegistroRestricaoEletricaHabilita(Register):
    """
    Registro que contém a associação entre uma restrição
    e uma regra de ativação,
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "RESTRICAO-ELETRICA-HABILITA"
    IDENTIFIER_DIGITS = 27
    LINE = Line(
        [
            IntegerField(size=20),
            IntegerField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_regra_ativacao(self) -> int | None:
        """
        O código da regra de ativação.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[1]

    @codigo_regra_ativacao.setter
    def codigo_regra_ativacao(self, n: int) -> None:
        self.data[1] = n


class RegistroRestricaoEletricaTratamentoViolacao(Register):
    """
    Registro que contém a definição do tipo de violação e valor
    do custo de violação de uma restrição elétrica,
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "RESTRICAO-ELETRICA-TRATAMENTO-VIOLACAO"
    IDENTIFIER_DIGITS = 38
    LINE = Line(
        [
            IntegerField(size=20),
            LiteralField(size=200),
            FloatField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def tipo_violacao(self) -> str | None:
        """
        O tipo de violação.

        :return: O tipo de violação
        :rtype: Optional[str]
        """
        return self.data[1]

    @tipo_violacao.setter
    def tipo_violacao(self, n: str) -> None:
        self.data[1] = n

    @property
    def custo_violacao(self) -> float | None:
        """
        O custo de violação.

        :return: O custo
        :rtype: Optional[float]
        """
        return self.data[2]

    @custo_violacao.setter
    def custo_violacao(self, n: float) -> None:
        self.data[2] = n


class RegistroRestricaoEletricaTratamentoViolacaoPeriodo(Register):
    """
    Registro que contém a definição do tipo de violação e valor
    do custo de violação de uma restrição elétrica definida para
    um intervalo de estágios,
    definido através do nome completo do card.
    """

    __slots__ = []

    IDENTIFIER = "RESTRICAO-ELETRICA-TRATAMENTO-VIOLACAO-PERIODO"
    IDENTIFIER_DIGITS = 46
    LINE = Line(
        [
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            LiteralField(size=200),
            FloatField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio_inicio(self) -> int | None:
        """
        O estágio de início.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicio.setter
    def estagio_inicio(self, c: int) -> None:
        self.data[1] = c

    @property
    def estagio_fim(self) -> int | None:
        """
        O estágio de fim.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_fim.setter
    def estagio_fim(self, c: int) -> None:
        self.data[2] = c

    @property
    def tipo_violacao(self) -> str | None:
        """
        O tipo de violação.

        :return: O tipo de violação
        :rtype: Optional[str]
        """
        return self.data[3]

    @tipo_violacao.setter
    def tipo_violacao(self, n: str) -> None:
        self.data[3] = n

    @property
    def custo_violacao(self) -> float | None:
        """
        O custo de violação.

        :return: O custo
        :rtype: Optional[float]
        """
        return self.data[4]

    @custo_violacao.setter
    def custo_violacao(self, n: float) -> None:
        self.data[4] = n


class RegistroReHorizPer(Register):
    """
    Registro que contém o cadastro do horizonte de validade
    da restrição RE, através de um horizonte de período,
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "RE-HORIZ-PER"
    IDENTIFIER_DIGITS = 12
    LINE = Line(
        [
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio_inicio(self) -> int | None:
        """
        O estágio de início da validade da restrição.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicio.setter
    def estagio_inicio(self, c: int) -> None:
        self.data[1] = c

    @property
    def estagio_fim(self) -> int | None:
        """
        O estágio de fim da validade da restrição.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_fim.setter
    def estagio_fim(self, n: int) -> None:
        self.data[2] = n


class RegistroReHorizData(Register):
    """
    Registro que contém o cadastro do horizonte de validade
    da restrição RE, através de um intervalo de datas,
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "RE-HORIZ-DATA"
    IDENTIFIER_DIGITS = 13
    LINE = Line(
        [
            IntegerField(size=20),
            DatetimeField(format=FORMATO_CAMPOS_DATA_LIBS),
            DatetimeField(format=FORMATO_CAMPOS_DATA_LIBS),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def data_inicio(self) -> datetime | None:
        """
        A data de início da validade da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[1]

    @data_inicio.setter
    def data_inicio(self, c: datetime) -> None:
        self.data[1] = c

    @property
    def data_fim(self) -> datetime | None:
        """
        A data de fim da validade da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[2]

    @data_fim.setter
    def data_fim(self, n: datetime) -> None:
        self.data[2] = n


class RegistroRe(Register):
    """
    Registro que contém um cadastro de restrição elétrica (RE),
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "RE"
    IDENTIFIER_DIGITS = 2
    LINE = Line(
        [
            IntegerField(size=20),
            LiteralField(size=200),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def formula(self) -> str | None:
        """
        A fórmula da restrição.

        :return: A fórmula
        :rtype: Optional[str]
        """
        return self.data[1]

    @formula.setter
    def formula(self, n: str) -> None:
        self.data[1] = n


class RegistroRePerPat(Register):
    """
    Registro que contém um cadastro de restrição elétrica (RE)
    que varia ao longo do tempo, informada por intervalo de estágios,
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "RE-PER-PAT"
    IDENTIFIER_DIGITS = 10
    LINE = Line(
        [
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            LiteralField(size=200),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio_inicio(self) -> int | None:
        """
        O estágio de início da restrição.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicio.setter
    def estagio_inicio(self, c: int) -> None:
        self.data[1] = c

    @property
    def estagio_fim(self) -> int | None:
        """
        O estágio de fim da restrição.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_fim.setter
    def estagio_fim(self, c: int) -> None:
        self.data[2] = c

    @property
    def patamar(self) -> int | None:
        """
        O índice do patamar de carga.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, c: int) -> None:
        self.data[3] = c

    @property
    def formula(self) -> str | None:
        """
        A fórmula da restrição.

        :return: A fórmula
        :rtype: Optional[str]
        """
        return self.data[4]

    @formula.setter
    def formula(self, n: str) -> None:
        self.data[4] = n


class RegistroReDataPat(Register):
    """
    Registro que contém um cadastro de restrição elétrica (RE)
    que variam ao longo do tempo, informada por intervalo de data,
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "RE-DATA-PAT"
    IDENTIFIER_DIGITS = 11
    LINE = Line(
        [
            IntegerField(size=20),
            DatetimeField(format=FORMATO_CAMPOS_DATA_LIBS),
            DatetimeField(format=FORMATO_CAMPOS_DATA_LIBS),
            IntegerField(size=20),
            LiteralField(size=200),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def data_inicio(self) -> datetime | None:
        """
        A data de início da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[1]

    @data_inicio.setter
    def data_inicio(self, c: datetime) -> None:
        self.data[1] = c

    @property
    def data_fim(self) -> datetime | None:
        """
        A data de fim da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[2]

    @data_fim.setter
    def data_fim(self, c: datetime) -> None:
        self.data[2] = c

    @property
    def patamar(self) -> int | None:
        """
        O índice do patamar de carga.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, c: int) -> None:
        self.data[3] = c

    @property
    def formula(self) -> str | None:
        """
        A fórmula da restrição.

        :return: A fórmula
        :rtype: Optional[str]
        """
        return self.data[4]

    @formula.setter
    def formula(self, n: str) -> None:
        self.data[4] = n


class RegistroReLimFormPerPat(Register):
    """
    Registro que contém os limites de cada restrição
    RE por período e patamar,
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "RE-LIM-FORM-PER-PAT"
    IDENTIFIER_DIGITS = 19
    LINE = Line(
        [
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            FloatField(size=20),
            FloatField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio_inicio(self) -> int | None:
        """
        O estágio de início da validade dos limites da restrição.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicio.setter
    def estagio_inicio(self, c: int) -> None:
        self.data[1] = c

    @property
    def estagio_fim(self) -> int | None:
        """
        O estágio de fim da validade dos limites da restrição.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_fim.setter
    def estagio_fim(self, v: int) -> None:
        self.data[2] = v

    @property
    def patamar(self) -> int | None:
        """
        O índice do patamar para os limites.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, v: int) -> None:
        self.data[3] = v

    @property
    def limite_inferior(self) -> str | None:
        """
        A equação que da o limite inferior da restrição.

        :return: A equação
        :rtype: Optional[str]
        """
        return self.data[4]

    @limite_inferior.setter
    def limite_inferior(self, v: str) -> None:
        self.data[4] = v

    @property
    def limite_superior(self) -> str | None:
        """
        A equação que da o limite superior da restrição.

        :return: A equação
        :rtype: Optional[str]
        """
        return self.data[5]

    @limite_superior.setter
    def limite_superior(self, v: str) -> None:
        self.data[5] = v


class RegistroReLimFormDataPat(Register):
    """
    Registro que contém os limites de cada restrição
    RE por intervalo de data e patamar,
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "RE-LIM-FORM-DATA-PAT"
    IDENTIFIER_DIGITS = 20
    LINE = Line(
        [
            IntegerField(size=20),
            DatetimeField(format=FORMATO_CAMPOS_DATA_LIBS),
            DatetimeField(format=FORMATO_CAMPOS_DATA_LIBS),
            IntegerField(size=20),
            FloatField(size=20),
            FloatField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def data_inicio(self) -> datetime | None:
        """
        A data de início da validade dos limites da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[1]

    @data_inicio.setter
    def data_inicio(self, c: datetime) -> None:
        self.data[1] = c

    @property
    def data_fim(self) -> datetime | None:
        """
        A data de fim da validade dos limites da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[2]

    @data_fim.setter
    def data_fim(self, v: datetime) -> None:
        self.data[2] = v

    @property
    def patamar(self) -> int | None:
        """
        O índice do patamar para os limites.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, v: int) -> None:
        self.data[3] = v

    @property
    def limite_inferior(self) -> str | None:
        """
        A equação que da o limite inferior da restrição.

        :return: A equação
        :rtype: Optional[str]
        """
        return self.data[4]

    @limite_inferior.setter
    def limite_inferior(self, v: str) -> None:
        self.data[4] = v

    @property
    def limite_superior(self) -> str | None:
        """
        A equação que da o limite superior da restrição.

        :return: A equação
        :rtype: Optional[str]
        """
        return self.data[5]

    @limite_superior.setter
    def limite_superior(self, v: str) -> None:
        self.data[5] = v


class RegistroAliasElet(Register):
    """
    Registro que contém um cadastro alias elétrico,
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "ALIAS-ELET"
    IDENTIFIER_DIGITS = 10
    LINE = Line(
        [
            IntegerField(size=20),
            LiteralField(size=200),
        ],
        delimiter=";",
    )

    @property
    def codigo_alias(self) -> int | None:
        """
        O código do alias.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_alias.setter
    def codigo_alias(self, c: int) -> None:
        self.data[0] = c

    @property
    def identificador_alias(self) -> str | None:
        """
        O identificador do alias elétrico personalizado.

        :return: O identificador
        :rtype: Optional[str]
        """
        return self.data[1]

    @identificador_alias.setter
    def identificador_alias(self, n: str) -> None:
        self.data[1] = n


class RegistroAliasEletValPerPat(Register):
    """
    Registro que contém os valores assumidos pelo alias
    para cada período e patamar,
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "ALIAS-ELET-VAL-PER-PAT"
    IDENTIFIER_DIGITS = 22
    LINE = Line(
        [
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            FloatField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_alias(self) -> int | None:
        """
        O código do alias.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_alias.setter
    def codigo_alias(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio_inicio(self) -> int | None:
        """
        O estágio de início da validade do dado.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicio.setter
    def estagio_inicio(self, c: int) -> None:
        self.data[1] = c

    @property
    def estagio_fim(self) -> int | None:
        """
        O estágio de fim da validade do dado.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_fim.setter
    def estagio_fim(self, v: int) -> None:
        self.data[2] = v

    @property
    def patamar(self) -> int | None:
        """
        O índice do patamar.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, v: int) -> None:
        self.data[3] = v

    @property
    def valor(self) -> float | None:
        """
        O valor do alias elétrico.

        :return: O valor
        :rtype: Optional[float]
        """
        return self.data[4]

    @valor.setter
    def valor(self, v: float) -> None:
        self.data[4] = v


class RegistroReRegraAtiva(Register):
    """
    Registro que define uma regra para ativação e desativação das
    restrições,
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "RE-REGRA-ATIVA"
    IDENTIFIER_DIGITS = 14
    LINE = Line(
        [
            IntegerField(size=20),
            LiteralField(size=200),
        ],
        delimiter=";",
    )

    @property
    def codigo_regra_ativacao(self) -> int | None:
        """
        O código da regra de ativação.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_regra_ativacao.setter
    def codigo_regra_ativacao(self, c: int) -> None:
        self.data[0] = c

    @property
    def regra_ativacao(self) -> str | None:
        """
        A regra condicional para ativação.

        :return: A regra
        :rtype: Optional[str]
        """
        return self.data[1]

    @regra_ativacao.setter
    def regra_ativacao(self, n: str) -> None:
        self.data[1] = n


class RegistroReHabilita(Register):
    """
    Registro que contém a associação entre uma restrição
    e uma regra de ativação,
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "RE-HABILITA"
    IDENTIFIER_DIGITS = 11
    LINE = Line(
        [
            IntegerField(size=20),
            IntegerField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_regra_ativacao(self) -> int | None:
        """
        O código da regra de ativação.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[1]

    @codigo_regra_ativacao.setter
    def codigo_regra_ativacao(self, n: int) -> None:
        self.data[1] = n


class RegistroReTratViol(Register):
    """
    Registro que contém a definição do tipo de violação e valor
    do custo de violação de uma restrição elétrica,
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "RE-TRAT-VIOL"
    IDENTIFIER_DIGITS = 12
    LINE = Line(
        [
            IntegerField(size=20),
            LiteralField(size=200),
            FloatField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def tipo_violacao(self) -> str | None:
        """
        O tipo de violação.

        :return: O tipo de violação
        :rtype: Optional[str]
        """
        return self.data[1]

    @tipo_violacao.setter
    def tipo_violacao(self, n: str) -> None:
        self.data[1] = n

    @property
    def custo_violacao(self) -> float | None:
        """
        O custo de violação.

        :return: O custo
        :rtype: Optional[float]
        """
        return self.data[2]

    @custo_violacao.setter
    def custo_violacao(self, n: float) -> None:
        self.data[2] = n


class RegistroReTratViolPer(Register):
    """
    Registro que contém a definição do tipo de violação e valor
    do custo de violação de uma restrição elétrica definida para
    um intervalo de estágios,
    definido através do nome alternativo (apelido) do card.
    """

    __slots__ = []

    IDENTIFIER = "RE-TRAT-VIOL-PER"
    IDENTIFIER_DIGITS = 16
    LINE = Line(
        [
            IntegerField(size=20),
            IntegerField(size=20),
            IntegerField(size=20),
            LiteralField(size=200),
            FloatField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> int | None:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int) -> None:
        self.data[0] = c

    @property
    def estagio_inicio(self) -> int | None:
        """
        O estágio de início.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicio.setter
    def estagio_inicio(self, c: int) -> None:
        self.data[1] = c

    @property
    def estagio_fim(self) -> int | None:
        """
        O estágio de fim.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_fim.setter
    def estagio_fim(self, c: int) -> None:
        self.data[2] = c

    @property
    def tipo_violacao(self) -> str | None:
        """
        O tipo de violação.

        :return: O tipo de violação
        :rtype: Optional[str]
        """
        return self.data[3]

    @tipo_violacao.setter
    def tipo_violacao(self, n: str) -> None:
        self.data[3] = n

    @property
    def custo_violacao(self) -> float | None:
        """
        O custo de violação.

        :return: O custo
        :rtype: Optional[float]
        """
        return self.data[4]

    @custo_violacao.setter
    def custo_violacao(self, n: float) -> None:
        self.data[4] = n
