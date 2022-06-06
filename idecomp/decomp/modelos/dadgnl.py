from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField

from typing import List, Optional


class TG(Register):
    """
    Registro que contém o cadastro das térmicas a GNL
    """

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
        ]
    )

    def __atualiza_dados_lista(
        self,
        novos_dados: list,
        indice_inicial: int,
        espacamento: int,
    ):
        atuais = len(self.data)
        ultimo_indice = indice_inicial + espacamento * len(novos_dados)
        diferenca = (ultimo_indice - atuais) // espacamento
        if diferenca > 0:
            self.data += [None] * (ultimo_indice - atuais)
            diferenca -= 1
        novos_dados += [None] * abs(diferenca)
        self.data[indice_inicial::espacamento] = novos_dados

    @property
    def codigo(self) -> Optional[int]:
        """
        O código de cadastro da UTE.

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def subsistema(self) -> Optional[int]:
        """
        O subsistema de cadastro da UTE.

        :return: O subsistema como um `int`.
        """
        return self.data[1]

    @subsistema.setter
    def subsistema(self, c: int):
        self.data[1] = c

    @property
    def nome(self) -> Optional[str]:
        """
        O nome de cadastro da UTE.

        :return: O nome.
        :rtype: Optional[str]
        """
        return self.data[2]

    @nome.setter
    def nome(self, nome: str):
        self.data[2] = nome

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio do despacho da UTE.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[3]

    @estagio.setter
    def estagio(self, estagio: int):
        self.data[3] = estagio

    @property
    def inflexibilidades(self) -> List[float]:
        """
        As inflexibilidades da UTE por patamar.

        :return: As inflexibilidades.
        :rtype: Optional[list[float]]
        """
        return [v for v in self.data[4::3] if v is not None]

    @inflexibilidades.setter
    def inflexibilidades(self, inflex: List[float]):
        self.__atualiza_dados_lista(inflex, 4, 3)

    @property
    def disponibilidades(self) -> List[float]:
        """
        As disponibilidades da UTE por patamar.

        :return: As disponibilidades.
        :rtype: Optional[list[float]]
        """
        return [v for v in self.data[5::3] if v is not None]

    @disponibilidades.setter
    def disponibilidades(self, disp: List[float]):
        self.__atualiza_dados_lista(disp, 5, 3)

    @property
    def cvus(self) -> List[float]:
        """
        Os CVUs da UTE por patamar.

        :return: Os CVUs.
        :rtype: Optional[list[float]]
        """
        return [v for v in self.data[6::3] if v is not None]

    @cvus.setter
    def cvus(self, cvu: List[float]):
        self.__atualiza_dados_lista(cvu, 6, 3)


class GS(Register):
    """
    Registro que contém o número de semanas dos meses envolvidos
    no estudo.
    """

    IDENTIFIER = "GS  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            IntegerField(1, 9),
        ]
    )

    @property
    def mes(self) -> Optional[int]:
        """
        O índice do mês associado ao registro GS

        :return: O índice.
        :rtype: Optional[int]
        """
        return self.data[0]

    @mes.setter
    def mes(self, m: int):
        self.data[0] = m

    @property
    def semanas(self) -> Optional[int]:
        """
        O número de semanas do mês associado ao registro GS

        :return: O número de semanas.
        :rtype: Optional[int]
        """
        return self.data[1]

    @semanas.setter
    def semanas(self, s: int):
        self.data[1] = s


class NL(Register):
    """
    Registro que contém o número de lags para o despacho de cada térmica
    de despacho antecipado em cada subsistema.
    """

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
    def codigo(self) -> Optional[int]:
        """
        O código da UTE associada ao registro NL

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def subsistema(self) -> Optional[int]:
        """
        O índice do subsistema de despacho da UTE

        :return: O subsistema.
        :rtype: Optional[int]
        """
        return self.data[1]

    @subsistema.setter
    def subsistema(self, s: int):
        self.data[1] = s

    @property
    def lag(self) -> Optional[int]:
        """
        O lag de despacho da UTE

        :return: O lag
        :rtype: Optional[int]
        """
        return self.data[2]

    @lag.setter
    def lag(self, lag: int):
        self.data[2] = lag


class GL(Register):
    """
    Registro que contém os cadastros de restrições elétricas.
    """

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
    def codigo(self) -> Optional[int]:
        """
        O código da UTE despachada no registro GL

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def subsistema(self) -> Optional[int]:
        """
        O índice do subsistema de despacho da UTE

        :return: O subsistema.
        :rtype: Optional[int]
        """
        return self.data[1]

    @subsistema.setter
    def subsistema(self, e: int):
        self.data[1] = e

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio de despacho da UTE

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio.setter
    def estagio(self, e: int):
        self.data[2] = e

    @property
    def geracoes(self) -> List[float]:
        """
        Os valores de geração por patamar para o despacho
        da UTE

        :return: As geracoes como `list[float]`
        """
        return [v for v in self.data[3:8:2] if v is not None]

    @geracoes.setter
    def geracoes(self, gers: List[float]):
        novos = len(gers)
        atuais = len(self.geracoes)
        if novos != atuais:
            raise ValueError(
                "Número de gerações incompatível. De"
                + f"vem ser fornecidos {atuais}, mas foram {novos}"
            )
        self.data[3:9:2] = gers

    @property
    def duracoes(self) -> List[float]:
        """
        Os valores de geração por patamar para o despacho
        da UTE

        :return: As durações como `list[float]`
        """
        return [v for v in self.data[4:9:2] if v is not None]

    @duracoes.setter
    def duracoes(self, durs: List[float]):
        novos = len(durs)
        atuais = len(self.duracoes)
        if novos != atuais:
            raise ValueError(
                "Número de durações incompatível. De"
                + f"vem ser fornecidos {atuais}, mas foram {novos}"
            )
        self.data[4:9:2] = durs

    @property
    def data_inicio(self) -> Optional[str]:
        """
        A data de despacho da UTE

        :return: A data no formato DDMMYYYY.
        :rtype: Optional[str]
        """
        return self.data[9]

    @data_inicio.setter
    def data_inicio(self, d: str):
        self.data[9] = d
