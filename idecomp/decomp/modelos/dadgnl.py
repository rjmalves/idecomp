from typing import Any

from cfinterface.components.floatfield import FloatField
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.register import Register


class TG(Register):
    """
    Registro que contém o cadastro das térmicas a GNL
    """

    __slots__: list[str] = []

    IDENTIFIER = "TG  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            LiteralField(10, 14),
            IntegerField(2, 24),
            FloatField(5, 29, 1),
            FloatField(5, 34, 1),
            FloatField(10, 39, 2),
            FloatField(5, 49, 1),
            FloatField(5, 54, 1),
            FloatField(10, 59, 2),
            FloatField(5, 69, 1),
            FloatField(5, 74, 1),
            FloatField(10, 79, 2),
            FloatField(5, 89, 1),
            FloatField(5, 94, 1),
            FloatField(10, 99, 2),
            FloatField(5, 109, 1),
            FloatField(5, 114, 1),
            FloatField(10, 119, 2),
        ]
    )

    def __atualiza_dados_lista(
        self,
        novos_dados: list[Any],
        indice_inicial: int,
        espacamento: int,
    ) -> None:
        atuais = len(self.data)
        ultimo_indice = indice_inicial + espacamento * len(novos_dados)
        diferenca = (ultimo_indice - atuais) // espacamento
        if diferenca > 0:
            self.data += [None] * (ultimo_indice - atuais)
            diferenca -= 1
        novos_dados += [None] * abs(diferenca)
        self.data[indice_inicial::espacamento] = novos_dados

    @property
    def codigo_usina(self) -> int | None:
        """
        O código de cadastro da UTE.

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_submercado(self) -> int | None:
        """
        O código do submercado de cadastro da UTE.

        :return: O código do submercado como um `int`.
        """
        return self.data[1]

    @codigo_submercado.setter
    def codigo_submercado(self, c: int) -> None:
        self.data[1] = c

    @property
    def nome(self) -> str | None:
        """
        O nome de cadastro da UTE.

        :return: O nome.
        :rtype: Optional[str]
        """
        return self.data[2]

    @nome.setter
    def nome(self, nome: str) -> None:
        self.data[2] = nome

    @property
    def estagio(self) -> int | None:
        """
        O estágio do despacho da UTE.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[3]

    @estagio.setter
    def estagio(self, estagio: int) -> None:
        self.data[3] = estagio

    @property
    def inflexibilidade(self) -> list[float]:
        """
        A inflexibilidade da UTE por patamar.

        :return: A inflexibilidade.
        :rtype: Optional[list[float]]
        """
        return [v for v in self.data[4::3] if v is not None]

    @inflexibilidade.setter
    def inflexibilidade(self, inflex: list[float]) -> None:
        self.__atualiza_dados_lista(inflex, 4, 3)

    @property
    def disponibilidade(self) -> list[float]:
        """
        A disponibilidade da UTE por patamar.

        :return: A disponibilidade.
        :rtype: Optional[list[float]]
        """
        return [v for v in self.data[5::3] if v is not None]

    @disponibilidade.setter
    def disponibilidade(self, disp: list[float]) -> None:
        self.__atualiza_dados_lista(disp, 5, 3)

    @property
    def cvu(self) -> list[float]:
        """
        Os CVUs da UTE por patamar.

        :return: Os CVUs.
        :rtype: Optional[list[float]]
        """
        return [v for v in self.data[6::3] if v is not None]

    @cvu.setter
    def cvu(self, cvu: list[float]) -> None:
        self.__atualiza_dados_lista(cvu, 6, 3)


