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

    __slots__ = []

    IDENTIFIER = "TE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line([LiteralField(75, 4)])

    @property
    def titulo(self) -> Optional[str]:
        """
        O único conteúdo do registro (título do estudo).

        :return: O título do estudo
        :rtype: str | None
        """
        return self.data[0]

    @titulo.setter
    def titulo(self, t: str):
        self.data[0] = t


class SB(Register):
    """
    Registro que contém o cadastro dos submercados.
    """

    __slots__ = []

    IDENTIFIER = "SB  "
    IDENTIFIER_DIGITS = 4
    LINE = Line([IntegerField(2, 4), LiteralField(2, 9)])

    @property
    def codigo_submercado(self) -> Optional[int]:
        """
        O código de cadastro do submercado.

        :return: O código.
        :rtype: int | None]
        """
        return self.data[0]

    @codigo_submercado.setter
    def codigo_submercado(self, cod: int):
        self.data[0] = cod

    @property
    def nome_submercado(self) -> Optional[str]:
        """
        O nome de cadastro do submercado.

        :return: O nome.
        :rtype: str | None
        """
        return self.data[1]

    @nome_submercado.setter
    def nome_submercado(self, n: str):
        self.data[1] = n


class UH(Register):
    """
    Registro que contém o cadastro das UHEs, com os seus volumes
    iniciais no estudo.
    """

    __slots__ = []

    IDENTIFIER = "UH  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(2, 9),
            FloatField(10, 14, 2),
            FloatField(10, 25, 2),
            IntegerField(1, 39),
            IntegerField(2, 44),
            FloatField(10, 49, 2),
            FloatField(10, 59, 2),
            IntegerField(1, 69),
            LiteralField(2, 71),
        ]
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código de cadastro da UHE.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, cod: int):
        self.data[0] = cod

    @property
    def codigo_ree(self) -> Optional[int]:
        """
        O REE de cadastro da UHE.

        :return: O REE.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_ree.setter
    def codigo_ree(self, n: int):
        self.data[1] = n

    @property
    def volume_inicial(self) -> Optional[float]:
        """
        O volume inicial da UHE para o estudo.

        :return: O volume.
        :rtype: float | None
        """
        return self.data[2]

    @volume_inicial.setter
    def volume_inicial(self, v: float):
        self.data[2] = v

    @property
    def vazao_defluente_minima(self) -> Optional[float]:
        """
        O vazão defluente mínima da usina em m3/s.

        :return: A vazão em m3/s.
        :rtype: float | None
        """
        return self.data[3]

    @vazao_defluente_minima.setter
    def vazao_defluente_minima(self, v: float):
        self.data[3] = v

    @property
    def evaporacao(self) -> Optional[int]:
        """
        A consideração ou não de evaporação para a UHE.

        :return: A consideração.
        :rtype: int | None
        """
        return self.data[4]

    @evaporacao.setter
    def evaporacao(self, e: int):
        self.data[4] = e

    @property
    def estagio_inicio_producao(self) -> Optional[int]:
        """
        Estágio a partir da qual a usina começa a produzir energia.

        :return: O índice do estágio.
        :rtype: int | None
        """
        return self.data[5]

    @estagio_inicio_producao.setter
    def estagio_inicio_producao(self, e: int):
        self.data[5] = e

    @property
    def volume_morto_inicial(self) -> Optional[float]:
        """
        Volume morto inicial da usina.

        :return: O volume em hm3.
        :rtype: float | None
        """
        return self.data[6]

    @volume_morto_inicial.setter
    def volume_morto_inicial(self, e: float):
        self.data[6] = e

    @property
    def limite_superior_vertimento(self) -> Optional[float]:
        """
        O limite superior para vertimento da usina.

        :return: O limite em m3/s.
        :rtype: float | None
        """
        return self.data[7]

    @limite_superior_vertimento.setter
    def limite_superior_vertimento(self, e: float):
        self.data[7] = e

    @property
    def balanco_hidrico_patamar(self) -> Optional[int]:
        """
        Consideração do balanço hídrico por patamar.

        :return: A consideração, ou não.
        :rtype: int | None
        """
        return self.data[8]

    @balanco_hidrico_patamar.setter
    def balanco_hidrico_patamar(self, e: int):
        self.data[8] = e

    @property
    def configuracao_newave(self) -> Optional[str]:
        """
        Sinaliza a existência da usina na configuração
        do NEWAVE, para compatibilização.

        :return: A existência da usina na configuração.
        :rtype: str | None
        """
        return self.data[9]

    @configuracao_newave.setter
    def configuracao_newave(self, e: str):
        self.data[9] = e


class CT(Register):
    """
    Registro que contém o cadastro das usinas termelétricas com
    os seus custos e capacidades.

    """

    __slots__ = []

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
            FloatField(5, 89, 2),
            FloatField(5, 94, 2),
            FloatField(10, 99, 2),
            FloatField(5, 109, 2),
            FloatField(5, 114, 2),
            FloatField(10, 119, 2),
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
    def codigo_usina(self) -> Optional[int]:
        """
        O código de cadastro da UTE.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, codigo: int):
        self.data[0] = codigo

    @property
    def codigo_submercado(self) -> Optional[int]:
        """
        O submercado de cadastro da UTE.

        :return: O submercado.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_submercado.setter
    def codigo_submercado(self, submercado: int):
        self.data[1] = submercado

    @property
    def nome_usina(self) -> Optional[str]:
        """
        O nome de cadastro da UTE.

        :return: O nome como uma `str`.
        :rtype: str | None
        """
        return self.data[2]

    @nome_usina.setter
    def nome_usina(self, nome: str):
        self.data[2] = nome

    @property
    def estagio(self) -> Optional[str]:
        """
        O estágio associado às propriedades cadastradas.

        :return: O estágio.
        :rtype: int | None
        """
        return self.data[3]

    @estagio.setter
    def estagio(self, estagio: int):
        self.data[3] = estagio

    @property
    def inflexibilidade(self) -> Optional[List[float]]:
        """
        A inflexibilidade da UTE por patamar.

        :return: A inflexibilidade.
        :rtype: list[float] | None
        """
        return [v for v in self.data[4::3] if v is not None]

    @inflexibilidade.setter
    def inflexibilidade(self, inflex: List[float]):
        self.__atualiza_dados_lista(inflex, 4, 3)

    @property
    def disponibilidade(self) -> Optional[List[float]]:
        """
        A disponibilidade da UTE por patamar.

        :return: A disponibilidade.
        :rtype: list[float] | None
        """
        return [v for v in self.data[5::3] if v is not None]

    @disponibilidade.setter
    def disponibilidade(self, disp: List[float]):
        self.__atualiza_dados_lista(disp, 5, 3)

    @property
    def cvu(self) -> Optional[List[float]]:
        """
        O CVU da UTE por patamar.

        :return: O CVU.
        :rtype: list[float] | None
        """
        return [v for v in self.data[6::3] if v is not None]

    @cvu.setter
    def cvu(self, cvu: List[float]):
        self.__atualiza_dados_lista(cvu, 6, 3)


class UE(Register):
    """
    Registro que contém o cadastro das estações de bombeamento
    (usinas elevatórias).
    """

    __slots__ = []

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

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O código de cadastro da UE.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, cod: int):
        self.data[0] = cod

    @property
    def codigo_submercado(self) -> Optional[int]:
        """
        O submercado de cadastro da UE, conforme registro SB.

        :return: O submercado.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_submercado.setter
    def codigo_submercado(self, n: int):
        self.data[1] = n

    @property
    def nome_usina(self) -> Optional[str]:
        """
        O nome da estação de bombeamento.

        :return: O nome.
        :rtype: str | None
        """
        return self.data[2]

    @nome_usina.setter
    def nome_usina(self, v: str):
        self.data[2] = v

    @property
    def codigo_usina_montante(self) -> Optional[int]:
        """
        O código da UHE a montante, conforme registro UH.

        :return: O código.
        :rtype: int | None
        """
        return self.data[3]

    @codigo_usina_montante.setter
    def codigo_usina_montante(self, v: int):
        self.data[3] = v

    @property
    def codigo_usina_jusante(self) -> Optional[int]:
        """
        O código da UHE a jusante, conforme registro UH.

        :return: O código.
        :rtype: int | None
        """
        return self.data[4]

    @codigo_usina_jusante.setter
    def codigo_usina_jusante(self, e: int):
        self.data[4] = e

    @property
    def vazao_minima_bombeavel(self) -> Optional[float]:
        """
        A vazão mínima bombeável.

        :return: A vazão em m3/s
        :rtype: float | None
        """
        return self.data[5]

    @vazao_minima_bombeavel.setter
    def vazao_minima_bombeavel(self, e: float):
        self.data[5] = e

    @property
    def vazao_maxima_bombeavel(self) -> Optional[float]:
        """
        A vazão mínima bombeável.

        :return: A vazão em m3/s
        :rtype: float | None
        """
        return self.data[6]

    @vazao_maxima_bombeavel.setter
    def vazao_maxima_bombeavel(self, e: float):
        self.data[6] = e

    @property
    def taxa_consumo(self) -> Optional[float]:
        """
        A taxa de consumo.

        :return: A taxa em MWmed/m3/s.
        :rtype: float | None
        """
        return self.data[7]

    @taxa_consumo.setter
    def taxa_consumo(self, e: float):
        self.data[7] = e


