from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField

from typing import Optional, List, IO
from numpy import abs  # type: ignore


class TE(Register):
    """
    Registro que contém a usina modificada.
    """

    IDENTIFIER = "TE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line([LiteralField(75, 4)])

    @property
    def titulo(self) -> Optional[str]:
        """
        O único conteúdo do registro (título do estudo).

        :return: O título do estudo
        :rtype: Optional[str]
        """
        return self.data[0]

    @titulo.setter
    def titulo(self, t: str):
        self.data[0] = t


class SB(Register):
    """
    Registro que contém o cadastro dos subsistemas.
    """

    IDENTIFIER = "SB  "
    IDENTIFIER_DIGITS = 4
    LINE = Line([IntegerField(2, 4), LiteralField(2, 9)])

    @property
    def codigo(self) -> Optional[int]:
        """
        O código de cadastro do subsistema.

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, cod: int):
        self.data[0] = cod

    @property
    def nome(self) -> Optional[str]:
        """
        O nome de cadastro do subsistema.

        :return: O nome.
        :rtype: Optional[str]
        """
        return self.data[1]

    @nome.setter
    def nome(self, n: str):
        self.data[1] = n


class UH(Register):
    """
    Registro que contém o cadastro das UHEs, com os seus volumes
    iniciais no estudo.
    """

    IDENTIFIER = "UH  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            FloatField(6, 18, 2),
            IntegerField(1, 39),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código de cadastro da UHE.

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, cod: int):
        self.data[0] = cod

    @property
    def ree(self) -> Optional[int]:
        """
        O REE de cadastro da UHE.

        :return: O REE.
        :rtype: Optional[int]
        """
        return self.data[1]

    @ree.setter
    def ree(self, n: str):
        self.data[1] = n

    @property
    def volume_inicial(self) -> Optional[float]:
        """
        O volume inicial da UHE para o estudo.

        :return: O volume.
        :rtype: Optional[float]
        """
        return self.data[2]

    @volume_inicial.setter
    def volume_inicial(self, v: float):
        self.data[2] = v

    @property
    def evaporacao(self) -> Optional[bool]:
        """
        A consideração ou não de evaporação para a UHE.

        :return: A consideração.
        :rtype: Optional[bool]
        """
        return self.data[3]

    @evaporacao.setter
    def evaporacao(self, e: bool):
        self.data[3] = e


class CT(Register):
    """
    Registro que contém o cadastro das usinas termelétricas com
    os seus custos e capacidades.
    """

    IDENTIFIER = "CT  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            LiteralField(10, 14),
            IntegerField(2, 24),
            FloatField(5, 29, 2),
            FloatField(5, 34, 2),
            FloatField(10, 39, 2),
            FloatField(5, 49, 2),
            FloatField(5, 54, 2),
            FloatField(10, 59, 2),
            FloatField(5, 69, 2),
            FloatField(5, 74, 2),
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
    def codigo(self, codigo: int):
        self.data[0] = codigo

    @property
    def subsistema(self) -> Optional[int]:
        """
        O subsistema de cadastro da UTE.

        :return: O subsistema.
        :rtype: Optional[int]
        """
        return self.data[1]

    @subsistema.setter
    def subsistema(self, subsistema: int):
        self.data[1] = subsistema

    @property
    def nome(self) -> Optional[str]:
        """
        O nome de cadastro da UTE.

        :return: O nome como uma `str`.
        :rtype: Optional[str]
        """
        return self.data[2]

    @nome.setter
    def nome(self, nome: str):
        self.data[2] = nome

    @property
    def estagio(self) -> Optional[str]:
        """
        O estágio associado às propriedades cadastradas.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[3]

    @estagio.setter
    def estagio(self, estagio: int):
        self.data[3] = estagio

    @property
    def inflexibilidades(self) -> Optional[List[float]]:
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
    def disponibilidades(self) -> Optional[List[float]]:
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
    def cvus(self) -> Optional[List[float]]:
        """
        Os CVUs da UTE por patamar.

        :return: Os CVUs.
        :rtype: Optional[list[float]]
        """
        return [v for v in self.data[6::3] if v is not None]

    @cvus.setter
    def cvus(self, cvu: List[float]):
        self.__atualiza_dados_lista(cvu, 6, 3)


class UE(Register):
    """
    Registro que contém o cadastro das estações de bombeamento
    (usinas elevatórias).
    """

    IDENTIFIER = "UE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            LiteralField(12, 14),
            IntegerField(3, 29),
            IntegerField(3, 34),
            FloatField(10, 39, 1),
            FloatField(10, 49, 1),
            FloatField(10, 59, 2),
        ]
    )