class GS(Register):
    """
    Registro que contém o número de semanas dos meses envolvidos
    no estudo.
    """

    __slots__: list[str] = []

    IDENTIFIER = "GS  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            IntegerField(1, 9),
        ]
    )

    @property
    def mes(self) -> int | None:
        """
        O índice do mês associado ao registro GS

        :return: O índice.
        :rtype: Optional[int]
        """
        return self.data[0]

    @mes.setter
    def mes(self, m: int) -> None:
        self.data[0] = m

    @property
    def semanas(self) -> int | None:
        """
        O número de semanas do mês associado ao registro GS

        :return: O número de semanas.
        :rtype: Optional[int]
        """
        return self.data[1]

    @semanas.setter
    def semanas(self, s: int) -> None:
        self.data[1] = s


class NL(Register):
    """
    Registro que contém o número de lags para o despacho de cada térmica
    de despacho antecipado em cada subsistema.
    """

    __slots__: list[str] = []

    IDENTIFIER = "NL  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            IntegerField(1, 14),
        ]
    )

    @property
    def codigo_usina(self) -> int | None:
        """
        O código da UTE associada ao registro NL

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_submercado(self) -> int | None:
        """
        O código do submercado de despacho da UTE

        :return: O código do submercado.
        :rtype: Optional[int]
        """
        return self.data[1]

    @codigo_submercado.setter
    def codigo_submercado(self, s: int) -> None:
        self.data[1] = s

    @property
    def lag(self) -> int | None:
        """
        O lag de despacho da UTE

        :return: O lag
        :rtype: Optional[int]
        """
        return self.data[2]

    @lag.setter
    def lag(self, lag: int) -> None:
        self.data[2] = lag


class GL(Register):
    """
    Registro que contém os cadastros de restrições elétricas.
    """

    __slots__: list[str] = []

    IDENTIFIER = "GL  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            IntegerField(2, 14),
            FloatField(10, 19, 2),
            FloatField(5, 29, 0),
            FloatField(10, 34, 2),
            FloatField(5, 44, 0),
            FloatField(10, 49, 2),
            FloatField(5, 59, 0),
            LiteralField(8, 65),
        ]
    )

    @property
    def codigo_usina(self) -> int | None:
        """
        O código da UTE despachada no registro GL

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int) -> None:
        self.data[0] = c

    @property
    def codigo_submercado(self) -> int | None:
        """
        O código do submercado de despacho da UTE

        :return: O código do submercado.
        :rtype: Optional[int]
        """
        return self.data[1]

    @codigo_submercado.setter
    def codigo_submercado(self, e: int) -> None:
        self.data[1] = e

    @property
    def estagio(self) -> int | None:
        """
        O estágio de despacho da UTE

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio.setter
    def estagio(self, e: int) -> None:
        self.data[2] = e

    @property
    def geracao(self) -> list[float]:
        """
        Os valores de geração por patamar para o despacho
        da UTE

        :return: As gerações como `list[float]`
        """
        return [v for v in self.data[3:8:2] if v is not None]

    @geracao.setter
    def geracao(self, gers: list[float]) -> None:
        novos = len(gers)
        atuais = len(self.geracao)
        if novos != atuais:
            raise ValueError(
                "Número de gerações incompatível. De"
                + f"vem ser fornecidos {atuais}, mas foram {novos}"
            )
        self.data[3:9:2] = gers

    @property
    def duracao(self) -> list[float]:
        """
        As durações de cada patamar para o despacho
        da UTE

        :return: As durações como `list[float]`
        """
        return [v for v in self.data[4:9:2] if v is not None]

    @duracao.setter
    def duracao(self, durs: list[float]) -> None:
        novos = len(durs)
        atuais = len(self.duracao)
        if novos != atuais:
            raise ValueError(
                "Número de durações incompatível. De"
                + f"vem ser fornecidos {atuais}, mas foram {novos}"
            )
        self.data[4:9:2] = durs

    @property
    def data_inicio(self) -> str | None:
        """
        A data de despacho da UTE

        :return: A data no formato DDMMYYYY.
        :rtype: Optional[str]
        """
        return self.data[9]

    @data_inicio.setter
    def data_inicio(self, d: str) -> None:
        self.data[9] = d