class DP(Register):
    """
    Registro que contém o cadastro das durações dos patamares.

    """

    __slots__ = []

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
            FloatField(10, 79, 1),
            FloatField(10, 89, 1),
            FloatField(10, 99, 1),
            FloatField(10, 109, 1),
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
        :rtype: int | None
        """
        return self.data[0]

    @estagio.setter
    def estagio(self, e: int):
        self.data[0] = e

    @property
    def codigo_submercado(self) -> Optional[int]:
        """
        O submercado associado às durações especificadas.

        :return: O submercado.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_submercado.setter
    def codigo_submercado(self, sub: int):
        self.data[1] = sub

    @property
    def numero_patamares(self) -> Optional[int]:
        """
        O número de patamares.

        :return: O número de patamares.
        :rtype: int | None
        """
        return self.data[2]

    @numero_patamares.setter
    def numero_patamares(self, n: int):
        self.data[2] = n

    @property
    def carga(self) -> Optional[List[float]]:
        """
        A carga em Mwmed pata cada patamar de carga

        :return: A carga.
        :rtype: list[float] | None
        """
        return [v for v in self.data[3::2] if v is not None]

    @carga.setter
    def carga(self, c: List[float]):
        self.__atualiza_dados_lista(c, 3, 2)

    @property
    def duracao(self) -> Optional[List[float]]:
        """
        A duração de cada patamar de carga em horas

        :return: A duração em horas.
        :rtype: list[float] | None
        """
        return [v for v in self.data[4::2] if v is not None]

    @duracao.setter
    def duracao(self, d: List[float]):
        self.__atualiza_dados_lista(d, 4, 2)


class PQ(Register):
    """
    Registro que contém o cadastro da geração por pequenas usinas.

    """

    __slots__ = []

    IDENTIFIER = "PQ  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            LiteralField(10, 4),
            IntegerField(2, 14),
            IntegerField(2, 19),
            FloatField(5, 24, 0),
            FloatField(5, 29, 0),
            FloatField(5, 34, 0),
            FloatField(5, 39, 0),
            FloatField(5, 44, 0),
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
    def nome(self) -> Optional[str]:
        """
        O nome da geração.

        :return: O nome.
        :rtype: str | None
        """
        return self.data[0]

    @nome.setter
    def nome(self, nome: str):
        self.data[0] = nome

    @property
    def codigo_submercado(self) -> Optional[int]:
        """
        O submercado associado à geração.

        :return: O submercado.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_submercado.setter
    def codigo_submercado(self, sub: int):
        self.data[1] = sub

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio associado à geração.

        :return: O estágio.
        :rtype: int | None
        """
        return self.data[2]

    @estagio.setter
    def estagio(self, e: int):
        self.data[2] = e

    @property
    def geracao(self) -> Optional[List[float]]:
        """
        A geração em Mwmed para cada patamar de carga.

        :return: A geração.
        :rtype: list[float] | None
        """
        return [v for v in self.data[3:8] if v is not None]

    @geracao.setter
    def geracao(self, c: List[float]):
        self.__atualiza_dados_lista(c, 3, 1)


class CD(Register):
    """
    Registro que contém o cadastro dos custos de déficit.

    """

    __slots__ = []

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
            FloatField(5, 74, 1),
            FloatField(10, 79, 2),
            FloatField(5, 89, 1),
            FloatField(10, 94, 2),
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
    def codigo_curva(self) -> Optional[int]:
        """
        O código da curva de déficit.

        :return: O código da curva.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_curva.setter
    def codigo_curva(self, n: int):
        self.data[0] = n

    @property
    def codigo_submercado(self) -> Optional[int]:
        """
        O código do submercado associado.

        :return: O submercado.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_submercado.setter
    def codigo_submercado(self, s: int):
        self.data[1] = s

    @property
    def nome_curva(self) -> Optional[str]:
        """
        O nome da curva de déficit

        :return: O nome.
        :rtype: str | None
        """
        return self.data[2]

    @nome_curva.setter
    def nome_curva(self, n: str):
        self.data[2] = n

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio de vigência do custo de déficit

        :return: O estágio.
        :rtype: int | None
        """
        return self.data[3]

    @estagio.setter
    def estagio(self, e: int):
        self.data[3] = e

    @property
    def limite_superior(self) -> Optional[List[float]]:
        """
        O limite superior para consideração dos custos.

        :return: Os limites.
        :rtype: list[float] | None
        """
        return [v for v in self.data[4::2] if v is not None]

    @limite_superior.setter
    def limite_superior(self, lim: List[float]):
        self.__atualiza_dados_lista(lim, 4, 2)

    @property
    def custo(self) -> Optional[List[float]]:
        """
        O custo de déficit.

        :return: O custo.
        :rtype: list[float] | None
        """
        return [v for v in self.data[5::2] if v is not None]

    @custo.setter
    def custo(self, cus: List[float]):
        self.__atualiza_dados_lista(cus, 5, 2)


class RI(Register):
    """
    Registro que contém as restrições de Itaipu.

    """

    __slots__ = []

    IDENTIFIER = "RI  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(3, 8),
            IntegerField(3, 12),
            FloatField(7, 16, 1),
            FloatField(7, 23, 1),
            FloatField(7, 30, 1),
            FloatField(7, 37, 1),
            FloatField(7, 44, 1),
            FloatField(7, 51, 1),
            FloatField(7, 58, 1),
            FloatField(7, 65, 1),
            FloatField(7, 72, 1),
            FloatField(7, 79, 1),
            FloatField(7, 86, 1),
            FloatField(7, 93, 1),
            FloatField(7, 100, 1),
            FloatField(7, 107, 1),
            FloatField(7, 114, 1),
            FloatField(7, 121, 1),
            FloatField(7, 128, 1),
            FloatField(7, 135, 1),
            FloatField(7, 142, 1),
            FloatField(7, 149, 1),
            FloatField(7, 156, 1),
            FloatField(7, 163, 1),
            FloatField(7, 170, 1),
            FloatField(7, 177, 1),
            FloatField(7, 184, 1),
        ]
    )


class IA(Register):
    """
    Registro que contém os limites de intercâmbio entre os subsistemas.

    """

    __slots__ = []

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
            FloatField(10, 79, 0),
            FloatField(10, 89, 0),
            FloatField(10, 99, 0),
            FloatField(10, 109, 0),
        ]
    )


class TX(Register):
    """
    Registro que contém a taxa de desconto anual do modelo.
    """

    __slots__ = []

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
        :rtype: float | None
        """
        return self.data[0]

    @taxa.setter
    def taxa(self, t: float):
        self.data[0] = t


class GP(Register):
    """
    Registro que contém o gap de tolerância para convergência.
    """

    __slots__ = []

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
        :rtype: float | None
        """
        return self.data[0]

    @gap.setter
    def gap(self, g: float):
        self.data[0] = g


class NI(Register):
    """
    Registro que contém o número máximo de iterações do modelo.
    """

    __slots__ = []

    IDENTIFIER = "NI  "
    IDENTIFIER_DIGITS = 4
    LINE = Line([IntegerField(3, 4), IntegerField(1, 8)])

    @property
    def iteracoes(self) -> Optional[int]:
        """
        O número máximo de iterações do modelo no estudo

        :return: O número de iterações.
        :rtype: int | None
        """
        return self.data[0]

    @iteracoes.setter
    def iteracoes(self, i: int):
        self.data[0] = i

    @property
    def tipo_limite(self) -> Optional[int]:
        """
        Se o número de interações fornecido é mínimo ou máximo.

        :return: O tipo de limite de iterações
        :rtype: int | None
        """
        return self.data[1]

    @tipo_limite.setter
    def tipo_limite(self, i: int):
        self.data[1] = i


class DT(Register):
    """
    Registro que contém a data de referência do estudo.
    """

    __slots__ = []

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
        :rtype: int | None
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
        :rtype: int | None
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
        :rtype: int | None
        """
        return self.data[2]

    @ano.setter
    def ano(self, a: int):
        self.data[2] = a