class DP(Register):
    """
    Registro que contém o cadastro das durações dos patamares.
    """

    IDENTIFIER = "DP  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            IntegerField(2, 9),
            IntegerField(1, 14),
            FloatField(10, 19, 1),
            FloatField(10, 29, 1),
            FloatField(10, 39, 1),
            FloatField(10, 49, 1),
            FloatField(10, 59, 1),
            FloatField(10, 69, 1),
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
    def estagio(self) -> Optional[int]:
        """
        O estágio associado às durações especificadas.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[0]

    @estagio.setter
    def estagio(self, e: int):
        self.data[0] = e

    @property
    def subsistema(self) -> Optional[int]:
        """
        O subsistema associado às durações especificadas.

        :return: O subsistema.
        :rtype: Optional[int]
        """
        return self.data[1]

    @subsistema.setter
    def subsistema(self, sub: int):
        self.data[1] = sub

    @property
    def num_patamares(self) -> Optional[int]:
        """
        O número de patamares.

        :return: O número de patamares.
        :rtype: Optional[int]
        """
        return self.data[2]

    @num_patamares.setter
    def num_patamares(self, n: int):
        self.data[2] = n

    @property
    def cargas(self) -> Optional[List[float]]:
        """
        As cargas em Mwmed pata cada patamar de carga

        :return: As cargas.
        :rtype: Optional[list[float]]
        """
        return [v for v in self.data[3::2] if v is not None]

    @cargas.setter
    def cargas(self, c: List[float]):
        self.__atualiza_dados_lista(c, 3, 2)

    @property
    def duracoes(self) -> Optional[List[float]]:
        """
        As durações de cada patamar de carga em horas

        :return: As durações em horas.
        :rtype: Optional[list[float]]
        """
        return [v for v in self.data[4::2] if v is not None]

    @duracoes.setter
    def duracoes(self, d: List[float]):
        self.__atualiza_dados_lista(d, 4, 2)


class CD(Register):
    """
    Registro que contém o cadastro dos custos de déficit.
    """

    IDENTIFIER = "CD  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            IntegerField(2, 9),
            LiteralField(10, 14),
            IntegerField(2, 24),
            FloatField(5, 29, 1),
            FloatField(10, 34, 2),
            FloatField(5, 44, 1),
            FloatField(10, 49, 2),
            FloatField(5, 59, 1),
            FloatField(10, 64, 2),
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
    def numero_curva(self) -> Optional[int]:
        return self.data[0]

    @numero_curva.setter
    def numero_curva(self, n: int):
        self.data[0] = n

    @property
    def subsistema(self) -> Optional[int]:
        return self.data[1]

    @subsistema.setter
    def subsistema(self, s: int):
        self.data[1] = s

    @property
    def nome_curva(self) -> Optional[str]:
        return self.data[2]

    @nome_curva.setter
    def nome_curva(self, n: str):
        self.data[2] = n

    @property
    def estagio(self) -> Optional[int]:
        return self.data[3]

    @estagio.setter
    def estagio(self, e: int):
        self.data[3] = e

    @property
    def limites_superiores(self) -> Optional[List[float]]:
        return [v for v in self.data[4::2] if v is not None]

    @limites_superiores.setter
    def limites_superiores(self, lim: List[float]):
        self.__atualiza_dados_lista(lim, 4, 2)

    @property
    def custos(self) -> Optional[List[float]]:
        return [v for v in self.data[5::2] if v is not None]

    @custos.setter
    def custos(self, cus: List[float]):
        self.__atualiza_dados_lista(cus, 5, 2)


class RI(Register):
    """
    Registro que contém as restrições de Itaipu.
    """

    IDENTIFIER = "RI  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            IntegerField(3, 13),
            FloatField(7, 16, 0),
            FloatField(7, 23, 0),
            FloatField(7, 30, 0),
            FloatField(7, 37, 0),
            FloatField(7, 44, 0),
            FloatField(7, 51, 0),
            FloatField(7, 58, 0),
            FloatField(7, 65, 0),
            FloatField(7, 72, 0),
            FloatField(7, 79, 0),
            FloatField(7, 86, 0),
            FloatField(7, 93, 0),
            FloatField(7, 100, 0),
            FloatField(7, 107, 0),
            FloatField(7, 114, 0),
        ]
    )


class IA(Register):
    """
    Registro que contém os limites de intercâmbio entre os subsistemas.
    """

    IDENTIFIER = "IA  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            LiteralField(2, 9),
            LiteralField(2, 14),
            IntegerField(1, 17),
            FloatField(10, 19, 0),
            FloatField(10, 29, 0),
            FloatField(10, 39, 0),
            FloatField(10, 49, 0),
            FloatField(10, 59, 0),
            FloatField(10, 69, 0),
        ]
    )


class TX(Register):
    """
    Registro que contém a taxa de desconto anual do modelo.
    """

    IDENTIFIER = "TX  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            FloatField(5, 4, 0),
        ]
    )

    @property
    def taxa(self) -> Optional[float]:
        """
        A taxa de desconto em % utilizada no estudo.

        :return: A taxa.
        :rtype: Optional[float]
        """
        return self.data[0]

    @taxa.setter
    def taxa(self, t: float):
        self.data[0] = t


class GP(Register):
    """
    Registro que contém o gap de tolerância para convergência.
    """

    IDENTIFIER = "GP  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            FloatField(10, 4, 6),
        ]
    )

    @property
    def gap(self) -> Optional[float]:
        """
        O gap considerado para convergência no estudo

        :return: O gap.
        :rtype: Optional[float]
        """
        return self.data[0]

    @gap.setter
    def gap(self, g: float):
        self.data[0] = g


class NI(Register):
    """
    Registro que contém o número máximo de iterações do modelo.
    """

    IDENTIFIER = "NI  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
        ]
    )

    @property
    def iteracoes(self) -> Optional[int]:
        """
        O número máximo de iterações do modelo no estudo

        :return: O número de iterações.
        :rtype: Optional[int]
        """
        return self.data[0]

    @iteracoes.setter
    def iteracoes(self, i: int):
        self.data[0] = i


class DT(Register):
    """
    Registro que contém a data de referência do estudo.
    """

    IDENTIFIER = "DT  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            IntegerField(2, 9),
            IntegerField(4, 14),
        ]
    )

    @property
    def dia(self) -> Optional[int]:
        """
        O dia de referência para realização do estudo

        :return: O dia
        :rtype: Optional[int]
        """
        return self.data[0]

    @dia.setter
    def dia(self, d: int):
        self.data[0] = d

    @property
    def mes(self) -> Optional[int]:
        """
        O mês de referência para realização do estudo

        :return: O mês
        :rtype: Optional[int]
        """
        return self.data[1]

    @mes.setter
    def mes(self, m: int):
        self.data[1] = m

    @property
    def ano(self) -> Optional[int]:
        """
        O ano de referência para realização do estudo

        :return: O ano
        :rtype: Optional[int]
        """
        return self.data[2]

    @ano.setter
    def ano(self, a: int):
        self.data[2] = a


class MP(Register):
    """
    Registro que contém as manutenções programadas das UHEs.
    """

    IDENTIFIER = "MP  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 7),
            FloatField(5, 9, 3),
            FloatField(5, 14, 3),
            FloatField(5, 19, 3),
            FloatField(5, 24, 3),
            FloatField(5, 29, 3),
            FloatField(5, 34, 3),
            FloatField(5, 39, 3),
            FloatField(5, 44, 3),
            FloatField(5, 49, 3),
            FloatField(5, 54, 3),
            FloatField(5, 59, 3),
            FloatField(5, 64, 3),
            FloatField(5, 69, 3),
        ]
    )


class MT(Register):
    """
    Registro que contém as manutenções programadas das UTEs.
    """

    IDENTIFIER = "MT  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            FloatField(5, 14, 3),
            FloatField(5, 19, 3),
            FloatField(5, 24, 3),
            FloatField(5, 29, 3),
            FloatField(5, 34, 3),
            FloatField(5, 39, 3),
            FloatField(5, 44, 3),
            FloatField(5, 49, 3),
            FloatField(5, 54, 3),
            FloatField(5, 59, 3),
            FloatField(5, 64, 3),
            FloatField(5, 69, 3),
            FloatField(5, 74, 3),
        ]
    )


class FD(Register):
    """
    Registro que contém as manutenções programadas das UTEs.
    """

    IDENTIFIER = "FD  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 7),
            FloatField(5, 9, 3),
            FloatField(5, 14, 3),
            FloatField(5, 19, 3),
            FloatField(5, 24, 3),
            FloatField(5, 29, 3),
            FloatField(5, 34, 3),
            FloatField(5, 39, 3),
            FloatField(5, 44, 3),
            FloatField(5, 49, 3),
            FloatField(5, 54, 3),
            FloatField(5, 59, 3),
            FloatField(5, 64, 3),
            FloatField(5, 69, 3),
        ]
    )


class VE(Register):
    """
    Registro que contém os volumes de espera das UHEs.
    """

    IDENTIFIER = "VE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(5, 9, 2),
            FloatField(5, 14, 2),
            FloatField(5, 19, 2),
            FloatField(5, 24, 2),
            FloatField(5, 29, 2),
            FloatField(5, 34, 2),
            FloatField(5, 39, 2),
            FloatField(5, 44, 2),
            FloatField(5, 49, 2),
            FloatField(5, 54, 2),
            FloatField(5, 59, 2),
            FloatField(5, 64, 2),
            FloatField(5, 69, 2),
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
        O código do posto associado ao volume.

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def volumes(self) -> Optional[List[float]]:
        """
        Os volumes de espera por estagio.

        :return: Os volumes.
        :rtype: Optional[List[float]]
        """
        return [v for v in self.data[1:] if v is not None]

    @volumes.setter
    def volumes(self, cus: List[float]):
        self.__atualiza_dados_lista(cus, 1, 1)


class RE(Register):
    """
    Registro que contém os cadastros de restrições elétricas.
    """

    IDENTIFIER = "RE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            IntegerField(2, 14),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código de cadastro para a restrição

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def estagio_inicial(self) -> Optional[int]:
        """
        O estágio inicial para consideração da restrição

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicial.setter
    def estagio_inicial(self, e: int):
        self.data[1] = e

    @property
    def estagio_final(self) -> Optional[int]:
        """
        O estágio final para consideração da restrição

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_final.setter
    def estagio_final(self, e: int):
        self.data[2] = e


class LU(Register):
    """
    Registro que contém os cadastros de limites das restrições elétricas.
    """

    IDENTIFIER = "LU  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            FloatField(10, 14, 1),
            FloatField(10, 24, 1),
            FloatField(10, 34, 1),
            FloatField(10, 44, 1),
            FloatField(10, 54, 1),
            FloatField(10, 64, 1),
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
        O código da restrição RE associada aos limites

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio inicial para consideração dos limites, até
        que sejam especificados novos limites.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, e: int):
        self.data[1] = e

    @property
    def limites_inferiores(self) -> Optional[List[float]]:
        """
        Os limites inferiores por patamar para a restrição elétrica

        :return: Os limites
        :rtype: Optional[list[float]]
        """
        return self.data[2::2]

    @limites_inferiores.setter
    def limites_inferiores(self, lim: List[float]):
        self.__atualiza_dados_lista(lim, 2, 2)

    @property
    def limites_superiores(self) -> Optional[List[float]]:
        """
        Os limites superiores por patamar para a restrição elétrica

        :return: Os limites
        :rtype: Optional[list[float]]
        """
        return self.data[3::2]

    @limites_superiores.setter
    def limites_superiores(self, lim: List[float]):
        self.__atualiza_dados_lista(lim, 3, 2)


class FU(Register):
    """
    Registro que contém os coeficientes das usinas hidráulicas
    nas restrições elétricas.
    """

    IDENTIFIER = "FU  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            IntegerField(3, 14),
            FloatField(10, 19, 7),
            IntegerField(2, 30),
        ]
    )


class FT(Register):
    """
    Registro que contém os coeficientes das usinas térmicas
    nas restrições elétricas.
    """

    IDENTIFIER = "FT  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            IntegerField(3, 14),
            IntegerField(2, 19),
            FloatField(10, 24, 7),
        ]
    )


class FI(Register):
    """
    Registro que contém o sentido do fluxo da interligação
    entre os subsistemas associados à restrição elétrica.
    """

    IDENTIFIER = "FI  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            LiteralField(2, 14),
            LiteralField(2, 19),
            FloatField(10, 24, 7),
        ]
    )


class VI(Register):
    """
    Registro que contém os tempos de viagem da água entre usinas.
    """

    IDENTIFIER = "VI  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(3, 9),
            FloatField(5, 14, 0),
            FloatField(5, 19, 0),
            FloatField(5, 24, 0),
            FloatField(5, 29, 0),
            FloatField(5, 34, 0),
            FloatField(5, 39, 0),
            FloatField(5, 44, 0),
            FloatField(5, 49, 0),
            FloatField(5, 54, 0),
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
    def uhe(self) -> Optional[int]:
        """
        O código da UHE a partir do qual é contabilizado
        o tempo de viagem.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def duracao(self) -> Optional[int]:
        """
        A duração da viagem da água (em horas) entre a UHE do
        código informado e sua usina à jusante segundo o hidr.

        :return: A duração
        :rtype: Optional[int]
        """
        return self.data[1]

    @duracao.setter
    def duracao(self, d: int):
        self.data[1] = d

    @property
    def vazoes(self) -> Optional[List[float]]:
        """
        As vazões defluentes das semanas passadas para a usina
        do código informado. A posição da vazão na lista indica
        a qual semana passada se refere [s-1, s-2, s-3, ...].

        :return: As vazões
        :rtype: Optional[list[float]]
        """
        return [v for v in self.data[2::] if v is not None]

    @vazoes.setter
    def vazoes(self, v: List[float]):
        self.__atualiza_dados_lista(v, 2, 1)


