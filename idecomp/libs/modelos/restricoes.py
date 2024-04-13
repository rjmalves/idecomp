from typing import Optional
from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from cfinterface.components.datetimefield import DatetimeField
from datetime import datetime


class RegistroREHorizPer(Register):
    """
    Registro que contém o cadastro do horizonte de validade
    da restrição RE, através de um horizonte de período.
    """

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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def periodo_inicio(self) -> Optional[int]:
        """
        O período de início da validade da restrição.

        :return: O período
        :rtype: Optional[int]
        """
        return self.data[1]

    @periodo_inicio.setter
    def periodo_inicio(self, c: int):
        self.data[1] = c

    @property
    def periodo_fim(self) -> Optional[int]:
        """
        O período de fim da validade da restrição.

        :return: O período
        :rtype: Optional[int]
        """
        return self.data[2]

    @periodo_fim.setter
    def periodo_fim(self, n: int):
        self.data[2] = n


class RegistroREHorizData(Register):
    """
    Registro que contém o cadastro do horizonte de validade
    da restrição RE, através de um intervalo de datas.
    """

    IDENTIFIER = "RE-HORIZ-DATA"
    IDENTIFIER_DIGITS = 13
    LINE = Line(
        [
            IntegerField(size=20),
            DatetimeField(format="%Y/%m/%d"),
            DatetimeField(format="%Y/%m/%d"),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def data_inicio(self) -> Optional[datetime]:
        """
        A data de início da validade da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[1]

    @data_inicio.setter
    def data_inicio(self, c: datetime):
        self.data[1] = c

    @property
    def data_fim(self) -> Optional[datetime]:
        """
        A data de fim da validade da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[2]

    @data_fim.setter
    def data_fim(self, n: datetime):
        self.data[2] = n


class RegistroRE(Register):
    """
    Registro que contém um cadastro de restrição elétrica (RE).
    """

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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def formula(self) -> Optional[str]:
        """
        A fórmula da restrição.

        :return: A fórmula
        :rtype: Optional[str]
        """
        return self.data[1]

    @formula.setter
    def formula(self, n: str):
        self.data[1] = n


class RegistroREPerPat(Register):
    """
    Registro que contém um cadastro de restrição elétrica (RE)
    que varia ao longo do tempo, informada por intervalo de período.
    """

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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def periodo_inicio(self) -> Optional[int]:
        """
        O período de início da restrição.

        :return: O período
        :rtype: Optional[int]
        """
        return self.data[1]

    @periodo_inicio.setter
    def periodo_inicio(self, c: int):
        self.data[1] = c

    @property
    def periodo_fim(self) -> Optional[int]:
        """
        O período de fim da restrição.

        :return: O período
        :rtype: Optional[int]
        """
        return self.data[2]

    @periodo_fim.setter
    def periodo_fim(self, c: int):
        self.data[2] = c

    @property
    def patamar(self) -> Optional[int]:
        """
        O índice do patamar de carga.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, c: int):
        self.data[3] = c

    @property
    def formula(self) -> Optional[str]:
        """
        A fórmula da restrição.

        :return: A fórmula
        :rtype: Optional[str]
        """
        return self.data[4]

    @formula.setter
    def formula(self, n: str):
        self.data[4] = n


class RegistroREDataPat(Register):
    """
    Registro que contém um cadastro de restrição elétrica (RE)
    que variam ao longo do tempo, informada por intervalo de data.
    """

    IDENTIFIER = "RE-DATA-PAT"
    IDENTIFIER_DIGITS = 11
    LINE = Line(
        [
            IntegerField(size=20),
            DatetimeField(format="%Y/%m/%d"),
            DatetimeField(format="%Y/%m/%d"),
            IntegerField(size=20),
            LiteralField(size=200),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def data_inicio(self) -> Optional[datetime]:
        """
        A data de início da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[1]

    @data_inicio.setter
    def data_inicio(self, c: datetime):
        self.data[1] = c

    @property
    def data_fim(self) -> Optional[datetime]:
        """
        A data de fim da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[2]

    @data_fim.setter
    def data_fim(self, c: datetime):
        self.data[2] = c

    @property
    def patamar(self) -> Optional[int]:
        """
        O índice do patamar de carga.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, c: int):
        self.data[3] = c

    @property
    def formula(self) -> Optional[str]:
        """
        A fórmula da restrição.

        :return: A fórmula
        :rtype: Optional[str]
        """
        return self.data[4]

    @formula.setter
    def formula(self, n: str):
        self.data[4] = n


class RegistroRELimFormPerPat(Register):
    """
    Registro que contém os limites de cada restrição
    RE por período e patamar.
    """

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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def periodo_inicio(self) -> Optional[int]:
        """
        O período de início da validade dos limites da restrição.

        :return: O período
        :rtype: Optional[int]
        """
        return self.data[1]

    @periodo_inicio.setter
    def periodo_inicio(self, c: int):
        self.data[1] = c

    @property
    def periodo_fim(self) -> Optional[int]:
        """
        O período de fim da validade dos limites da restrição.

        :return: O período
        :rtype: Optional[int]
        """
        return self.data[2]

    @periodo_fim.setter
    def periodo_fim(self, v: int):
        self.data[2] = v

    @property
    def patamar(self) -> Optional[int]:
        """
        O índice do patamar para os limites.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, v: int):
        self.data[3] = v

    @property
    def limite_inferior(self) -> Optional[str]:
        """
        A equação que da o limite inferior da restrição.

        :return: A equação
        :rtype: Optional[str]
        """
        return self.data[4]

    @limite_inferior.setter
    def limite_inferior(self, v: str):
        self.data[4] = v

    @property
    def limite_superior(self) -> Optional[str]:
        """
        A equação que da o limite superior da restrição.

        :return: A equação
        :rtype: Optional[str]
        """
        return self.data[5]

    @limite_superior.setter
    def limite_superior(self, v: str):
        self.data[5] = v


class RegistroRELimFormDataPat(Register):
    """
    Registro que contém os limites de cada restrição
    RE por intervalo de data e patamar.
    """

    IDENTIFIER = "RE-LIM-FORM-DATA-PAT"
    IDENTIFIER_DIGITS = 20
    LINE = Line(
        [
            IntegerField(size=20),
            DatetimeField(format="%Y/%m/%d"),
            DatetimeField(format="%Y/%m/%d"),
            IntegerField(size=20),
            FloatField(size=20),
            FloatField(size=20),
        ],
        delimiter=";",
    )

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def data_inicio(self) -> Optional[datetime]:
        """
        A data de início da validade dos limites da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[1]

    @data_inicio.setter
    def data_inicio(self, c: datetime):
        self.data[1] = c

    @property
    def data_fim(self) -> Optional[datetime]:
        """
        A data de fim da validade dos limites da restrição.

        :return: A data
        :rtype: Optional[datetime]
        """
        return self.data[2]

    @data_fim.setter
    def data_fim(self, v: datetime):
        self.data[2] = v

    @property
    def patamar(self) -> Optional[int]:
        """
        O índice do patamar para os limites.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, v: int):
        self.data[3] = v

    @property
    def limite_inferior(self) -> Optional[str]:
        """
        A equação que da o limite inferior da restrição.

        :return: A equação
        :rtype: Optional[str]
        """
        return self.data[4]

    @limite_inferior.setter
    def limite_inferior(self, v: str):
        self.data[4] = v

    @property
    def limite_superior(self) -> Optional[str]:
        """
        A equação que da o limite superior da restrição.

        :return: A equação
        :rtype: Optional[str]
        """
        return self.data[5]

    @limite_superior.setter
    def limite_superior(self, v: str):
        self.data[5] = v


class RegistroAliasElet(Register):
    """
    Registro que contém um cadastro alias elétrico.
    """

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
    def codigo_alias(self) -> Optional[int]:
        """
        O código do alias.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_alias.setter
    def codigo_alias(self, c: int):
        self.data[0] = c

    @property
    def identificador_alias(self) -> Optional[str]:
        """
        O identificador do alias elétrico personalizado.

        :return: O identificador
        :rtype: Optional[str]
        """
        return self.data[1]

    @identificador_alias.setter
    def identificador_alias(self, n: str):
        self.data[1] = n


class RegistroAliasEletValPerPat(Register):
    """
    Registro que contém os valores assumidos pelo alias
    para cada período e patamar.
    """

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
    def codigo_alias(self) -> Optional[int]:
        """
        O código do alias.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_alias.setter
    def codigo_alias(self, c: int):
        self.data[0] = c

    @property
    def periodo_inicio(self) -> Optional[int]:
        """
        O período de início da validade do dado.

        :return: O período
        :rtype: Optional[int]
        """
        return self.data[1]

    @periodo_inicio.setter
    def periodo_inicio(self, c: int):
        self.data[1] = c

    @property
    def periodo_fim(self) -> Optional[int]:
        """
        O período de fim da validade do dado.

        :return: O período
        :rtype: Optional[int]
        """
        return self.data[2]

    @periodo_fim.setter
    def periodo_fim(self, v: int):
        self.data[2] = v

    @property
    def patamar(self) -> Optional[int]:
        """
        O índice do patamar.

        :return: O patamar
        :rtype: Optional[int]
        """
        return self.data[3]

    @patamar.setter
    def patamar(self, v: int):
        self.data[3] = v

    @property
    def valor(self) -> Optional[float]:
        """
        O valor do alias elétrico.

        :return: O valor
        :rtype: Optional[float]
        """
        return self.data[4]

    @valor.setter
    def valor(self, v: float):
        self.data[4] = v


class RegistroRERegraAtiva(Register):
    """
    Registro que define uma regra para ativação e desativação das
    restrições.
    """

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
    def codigo_regra_ativacao(self) -> Optional[int]:
        """
        O código da regra de ativação.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_regra_ativacao.setter
    def codigo_regra_ativacao(self, c: int):
        self.data[0] = c

    @property
    def regra_ativacao(self) -> Optional[str]:
        """
        A regra condicional para ativação.

        :return: A regra
        :rtype: Optional[str]
        """
        return self.data[1]

    @regra_ativacao.setter
    def regra_ativacao(self, n: str):
        self.data[1] = n


class RegistroREHabilita(Register):
    """
    Registro que contém a associação entre uma restrição
    e uma regra de ativação.
    """

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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def codigo_regra_ativacao(self) -> Optional[int]:
        """
        O código da regra de ativação.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[1]

    @codigo_regra_ativacao.setter
    def codigo_regra_ativacao(self, n: int):
        self.data[1] = n


class RegistroRETratViol(Register):
    """
    Registro que contém a definição do tipo de violação e valor
    do custo de violação de uma restrição elétrica.
    """

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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def tipo_violacao(self) -> Optional[str]:
        """
        O tipo de violação.

        :return: O tipo de violação
        :rtype: Optional[str]
        """
        return self.data[1]

    @tipo_violacao.setter
    def tipo_violacao(self, n: str):
        self.data[1] = n

    @property
    def custo_violacao(self) -> Optional[float]:
        """
        O custo de violação.

        :return: O custo
        :rtype: Optional[float]
        """
        return self.data[2]

    @custo_violacao.setter
    def custo_violacao(self, n: float):
        self.data[2] = n


class RegistroRETratViolPer(Register):
    """
    Registro que contém a definição do tipo de violação e valor
    do custo de violação de uma restrição elétrica definida para
    um intervalo de período.
    """

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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def periodo_inicio(self) -> Optional[int]:
        """
        O período de início.

        :return: O período
        :rtype: Optional[int]
        """
        return self.data[1]

    @periodo_inicio.setter
    def periodo_inicio(self, c: int):
        self.data[1] = c

    @property
    def periodo_fim(self) -> Optional[int]:
        """
        O período de fim.

        :return: O período
        :rtype: Optional[int]
        """
        return self.data[2]

    @periodo_fim.setter
    def periodo_fim(self, c: int):
        self.data[2] = c

    @property
    def tipo_violacao(self) -> Optional[str]:
        """
        O tipo de violação.

        :return: O tipo de violação
        :rtype: Optional[str]
        """
        return self.data[3]

    @tipo_violacao.setter
    def tipo_violacao(self, n: str):
        self.data[3] = n

    @property
    def custo_violacao(self) -> Optional[float]:
        """
        O custo de violação.

        :return: O custo
        :rtype: Optional[float]
        """
        return self.data[4]

    @custo_violacao.setter
    def custo_violacao(self, n: float):
        self.data[4] = n