class MP(Register):
    """
    Registro que contém as manutenções programadas das UHEs.

    """

    __slots__ = []

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
            FloatField(5, 74, 3),
            FloatField(5, 79, 3),
            FloatField(5, 84, 3),
            FloatField(5, 89, 3),
            FloatField(5, 94, 3),
            FloatField(5, 99, 3),
            FloatField(5, 104, 3),
            FloatField(5, 109, 3),
            FloatField(5, 114, 3),
            FloatField(5, 119, 3),
            FloatField(5, 124, 3),
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
    def codigo_usina(self) -> Optional[int]:
        """
        O código da UHE associada às manutenções programadas.

        :return: O código como `int`.
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def frequencia(self) -> Optional[int]:
        """
        A frequência quando se trata da UHE Itaipu.

        :return: A frequência como `int`.
        """
        return self.data[1]

    @frequencia.setter
    def frequencia(self, c: int):
        self.data[1] = c

    @property
    def manutencao(self) -> Optional[List[float]]:
        """
        Os fatores de manutenção programada por estágio do
        estudo. A posição na lista indica a qual estágio
        ele está associada [e1, e2, e3, ...].

        :return: As manutenções.
        :type: list[float] | None
        """
        return [v for v in self.data[2::] if v is not None]

    @manutencao.setter
    def manutencao(self, m: List[float]):
        self.__atualiza_dados_lista(m, 2, 1)


class MT(Register):
    """
    Registro que contém as manutenções programadas das UTEs.

    """

    __slots__ = []

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
            FloatField(5, 79, 3),
            FloatField(5, 84, 3),
            FloatField(5, 89, 3),
            FloatField(5, 94, 3),
            FloatField(5, 99, 3),
            FloatField(5, 104, 3),
            FloatField(5, 109, 3),
            FloatField(5, 114, 3),
            FloatField(5, 119, 3),
            FloatField(5, 124, 3),
            FloatField(5, 129, 3),
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
    def codigo_usina(self) -> Optional[int]:
        """
        O código da UTE associada às manutenções programadas.

        :return: O código como `int`.
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def codigo_submercado(self) -> Optional[int]:
        """
        O código do submercado ao qual a UTE pertence.

        :return: O código como `int`.
        """
        return self.data[1]

    @codigo_submercado.setter
    def codigo_submercado(self, c: int):
        self.data[1] = c

    @property
    def manutencao(self) -> Optional[List[float]]:
        """
        Os fatores de manutenção programada por estágio do
        estudo. A posição na lista indica a qual estágio
        ele está associada [e1, e2, e3, ...].

        :return: As manutenções.
        :type: list[float] | None
        """
        return [v for v in self.data[2::] if v is not None]

    @manutencao.setter
    def manutencao(self, m: List[float]):
        self.__atualiza_dados_lista(m, 2, 1)


class FD(Register):
    """
    Registro que contém os fatores de disponibilidade das UHEs.

    """

    __slots__ = []

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
            FloatField(5, 74, 3),
            FloatField(5, 79, 3),
            FloatField(5, 84, 3),
            FloatField(5, 89, 3),
            FloatField(5, 94, 3),
            FloatField(5, 99, 3),
            FloatField(5, 104, 3),
            FloatField(5, 109, 3),
            FloatField(5, 114, 3),
            FloatField(5, 119, 3),
            FloatField(5, 124, 3),
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
    def codigo_usina(self) -> Optional[int]:
        """
        O código da UHE associada aos fatores de disponibilidade.

        :return: O código como `int`.
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def frequencia(self) -> Optional[int]:
        """
        A frequência quando se trata da UHE Itaipu.

        :return: A frequência como `int`.
        """
        return self.data[1]

    @frequencia.setter
    def frequencia(self, c: int):
        self.data[1] = c

    @property
    def fator(self) -> Optional[List[float]]:
        """
        Os fatores de disponibilidade por estágio do
        estudo. A posição na lista indica a qual estágio
        ele está associada [e1, e2, e3, ...].

        :return: Os fatores.
        :type: list[float] | None
        """
        return [v for v in self.data[2::] if v is not None]

    @fator.setter
    def fator(self, m: List[float]):
        self.__atualiza_dados_lista(m, 2, 1)


class VE(Register):
    """
    Registro que contém os volumes de espera das UHEs.

    """

    __slots__ = []

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
            FloatField(5, 74, 2),
            FloatField(5, 79, 2),
            FloatField(5, 84, 2),
            FloatField(5, 89, 2),
            FloatField(5, 94, 2),
            FloatField(5, 99, 2),
            FloatField(5, 104, 2),
            FloatField(5, 109, 2),
            FloatField(5, 114, 2),
            FloatField(5, 119, 2),
            FloatField(5, 124, 2),
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
    def codigo_usina(self) -> Optional[int]:
        """
        O código da usina associada ao volume.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def volume(self) -> Optional[List[float]]:
        """
        O volume de espera por estagio.

        :return: O volume.
        :rtype: list[float] | None
        """
        return [v for v in self.data[1:] if v is not None]

    @volume.setter
    def volume(self, cus: List[float]):
        self.__atualiza_dados_lista(cus, 1, 1)


class RE(Register):
    """
    Registro que contém os cadastros de restrições elétricas.
    """

    __slots__ = []

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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código de cadastro para a restrição

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def estagio_inicial(self) -> Optional[int]:
        """
        O estágio inicial para consideração da restrição

        :return: O estágio.
        :rtype: int | None
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
        :rtype: int | None
        """
        return self.data[2]

    @estagio_final.setter
    def estagio_final(self, e: int):
        self.data[2] = e


class LU(Register):
    """
    Registro que contém os cadastros de limites das restrições elétricas.

    """

    __slots__ = []

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
            FloatField(10, 74, 1),
            FloatField(10, 84, 1),
            FloatField(10, 94, 1),
            FloatField(10, 104, 1),
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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição RE associada aos limites

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio inicial para consideração dos limites, até
        que sejam especificados novos limites.

        :return: O estágio.
        :rtype: int | None
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, e: int):
        self.data[1] = e

    @property
    def limite_inferior(self) -> Optional[List[float]]:
        """
        O limite inferior por patamar para a restrição elétrica

        :return: O limite
        :rtype: list[float] | None
        """
        return self.data[2::2]

    @limite_inferior.setter
    def limite_inferior(self, lim: List[float]):
        self.__atualiza_dados_lista(lim, 2, 2)

    @property
    def limite_superior(self) -> Optional[List[float]]:
        """
        O limite superior por patamar para a restrição elétrica

        :return: O limite
        :rtype: list[float] | None
        """
        return self.data[3::2]

    @limite_superior.setter
    def limite_superior(self, lim: List[float]):
        self.__atualiza_dados_lista(lim, 3, 2)


class FU(Register):
    """
    Registro que contém os coeficientes das usinas hidráulicas
    nas restrições elétricas.
    """

    __slots__ = []

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

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição elétrica, segundo registro RE.

        :return: O código como `int`.
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio associado.

        :return: O estágio como `int`.
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, c: int):
        self.data[1] = c

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O número da UHE conforme registro UH.

        :return: O número da UHE como `int`.
        """
        return self.data[2]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[2] = c

    @property
    def coeficiente(self) -> Optional[float]:
        """
        O coeficiente de participação da usina na restrição.

        :return: O coeficiente como `float`
        """
        return self.data[3]

    @coeficiente.setter
    def coeficiente(self, f: float):
        self.data[3] = f

    @property
    def frequencia(self) -> Optional[int]:
        """
        A frequência para restrição elétrica, valendo 50 ou 60
        para Itaipu e 0 para as demais.

        :return: O número da frequencia como `int`.
        """
        return self.data[4]

    @frequencia.setter
    def frequencia(self, c: int):
        self.data[4] = c


class FT(Register):
    """
    Registro que contém os coeficientes das usinas térmicas
    nas restrições elétricas.
    """

    __slots__ = []

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

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição elétrica, segundo registro RE.

        :return: O código como `int`.
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio associado.

        :return: O estágio como `int`.
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, c: int):
        self.data[1] = c

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O número da UTE conforme registro CT.

        :return: O número da UTE como `int`.
        """
        return self.data[2]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[2] = c

    @property
    def codigo_submercado(self) -> Optional[int]:
        """
        O código do submercado conforme registros CT ou TG.

        :return: O código do submercado como `int`.
        """
        return self.data[3]

    @codigo_submercado.setter
    def codigo_submercado(self, s: int):
        self.data[3] = s

    @property
    def coeficiente(self) -> Optional[float]:
        """
        O coeficiente de participação da usina na restrição.

        :return: O coeficiente como `float`
        """
        return self.data[4]

    @coeficiente.setter
    def coeficiente(self, f: float):
        self.data[4] = f