class IR(Register):
    """
    Registro que contém as configurações de
    geração de relatórios de saída.
    """

    IDENTIFIER = "IR  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            LiteralField(7, 4),
            IntegerField(2, 14),
            IntegerField(2, 19),
            IntegerField(5, 24),
        ]
    )

    @property
    def tipo(self) -> Optional[str]:
        """
        Mnemônico que contém o tipo de relatório de
        saída escolhido.

        :return: O mnemônico.
        :rtype: Optional[str]
        """
        return self.data[0]

    @tipo.setter
    def tipo(self, t: str):
        self.data[0] = t


class CI(Register):
    """
    Registro que define contratos de importação de energia.
    """

    IDENTIFIER = "CI  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 8),
            LiteralField(10, 11),
            IntegerField(2, 24),
            FloatField(5, 29, 0),
            FloatField(5, 34, 0),
            FloatField(10, 39, 2),
            FloatField(5, 49, 0),
            FloatField(5, 54, 0),
            FloatField(10, 59, 2),
            FloatField(5, 69, 0),
            FloatField(5, 74, 0),
            FloatField(10, 79, 2),
            FloatField(5, 89, 3),
        ]
    )


class CE(Register):
    """
    Registro que define contratos de exportação de energia.
    """

    IDENTIFIER = "CE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 8),
            LiteralField(10, 11),
            IntegerField(2, 24),
            FloatField(5, 29, 0),
            FloatField(5, 34, 0),
            FloatField(10, 39, 2),
            FloatField(5, 49, 0),
            FloatField(5, 54, 0),
            FloatField(10, 59, 2),
            FloatField(5, 69, 0),
            FloatField(5, 74, 0),
            FloatField(10, 79, 2),
            FloatField(5, 89, 3),
        ]
    )