class FI(Register):
    """
    Registro que contém o sentido do fluxo da interligação
    entre os subsistemas associados à restrição elétrica.
    """

    __slots__ = []

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

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição elétrica, segundo registro RE.

        :return: O código como `int`.
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio associado.

        :return: O estágio como `int`.
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, c: int):
        self.data[1] = c

    @property
    def codigo_submercado_de(self) -> Optional[str]:
        """
        O submercado de origem conforme registros SB.

        :return: O submercado como `str`.
        """
        return self.data[2]

    @codigo_submercado_de.setter
    def codigo_submercado_de(self, s: str):
        self.data[2] = s

    @property
    def codigo_submercado_para(self) -> Optional[str]:
        """
        O submercado de destino conforme registros SB.

        :return: O  submercado como `str`.
        """
        return self.data[3]

    @codigo_submercado_para.setter
    def codigo_submercado_para(self, s: str):
        self.data[3] = s

    @property
    def coeficiente(self) -> Optional[float]:
        """
        O coeficiente de participação da interligação.

        :return: O coeficiente como `float`
        """
        return self.data[4]

    @coeficiente.setter
    def coeficiente(self, f: float):
        self.data[4] = f


class VI(Register):
    """
    Registro que contém os tempos de viagem da água entre usinas.
    """

    __slots__ = []

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
    def codigo_usina(self) -> Optional[int]:
        """
        O código da UHE a partir do qual é contabilizado
        o tempo de viagem.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def duracao(self) -> Optional[int]:
        """
        A duração da viagem da água (em horas) entre a UHE do
        código informado e sua usina à jusante segundo o hidr.

        :return: A duração
        :rtype: int | None
        """
        return self.data[1]

    @duracao.setter
    def duracao(self, d: int):
        self.data[1] = d

    @property
    def vazao(self) -> Optional[List[float]]:
        """
        As vazões defluentes das semanas passadas para a usina
        do código informado. A posição da vazão na lista indica
        a qual semana passada se refere [s-1, s-2, s-3, ...].

        :return: As vazões
        :rtype: list[float] | None
        """
        return [v for v in self.data[2::] if v is not None]

    @vazao.setter
    def vazao(self, v: List[float]):
        self.__atualiza_dados_lista(v, 2, 1)


class IR(Register):
    """
    Registro que contém as configurações de
    geração de relatórios de saída.
    """

    __slots__ = []

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
        :rtype: str | None
        """
        return self.data[0]

    @tipo.setter
    def tipo(self, t: str):
        self.data[0] = t


class CI(Register):
    """
    Registro que define contratos de importação de energia.
    """

    __slots__ = []

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

    __slots__ = []

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

    __slots__ = []

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
        :rtype: str | None
        """
        return self.data[0]

    @property
    def caminho(self) -> Optional[str]:
        """
        O caminho relativo ou completo para o arquivo da
        FCF.

        :return: O caminho.
        :rtype: str | None
        """
        return self.data[1]

    @caminho.setter
    def caminho(self, c: str):
        self.data[1] = c


class EA(Register):
    """
    Registro que a ENA dos meses que antecedem o estudo.
    """

    __slots__ = []

    IDENTIFIER = "EA  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            FloatField(10, 11, 2),
            FloatField(10, 21, 2),
            FloatField(10, 31, 2),
            FloatField(10, 41, 2),
            FloatField(10, 51, 2),
            FloatField(10, 61, 2),
            FloatField(10, 71, 2),
            FloatField(10, 81, 2),
            FloatField(10, 91, 2),
            FloatField(10, 101, 2),
            FloatField(10, 111, 2),
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
    def codigo_ree(self) -> Optional[int]:
        """
        O código do REE

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_ree.setter
    def codigo_ree(self, c: int):
        self.data[0] = c

    @property
    def ena(self) -> Optional[List[float]]:
        """
        A ENA passada para o REE.

        :return: O ena.
        :rtype: list[float] | None
        """
        return [v for v in self.data[1::] if v is not None]

    @ena.setter
    def ena(self, c: List[float]):
        self.__atualiza_dados_lista(c, 1, 1)
        self.data[1:] = c


class ES(Register):
    """
    Registro que define a ENA das semanas que antecedem o estudo.
    """

    __slots__ = []

    IDENTIFIER = "ES  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            IntegerField(1, 9),
            FloatField(10, 14, 2),
            FloatField(10, 24, 2),
            FloatField(10, 34, 2),
            FloatField(10, 44, 2),
            FloatField(10, 54, 2),
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
    def codigo_ree(self) -> Optional[int]:
        """
        O código do REE

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_ree.setter
    def codigo_ree(self, c: int):
        self.data[0] = c

    @property
    def numero_semanas_mes_anterior(self) -> Optional[int]:
        """
        O número de semanas do mês anterior

        :return: O número de semanas.
        :rtype: int | None
        """
        return self.data[1]

    @numero_semanas_mes_anterior.setter
    def numero_semanas_mes_anterior(self, c: int):
        self.data[1] = c

    @property
    def ena(self) -> Optional[List[float]]:
        """
        A ENA passada para o REE.

        :return: O ena.
        :rtype: list[float] | None
        """
        return [v for v in self.data[2::] if v is not None]

    @ena.setter
    def ena(self, c: List[float]):
        self.__atualiza_dados_lista(c, 1, 1)
        self.data[2:] = c


class QI(Register):
    """
    Registro que define o tempo de viagem para o cálculo da ENA.
    """

    __slots__ = []

    IDENTIFIER = "QI  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(5, 9, 1),
            FloatField(5, 14, 1),
            FloatField(5, 19, 1),
            FloatField(5, 24, 1),
            FloatField(5, 29, 1),
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
    def codigo_usina(self) -> Optional[int]:
        """
        O índice da UHE

        :return: O índice.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def vazao(self) -> Optional[List[float]]:
        """
        As vazões incrementais para cálculo da ENA.

        :return: As incrementais para cálculo da ENA.
        :rtype: list[float] | None
        """
        return [v for v in self.data[1::] if v is not None]

    @vazao.setter
    def vazao(self, c: List[float]):
        self.__atualiza_dados_lista(c, 1, 1)
        self.data[1:] = c


class RT(Register):
    """
    Registro utilizado para retirada de restrições de soleira de
    vertedouro e de canais de desvio.
    """

    __slots__ = []

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
        :rtype: str | None
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
            FloatField(5, 49, 2),
            FloatField(5, 54, 2),
            FloatField(5, 59, 2),
            FloatField(5, 64, 2),
            FloatField(5, 69, 2),
            FloatField(5, 74, 2),
            FloatField(5, 79, 2),
            FloatField(5, 84, 2),
            FloatField(5, 89, 2),
            FloatField(5, 94, 2),
            FloatField(5, 99, 2),
            FloatField(5, 104, 2),
            FloatField(5, 109, 2),
            FloatField(5, 114, 2),
            FloatField(5, 119, 2),
            FloatField(5, 124, 2),
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
    def codigo_usina(self) -> Optional[int]:
        """
        O código da UHE associada às taxas de irrigação

        :return: O código como `int`.
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def taxa(self) -> Optional[List[float]]:
        """
        As taxas de irrigação por estágio do estudo. A
        posição da taxa na lista indica a qual estágio
        ela está associada [e1, e2, e3, ...].

        :return: As taxas.
        :type: list[float] | None
        """
        return [v for v in self.data[1::] if v is not None]

    @taxa.setter
    def taxa(self, tx: List[float]):
        self.__atualiza_dados_lista(tx, 1, 1)


class DA(Register):
    """
    Registro que contém as retiradas de água para outros usos
    (desvios de água) por UHE.
    """

    __slots__ = []

    IDENTIFIER = "DA  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            IntegerField(3, 9),
            IntegerField(2, 13),
            FloatField(6, 16, 2),
            FloatField(4, 24, 1),
            FloatField(10, 34, 2),
        ]
    )

    @property
    def codigo_usina_retirada(self) -> Optional[int]:
        """
        O código da UHE a montante da qual será feita a retirada.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina_retirada.setter
    def codigo_usina_retirada(self, c: int):
        self.data[0] = c

    @property
    def codigo_usina_retorno(self) -> Optional[int]:
        """
        O código da UHE a montante da qual se derá o retorno.

        :return: O código
        :rtype: int | None
        """
        return self.data[1]

    @codigo_usina_retorno.setter
    def codigo_usina_retorno(self, c: int):
        self.data[1] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio associado à restrição DA.

        :return: O estágio
        :rtype: int | None
        """
        return self.data[2]

    @estagio.setter
    def estagio(self, c: int):
        self.data[2] = c

    @property
    def vazao_desviada(self) -> Optional[float]:
        """
        A vazão a ser desviada em m³/s.

        :return: A vazão
        :rtype: float | None
        """
        return self.data[3]

    @vazao_desviada.setter
    def vazao_desviada(self, c: float):
        self.data[3] = c

    @property
    def retorno_percentual(self) -> Optional[float]:
        """
        O retorno em percentual da vazão desviada.

        :return: O retorno percentual
        :rtype: float | None
        """
        return self.data[4]

    @retorno_percentual.setter
    def retorno_percentual(self, c: float):
        self.data[4] = c

    @property
    def custo(self) -> Optional[float]:
        """
        O custo de não antedimento do desvio em $/hm³.

        :return: O custo
        :rtype: float | None
        """
        return self.data[5]

    @custo.setter
    def custo(self, c: float):
        self.data[5] = c


class FP(Register):
    """
    Registro que contém os cadastros de restrições de alteração na
    função de produção das usinas.
    """

    __slots__ = []

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
    def codigo_usina(self) -> Optional[int]:
        """
        O código da UHE associada à restrição FP.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio associado à restrição FP.

        :return: O estágio
        :rtype: int | None
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
        :rtype: int | None
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
        :rtype: int | None
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
        :rtype: float | None
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
        :rtype: float | None
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
        :rtype: int | None
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
        :rtype: int | None
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
        :rtype: float | None
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
        :rtype: float | None
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

    __slots__ = []

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
    def codigo_ree(self) -> Optional[int]:
        """
        O código do REE associado às vazões mínimas.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_ree.setter
    def codigo_ree(self, r: int):
        self.data[0] = r

    @property
    def vazao(self) -> Optional[List[float]]:
        """
        As vazões defluentes mínimas (percentuais)
        para o REE, por estágio [e1, e2, e3, ...].

        :return: A vazão.
        :rtype: list[float] | None
        """
        return [v for v in self.data[1:] if v is not None]

    @vazao.setter
    def vazao(self, v: List[float]):
        self.__atualiza_dados_lista(v, 1, 1)
        self.data[1:] = v


class EZ(Register):
    """
    Registro que contém o percentual máximo do
    volume útil para acoplamento.
    """

    __slots__ = []

    IDENTIFIER = "EZ  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(3, 4),
            FloatField(5, 9, 2),
        ]
    )

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        Código da UHE associada, conforme registro UH.

        :return: O código da UHE.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def volume(self) -> Optional[float]:
        """
        O volume útil considerado para cálculo.

        :return: O volume útil em % do volume máximo.
        :rtype: float | None
        """
        return self.data[1]

    @volume.setter
    def volume(self, u: float):
        self.data[1] = u


class HV(Register):
    """
    Registro que contém os cadastros de restrições de volume armazenado.
    """

    __slots__ = []

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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição HV.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def estagio_inicial(self) -> Optional[int]:
        """
        O estágio inicial de consideração da restrição HV.

        :return: O estágio.
        :rtype: int | None
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
        :rtype: int | None
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

    __slots__ = []

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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição HV associada aos limites

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """'
        O estágio de consideração dos limites.

        :return: O estágio.
        :rtype: int | None
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
        :rtype: float | None
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
        :rtype: float | None
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

    __slots__ = []

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

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição de volume, segundo registro HV.

        :return: O código como `int`.
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio associado.

        :return: O estágio como `int`.
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, c: int):
        self.data[1] = c

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O número da UHE ou estação de bombeamento conforme registros UH ou UE.

        :return: O número da UHE como `int`.
        """
        return self.data[2]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[2] = c

    @property
    def coeficiente(self) -> Optional[float]:
        """
        O coeficiente da variável na restrição.

        :return: O coeficiente como `float`
        """
        return self.data[3]

    @coeficiente.setter
    def coeficiente(self, f: float):
        self.data[3] = f

    @property
    def tipo(self) -> Optional[str]:
        """
        O mnemônico de tipo da restrição.

        :return: O tipo como `str`.
        """
        return self.data[4]

    @tipo.setter
    def tipo(self, t: str):
        self.data[4] = t


class HQ(Register):
    """
    Registro que contém os cadastros de restrições de vazões.
    """

    __slots__ = []

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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição HQ.

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def estagio_inicial(self) -> Optional[int]:
        """
        O estágio inicial de consideração da restrição HQ.

        :return: O estágio.
        :rtype: int | None
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
        :rtype: int | None
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

    __slots__ = []

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
            FloatField(10, 74, 1),
            FloatField(10, 84, 1),
            FloatField(10, 94, 1),
            FloatField(10, 104, 1),
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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição HQ associada aos limites

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio de consideração dos limites.

        :return: O estágio.
        :rtype: int | None
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, e: int):
        self.data[1] = e

    @property
    def limite_inferior(self) -> Optional[List[float]]:
        """
        O limite inferior por patamar para a vazão.

        :return: Os limites.
        :rtype: list[float] | None
        """
        return self.data[2::2]

    @limite_inferior.setter
    def limite_inferior(self, lim: List[float]):
        self.__atualiza_dados_lista(lim, 2, 2)

    @property
    def limite_superior(self) -> Optional[List[float]]:
        """
        O limite superior por patamar para a vazão.

        :return: Os limites.
        :rtype: list[float] | None
        """
        return self.data[3::2]

    @limite_superior.setter
    def limite_superior(self, lim: List[float]):
        self.__atualiza_dados_lista(lim, 3, 2)


class CQ(Register):
    """
    Registro que contém os coeficientes das usinas hidráulicas
    nas restrições de vazão.
    """

    __slots__ = []

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

    @property
    def codigo_restricao(self) -> Optional[int]:
        """
        O código da restrição de vazão, segundo registro HQ.

        :return: O código como `int`.
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio associado.

        :return: O estágio como `int`.
        """
        return self.data[1]

    @estagio.setter
    def estagio(self, c: int):
        self.data[1] = c

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O número da UHE conforme registro UH.

        :return: O número da UHE como `int`.
        """
        return self.data[2]

    @codigo_usina.setter
    def codigo_usina(self, c: int):
        self.data[2] = c

    @property
    def coeficiente(self) -> Optional[float]:
        """
        O coeficiente da variável na restrição.

        :return: O coeficiente como `float`
        """
        return self.data[3]

    @coeficiente.setter
    def coeficiente(self, f: float):
        self.data[3] = f

    @property
    def tipo(self) -> Optional[str]:
        """
        O mnemônico de tipo da restrição.

        :return: O tipo como `str`.
        """
        return self.data[4]

    @tipo.setter
    def tipo(self, t: str):
        self.data[4] = t


class AR(Register):
    """
    Registro que contém as configurações de aversão a risco.
    """

    __slots__ = []

    IDENTIFIER = "AR  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [IntegerField(3, 5), FloatField(5, 11, 0), FloatField(5, 17, 0)]
    )

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio inicial de aplicação do CVaR.

        :return: O índice do estágio inicial.
        :rtype: int | None
        """
        return self.data[0]

    @estagio.setter
    def estagio(self, p: int):
        self.data[0] = p

    @property
    def lamb(self) -> Optional[float]:
        """
        O valor de lambda utilizado no CVaR.

        :return: O valor de lambda
        :rtype: float | None
        """
        return self.data[1]

    @lamb.setter
    def lamb(self, v: float):
        self.data[1] = v

    @property
    def alfa(self) -> Optional[float]:
        """
        O valor de alfa utilizado no CVaR.

        :return: O valor de alfa
        :rtype: float | None
        """
        return self.data[2]

    @alfa.setter
    def alfa(self, v: float):
        self.data[2] = v


class EV(Register):
    """
    Registro que contém as configurações de consideração
    da evaporação.
    """

    __slots__ = []

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
        :rtype: int | None
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
        :rtype: str | None
        """
        return self.data[1]

    @volume_referencia.setter
    def volume_referencia(self, v: str):
        self.data[1] = v