class FC(Register):
    """
    Registro que contém informações para acessar a FCF fornecida
    pelo NEWAVE.
    """

    IDENTIFIER = "FC  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            LiteralField(6, 4),
            LiteralField(200, 14),
        ]
    )

    @property
    def tipo(self) -> Optional[str]:
        """
        O tipo de arquivo da FCF na forma dos mnemônicos
        aceitos pelo DECOMP.

        :return: O mnemônico.
        :rtype: Optional[str]
        """
        return self.data[0]

    @property
    def caminho(self) -> Optional[str]:
        """
        O caminho relativo ou completo para o arquivo da
        FCF.

        :return: O caminho.
        :rtype: Optional[str]
        """
        return self.data[1]

    @caminho.setter
    def caminho(self, c: str):
        self.data[1] = c


class RT(Register):
    """
    Registro utilizado para retirada de restrições de soleira de
    vertedouro e de canais de desvio.
    """

    IDENTIFIER = "RT  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            LiteralField(6, 4),
        ]
    )

    @property
    def restricao(self) -> Optional[str]:
        """
        O mnemônico da restrição removida.

        :return: O mnemônico
        :rtype: Optional[str]
        """
        return self.data[0]

    @restricao.setter
    def restricao(self, m: str):
        self.data[0] = m