class FJ(Register):
    """
    Registro que contém o arquivo de polinômios de jusante.
    """

    __slots__ = []

    IDENTIFIER = "FJ  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            LiteralField(12, 4),
        ]
    )

    @property
    def arquivo(self) -> str:
        """
        O nome do arquivo.

        :return: O nome
        :rtype: str | None
        """
        return self.data[0]

    @arquivo.setter
    def arquivo(self, a: str):
        self.data[0] = a


class HE(Register):
    """
    Registro que contém o cadastro de uma restrição de energia
    armazenada.
    """

    __slots__ = []

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
    def codigo_restricao(self) -> Optional[int]:
        """
        O código de cadastro da restrição HE

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def tipo_limite(self) -> Optional[int]:
        """
        O tipo de limite especificado na restrição HE,
        em valor absoluto ou percentual.

        :return: O tipo.
        :rtype: int | None
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
        :rtype: float | None
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
        :rtype: int | None
        """
        return self.data[3]

    @estagio.setter
    def estagio(self, e: int):
        self.data[3] = e

    @property
    def valor_penalidade(self) -> Optional[float]:
        """
        O valor da penalidade para a violação da restrição.

        :return: O valor.
        :rtype: float | None
        """
        return self.data[4]

    @valor_penalidade.setter
    def valor_penalidade(self, p: float):
        self.data[4] = p

    @property
    def forma_calculo_produtibilidades(self) -> Optional[int]:
        """
        Flag para indicar a forma de cálculo das produtividades
        das usinas usadas nas restrição.

        :return: A flag.
        :rtype: int | None
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
        :rtype: int | None
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
        :rtype: int | None
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
        :rtype: str | None
        """
        return self.data[8]

    @arquivo_produtibilidades.setter
    def arquivo_produtibilidades(self, t: str):
        self.data[8] = t


class CM(Register):
    """
    Registro que contém os coeficientes de uma restrição RHE.
    """

    __slots__ = []

    IDENTIFIER = "CM  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [IntegerField(3, 4), IntegerField(3, 9), FloatField(10, 14, 2)]
    )

    @property
    def codigo_restricao(self) -> int:
        """
        O código de cadastro da restrição CM

        :return: O código.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_restricao.setter
    def codigo_restricao(self, c: int):
        self.data[0] = c

    @property
    def codigo_ree(self) -> int:
        """
        O REE do coeficiente

        :return: O REE.
        :rtype: int | None
        """
        return self.data[1]

    @codigo_ree.setter
    def codigo_ree(self, e: int):
        self.data[1] = e

    @property
    def coeficiente(self) -> float:
        """
        O coeficiente de energia considerado

        :return: O coeficiente.
        :rtype: float | None
        """
        return self.data[2]

    @coeficiente.setter
    def coeficiente(self, c: float):
        self.data[2] = c


class PD(Register):
    """
    Registro que contém a escolha do algoritmo para
    resolução do PL.
    """

    __slots__ = []

    IDENTIFIER = "PD  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            LiteralField(6, 4),
        ]
    )

    @property
    def algoritmo(self) -> Optional[str]:
        """
        O algoritmo considerado.

        :return: O identificador do algoritmo.
        :rtype: str | None
        """
        return self.data[0]

    @algoritmo.setter
    def algoritmo(self, m: str):
        self.data[0] = m


class PU(Register):
    """
    Registro que habilita a solução do problema
    via PL único.
    """

    __slots__ = []

    IDENTIFIER = "PU  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(1, 4),
        ]
    )

    @property
    def pl(self) -> Optional[int]:
        """
        O tipo de pl considerado.

        :return: O identificador do pl.
        :rtype: int | None
        """
        return self.data[0]

    @pl.setter
    def pl(self, m: int):
        self.data[0] = m


class RC(Register):
    """
    Registro que inclui restrições do tipo escada.
    """

    __slots__ = []

    IDENTIFIER = "RC  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            LiteralField(6, 4),
        ]
    )

    @property
    def mnemonico(self) -> Optional[str]:
        """
        O tipo de mnemonico considerado.

        :return: O identificador do mnemonico.
        :rtype: str | None
        """
        return self.data[0]

    @mnemonico.setter
    def mnemonico(self, m: str):
        self.data[0] = m


class PE(Register):
    """
    Registro que altera as penalidades de vertimento,
    intercâmbio e desvios.
    """

    __slots__ = []

    IDENTIFIER = "PE  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(2, 4),
            IntegerField(1, 7),
            FloatField(10, 9, 6),
        ]
    )

    @property
    def codigo_submercado(self) -> Optional[int]:
        """
        O código do submercado considerado

        :return: O código do submercado.
        :rtype: int | None
        """
        return self.data[0]

    @codigo_submercado.setter
    def codigo_submercado(self, m: int):
        self.data[0] = m

    @property
    def tipo(self) -> Optional[int]:
        """
        O tipo de penalidade a ser modificado

        :return: O indice do tipo de penalidade
        :rtype: int | None
        """
        return self.data[1]

    @tipo.setter
    def tipo(self, m: int):
        self.data[1] = m

    @property
    def penalidade(self) -> Optional[float]:
        """
        O novo valor de penalidade

        :return: O valor da penalidade
        :rtype: float | None
        """
        return self.data[2]

    @penalidade.setter
    def penalidade(self, m: float):
        self.data[2] = m


class TS(Register):
    """
    Registro que altera as tolerâncias do solver.
    """

    __slots__ = []

    IDENTIFIER = "TS  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            FloatField(17, 4, 15),
            FloatField(17, 22, 15),
            IntegerField(1, 42),
            FloatField(17, 22, 15),
        ]
    )

    @property
    def tolerancia_primaria(self) -> Optional[float]:
        """
        A nova tolerância primária do solver.

        :return: A tolerância
        :rtype: float | None
        """
        return self.data[0]

    @tolerancia_primaria.setter
    def tolerancia_primaria(self, m: float):
        self.data[0] = m

    @property
    def tolerancia_secundaria(self) -> Optional[float]:
        """
        A nova tolerância secundária do solver.

        :return: A tolerância
        :rtype: float | None
        """
        return self.data[1]

    @tolerancia_secundaria.setter
    def tolerancia_secundaria(self, m: float):
        self.data[1] = m

    @property
    def zera_coeficientes(self) -> Optional[int]:
        """
        Habilita ou não a funcionalidade de zerar coeficientes
        em casos de cortes não ótimos.

        :return: O valor do flag
        :rtype: int | None
        """
        return self.data[2]

    @zera_coeficientes.setter
    def zera_coeficientes(self, m: int):
        self.data[2] = m

    @property
    def tolerancia_teste_otimalidade(self) -> Optional[float]:
        """
        A nova tolerância usada no teste de otimalidade da
        solução do PL.

        :return: A tolerância
        :rtype: float | None
        """
        return self.data[3]

    @tolerancia_teste_otimalidade.setter
    def tolerancia_teste_otimalidade(self, m: float):
        self.data[3] = m