class TI(Register):
    """
    Registro que contém as taxas de irrigação por UHE.
    """

    IDENTIFIER = "TI  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(5, 9, 2),
            FloatField(5, 14, 2),
            FloatField(5, 19, 2),
            FloatField(5, 24, 2),
            FloatField(5, 29, 2),
            FloatField(5, 34, 2),
            FloatField(5, 39, 2),
            FloatField(5, 44, 2),
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
        O código da UHE associada às taxas de irrigação

        :return: O código como `int`.
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def taxas(self) -> Optional[List[float]]:
        """
        As taxas de irrigação por estágio do estudo. A
        posição da taxa na lista indica a qual estágio
        ela está associada [e1, e2, e3, ...].

        :return: As taxas.
        :type: Optional[list[float]]
        """
        return [v for v in self.data[1::] if v is not None]

    @taxas.setter
    def taxas(self, tx: List[float]):
        self.__atualiza_dados_lista(tx, 1, 1)


class FP(Register):
    """
    Registro que contém os cadastros de restrições de alteração na
    função de produção das usinas.
    """

    IDENTIFIER = "FP  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(3, 9),
            IntegerField(1, 14),
            IntegerField(4, 16),
            FloatField(5, 21, 0),
            FloatField(5, 27, 0),
            IntegerField(1, 34),
            IntegerField(4, 36),
            FloatField(5, 41, 0),
            FloatField(5, 47, 0),
            FloatField(5, 54, 0),
            FloatField(5, 60, 0),
            FloatField(5, 66, 0),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código da UHE associada à restrição FP.

        :return: O código
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio associado à restrição FP.

        :return: O estágio
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, e: int):
        self.data[1] = e

    @property
    def tipo_entrada_janela_turbinamento(self) -> Optional[int]:
        """
        O tipo de entrada da janela de turbinamento fornecido
        na restrição FP. 0 para limites em percentual da vazão turbinada
        máxima das usinas, 1 para limites em m3/s.

        :return: O tipo de entrada
        :rtype: Optional[int]
        """
        return self.data[2]

    @tipo_entrada_janela_turbinamento.setter
    def tipo_entrada_janela_turbinamento(self, t: int):
        self.data[2] = t

    @property
    def numero_pontos_turbinamento(self) -> Optional[int]:
        """
        O número de pontos para discretização da janela de
        turbinamento. Máximo permitido de 1000 pontos.

        :return: O número de pontos
        :rtype: Optional[int]
        """
        return self.data[3]

    @numero_pontos_turbinamento.setter
    def numero_pontos_turbinamento(self, n: int):
        self.data[3] = n

    @property
    def limite_inferior_janela_turbinamento(self) -> Optional[float]:
        """
        O limite inferior da janela de turbinamento.

        :return: O limite.
        :rtype: Optional[float]
        """
        return self.data[4]

    @limite_inferior_janela_turbinamento.setter
    def limite_inferior_janela_turbinamento(self, lim: float):
        self.data[4] = lim

    @property
    def limite_superior_janela_turbinamento(self) -> Optional[float]:
        """
        O limite superior da janela de turbinamento.

        :return: O limite.
        :rtype: Optional[float]
        """
        return self.data[5]

    @limite_superior_janela_turbinamento.setter
    def limite_superior_janela_turbinamento(self, lim: float):
        self.data[5] = lim

    @property
    def tipo_entrada_janela_volume(self) -> Optional[int]:
        """
        O tipo de entrada da janela de volume fornecido
        na restrição FP. 0 para limites em percentual do volume útil
        das usinas, 1 para limites em hm3.

        :return: O tipo de entrada.
        :rtype: Optional[int]
        """
        return self.data[6]

    @tipo_entrada_janela_volume.setter
    def tipo_entrada_janela_volume(self, t: int):
        self.data[6] = t

    @property
    def numero_pontos_volume(self) -> Optional[int]:
        """
        O número de pontos para discretização da janela de
        volume. Máximo permitido de 1000 pontos.

        :return: O número de pontos.
        :rtype: Optional[int]
        """
        return self.data[7]

    @numero_pontos_volume.setter
    def numero_pontos_volume(self, n: int):
        self.data[7] = n

    @property
    def limite_inferior_janela_volume(self) -> Optional[float]:
        """
        A redução aplicada ao volume útil da usina, para ser utilizado
        como limite inferior da janela de volume.

        :return: O limite.
        :rtype: Optional[float]
        """
        return self.data[8]

    @limite_inferior_janela_volume.setter
    def limite_inferior_janela_volume(self, lim: float):
        self.data[8] = lim

    @property
    def limite_superior_janela_volume(self) -> Optional[float]:
        """
        O acréscimo aplicado ao volume útil da usina, para ser utilizado
        como limite superior da janela de volume.

        :return: O limite.
        :rtype: Optional[float]
        """
        return self.data[9]

    @limite_superior_janela_volume.setter
    def limite_superior_janela_volume(self, lim: float):
        self.data[9] = lim


class RQ(Register):
    """
    Registro que contém os percentuais de vazão defluente
    mínima histórica para cada REE.
    """

    IDENTIFIER = "RQ  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            FloatField(5, 9, 2),
            FloatField(5, 14, 2),
            FloatField(5, 19, 2),
            FloatField(5, 24, 2),
            FloatField(5, 29, 2),
            FloatField(5, 34, 2),
            FloatField(5, 39, 2),
            FloatField(5, 44, 2),
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
    def ree(self) -> Optional[int]:
        """
        O código do REE associado às vazões mínimas.

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @ree.setter
    def ree(self, r: int):
        self.data[0] = r

    @property
    def vazoes(self) -> Optional[List[float]]:
        """
        As vazões defluentes mínimas (percentuais)
        para o REE, por estágio [e1, e2, e3, ...].

        :return: As vazoes.
        :rtype: Optional[list[float]]
        """
        return [v for v in self.data[1:] if v is not None]

    @vazoes.setter
    def vazoes(self, v: List[float]):
        self.__atualiza_dados_lista(v, 1, 1)
        self.data[1:] = v


class EZ(Register):
    """
    Registro que contém o percentual máximo do
    volume útil para acoplamento.
    """

    IDENTIFIER = "EZ  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(5, 9, 2),
        ]
    )


class HV(Register):
    """
    Registro que contém os cadastros de restrições de volume armazenado.
    """

    IDENTIFIER = "HV  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            IntegerField(2, 14),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código da UHE associada à restrição HV.

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def estagio_inicial(self) -> Optional[int]:
        """
        O estágio inicial de consideração da restrição HV.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicial.setter
    def estagio_inicial(self, e: int):
        self.data[1] = e

    @property
    def estagio_final(self) -> Optional[int]:
        """
        O estágio final de consideração da restrição HV.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_final.setter
    def estagio_final(self, e: int):
        self.data[2] = e


class LV(Register):
    """
    Registro que contém os cadastros dos limites das
    restrições de volume armazenado.
    """

    IDENTIFIER = "LV  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            FloatField(10, 14, 2),
            FloatField(10, 24, 2),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código da restrição HV associada aos limites

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio de consideração dos limites.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, e: int):
        self.data[1] = e

    @property
    def limite_inferior(self) -> Optional[float]:
        """
        O limite inferior para o armazenamento.

        :return: O limite.
        :rtype: Optional[float]
        """
        return self.data[2]

    @limite_inferior.setter
    def limite_inferior(self, lim: float):
        self.data[2] = lim

    @property
    def limite_superior(self) -> Optional[float]:
        """
        O limite superior para o armazenamento.

        :return: O limite.
        :rtype: Optional[float]
        """
        return self.data[3]

    @limite_superior.setter
    def limite_superior(self, lim: float):
        self.data[3] = lim


class CV(Register):
    """
    Registro que contém os coeficientes das usinas hidráulicas
    nas restrições de volume armazenado.
    """

    IDENTIFIER = "CV  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            IntegerField(3, 14),
            FloatField(10, 19, 7),
            LiteralField(4, 34),
        ]
    )


class HQ(Register):
    """
    Registro que contém os cadastros de restrições de vazões.
    """

    IDENTIFIER = "HQ  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            IntegerField(2, 14),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código da UHE associada à restrição HQ.

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def estagio_inicial(self) -> Optional[int]:
        """
        O estágio inicial de consideração da restrição HQ.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio_inicial.setter
    def estagio_inicial(self, e: int):
        self.data[1] = e

    @property
    def estagio_final(self) -> Optional[int]:
        """
        O estágio final de consideração da restrição HQ.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[2]

    @estagio_final.setter
    def estagio_final(self, e: int):
        self.data[2] = e


class LQ(Register):
    """
    Registro que contém os cadastros dos limites das
    restrições de vazão.
    """

    IDENTIFIER = "LQ  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            FloatField(10, 14, 2),
            FloatField(10, 24, 2),
            FloatField(10, 34, 2),
            FloatField(10, 44, 2),
            FloatField(10, 54, 2),
            FloatField(10, 64, 2),
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
        O código da restrição HQ associada aos limites

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio de consideração dos limites.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, e: int):
        self.data[1] = e

    @property
    def limites_inferiores(self) -> Optional[List[float]]:
        """
        Os limites inferiores por patamar para a vazão.

        :return: Os limites.
        :rtype: Optional[list[float]]
        """
        return self.data[2::2]

    @limites_inferiores.setter
    def limites_inferiores(self, lim: List[float]):
        self.__atualiza_dados_lista(lim, 2, 2)

    @property
    def limites_superiores(self) -> Optional[List[float]]:
        """
        Os limites superiores por patamar para a vazão.

        :return: Os limites.
        :rtype: Optional[list[float]]
        """
        return self.data[3::2]

    @limites_superiores.setter
    def limites_superiores(self, lim: List[float]):
        self.__atualiza_dados_lista(lim, 3, 2)


class CQ(Register):
    """
    Registro que contém os coeficientes das usinas hidráulicas
    nas restrições de vazão.
    """

    IDENTIFIER = "CQ  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            IntegerField(3, 14),
            FloatField(10, 19, 7),
            LiteralField(4, 34),
        ]
    )


class AR(Register):
    """
    Registro que contém as configurações de aversão a risco.
    """

    IDENTIFIER = "AR  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 5),
        ]
    )


class EV(Register):
    """
    Registro que contém as configurações de consideração
    da evaporação.
    """

    IDENTIFIER = "EV  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(1, 4),
            LiteralField(3, 9),
        ]
    )

    @property
    def modelo(self) -> Optional[int]:
        """
        O modelo de evaporação considerado

        :return: O modelo.
        :rtype: Optional[int]
        """
        return self.data[0]

    @modelo.setter
    def modelo(self, m: int):
        self.data[0] = m

    @property
    def volume_referencia(self) -> Optional[str]:
        """
        O mnemônico para o volume considerado

        :return: O mnemônico.
        :rtype: Optional[str]
        """
        return self.data[1]

    @volume_referencia.setter
    def volume_referencia(self, v: str):
        self.data[1] = v


class FJ(Register):
    """
    Registro que contém o arquivo de polinômios de jusante.
    """

    IDENTIFIER = "FJ  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            LiteralField(12, 4),
        ]
    )

    @property
    def arquivo(self) -> str:
        return self.data[0]

    @arquivo.setter
    def arquivo(self, a: str):
        self.data[0] = a


class HE(Register):
    """
    Registro que contém o cadastro de uma restrição de energia
    armazenada.
    """

    IDENTIFIER = "HE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(1, 9),
            FloatField(10, 14, 2),
            IntegerField(2, 25),
            FloatField(10, 28, 2),
            IntegerField(1, 39),
            IntegerField(1, 41),
            IntegerField(1, 43),
            LiteralField(12, 45),
        ]
    )

    @property
    def codigo(self) -> Optional[int]:
        """
        O código de cadastro da restrição HE

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def tipo_limite(self) -> Optional[int]:
        """
        O tipo de limite especificado na restrição HE,
        em valor absoluto ou percentual.

        :return: O tipo.
        :rtype: Optional[int]
        """
        return self.data[1]

    @tipo_limite.setter
    def tipo_limite(self, t: int):
        self.data[1] = t

    @property
    def limite(self) -> Optional[float]:
        """
        O limite para a energia armazenada associada
        ao registro HE.

        :return: O limite.
        :rtype: Optional[float]
        """
        return self.data[2]

    @limite.setter
    def limite(self, lim: float):
        self.data[2] = lim

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio para consideração da restrição.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[3]

    @estagio.setter
    def estagio(self, e: int):
        self.data[3] = e

    @property
    def penalidade(self) -> Optional[float]:
        """
        O valor da penalidade para a violação da restrição.

        :return: O valor.
        :rtype: Optional[float]
        """
        return self.data[4]

    @penalidade.setter
    def penalidade(self, p: float):
        self.data[4] = p

    @property
    def forma_calculo_produtibilidades(self) -> Optional[int]:
        """
        Flag para indicar a forma de cálculo das produtividades
        das usinas usadas nas restrição.

        :return: A flag.
        :rtype: Optional[float]
        """
        return self.data[5]

    @forma_calculo_produtibilidades.setter
    def forma_calculo_produtibilidades(self, t: int):
        self.data[5] = t

    @property
    def tipo_valores_produtibilidades(self) -> Optional[int]:
        """
        Flag para indicar o tipo dos valores das produtividades
        das usinas usadas nas restrição.

        :return: O tipo.
        :rtype: Optional[int]
        """
        return self.data[6]

    @tipo_valores_produtibilidades.setter
    def tipo_valores_produtibilidades(self, t: int):
        self.data[6] = t

    @property
    def tipo_penalidade(self) -> Optional[int]:
        """
        O tipo de penalidade a ser considerada ao violar a
        restrição (inviabilidade ou penalização).

        :return: O tipo.
        :rtype: Optional[int]
        """
        return self.data[7]

    @tipo_penalidade.setter
    def tipo_penalidade(self, t: int):
        self.data[7] = t

    @property
    def arquivo_produtibilidades(self) -> Optional[str]:
        """
        O arquivo com as definições das produtibilidades usadas
        para o cálculo da restrição RHE.

        :return: O arquivo externo com as produbitibilidades.
        :rtype: Optional[str]
        """
        return self.data[8]

    @arquivo_produtibilidades.setter
    def arquivo_produtibilidades(self, t: str):
        self.data[8] = t