class PV(Register):
    """
    Registro que altera as penalidades das variáveis de folga
    do problema e as tolerâncias para a viabilidade das restrições.
    """

    __slots__ = []

    IDENTIFIER = "PV  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            FloatField(20, 5, 5),
            FloatField(20, 28, 5),
            IntegerField(3, 51),
            FloatField(3, 57, 1),
            FloatField(20, 63, 5),
            FloatField(20, 86, 5),
        ]
    )

    @property
    def penalidade_variaveis_folga(self) -> Optional[float]:
        """
        A nova penalidade para as variáveis de folga (R$/MWh).

        :return: A tolerância
        :rtype: float | None
        """
        return self.data[0]

    @penalidade_variaveis_folga.setter
    def penalidade_variaveis_folga(self, m: float):
        self.data[0] = m

    @property
    def tolerancia_viabilidade_restricoes(self) -> Optional[float]:
        """
        A nova tolerância para a viabilidade das restrições.

        :return: A tolerância
        :rtype: float | None
        """
        return self.data[1]

    @tolerancia_viabilidade_restricoes.setter
    def tolerancia_viabilidade_restricoes(self, m: float):
        self.data[1] = m

    @property
    def iteracoes_atualizacao_penalidade(self) -> Optional[int]:
        """
        O número de iterações para atualização da penalidade variável
        iterativa para as folgas.

        :return: O número de iterações
        :rtype: int | None
        """
        return self.data[2]

    @iteracoes_atualizacao_penalidade.setter
    def iteracoes_atualizacao_penalidade(self, m: int):
        self.data[2] = m

    @property
    def fator_multiplicacao_folga(self) -> Optional[float]:
        """
        O fator para multiplicação da folga ao longo das restrições.

        :return: A tolerância
        :rtype: float | None
        """
        return self.data[3]

    @fator_multiplicacao_folga.setter
    def fator_multiplicacao_folga(self, m: float):
        self.data[3] = m

    @property
    def valor_inicial_variaveis_folga(self) -> Optional[float]:
        """
        O valor inicial ou mínimo para as variáveis de folga.

        :return: O valor mínimo
        :rtype: float | None
        """
        return self.data[4]

    @valor_inicial_variaveis_folga.setter
    def valor_inicial_variaveis_folga(self, m: float):
        self.data[4] = m

    @property
    def valor_final_variaveis_folga(self) -> Optional[float]:
        """
        O valor final ou máximo para as variáveis de folga.

        :return: O valor máximo
        :rtype: float | None
        """
        return self.data[5]

    @valor_final_variaveis_folga.setter
    def valor_final_variaveis_folga(self, m: float):
        self.data[5] = m


class CX(Register):
    """
    Registro que mapeia o acoplamento de usinas que representam
    complexos no NEWAVE com o DECOMP.
    """

    __slots__ = []

    IDENTIFIER = "CX  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(4, 4),
            IntegerField(4, 9),
        ]
    )

    @property
    def codigo_newave(self) -> Optional[int]:
        """
        O código da usina no NEWAVE

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_newave.setter
    def codigo_newave(self, m: int):
        self.data[0] = m

    @property
    def codigo_decomp(self) -> Optional[int]:
        """
        O código da usina no DECOMP

        :return: O código
        :rtype: int | None
        """
        return self.data[1]

    @codigo_decomp.setter
    def codigo_decomp(self, m: int):
        self.data[1] = m


class FA(Register):
    """
    Registro que indica o nome do arquivo índice CSV.
    """

    __slots__ = []

    IDENTIFIER = "FA  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            LiteralField(50, 4),
        ]
    )

    @property
    def arquivo(self) -> Optional[str]:
        """
        O nome do arquivo índice CSV.

        :return: O nome do arquivo
        :rtype: str | None
        """
        return self.data[0]

    @arquivo.setter
    def arquivo(self, m: str):
        self.data[0] = m


class VT(Register):
    """
    Registro que indica o nome do arquivo com cenários de vento.
    """

    __slots__ = []

    IDENTIFIER = "VT  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            LiteralField(50, 4),
        ]
    )

    @property
    def arquivo(self) -> Optional[str]:
        """
        O nome do arquivo com cenários de vento.

        :return: O nome do arquivo
        :rtype: str | None
        """
        return self.data[0]

    @arquivo.setter
    def arquivo(self, m: str):
        self.data[0] = m


class CS(Register):
    """
    Registro que habilita a consistência de dados.
    """

    __slots__ = []

    IDENTIFIER = "CS  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(1, 4),
        ]
    )

    @property
    def consistencia(self) -> Optional[int]:
        """
        Habilita ou não a consistência de dados.

        :return: O nvalor do flag
        :rtype: int | None
        """
        return self.data[0]

    @consistencia.setter
    def consistencia(self, m: int):
        self.data[0] = m


class ACNUMPOS(Register):
    """
    Registro AC específico para alteração no número do posto.
    """

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def codigo_posto(self) -> Optional[int]:
        return self.data[1]

    @codigo_posto.setter
    def codigo_posto(self, u: int):
        self.data[1] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        """
        O número da UHE conforme registro UH.

        :return: O número da UHE como `int`.
        """
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def codigo_usina_jusante(self) -> Optional[int]:
        """
        O número da UHE de jusante conforme registro UH.

        :return: O número da UHE como `int`.
        """
        return self.data[1]

    @codigo_usina_jusante.setter
    def codigo_usina_jusante(self, u: int):
        self.data[1] = u

    @property
    def mes(self) -> Optional[str]:
        """
        O mês de validade da alteração de cadastro.

        :return: O mês como `str`.
        """
        return self.data[-3]

    @mes.setter
    def mes(self, m: str):
        self.data[-3] = m

    @property
    def semana(self) -> Optional[int]:
        """
        A semana de validade da alteração de cadastro.

        :return: A semana como `int`
        """
        return self.data[-2]

    @semana.setter
    def semana(self, s: int):
        self.data[-2] = s

    @property
    def ano(self) -> Optional[int]:
        """
        O ano de validade da alteração de cadastro.

        :return: O ano como `int`
        """
        return self.data[-1]

    @ano.setter
    def ano(self, m: int):
        self.data[-1] = m


class ACDESVIO(Register):
    """
    Registro AC específico para alteração na usina de jusante
    para canal de desvio e limite da vazão no canal.
    """

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def codigo_usina_jusante(self) -> Optional[int]:
        return self.data[1]

    @codigo_usina_jusante.setter
    def codigo_usina_jusante(self, u: int):
        self.data[1] = u

    @property
    def limite_vazao(self) -> Optional[float]:
        return self.data[2]

    @limite_vazao.setter
    def limite_vazao(self, u: float):
        self.data[2] = u

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

    __slots__ = []

    IDENTIFIER = r"AC  ([\d ]{1,3})  VOLMIN"
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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def volume(self) -> Optional[float]:
        return self.data[1]

    @volume.setter
    def volume(self, u: float):
        self.data[1] = u

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

    __slots__ = []

    IDENTIFIER = r"AC  ([\d ]{1,3})  VOLMAX"
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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def volume(self) -> Optional[float]:
        return self.data[1]

    @volume.setter
    def volume(self, u: float):
        self.data[1] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def ordem(self) -> Optional[int]:
        return self.data[1]

    @ordem.setter
    def ordem(self, u: int):
        self.data[1] = u

    @property
    def coeficiente(self) -> Optional[float]:
        return self.data[2]

    @coeficiente.setter
    def coeficiente(self, u: float):
        self.data[2] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def ordem(self) -> Optional[int]:
        return self.data[1]

    @ordem.setter
    def ordem(self, u: int):
        self.data[1] = u

    @property
    def coeficiente(self) -> Optional[float]:
        return self.data[2]

    @coeficiente.setter
    def coeficiente(self, u: float):
        self.data[2] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def produtibilidade(self) -> Optional[float]:
        return self.data[1]

    @produtibilidade.setter
    def produtibilidade(self, u: float):
        self.data[1] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def coeficiente(self) -> Optional[float]:
        return self.data[1]

    @coeficiente.setter
    def coeficiente(self, u: float):
        self.data[1] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def numero_curva(self) -> Optional[int]:
        return self.data[1]

    @numero_curva.setter
    def numero_curva(self, u: int):
        self.data[1] = u

    @property
    def nivel(self) -> Optional[float]:
        return self.data[2]

    @nivel.setter
    def nivel(self, u: float):
        self.data[2] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def indice_polimonio(self) -> Optional[int]:
        return self.data[1]

    @indice_polimonio.setter
    def indice_polimonio(self, u: int):
        self.data[1] = u

    @property
    def ordem(self) -> Optional[int]:
        return self.data[2]

    @ordem.setter
    def ordem(self, u: int):
        self.data[2] = u

    @property
    def coeficiente(self) -> Optional[float]:
        return self.data[3]

    @coeficiente.setter
    def coeficiente(self, u: float):
        self.data[3] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def mes_coeficiente(self) -> Optional[int]:
        return self.data[1]

    @mes_coeficiente.setter
    def mes_coeficiente(self, u: int):
        self.data[1] = u

    @property
    def coeficiente(self) -> Optional[int]:
        return self.data[2]

    @coeficiente.setter
    def coeficiente(self, u: int):
        self.data[2] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def numero_conjuntos(self) -> Optional[int]:
        return self.data[1]

    @numero_conjuntos.setter
    def numero_conjuntos(self, u: int):
        self.data[1] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def indice_conjunto(self) -> Optional[int]:
        return self.data[1]

    @indice_conjunto.setter
    def indice_conjunto(self, u: int):
        self.data[1] = u

    @property
    def numero_maquinas(self) -> Optional[int]:
        return self.data[2]

    @numero_maquinas.setter
    def numero_maquinas(self, u: int):
        self.data[2] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def indice_conjunto(self) -> Optional[int]:
        return self.data[1]

    @indice_conjunto.setter
    def indice_conjunto(self, u: int):
        self.data[1] = u

    @property
    def potencia(self) -> Optional[float]:
        return self.data[2]

    @potencia.setter
    def potencia(self, u: float):
        self.data[2] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def indice_conjunto(self) -> Optional[int]:
        return self.data[1]

    @indice_conjunto.setter
    def indice_conjunto(self, u: int):
        self.data[1] = u

    @property
    def vazao(self) -> Optional[int]:
        return self.data[2]

    @vazao.setter
    def vazao(self, u: int):
        self.data[2] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def cota(self) -> Optional[float]:
        return self.data[1]

    @cota.setter
    def cota(self, u: float):
        self.data[1] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def considera_influencia(self) -> Optional[int]:
        return self.data[1]

    @considera_influencia.setter
    def considera_influencia(self, u: int):
        self.data[1] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def vazao(self) -> Optional[int]:
        return self.data[1]

    @vazao.setter
    def vazao(self, u: int):
        self.data[1] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def tipo_perda(self) -> Optional[int]:
        return self.data[1]

    @tipo_perda.setter
    def tipo_perda(self, u: int):
        self.data[1] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def codigo_usina_jusante(self) -> Optional[int]:
        return self.data[1]

    @codigo_usina_jusante.setter
    def codigo_usina_jusante(self, u: int):
        self.data[1] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def volume(self) -> Optional[float]:
        return self.data[1]

    @volume.setter
    def volume(self, u: float):
        self.data[1] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def volume(self) -> Optional[float]:
        return self.data[1]

    @volume.setter
    def volume(self, u: float):
        self.data[1] = u

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

    __slots__ = []

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
    def write(self, file: IO, storage: str = "", *args, **kwargs) -> bool:
        line = self.__class__.LINE.write(self.data)
        line = (
            self.__class__.IDENTIFIER[:2]  # type: ignore
            + line[2:9]
            + self.__class__.IDENTIFIER[18:]
            + line[15:]
        )
        file.write(line)
        return True

    @property
    def codigo_usina(self) -> Optional[int]:
        return self.data[0]

    @codigo_usina.setter
    def codigo_usina(self, u: int):
        self.data[0] = u

    @property
    def codigo_posto(self) -> Optional[int]:
        return self.data[1]

    @codigo_posto.setter
    def codigo_posto(self, u: int):
        self.data[1] = u

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


class VL(Register):
    """
    Registro que define uma usina que sofre influência de vazão lateral
    na cota de jusante.
    """

    __slots__ = []

    IDENTIFIER = "VL  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(4, 4),
            FloatField(15, 10, 2),
            FloatField(
                size=15, starting_position=26, decimal_digits=9, format="E"
            ),
            FloatField(
                size=15, starting_position=42, decimal_digits=9, format="E"
            ),
            FloatField(
                size=15, starting_position=58, decimal_digits=9, format="E"
            ),
            FloatField(
                size=15, starting_position=74, decimal_digits=9, format="E"
            ),
            FloatField(
                size=15, starting_position=90, decimal_digits=9, format="E"
            ),
        ]
    )

    @property
    def codigo_usina_influenciada(self) -> Optional[int]:
        """
        O código da UHE influenciada.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina_influenciada.setter
    def codigo_usina_influenciada(self, c: int):
        self.data[0] = c

    @property
    def fator_impacto_defluencia(self) -> Optional[float]:
        """
        O fator de impacto referente a defluência da usina influenciada.

        :return: O fator da defluência
        :rtype: float | None
        """
        return self.data[1]

    @fator_impacto_defluencia.setter
    def fator_impacto_defluencia(self, c: float):
        self.data[1] = c

    @property
    def coeficiente_a0(self) -> Optional[float]:
        """
        O coeficiente de grau 0 do polinômio de jusante.

        :return: O coeficiente de grau 0 do polinômio
        :rtype: float | None
        """
        return self.data[2]

    @coeficiente_a0.setter
    def coeficiente_a0(self, c: float):
        self.data[2] = c

    @property
    def coeficiente_a1(self) -> Optional[float]:
        """
        O coeficiente de grau 1 do polinômio de jusante.

        :return: O coeficiente de grau 1 do polinômio
        :rtype: float | None
        """
        return self.data[3]

    @coeficiente_a1.setter
    def coeficiente_a1(self, c: float):
        self.data[3] = c

    @property
    def coeficiente_a2(self) -> Optional[float]:
        """
        O coeficiente de grau 2 do polinômio de jusante.

        :return: O coeficiente de grau 2 do polinômio
        :rtype: float | None
        """
        return self.data[4]

    @coeficiente_a2.setter
    def coeficiente_a2(self, c: float):
        self.data[4] = c

    @property
    def coeficiente_a3(self) -> Optional[float]:
        """
        O coeficiente de grau 3 do polinômio de jusante.

        :return: O coeficiente de grau 3 do polinômio
        :rtype: float | None
        """
        return self.data[5]

    @coeficiente_a3.setter
    def coeficiente_a3(self, c: float):
        self.data[5] = c

    @property
    def coeficiente_a4(self) -> Optional[float]:
        """
        O coeficiente de grau 4 do polinômio de jusante.

        :return: O coeficiente de grau 4 do polinômio
        :rtype: float | None
        """
        return self.data[6]

    @coeficiente_a4.setter
    def coeficiente_a4(self, c: float):
        self.data[6] = c


class VU(Register):
    """
    Registro que define uma usina que tem influência sobre a vazão de
    jusante da primeira.
    """

    __slots__ = []

    IDENTIFIER = "VU  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(4, 4),
            IntegerField(4, 10),
            FloatField(15, 16, 2),
        ]
    )

    @property
    def codigo_usina_influenciada(self) -> Optional[int]:
        """
        O código da UHE influenciada.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina_influenciada.setter
    def codigo_usina_influenciada(self, c: int):
        self.data[0] = c

    @property
    def codigo_usina_influenciadora(self) -> Optional[int]:
        """
        O código da UHE cuja vazão defluente influencia
        lateralmente.

        :return: O código
        :rtype: int | None
        """
        return self.data[1]

    @codigo_usina_influenciadora.setter
    def codigo_usina_influenciadora(self, c: int):
        self.data[1] = c

    @property
    def fator_impacto_defluencia(self) -> Optional[float]:
        """
        O fator de impacto referente a defluência da usina influenciadora.

        :return: O fator da defluência
        :rtype: float | None
        """
        return self.data[2]

    @fator_impacto_defluencia.setter
    def fator_impacto_defluencia(self, c: float):
        self.data[2] = c


class VA(Register):
    """
    Registro que define um posto de vazão que tem influência sobre a vazão de
    jusante da primeira.
    """

    __slots__ = []

    IDENTIFIER = "VA  "
    IDENTIFIER_DIGITS = 4
    LINE = Line(
        [
            IntegerField(4, 4),
            IntegerField(4, 10),
            FloatField(15, 16, 2),
        ]
    )

    @property
    def codigo_usina_influenciada(self) -> Optional[int]:
        """
        O código da UHE influenciada.

        :return: O código
        :rtype: int | None
        """
        return self.data[0]

    @codigo_usina_influenciada.setter
    def codigo_usina_influenciada(self, c: int):
        self.data[0] = c

    @property
    def codigo_posto_influenciador(self) -> Optional[int]:
        """
        O código do posto cuja vazão incremental influencia
        lateralmente.

        :return: O código
        :rtype: int | None
        """
        return self.data[1]

    @codigo_posto_influenciador.setter
    def codigo_posto_influenciador(self, c: int):
        self.data[1] = c

    @property
    def fator_impacto_incremental(self) -> Optional[float]:
        """
        O fator de impacto referente a incremental do posto influenciador.

        :return: O fator da vazão incremental
        :rtype: float | None
        """
        return self.data[2]

    @fator_impacto_incremental.setter
    def fator_impacto_incremental(self, c: float):
        self.data[2] = c