class CM(Register):
    """
    Registro que contém os coeficientes de uma restrição RHE.
    """

    IDENTIFIER = "CM  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [IntegerField(3, 4), IntegerField(3, 9), FloatField(10, 14, 2)]
    )

    @property
    def codigo(self) -> int:
        """
        O código de cadastro da restrição CM

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @codigo.setter
    def codigo(self, c: int):
        self.data[0] = c

    @property
    def ree(self) -> int:
        """
        O REE do coeficiente

        :return: O REE.
        :rtype: Optional[int]
        """
        return self.data[1]

    @ree.setter
    def ree(self, e: int):
        self.data[1] = e

    @property
    def coeficiente(self) -> float:
        """
        O coeficiente de energia considerado

        :return: O coeficiente.
        :rtype: Optional[float]
        """
        return self.data[2]

    @coeficiente.setter
    def coeficiente(self, c: float):
        self.data[2] = c


class ACNUMPOS(Register):
    """
    Registro AC específico para alteração no número do posto.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  NUMPOS"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACNUMJUS(Register):
    """
    Registro AC específico para alteração na usina de jusante.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  NUMJUS"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACDESVIO(Register):
    """
    Registro AC específico para alteração na usina de jusante
    para canal de desvio e limite da vazão no canal.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  DESVIO"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(10, 24, 2),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACVOLMIN(Register):
    """
    Registro AC específico para alteração de volume mínimo.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  VOLMIN"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(10, 24, 2),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACVOLMAX(Register):
    """
    Registro AC específico para alteração de volume máximo.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  VOLMAX"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(10, 24, 2),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACCOTVOL(Register):
    """
    Registro AC específico para alteração de um coeficiente do
    polinômio cota-volume.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  COTVOL"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(15, 24, 3),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACCOTARE(Register):
    """
    Registro AC específico para alteração de um coeficiente do
    polinômio cota-área.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  COTARE"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(15, 24, 3),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACPROESP(Register):
    """
    Registro AC específico para alteração do coeficiente de perdas
    hidráulicas em função da queda bruta (%,m,k).
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  PROESP"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(10, 19, 3),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACPERHID(Register):
    """
    Registro AC específico para alteração do coeficiente de perdas
    hidráulicas em função da queda bruta (%,m,k).
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  PERHID"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(10, 19, 3),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACNCHAVE(Register):
    """
    Registro AC específico para alteração do número da curva-chave
    (cota-vazão) e nível de jusante da faixa associada (m).
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  NCHAVE"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(10, 24, 3),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACCOTVAZ(Register):
    """
    Registro AC específico para alteração de um coeficiente do
    polinômio cota-vazão.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  COTVAZ"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            IntegerField(5, 24),
            FloatField(15, 29, 3),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACCOFEVA(Register):
    """
    Registro AC específico para alteração do coeficiente de evaporação
    mensal para cada mês.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  COFEVA"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            IntegerField(5, 24),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACNUMCON(Register):
    """
    Registro AC específico para alteração no número de conjuntos
    de máquinas.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  NUMCON"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACNUMMAQ(Register):
    """
    Registro AC específico para alteração do número de máquinas
    em cada conjunto de máquinas.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  NUMMAQ"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            IntegerField(5, 24),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACPOTEFE(Register):
    """
    Registro AC específico para alteração da potência efetiva
    por unidade geradora em um conjunto de máquinas.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  POTEFE"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(10, 24, 2),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACALTEFE(Register):
    """
    Registro AC específico para alteração da altura efetiva
    de queda para um conjunto de máquinas.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  ALTEFE"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            FloatField(10, 24, 2),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACVAZEFE(Register):
    """
    Registro AC específico para alteração da vazão efetiva
    para um conjunto de máquinas.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  VAZEFE"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            IntegerField(5, 24),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACJUSMED(Register):
    """
    Registro AC específico para alteração da cota média do canal
    de fuga em metros.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  JUSMED"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(10, 19, 2),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACVERTJU(Register):
    """
    Registro AC específico para consideração da influência do vertimento
    no canal de fuga.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  VERTJU"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACVAZMIN(Register):
    """
    Registro AC específico para alteração da vazão mínima.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  VAZMIN"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACTIPERH(Register):
    """
    Registro AC específico para alteração do tipo de perdas hidráulicas.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  TIPERH"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACJUSENA(Register):
    """
    Registro AC específico para alteração do índice de
    aproveitamento de jusante para cálculo das energias
    armazenada e afluente.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  JUSENA"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACVSVERT(Register):
    """
    Registro AC específico para alteração do volume mínimo para operação
    do vertedor.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  VSVERT"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(10, 19, 2),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACVMDESV(Register):
    """
    Registro AC específico para alteração do volume mínimo para operação
    do canal de desvio.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  VMDESV"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(10, 19, 2),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACNPOSNW(Register):
    """
    Registro AC específico para alteração do posto de acoplamento
    com o NEWAVE.
    """

    IDENTIFIER = r"AC  ([\d ]{1,3})  NPOSNW"
    IDENTIFIER_DIGITS = 15
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(5, 19),
            LiteralField(3, 69),
            IntegerField(2, 73),
            IntegerField(4, 76),
        ]
    )

    # Override
    def write(self, file: IO) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def uhe(self) -> Optional[int]:
        return self.data[0]

    @uhe.setter
    def uhe(self, u: int):
        self.data[0] = u

    @property
    def mes(self) -> Optional[str]:
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m
