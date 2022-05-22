from cfinterface.components.register import Register
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField

from typing import Optional, List


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
            FloatField(10, 59, 2),
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

    @property
    def codigo(self) -> Optional[int]:
        """
        O código de cadastro da UTE.

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @property
    def subsistema(self) -> Optional[int]:
        """
        O subsistema de cadastro da UTE.

        :return: O subsistema.
        :rtype: Optional[int]
        """
        return self.data[1]

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

    @property
    def inflexibilidades(self) -> Optional[List[float]]:
        """
        As inflexibilidades da UTE por patamar.

        :return: As inflexibilidades.
        :rtype: Optional[list[float]]
        """
        return self.data[4::3]

    @inflexibilidades.setter
    def inflexibilidades(self, inflex: List[float]):
        novas = len(inflex)
        atuais = len(self.inflexibilidades)
        if novas != atuais:
            raise ValueError(
                "Número de inflexibilidades incompatível. De"
                + f"vem ser fornecidas {atuais}, mas foram {novas}"
            )
        self.data[4::3] = inflex

    @property
    def disponibilidades(self) -> Optional[List[float]]:
        """
        As disponibilidades da UTE por patamar.

        :return: As disponibilidades.
        :rtype: Optional[list[float]]
        """
        return self.data[5::3]

    @disponibilidades.setter
    def disponibilidades(self, disp: List[float]):
        novas = len(disp)
        atuais = len(self.disponibilidades)
        if novas != atuais:
            raise ValueError(
                "Número de disponibilidades incompatível. De"
                + f"vem ser fornecidas {atuais}, mas foram {novas}"
            )
        self.data[5::3] = disp

    @property
    def cvus(self) -> Optional[List[float]]:
        """
        Os CVUs da UTE por patamar.

        :return: Os CVUs.
        :rtype: Optional[list[float]]
        """
        return self.data[6::3]

    @cvus.setter
    def cvus(self, cvu: List[float]):
        novas = len(cvu)
        atuais = len(self.cvus)
        if novas != atuais:
            raise ValueError(
                "Número de CVUs incompatível. De"
                + f"vem ser fornecidas {atuais}, mas foram {novas}"
            )
        self.data[6::3] = cvu


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

    @property
    def estagio(self) -> Optional[int]:
        """
        O estágio associado às durações especificadas.

        :return: O estágio.
        :rtype: Optional[int]
        """
        return self.data[0]

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

    @property
    def cargas(self) -> Optional[List[float]]:
        """
        As cargas em Mwmed pata cada patamar de carga

        :return: As cargas.
        :rtype: Optional[list[float]]
        """
        return self.data[3::2]

    @cargas.setter
    def cargas(self, c: List[float]):
        novas = len(c)
        atuais = len(self.cargas)
        if novas != atuais:
            raise ValueError(
                "Número de cargas incompatível. De"
                + f"vem ser fornecidas {atuais}, mas foram {novas}"
            )
        self.data[3::2] = c

    @property
    def duracoes(self) -> Optional[List[float]]:
        """
        As durações de cada patamar de carga em horas

        :return: As durações em horas.
        :rtype: Optional[list[float]]
        """
        return self.data[4::2]

    @duracoes.setter
    def duracoes(self, d: List[float]):
        novas = len(d)
        atuais = len(self.duracoes)
        if novas != atuais:
            raise ValueError(
                "Número de durações incompatível. De"
                + f"vem ser fornecidas {atuais}, mas foram {novas}"
            )
        self.data[4::2] = d


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
        return self.data[4::2]

    @limites_superiores.setter
    def limites_superiores(self, lim: List[float]):
        novos = len(lim)
        atuais = len(self.limites_superiores)
        if novos != atuais:
            raise ValueError(
                "Número de limites incompatível. De"
                + f"vem ser fornecidos {atuais}, mas foram {novos}"
            )
        self.data[4::2] = lim

    @property
    def custos(self) -> Optional[List[float]]:
        return self.data[5::2]

    @custos.setter
    def custos(self, cus: List[float]):
        novos = len(cus)
        atuais = len(self.custos)
        if novos != atuais:
            raise ValueError(
                "Número de custos incompatível. De"
                + f"vem ser fornecidos {atuais}, mas foram {novos}"
            )
        self.data[5::2] = cus


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
            FloatField(5, 16, 0),
            FloatField(5, 21, 0),
            FloatField(5, 26, 0),
            FloatField(5, 31, 0),
            FloatField(5, 36, 0),
            FloatField(5, 41, 0),
            FloatField(5, 46, 0),
            FloatField(5, 51, 0),
            FloatField(5, 56, 0),
            FloatField(5, 61, 0),
            FloatField(5, 66, 0),
            FloatField(5, 71, 0),
            FloatField(5, 76, 0),
            FloatField(5, 81, 0),
            FloatField(5, 86, 0),
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
            IntegerField(2, 9),
            IntegerField(2, 14),
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
            FloatField(5, 12, 3),
            FloatField(5, 15, 3),
            FloatField(5, 18, 3),
            FloatField(5, 21, 3),
            FloatField(5, 24, 3),
            FloatField(5, 27, 3),
            FloatField(5, 30, 3),
            FloatField(5, 33, 3),
            FloatField(5, 36, 3),
            FloatField(5, 39, 3),
            FloatField(5, 42, 3),
            FloatField(5, 45, 3),
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
    Registro que contém as manutenções programadas das UTEs.
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

    @property
    def codigo(self) -> Optional[int]:
        """
        O código do posto associado ao volume.

        :return: O código.
        :rtype: Optional[int]
        """
        return self.data[0]

    @property
    def volumes(self) -> Optional[List[float]]:
        """
        Os volumes de espera por estagio.

        :return: Os volumes.
        :rtype: Optional[List[float]]
        """
        return self.data[1:]

    @volumes.setter
    def volumes(self, cus: List[float]):
        novos = len(cus)
        atuais = len(self.volumes)
        if novos != atuais:
            raise ValueError(
                "Número de volumes incompatível. De"
                + f"vem ser fornecidos {atuais}, mas foram {novos}"
            )
        self.data[1:] = cus


from typing import IO, List, Type
from idecomp._utils.utils import formata_numero
from idecomp._utils.registros import RegistroAn, RegistroFn, RegistroIn
from idecomp._utils.registrodecomp import RegistroDecomp
from idecomp._utils.registrodecomp import TipoRegistroAC
from idecomp._utils.leituraregistros import LeituraRegistros


class RE(RegistroDecomp):
    """
    Registro que contém os cadastros de restrições elétricas.
    """

    mnemonico = "RE"

    def __init__(self):
        super().__init__(RE.mnemonico, True)
        self._dados = [0, 0, 0]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_estagio = RegistroIn(2)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        self._dados[2] = reg_estagio.le_registro(self._linha, 14)

    def escreve(self, arq: IO):
        linha = (
            f"{RE.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(2)
            + "   "
            + f"{self._dados[2]}".rjust(2)
            + "\n"
        )
        arq.write(linha)

    @property
    def codigo(self) -> int:
        """
        O código de cadastro para a restrição

        :return: O código como `int`.
        """
        return self._dados[0]

    @property
    def estagio_inicial(self) -> int:
        """
        O estágio inicial para consideração da restrição

        :return: O estágio como `int`.
        """
        return self._dados[1]

    @property
    def estagio_final(self) -> int:
        """
        O estágio final para consideração da restrição

        :return: O estágio como `int`.
        """
        return self._dados[2]


class LU(RegistroDecomp):
    """
    Registro que contém os cadastros de restrições elétricas.
    """

    mnemonico = "LU"
    default = 1e21

    def __init__(self):
        super().__init__(LU.mnemonico, True)
        self._dados = [0, 0] + [LU.default] * 6

    def le(self):
        reg_cod = RegistroIn(3)
        reg_estagio = RegistroIn(2)
        reg_limite = RegistroFn(10)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        ci = 14
        for i in range(2, len(self._dados)):
            cf = ci + 10
            if len(self._linha[ci:cf].strip()) != 0:
                self._dados[i] = reg_limite.le_registro(self._linha, ci)
            ci = cf

    def escreve(self, arq: IO):
        linha = (
            f"{LU.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(2)
            + "   "
        )
        for i in range(2, len(self._dados)):
            if self._dados[i] != LU.default:
                linha += f"{round(self._dados[i], 2)}".rjust(10)
            else:
                linha += "          "

        arq.write(linha + "\n")

    @property
    def codigo(self) -> int:
        """
        O código da restrição RE associada aos limites

        :return: O código como `int`.
        """
        return self._dados[0]

    @property
    def estagio(self) -> int:
        """
        O estágio inicial para consideração dos limites, até
        que sejam especificados novos limites.

        :return: O estágio como `int`.
        """
        return self._dados[1]

    @estagio.setter
    def estagio(self, e: int):
        self._dados[1] = e

    @property
    def limites_inferiores(self) -> List[float]:
        """
        Os limites inferiores por patamar para a restrição elétrica

        :return: Os limites como `list[float]`
        """
        return self._dados[2::2]

    @limites_inferiores.setter
    def limites_inferiores(self, lim: List[float]):
        novos = len(lim)
        atuais = len(self.limites_inferiores)
        if novos != atuais:
            raise ValueError(
                "Número de limites incompatível. De"
                + f"vem ser fornecidos {atuais}, mas foram {novos}"
            )
        self._dados[2::2] = lim

    @property
    def limites_superiores(self) -> List[float]:
        """
        Os limites superiores por patamar para a restrição elétrica

        :return: Os limites como `list[float]`
        """
        return self._dados[3::2]

    @limites_superiores.setter
    def limites_superiores(self, lim: List[float]):
        novos = len(lim)
        atuais = len(self.limites_superiores)
        if novos != atuais:
            raise ValueError(
                "Número de limites incompatível. De"
                + f"vem ser fornecidos {atuais}, mas foram {novos}"
            )
        self._dados[3::2] = lim


class FU(RegistroDecomp):
    """
    Registro que contém os coeficientes das usinas hidráulicas
    nas restrições elétricas.
    """

    mnemonico = "FU"

    def __init__(self):
        super().__init__(FU.mnemonico, True)
        self._dados = [0, 0, 0, 0.0, 0]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_estagio = RegistroIn(2)
        reg_uhe = RegistroIn(3)
        reg_fator = RegistroFn(10)
        reg_freq = RegistroIn(2)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        self._dados[2] = reg_uhe.le_registro(self._linha, 14)
        self._dados[3] = reg_fator.le_registro(self._linha, 19)
        if self._linha[30:32].strip().isnumeric():
            self._dados[4] = reg_freq.le_registro(self._linha, 30)

    def escreve(self, arq: IO):
        linha = (
            f"{FU.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(2)
            + "   "
            + f"{self._dados[2]}".rjust(3)
            + "  "
            + f"{round(self._dados[3], 2)}".rjust(10)
        )
        if self._dados[4] != 0:
            linha += f" {self._dados[4]}"
        linha += "\n"
        arq.write(linha)


class FT(RegistroDecomp):
    """
    Registro que contém os coeficientes das usinas térmicas
    nas restrições elétricas.
    """

    mnemonico = "FT"

    def __init__(self):
        super().__init__(FT.mnemonico, True)
        self._dados = [0, 0, 0, 0, 0.0]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_estagio = RegistroIn(2)
        reg_ute = RegistroIn(3)
        reg_subsis = RegistroIn(2)
        reg_fator = RegistroFn(10)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        self._dados[2] = reg_ute.le_registro(self._linha, 14)
        self._dados[3] = reg_subsis.le_registro(self._linha, 19)
        self._dados[4] = reg_fator.le_registro(self._linha, 24)

    def escreve(self, arq: IO):
        linha = (
            f"{FT.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(2)
            + "   "
            + f"{self._dados[2]}".rjust(3)
            + "  "
            + f"{self._dados[3]}".rjust(2)
            + "   "
            + f"{round(self._dados[4], 2)}".rjust(10)
        )
        linha += "\n"
        arq.write(linha)


class FI(RegistroDecomp):
    """
    Registro que contém o sentido do fluxo da interligação
    entre os subsistemas associados à restrição elétrica.
    """

    mnemonico = "FI"

    def __init__(self):
        super().__init__(FI.mnemonico, True)
        self._dados = [0, 0, "", "", 0.0]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_estagio = RegistroIn(2)
        reg_subsis = RegistroAn(2)
        reg_fator = RegistroFn(10)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        self._dados[2] = reg_subsis.le_registro(self._linha, 14)
        self._dados[3] = reg_subsis.le_registro(self._linha, 19)
        self._dados[4] = reg_fator.le_registro(self._linha, 24)

    def escreve(self, arq: IO):
        linha = (
            f"{FI.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(2)
            + "   "
            + f"{self._dados[2]}".rjust(2)
            + "   "
            + f"{self._dados[3]}".rjust(2)
            + "   "
            + f"{round(self._dados[4], 2)}".rjust(10)
        )
        linha += "\n"
        arq.write(linha)


class VI(RegistroDecomp):
    """
    Registro que contém os tempos de viagem da água entre usinas.
    """

    mnemonico = "VI"

    def __init__(self):
        super().__init__(VI.mnemonico, True)
        self._dados = [0, 0]

    def le(self):
        reg_usi = RegistroIn(3)
        reg_dur = RegistroIn(3)
        reg_tempo = RegistroFn(5)
        self._dados[0] = reg_usi.le_registro(self._linha, 4)
        self._dados[1] = reg_dur.le_registro(self._linha, 9)
        ci = 14
        for i in range(24):
            cf = ci + 5
            if len(self._linha[ci:cf].strip()) == 0:
                break
            self._dados.append(reg_tempo.le_registro(self._linha, ci))
            ci = cf

    def escreve(self, arq: IO):
        linha = (
            f"{VI.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(3)
            + "  "
        )
        for i in range(2, len(self._dados)):
            a_escrever = f"{round(self._dados[i], 2)}".rjust(5)
            if len(a_escrever) > 5:
                a_escrever = f"{round(self._dados[i], 1)}".rjust(5)
            if len(a_escrever) > 5:
                a_escrever = f"{int(self._dados[i])}".rjust(5)
            linha += a_escrever
        linha += "\n"
        arq.write(linha)

    @property
    def uhe(self) -> int:
        """
        O código da UHE a partir do qual é contabilizado
        o tempo de viagem.

        :return: O código como `int`
        """
        return self._dados[0]

    @property
    def duracao(self) -> int:
        """
        A duração da viagem da água (em horas) entre a UHE do
        código informado e sua usina à jusante segundo o hidr.

        :return: A duração como `int`
        """
        return self._dados[1]

    @duracao.setter
    def duracao(self, d: int):
        self._dados[1] = d

    @property
    def vazoes(self) -> List[float]:
        """
        As vazões defluentes das semanas passadas para a usina
        do código informado. A posição da vazão na lista indica
        a qual semana passada se refere [s-1, s-2, s-3, ...].

        :return: A duração como `int`
        """
        return self._dados[2:]

    @vazoes.setter
    def vazoes(self, v: List[float]):
        novos = len(v)
        atuais = len(self.vazoes)
        if novos != atuais:
            raise ValueError(
                "Número de vazões incompatível. De"
                + f"vem ser fornecidos {atuais}, mas foram {novos}"
            )
        self._dados[2:] = v


class ACNUMPOS(TipoRegistroAC):
    """
    Registro AC específico para alteração no número do posto.
    """

    mnemonico = "NUMPOS"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0

    def le(self):
        reg_usi = RegistroIn(5)
        self._dados = reg_usi.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados}".rjust(5)
        return linha


class ACNUMJUS(TipoRegistroAC):
    """
    Registro AC específico para alteração na usina de jusante.
    """

    mnemonico = "NUMJUS"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0

    def le(self):
        reg_usi = RegistroIn(5)
        self._dados = reg_usi.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados}".rjust(5)
        return linha


class ACDESVIO(TipoRegistroAC):
    """
    Registro AC específico para alteração na usina de jusante
    para canal de desvio e limite da vazão no canal.
    """

    mnemonico = "DESVIO"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = [0, 0.0]

    def le(self):
        reg_usi = RegistroIn(5)
        reg_desvio = RegistroFn(10)
        self._dados[0] = reg_usi.le_registro(self._linha, 19)
        self._dados[1] = reg_desvio.le_registro(self._linha, 24)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados[0]}".rjust(
            5
        ) + f"{round(self._dados[1], 2)}".rjust(10)
        return linha


class ACVOLMIN(TipoRegistroAC):
    """
    Registro AC específico para alteração na usina de jusante
    para canal de desvio e limite da vazão no canal.
    """

    mnemonico = "VOLMIN"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0.0

    def le(self):
        reg_desvio = RegistroFn(10)
        self._dados = reg_desvio.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{round(self._dados, 2)}".rjust(10)
        return linha


class ACVOLMAX(TipoRegistroAC):
    """
    Registro AC específico para alteração na usina de jusante
    para canal de desvio e limite da vazão no canal.
    """

    mnemonico = "VOLMAX"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0.0

    def le(self):
        reg_desvio = RegistroFn(10)
        self._dados = reg_desvio.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{round(self._dados, 2)}".rjust(10)
        return linha


class ACCOTVOL(TipoRegistroAC):
    """
    Registro AC específico para alteração de um coeficiente do
    polinômio cota-volume.
    """

    mnemonico = "COTVOL"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = [0, 0.0]

    def le(self):
        reg_indice = RegistroIn(5)
        reg_coef = RegistroFn(15)
        self._dados[0] = reg_indice.le_registro(self._linha, 19)
        self._dados[1] = reg_coef.le_registro(self._linha, 24)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados[0]}".rjust(
            5
        ) + f"{round(self._dados[1], 3)}".rjust(15)
        return linha


class ACCOTARE(TipoRegistroAC):
    """
    Registro AC específico para alteração de um coeficiente do
    polinômio cota-área.
    """

    mnemonico = "COTARE"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = [0, 0.0]

    def le(self):
        reg_indice = RegistroIn(5)
        reg_coef = RegistroFn(15)
        self._dados[0] = reg_indice.le_registro(self._linha, 19)
        self._dados[1] = reg_coef.le_registro(self._linha, 24)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados[0]}".rjust(
            5
        ) + f"{round(self._dados[1], 3)}".rjust(15)
        return linha


class ACPROESP(TipoRegistroAC):
    """
    Registro AC específico para alteração do coeficiente de perdas
    hidráulicas em função da queda bruta (%,m,k).
    """

    mnemonico = "PROESP"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0.0

    def le(self):
        reg_desvio = RegistroFn(10)
        self._dados = reg_desvio.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{round(self._dados, 2)}".rjust(10)
        return linha


class ACPERHID(TipoRegistroAC):
    """
    Registro AC específico para alteração do coeficiente de perdas
    hidráulicas em função da queda bruta (%,m,k).
    """

    mnemonico = "PERHID"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0.0

    def le(self):
        reg_desvio = RegistroFn(10)
        self._dados = reg_desvio.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{round(self._dados, 2)}".rjust(10)
        return linha


class ACNCHAVE(TipoRegistroAC):
    """
    Registro AC específico para alteração do número da curva-chave
    (cota-vazão) e nível de jusante da faixa associada (m).
    """

    mnemonico = "NCHAVE"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = [0, 0.0]

    def le(self):
        reg_usi = RegistroIn(5)
        reg_desvio = RegistroFn(10)
        self._dados[0] = reg_usi.le_registro(self._linha, 19)
        self._dados[1] = reg_desvio.le_registro(self._linha, 24)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados[0]}".rjust(
            5
        ) + f"{round(self._dados[1], 1)}".rjust(10)
        return linha


class ACCOTVAZ(TipoRegistroAC):
    """
    Registro AC específico para alteração de um coeficiente do
    polinômio cota-vazão.
    """

    mnemonico = "COTVAZ"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = [0, 0, 0.0]

    def le(self):
        reg_indice = RegistroIn(5)
        reg_coef = RegistroFn(15)
        self._dados[0] = reg_indice.le_registro(self._linha, 19)
        self._dados[1] = reg_indice.le_registro(self._linha, 24)
        self._dados[2] = reg_coef.le_registro(self._linha, 29)

    @property
    def linha_escrita(self) -> str:
        linha = (
            f"{self._dados[0]}".rjust(5)
            + f"{self._dados[1]}".rjust(5)
            + f"{round(self._dados[2], 3)}".rjust(15)
        )
        return linha


class ACCOFEVA(TipoRegistroAC):
    """
    Registro AC específico para alteração do coeficiente de evaporação
    mensal para cada mês.
    """

    mnemonico = "COFEVA"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = [0, 0]

    def le(self):
        reg_mes = RegistroIn(5)
        self._dados = reg_mes.le_linha_tabela(self._linha, 19, 0, 2)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados[0]}".rjust(5) + f"{self._dados[1]}".rjust(5)
        return linha


class ACNUMCON(TipoRegistroAC):
    """
    Registro AC específico para alteração no número de conjuntos
    de máquinas.
    """

    mnemonico = "NUMCON"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0

    def le(self):
        reg_usi = RegistroIn(5)
        self._dados = reg_usi.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados}".rjust(5)
        return linha


class ACNUMMAQ(TipoRegistroAC):
    """
    Registro AC específico para alteração do número de máquinas
    em cada conjunto de máquinas.
    """

    mnemonico = "NUMMAQ"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = [0, 0]

    def le(self):
        reg_mes = RegistroIn(5)
        self._dados = reg_mes.le_linha_tabela(self._linha, 19, 0, 2)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados[0]}".rjust(5) + f"{self._dados[1]}".rjust(5)
        return linha


class ACPOTEFE(TipoRegistroAC):
    """
    Registro AC específico para alteração da potência efetiva
    por unidade geradora em um conjunto de máquinas.
    """

    mnemonico = "POTEFE"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = [0, 0.0]

    def le(self):
        reg_usi = RegistroIn(5)
        reg_desvio = RegistroFn(10)
        self._dados[0] = reg_usi.le_registro(self._linha, 19)
        self._dados[1] = reg_desvio.le_registro(self._linha, 24)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados[0]}".rjust(
            5
        ) + f"{round(self._dados[1], 1)}".rjust(10)
        return linha


class ACALTEFE(TipoRegistroAC):
    """
    Registro AC específico para alteração da altura efetiva
    de queda para um conjunto de máquinas.
    """

    mnemonico = "ALTEFE"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = [0, 0.0]

    def le(self):
        reg_usi = RegistroIn(5)
        reg_desvio = RegistroFn(10)
        self._dados[0] = reg_usi.le_registro(self._linha, 19)
        self._dados[1] = reg_desvio.le_registro(self._linha, 24)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados[0]}".rjust(
            5
        ) + f"{round(self._dados[1], 1)}".rjust(10)
        return linha


class ACVAZEFE(TipoRegistroAC):
    """
    Registro AC específico para alteração da vazão efetiva
    para um conjunto de máquinas.
    """

    mnemonico = "VAZEFE"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = [0, 0]

    def le(self):
        reg_usi = RegistroIn(5)
        reg_vaz = RegistroIn(5)
        self._dados[0] = reg_usi.le_registro(self._linha, 19)
        self._dados[1] = reg_vaz.le_registro(self._linha, 24)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados[0]}".rjust(5) + f"{self._dados[1]}".rjust(5)
        return linha


class ACJUSMED(TipoRegistroAC):
    """
    Registro AC específico para alteração da cota média do canal
    de fuga em metros.
    """

    mnemonico = "JUSMED"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0.0

    def le(self):
        reg_desvio = RegistroFn(10)
        self._dados = reg_desvio.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{round(self._dados, 2)}".rjust(10)
        return linha


class ACVERTJU(TipoRegistroAC):
    """
    Registro AC específico para alteração da influência do vertimento
    na cota do canal de fuga.
    """

    mnemonico = "VERTJU"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0

    def le(self):
        reg_usi = RegistroIn(5)
        self._dados = reg_usi.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados}".rjust(5)
        return linha


class ACVAZMIN(TipoRegistroAC):
    """
    Registro AC específico para alteração da vazão mínima histórica.
    """

    mnemonico = "VAZMIN"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = -1

    def le(self):
        reg_usi = RegistroIn(5)
        if len(self._linha[19:24].strip()) > 0:
            self._dados = reg_usi.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        if self._dados != -1:
            linha = f"{self._dados}".rjust(5)
        else:
            linha = "".rjust(5)
        return linha


class ACTIPERH(TipoRegistroAC):
    """
    Registro AC específico para alteração do tipo de perdas hidráulicas.
    """

    mnemonico = "TIPERH"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = -1

    def le(self):
        reg_usi = RegistroIn(5)
        if len(self._linha[19:24].strip()) > 0:
            self._dados = reg_usi.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        if self._dados != -1:
            linha = f"{self._dados}".rjust(5)
        else:
            linha = "".rjust(5)
        return linha


class ACJUSENA(TipoRegistroAC):
    """
    Registro AC específico para alteração do índice de
    aproveitamento de jusante para cálculo das energias
    armazenada e afluente.
    """

    mnemonico = "JUSENA"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0

    def le(self):
        reg_usi = RegistroIn(5)
        self._dados = reg_usi.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados}".rjust(5)
        return linha


class ACVSVERT(TipoRegistroAC):
    """
    Registro AC específico para alteração do volume mínimo para operação
    do vertedor.
    """

    mnemonico = "VSVERT"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0.0

    def le(self):
        reg_desvio = RegistroFn(10)
        self._dados = reg_desvio.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{round(self._dados, 2)}".rjust(10)
        return linha


class ACVMDESV(TipoRegistroAC):
    """
    Registro AC específico para alteração do volume mínimo para operação
    do canal de desvio.
    """

    mnemonico = "VMDESV"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0.0

    def le(self):
        reg_desvio = RegistroFn(10)
        self._dados = reg_desvio.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{round(self._dados, 2)}".rjust(10)
        return linha


class ACNPOSNW(TipoRegistroAC):
    """
    Registro AC específico para alteração do posto de acoplamento
    com o NEWAVE.
    """

    mnemonico = "NPOSNW"

    def __init__(self, linha: str):
        super().__init__(linha)
        self._dados = 0

    def le(self):
        reg_usi = RegistroIn(5)
        self._dados = reg_usi.le_registro(self._linha, 19)

    @property
    def linha_escrita(self) -> str:
        linha = f"{self._dados}".rjust(5)
        return linha


class AC(RegistroDecomp):
    """
    Registro que contém as alterações de cadastro das usinas hidrelétricas.
    """

    mnemonico = "AC"
    modificacoes: List[Type[TipoRegistroAC]] = [
        ACNUMPOS,
        ACNUMJUS,
        ACDESVIO,
        ACVOLMIN,
        ACVOLMAX,
        ACCOTVOL,
        ACCOTARE,
        ACPROESP,
        ACPERHID,
        ACNCHAVE,
        ACCOTVAZ,
        ACCOFEVA,
        ACNUMCON,
        ACNUMMAQ,
        ACPOTEFE,
        ACALTEFE,
        ACVAZEFE,
        ACJUSMED,
        ACVERTJU,
        ACVAZMIN,
        ACTIPERH,
        ACJUSENA,
        ACVSVERT,
        ACVMDESV,
        ACNPOSNW,
    ]

    def __init__(self):
        super().__init__(AC.mnemonico, True)
        self._dados = [0, "", "", 0, 0]
        self._modificacao: TipoRegistroAC = None

    def le(self):
        def procura_modificacao() -> TipoRegistroAC:
            for m in AC.modificacoes:
                if m.mnemonico == self._dados[1]:
                    return m(self._linha)
            raise ValueError(
                f"Mnemônico {self._dados[1]} não"
                + " suportado para registro AC"
            )

        reg_usi = RegistroIn(3)
        reg_cod = RegistroAn(6)
        reg_mes = RegistroAn(3)
        reg_semana = RegistroIn(1)
        reg_ano = RegistroIn(4)
        self._dados[0] = reg_usi.le_registro(self._linha, 4)
        self._dados[1] = reg_cod.le_registro(self._linha, 9)
        if len(self._linha[69:72].strip()) == 3:
            self._dados[2] = reg_mes.le_registro(self._linha, 69)
        if self._linha[74:75].isnumeric():
            self._dados[3] = reg_semana.le_registro(self._linha, 74)
        if self._linha[76:80].isnumeric():
            self._dados[4] = reg_ano.le_registro(self._linha, 76)
        # Procura a modificação pelo mnemônico
        self._modificacao = procura_modificacao()
        # Faz a leitura segundo a lógica específica
        self._modificacao.le()

    def escreve(self, arq: IO):
        linha = (
            f"{AC.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(6)
        )
        linha = linha.ljust(19)
        linha += self._modificacao.linha_escrita
        if any(
            [self._dados[2] != "", self._dados[3] != 0, self._dados[4] != 0]
        ):
            linha = linha.ljust(69)
            linha += self._dados[2]
            linha = linha.ljust(74)
            if self._dados[3] != 0:
                linha += f"{self._dados[3]}"
            linha = linha.ljust(76)
            if self._dados[4] != 0:
                linha += f"{self._dados[4]}"

        linha += "\n"
        arq.write(linha)

    @property
    def uhe(self) -> int:
        return self._dados[0]

    @uhe.setter
    def uhe(self, u: int):
        self._dados[0] = u

    @property
    def modificacao(self) -> str:
        return self._dados[1]

    @modificacao.setter
    def modificacao(self, m: str):
        self._dados[1] = m

    @property
    def mes(self) -> str:
        return self._dados[2]

    @mes.setter
    def mes(self, m: str):
        self._dados[2] = m

    @property
    def semana(self) -> int:
        return self._dados[3]

    @semana.setter
    def semana(self, s: int):
        self._dados[3] = s

    @property
    def ano(self) -> int:
        return self._dados[4]

    @ano.setter
    def ano(self, m: int):
        self._dados[4] = m


class IR(RegistroDecomp):
    """
    Registro que contém as configurações de
    geração de relatórios de saída.
    """

    mnemonico = "IR"

    def __init__(self):
        super().__init__(IR.mnemonico, True)
        self._dados = ["", 0, 0, 0]

    def le(self):
        reg_mne = RegistroAn(7)
        reg_op1 = RegistroIn(2)
        reg_op2 = RegistroIn(2)
        reg_op3 = RegistroIn(5)
        self._dados[0] = reg_mne.le_registro(self._linha, 4)
        if self._linha[14:16].strip().isnumeric():
            self._dados[1] = reg_op1.le_registro(self._linha, 14)
        if self._linha[19:21].strip().isnumeric():
            self._dados[2] = reg_op2.le_registro(self._linha, 19)
        if self._linha[24:29].strip().isnumeric():
            self._dados[3] = reg_op3.le_registro(self._linha, 24)

    def escreve(self, arq: IO):
        linha = f"{IR.mnemonico}".ljust(4) + f"{self._dados[0]}".ljust(7)
        if self._dados[1] != 0:
            linha += "   " + f"{self._dados[1]}".zfill(2)
        if self._dados[2] != 0:
            linha = linha.ljust(19)
            linha += f"{self._dados[2]}".rjust(2)
        if self._dados[3] != 0:
            linha = linha.ljust(24)
            linha += f"{self._dados[3]}".rjust(5)
        linha += "\n"
        arq.write(linha)

    @property
    def tipo(self) -> str:
        """
        Mnemônico que contém o tipo de relatório de
        saída escolhido.

        :return: O mnemônico como `str`.
        """
        return self._dados[0]


class CI(RegistroDecomp):
    """
    Registro que define contratos de importação de energia.
    """

    mnemonico = "CI"

    def __init__(self):
        super().__init__(CI.mnemonico, True)
        self._dados = [
            0,
            0,
            "",
            0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]

    def le(self):
        reg_contrato = RegistroIn(3)
        reg_subsis = RegistroIn(2)
        reg_nome = RegistroAn(10)
        reg_estagio = RegistroIn(2)
        reg_limite = RegistroFn(5)
        reg_custo = RegistroFn(10)
        reg_fator = RegistroFn(5)
        self._dados[0] = reg_contrato.le_registro(self._linha, 4)
        self._dados[1] = reg_subsis.le_registro(self._linha, 8)
        self._dados[2] = reg_nome.le_registro(self._linha, 11)
        self._dados[3] = reg_estagio.le_registro(self._linha, 24)
        for i in range(3):
            self._dados[4 + i * 3] = reg_limite.le_registro(
                self._linha, 29 + i * 20
            )
            self._dados[5 + i * 3] = reg_limite.le_registro(
                self._linha, 34 + i * 20
            )
            self._dados[6 + i * 3] = reg_custo.le_registro(
                self._linha, 39 + i * 20
            )
        if self._linha[89:94].strip().isnumeric():
            self._dados[13] = reg_fator.le_registro(self._linha, 89)

    def escreve(self, arq: IO):
        linha = (
            f"{CI.mnemonico}".ljust(4)
            + f"{self._dados[0]}".zfill(3)
            + " "
            + f"{self._dados[1]}".rjust(2)
            + " "
            + f"{self._dados[2]}".ljust(10)
            + "   "
            + f"{self._dados[3]}".rjust(2)
            + "   "
        )
        for i in range(3):
            linha += f"{round(self._dados[4 + i * 3], 1)}".rjust(5)
            linha += f"{round(self._dados[5 + i * 3], 1)}".rjust(5)
            linha += f"{round(self._dados[6 + i * 3], 2)}".rjust(10)
        if self._dados[13] != 0.0:
            linha += f"{round(self._dados[13], 2)}".rjust(5)
        linha += "\n"
        arq.write(linha)


class CE(RegistroDecomp):
    """
    Registro que define contratos de importação de energia.
    """

    mnemonico = "CE"

    def __init__(self):
        super().__init__(CE.mnemonico, True)
        self._dados = [
            0,
            0,
            "",
            0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]

    def le(self):
        reg_contrato = RegistroIn(3)
        reg_subsis = RegistroIn(2)
        reg_nome = RegistroAn(10)
        reg_estagio = RegistroIn(2)
        reg_limite = RegistroFn(5)
        reg_custo = RegistroFn(10)
        reg_fator = RegistroFn(5)
        self._dados[0] = reg_contrato.le_registro(self._linha, 4)
        self._dados[1] = reg_subsis.le_registro(self._linha, 8)
        self._dados[2] = reg_nome.le_registro(self._linha, 11)
        self._dados[3] = reg_estagio.le_registro(self._linha, 24)
        for i in range(3):
            self._dados[4 + i * 3] = reg_limite.le_registro(
                self._linha, 29 + i * 20
            )
            self._dados[5 + i * 3] = reg_limite.le_registro(
                self._linha, 34 + i * 20
            )
            self._dados[6 + i * 3] = reg_custo.le_registro(
                self._linha, 39 + i * 20
            )
        if self._linha[89:94].strip().isnumeric():
            self._dados[13] = reg_fator.le_registro(self._linha, 89)

    def escreve(self, arq: IO):
        linha = (
            f"{CE.mnemonico}".ljust(4)
            + f"{self._dados[0]}".zfill(3)
            + " "
            + f"{self._dados[1]}".rjust(2)
            + " "
            + f"{self._dados[2]}".ljust(10)
            + "   "
            + f"{self._dados[3]}".rjust(2)
            + "   "
        )
        for i in range(3):
            linha += f"{round(self._dados[4 + i * 3], 1)}".rjust(5)
            linha += f"{round(self._dados[5 + i * 3], 1)}".rjust(5)
            linha += f"{round(self._dados[6 + i * 3], 2)}".rjust(10)
        if self._dados[13] != 0.0:
            linha += f"{round(self._dados[13], 2)}".rjust(5)
        linha += "\n"
        arq.write(linha)


class FC(RegistroDecomp):
    """
    Registro que contém informações para acessar a FCF fornecida
    pelo NEWAVE.
    """

    mnemonico = "FC"

    def __init__(self):
        super().__init__(FC.mnemonico, True)
        self._dados = ["", ""]

    def le(self):
        reg_mne = RegistroAn(6)
        reg_nome = RegistroAn(200)
        self._dados[0] = reg_mne.le_registro(self._linha, 4)
        self._dados[1] = reg_nome.le_registro(self._linha, 14)

    def escreve(self, arq: IO):
        linha = (
            f"{FC.mnemonico}".ljust(4)
            + f"{self._dados[0]}".ljust(6)
            + "    "
            + self._dados[1]
            + "\n"
        )
        arq.write(linha)

    @property
    def tipo(self) -> str:
        """
        O tipo de arquivo da FCF na forma dos mnemônicos
        aceitos pelo DECOMP.

        :return: O mnemônico como `str`.
        """
        return self._dados[0]

    @property
    def caminho(self) -> str:
        """
        O caminho relativo ou completo para o arquivo da
        FCF.

        :return: O caminho como `str`.
        """
        return self._dados[1]

    @caminho.setter
    def caminho(self, c: str):
        self._dados[1] = c


class RT(RegistroDecomp):
    """
    Registro utilizado para retirada de restrições de soleira de
    vertedouro e de canais de desvio.
    """

    mnemonico = "RT"

    def __init__(self):
        super().__init__(RT.mnemonico, True)
        self._dados = [""]

    def le(self):
        reg_mne = RegistroAn(6)
        self._dados[0] = reg_mne.le_registro(self._linha, 4)

    def escreve(self, arq: IO):
        linha = (
            f"{RT.mnemonico}".ljust(4) + f"{self._dados[0]}".ljust(6) + "\n"
        )
        arq.write(linha)

    @property
    def restricao(self) -> str:
        """
        O mnemônico da restrição removida.

        :return: O mnemônico como `str`.
        """
        return self._dados[0]

    @restricao.setter
    def restricao(self, m: str):
        self._dados[0] = m


class TI(RegistroDecomp):
    """
    Registro que contém as taxas de irrigação por UHE.
    """

    mnemonico = "TI"

    def __init__(self):
        super().__init__(TI.mnemonico, True)
        self._dados = [0]

    def le(self):
        reg_uhe = RegistroIn(3)
        reg_irrig = RegistroFn(5)
        self._dados[0] = reg_uhe.le_registro(self._linha, 4)
        ci = 9
        for i in range(24):
            cf = ci + 5
            if len(self._linha[ci:cf].strip()) == 0:
                break
            self._dados.append(reg_irrig.le_registro(self._linha, ci))
            ci = cf

    def escreve(self, arq: IO):
        linha = (
            f"{TI.mnemonico}".ljust(4) + f"{self._dados[0]}".rjust(3) + "  "
        )
        for i in range(1, len(self._dados)):
            # Verificação de segurança para tamanho do registro
            a_escrever = f"{round(self._dados[i], 2)}".rjust(5)
            if len(a_escrever) > 5:
                a_escrever = f"{round(self._dados[i], 1)}".rjust(5)
            if len(a_escrever) > 5:
                a_escrever = f"{int(self._dados[i])}".rjust(5)
            linha += a_escrever
        linha += "\n"
        arq.write(linha)

    @property
    def codigo(self) -> int:
        """
        O código da UHE associada às taxas de irrigação

        :return: O código como `int`.
        """
        return self._dados[0]

    @property
    def taxas(self) -> List[float]:
        """
        As taxas de irrigação por estágio do estudo. A
        posição da taxa na lista indica a qual estágio
        ela está associada [e1, e2, e3, ...].

        :return: As taxas como `list[float]`.
        """
        return self._dados[1:]

    @taxas.setter
    def taxas(self, tx: List[float]):
        novas = len(tx)
        atuais = len(self.taxas)
        if novas != atuais:
            raise ValueError(
                "Número de taxas incompatível. De"
                + f"vem ser fornecidas {atuais}, mas foram {novas}"
            )
        self._dados[1:] = tx


class FP(RegistroDecomp):
    """
    Registro que contém os cadastros de restrições de alteração na
    função de produção das usinas.
    """

    mnemonico = "FP"

    def __init__(self):
        super().__init__(FP.mnemonico, True)
        self._dados = [0, 0, 0, 0, 0.0, 0.0, 0, 0, 0.0, 0.0]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_estagio = RegistroIn(3)
        reg_flag = RegistroIn(1)
        reg_pontos = RegistroIn(4)
        reg_limite = RegistroFn(5)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        self._dados[2] = reg_flag.le_registro(self._linha, 14)
        self._dados[3] = reg_pontos.le_registro(self._linha, 16)
        self._dados[4] = reg_limite.le_registro(self._linha, 21)
        self._dados[5] = reg_limite.le_registro(self._linha, 27)
        self._dados[6] = reg_flag.le_registro(self._linha, 34)
        self._dados[7] = reg_pontos.le_registro(self._linha, 36)
        if len(self._linha[41:46].strip()) > 0:
            self._dados[8] = reg_limite.le_registro(self._linha, 41)
        if len(self._linha[47:52].strip()) > 0:
            self._dados[9] = reg_limite.le_registro(self._linha, 47)

    def escreve(self, arq: IO):
        linha = (
            f"{FP.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(3)
            + "  "
            + f"{self._dados[2]}"
            + " "
            + f"{self._dados[3]}".rjust(4)
            + " "
            + f"{self._dados[4]:.1f}".rjust(5)
            + " "
            + f"{self._dados[5]:.1f}".rjust(5)
            + "  "
            + f"{self._dados[6]}"
            + " "
            + f"{self._dados[7]}".rjust(4)
        )
        if self._dados[8] != 0:
            linha += " " + f"{self._dados[8]:.1f}".rjust(5)
        if self._dados[9] != 0:
            linha += " " + f"{self._dados[9]:.1f}".rjust(5)
        linha += "\n"
        arq.write(linha)

    @property
    def codigo(self) -> int:
        """
        O código da UHE associada à restrição FP.

        :return: O código como `int`.
        """
        return self._dados[0]

    @codigo.setter
    def codigo(self, c: int):
        self._dados[0] = c

    @property
    def estagio(self) -> int:
        """
        O estágio associado à restrição FP.

        :return: O estágio como `int`.
        """
        return self._dados[1]

    @estagio.setter
    def estagio(self, e: int):
        self._dados[1] = e

    @property
    def tipo_entrada_janela_turbinamento(self) -> int:
        """
        O tipo de entrada da janela de turbinamento fornecido
        na restrição FP. 0 para limites em percentual da vazão turbinada
        máxima das usinas, 1 para limites em m3/s.

        :return: O tipo de entrada como `int`.
        """
        return self._dados[2]

    @tipo_entrada_janela_turbinamento.setter
    def tipo_entrada_janela_turbinamento(self, t: int):
        self._dados[2] = t

    @property
    def numero_pontos_turbinamento(self) -> int:
        """
        O número de pontos para discretização da janela de
        turbinamento. Máximo permitido de 1000 pontos.

        :return: O número de pontos como `int`.
        """
        return self._dados[3]

    @numero_pontos_turbinamento.setter
    def numero_pontos_turbinamento(self, n: int):
        self._dados[3] = n

    @property
    def limite_inferior_janela_turbinamento(self) -> float:
        """
        O limite inferior da janela de turbinamento.

        :return: O limite como `float`.
        """
        return self._dados[4]

    @limite_inferior_janela_turbinamento.setter
    def limite_inferior_janela_turbinamento(self, lim: float):
        self._dados[4] = lim

    @property
    def limite_superior_janela_turbinamento(self) -> float:
        """
        O limite superior da janela de turbinamento.

        :return: O limite como `float`.
        """
        return self._dados[5]

    @limite_superior_janela_turbinamento.setter
    def limite_superior_janela_turbinamento(self, lim: float):
        self._dados[5] = lim

    @property
    def tipo_entrada_janela_volume(self) -> int:
        """
        O tipo de entrada da janela de volume fornecido
        na restrição FP. 0 para limites em percentual do volume útil
        das usinas, 1 para limites em hm3.

        :return: O tipo de entrada como `int`.
        """
        return self._dados[6]

    @tipo_entrada_janela_volume.setter
    def tipo_entrada_janela_volume(self, t: int):
        self._dados[6] = t

    @property
    def numero_pontos_volume(self) -> int:
        """
        O número de pontos para discretização da janela de
        volume. Máximo permitido de 1000 pontos.

        :return: O número de pontos como `int`.
        """
        return self._dados[7]

    @numero_pontos_volume.setter
    def numero_pontos_volume(self, n: int):
        self._dados[7] = n

    @property
    def limite_inferior_janela_volume(self) -> float:
        """
        A redução aplicada ao volume útil da usina, para ser utilizado
        como limite inferior da janela de volume.

        :return: O limite como `float`.
        """
        return self._dados[8]

    @limite_inferior_janela_volume.setter
    def limite_inferior_janela_volume(self, lim: float):
        self._dados[8] = lim

    @property
    def limite_superior_janela_volume(self) -> float:
        """
        O acréscimo aplicado ao volume útil da usina, para ser utilizado
        como limite superior da janela de volume.

        :return: O limite como `float`.
        """
        return self._dados[9]

    @limite_superior_janela_volume.setter
    def limite_superior_janela_volume(self, lim: float):
        self._dados[9] = lim


class RQ(RegistroDecomp):
    """
    Registro que contém os percentuais de vazão defluente
    mínima histórica para cada REE.
    """

    mnemonico = "RQ"

    def __init__(self):
        super().__init__(RQ.mnemonico, True)
        self._dados = [0]

    def le(self):
        reg_ree = RegistroIn(2)
        reg_vazao = RegistroFn(5)
        self._dados[0] = reg_ree.le_registro(self._linha, 4)
        ci = 9
        for i in range(24):
            cf = ci + 5
            if len(self._linha[ci:cf].strip()) == 0:
                break
            self._dados.append(reg_vazao.le_registro(self._linha, ci))
            ci = cf

    def escreve(self, arq: IO):
        linha = (
            f"{RQ.mnemonico}".ljust(4) + f"{self._dados[0]}".rjust(2) + "   "
        )
        for i in range(1, len(self._dados)):
            linha += f"{round(self._dados[i], 2)}".rjust(5)
        linha += "\n"
        arq.write(linha)

    @property
    def ree(self) -> int:
        """
        O código do REE associado às vazões mínimas.

        :return: O código como `int`.
        """
        return self._dados[0]

    @ree.setter
    def ree(self, r: int):
        self._dados[0] = r

    @property
    def vazoes(self) -> List[float]:
        """
        As vazões defluentes mínimas (percentuais)
        para o REE, por estágio [e1, e2, e3, ...].

        :return: As vazoes como `list[float]`.
        """
        return self._dados[1:]

    @vazoes.setter
    def vazoes(self, tx: List[float]):
        novas = len(tx)
        atuais = len(self.vazoes)
        if novas != atuais:
            raise ValueError(
                "Número de vazões incompatível. De"
                + f"vem ser fornecidas {atuais}, mas foram {novas}"
            )
        self._dados[1:] = tx


class EZ(RegistroDecomp):
    """
    Registro que contém o percentual máximo do
    volume útil para acoplamento.
    """

    mnemonico = "EZ"

    def __init__(self):
        super().__init__(EZ.mnemonico, True)
        self._dados = [0, 0.0]

    def le(self):
        reg_uhe = RegistroIn(3)
        reg_volume = RegistroFn(5)
        self._dados[0] = reg_uhe.le_registro(self._linha, 4)
        self._dados[1] = reg_volume.le_registro(self._linha, 9)

    def escreve(self, arq: IO):
        linha = (
            f"{EZ.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{round(self._dados[1], 2)}".rjust(5)
            + "\n"
        )
        arq.write(linha)


class HV(RegistroDecomp):
    """
    Registro que contém os cadastros de restrições de volume armazenado.
    """

    mnemonico = "HV"

    def __init__(self):
        super().__init__(HV.mnemonico, True)
        self._dados = [0, 0, 0]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_estagio = RegistroIn(2)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        self._dados[2] = reg_estagio.le_registro(self._linha, 14)

    def escreve(self, arq: IO):
        linha = (
            f"{HV.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(2)
            + "   "
            + f"{self._dados[2]}".rjust(2)
            + "\n"
        )
        arq.write(linha)

    @property
    def codigo(self) -> int:
        """
        O código da UHE associada à restrição HV.

        :return: O código como `int`.
        """
        return self._dados[0]

    @property
    def estagio_inicial(self) -> int:
        """
        O estágio inicial de consideração da restrição HV.

        :return: O estágio como `int`.
        """
        return self._dados[1]

    @property
    def estagio_final(self) -> int:
        """
        O estágio final de consideração da restrição HV.

        :return: O estágio como `int`.
        """
        return self._dados[2]


class LV(RegistroDecomp):
    """
    Registro que contém os limites das restrições de volume armazenado.
    """

    mnemonico = "LV"
    default = 1e21

    def __init__(self):
        super().__init__(LV.mnemonico, True)
        self._dados = [0, 0] + [LV.default] * 2

    def le(self):
        reg_cod = RegistroIn(3)
        reg_estagio = RegistroIn(2)
        reg_limite = RegistroFn(10)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        ci = 14
        for i in range(2, len(self._dados)):
            cf = ci + 10
            if len(self._linha[ci:cf].strip()) != 0:
                self._dados[i] = reg_limite.le_registro(self._linha, ci)
            ci = cf

    def escreve(self, arq: IO):
        linha = (
            f"{LV.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(2)
            + "   "
        )
        for i in range(2, len(self._dados)):
            if self._dados[i] != LV.default:
                linha += f"{round(self._dados[i], 2)}".rjust(10)
            else:
                linha += "          "

        arq.write(linha + "\n")

    @property
    def codigo(self) -> int:
        """
        O código da restrição HV associada aos limites

        :return: O código como `int`.
        """
        return self._dados[0]

    @property
    def estagio(self) -> int:
        """
        O estágio de consideração dos limites.

        :return: O estágio como `int`.
        """
        return self._dados[1]

    @estagio.setter
    def estagio(self, e: int):
        self._dados[1] = e

    @property
    def limite_inferior(self) -> float:
        """
        O limite inferior para o armazenamento.

        :return: O limite como `float`.
        """
        return self._dados[2]

    @limite_inferior.setter
    def limite_inferior(self, lim: float):
        self._dados[2] = lim

    @property
    def limites_superior(self) -> float:
        """
        O limite superior para o armazenamento.

        :return: O limite como `float`.
        """
        return self._dados[3]

    @limites_superior.setter
    def limites_superior(self, lim: float):
        self._dados[3] = lim


class CV(RegistroDecomp):
    """
    Registro que contém os coeficientes das usinas hidráulicas
    nas restrições de volume armazenado.
    """

    mnemonico = "CV"

    def __init__(self):
        super().__init__(CV.mnemonico, True)
        self._dados = [0, 0, 0, 0.0, ""]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_estagio = RegistroIn(2)
        reg_uhe = RegistroIn(3)
        reg_fator = RegistroFn(10)
        reg_tipo = RegistroAn(4)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        self._dados[2] = reg_uhe.le_registro(self._linha, 14)
        self._dados[3] = reg_fator.le_registro(self._linha, 19)
        self._dados[4] = reg_tipo.le_registro(self._linha, 34)

    def escreve(self, arq: IO):
        linha = (
            f"{CV.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(2)
            + "   "
            + f"{self._dados[2]}".rjust(3)
            + "  "
            + f"{round(self._dados[3], 8)}".rjust(10)
        )
        linha = linha.ljust(34)
        linha += self._dados[4]
        linha += "\n"
        arq.write(linha)


class HQ(RegistroDecomp):
    """
    Registro que contém os cadastros de restrições de vazões.
    """

    mnemonico = "HQ"

    def __init__(self):
        super().__init__(HQ.mnemonico, True)
        self._dados = [0, 0, 0]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_estagio = RegistroIn(2)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        self._dados[2] = reg_estagio.le_registro(self._linha, 14)

    def escreve(self, arq: IO):
        linha = (
            f"{HQ.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(2)
            + "  "
            + f"{self._dados[2]}".rjust(2)
            + "\n"
        )
        arq.write(linha)

    @property
    def codigo(self) -> int:
        """
        O código da UHE associada à restrição HQ.

        :return: O código como `int`.
        """
        return self._dados[0]

    @property
    def estagio_inicial(self) -> int:
        """
        O estágio inicial de consideração da restrição HQ.

        :return: O estágio como `int`.
        """
        return self._dados[1]

    @property
    def estagio_final(self) -> int:
        """
        O estágio final de consideração da restrição HQ.

        :return: O estágio como `int`.
        """
        return self._dados[2]


class LQ(RegistroDecomp):
    """
    Registro que contém os limites das restrições de volume armazenado.
    """

    mnemonico = "LQ"
    default = 1e21

    def __init__(self):
        super().__init__(LQ.mnemonico, True)
        self._dados = [0, 0] + [LQ.default] * 6

    def le(self):
        reg_cod = RegistroIn(3)
        reg_estagio = RegistroIn(2)
        reg_limite = RegistroFn(10)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        ci = 14
        for i in range(2, len(self._dados)):
            cf = ci + 10
            if len(self._linha[ci:cf].strip()) != 0:
                self._dados[i] = reg_limite.le_registro(self._linha, ci)
            ci = cf

    def escreve(self, arq: IO):
        linha = (
            f"{LQ.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(2)
            + "   "
        )
        for i in range(2, len(self._dados)):
            if self._dados[i] != LQ.default:
                linha += f"{round(self._dados[i], 2)}".rjust(10)
            else:
                linha += "          "

        arq.write(linha + "\n")

    @property
    def codigo(self) -> int:
        """
        O código da restrição HQ associada aos limites

        :return: O código como `int`.
        """
        return self._dados[0]

    @property
    def estagio(self) -> int:
        """
        O estágio de consideração dos limites.

        :return: O estágio como `int`.
        """
        return self._dados[1]

    @estagio.setter
    def estagio(self, e: int):
        self._dados[1] = e

    @property
    def limites_inferiores(self) -> List[float]:
        """
        Os limites inferiores por patamar para a vazão.

        :return: Os limites como `list[float]`.
        """
        return self._dados[2::2]

    @limites_inferiores.setter
    def limites_inferiores(self, lim: List[float]):
        novos = len(lim)
        atuais = len(self.limites_inferiores)
        if novos != atuais:
            raise ValueError(
                "Número de limites incompatível. De"
                + f"vem ser fornecidos {atuais}, mas foram {novos}"
            )
        self._dados[2::2] = lim

    @property
    def limites_superiores(self) -> List[float]:
        """
        Os limites superiores por patamar para a vazão.

        :return: Os limites como `list[float]`.
        """
        return self._dados[3::2]

    @limites_superiores.setter
    def limites_superiores(self, lim: List[float]):
        novos = len(lim)
        atuais = len(self.limites_superiores)
        if novos != atuais:
            raise ValueError(
                "Número de limites incompatível. De"
                + f"vem ser fornecidos {atuais}, mas foram {novos}"
            )
        self._dados[3::2] = lim


class CQ(RegistroDecomp):
    """
    Registro que contém os coeficientes das usinas hidráulicas
    nas restrições de vazão.
    """

    mnemonico = "CQ"

    def __init__(self):
        super().__init__(CQ.mnemonico, True)
        self._dados = [0, 0, 0, 0.0, ""]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_estagio = RegistroIn(2)
        reg_uhe = RegistroIn(3)
        reg_fator = RegistroFn(10)
        reg_tipo = RegistroAn(4)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        self._dados[2] = reg_uhe.le_registro(self._linha, 14)
        self._dados[3] = reg_fator.le_registro(self._linha, 19)
        self._dados[4] = reg_tipo.le_registro(self._linha, 34)

    def escreve(self, arq: IO):
        linha = (
            f"{CQ.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(2)
            + "   "
            + f"{self._dados[2]}".rjust(3)
            + "  "
            + f"{round(self._dados[3], 2)}".rjust(10)
        )
        linha = linha.ljust(34)
        linha += self._dados[4]
        linha += "\n"
        arq.write(linha)


class AR(RegistroDecomp):
    """
    Registro que contém as configurações de aversão a risco.
    """

    mnemonico = "AR"

    def __init__(self):
        super().__init__(AR.mnemonico, True)
        self._dados: int = 0

    def le(self):
        reg_linha = RegistroIn(3)
        self._dados = reg_linha.le_registro(self._linha, 5)

    def escreve(self, arq: IO):
        linha = (
            f"{AR.mnemonico}".ljust(4) + " " + f"{self.dados}".rjust(3) + "\n"
        )
        arq.write(linha)


class EV(RegistroDecomp):
    """
    Registro que contém as configurações de consideração
    da evaporação.
    """

    mnemonico = "EV"

    def __init__(self):
        super().__init__(EV.mnemonico, True)
        self._dados = [0, ""]

    def le(self):
        reg_linha = RegistroIn(1)
        reg_tipo = RegistroAn(3)
        self._dados[0] = reg_linha.le_registro(self._linha, 4)
        self._dados[1] = reg_tipo.le_registro(self._linha, 9)

    def escreve(self, arq: IO):
        linha = (
            f"{EV.mnemonico}".ljust(4)
            + f"{self._dados[0]}"
            + "    "
            + f"{self._dados[1]}".rjust(3)
            + "\n"
        )
        arq.write(linha)

    @property
    def modelo(self) -> int:
        return self._dados[0]

    @modelo.setter
    def modelo(self, m: int):
        self._dados[0] = m

    @property
    def volume_referencia(self) -> str:
        return self._dados[1]

    @volume_referencia.setter
    def volume_referencia(self, v: str):
        self._dados[1] = v


class FJ(RegistroDecomp):
    """
    Registro que contém as configurações de aversão a risco.
    """

    mnemonico = "FJ"

    def __init__(self):
        super().__init__(FJ.mnemonico, True)
        self._dados: str = ""

    def le(self):
        reg_linha = RegistroAn(12)
        self._dados = reg_linha.le_registro(self._linha, 4)

    def escreve(self, arq: IO):
        linha = f"{FJ.mnemonico}".ljust(4) + f"{self.dados}".rjust(12) + "\n"
        arq.write(linha)

    @property
    def arquivo(self) -> str:
        return self._dados

    @arquivo.setter
    def arquivo(self, a: str):
        self._dados = a


class HE(RegistroDecomp):
    """
    Registro que contém o cadastro de uma restrição de volume
    mínimo armazenado.
    """

    mnemonico = "HE"

    def __init__(self):
        super().__init__(HE.mnemonico, True)
        self._dados = [0, 0, 0.0, 0, 0.0, 0, 0, 0, ""]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_tipo_limite = RegistroIn(1)
        reg_limite = RegistroFn(10)
        reg_estagio = RegistroIn(2)
        reg_penal = RegistroFn(10)
        reg_inviab = RegistroIn(1)
        reg_prodrhe = RegistroAn(12)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_tipo_limite.le_registro(self._linha, 9)
        self._dados[2] = reg_limite.le_registro(self._linha, 14)
        self._dados[3] = reg_estagio.le_registro(self._linha, 25)
        self._dados[4] = reg_penal.le_registro(self._linha, 28)
        if self._linha[39].isnumeric():
            self._dados[5] = reg_inviab.le_registro(self._linha, 39)
        if self._linha[41].isnumeric():
            self._dados[6] = reg_inviab.le_registro(self._linha, 41)
        if self._linha[43].isnumeric():
            self._dados[7] = reg_inviab.le_registro(self._linha, 43)
        if len(self._linha[45:57]) > 2:
            self._dados[8] = reg_prodrhe.le_registro(self._linha, 45)

    def escreve(self, arq: IO):
        linha = (
            f"{HE.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}"
            + "    "
            + f"{round(self._dados[2], 2)}".rjust(10)
            + " "
            + f"{self._dados[3]}".rjust(2)
            + " "
            + f"{round(self._dados[4], 2)}".rjust(10)
            + " "
            + f"{self._dados[5]}"
            + " "
            + f"{self._dados[6]}"
            + " "
            + f"{self._dados[7]}"
            + " "
            + f"{self._dados[8]}".ljust(60).strip()
        )
        linha += "\n"
        arq.write(linha)

    @property
    def codigo(self) -> int:
        """
        O código de cadastro da restrição HE

        :return: O código como `int`.
        """
        return self._dados[0]

    @property
    def tipo_limite(self) -> int:
        """
        O tipo de limite especificado na restrição HE,
        em valor absoluto ou percentual.

        :return: O tipo como `int`.
        """
        return self._dados[1]

    @tipo_limite.setter
    def tipo_limite(self, t: int):
        self._dados[1] = t

    @property
    def limite(self) -> float:
        """
        O limite para a energia armazenada associada
        ao registro HE.

        :return: O limite como `float`.
        """
        return self._dados[2]

    @limite.setter
    def limite(self, lim: float):
        self._dados[2] = lim

    @property
    def estagio(self) -> int:
        """
        O estágio para consideração da restrição.

        :return: O estágio como `int`.
        """
        return self._dados[3]

    @estagio.setter
    def estagio(self, e: int):
        self._dados[3] = e

    @property
    def penalidade(self) -> float:
        """
        O valor da penalidade para a violação da restrição.

        :return: O valor como `float`.
        """
        return self._dados[4]

    @penalidade.setter
    def penalidade(self, p: float):
        self._dados[4] = p

    @property
    def forma_calculo_produtibilidades(self) -> int:
        """
        Flag para indicar a forma de cálculo das produtividades
        das usinas usadas nas restrição.

        :return: O tipo como `int`.
        """
        return self._dados[5]

    @forma_calculo_produtibilidades.setter
    def forma_calculo_produtibilidades(self, t: int):
        self._dados[5] = t

    @property
    def tipo_valores_produtibilidades(self) -> int:
        """
        Flag para indicar o tipo dos valores das produtividades
        das usinas usadas nas restrição.

        :return: O tipo como `int`.
        """
        return self._dados[6]

    @tipo_valores_produtibilidades.setter
    def tipo_valores_produtibilidades(self, t: int):
        self._dados[6] = t

    @property
    def tipo_penalidade(self) -> int:
        """
        O tipo de penalidade a ser considerada ao violar a
        restrição (inviabilidade ou penalização).

        :return: O tipo como `int`.
        """
        return self._dados[7]

    @tipo_penalidade.setter
    def tipo_penalidade(self, t: int):
        self._dados[7] = t

    @property
    def arquivo_produtibilidades(self) -> str:
        """
        O arquivo com as definições das produtibilidades usadas
        para o cálculo da restrição RHE.

        :return: O tipo como `int`.
        """
        return self._dados[8]

    @arquivo_produtibilidades.setter
    def arquivo_produtibilidades(self, t: str):
        self._dados[8] = t


class CM(RegistroDecomp):
    """
    Registro que contém os coeficientes de uma restrição RHE.
    """

    mnemonico = "CM"

    def __init__(self):
        super().__init__(CM.mnemonico, True)
        self._dados = [0, 0, 0.0]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_ree = RegistroIn(3)
        reg_coef = RegistroFn(10)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_ree.le_registro(self._linha, 9)
        self._dados[2] = reg_coef.le_registro(self._linha, 14)

    def escreve(self, arq: IO):
        linha = (
            f"{CM.mnemonico}".ljust(4)
            + f"{self._dados[0]}".rjust(3)
            + "  "
            + f"{self._dados[1]}".rjust(3)
            + "  "
            + f"{formata_numero(self._dados[2], 2, 10)}"
        )
        linha += "\n"
        arq.write(linha)

    @property
    def codigo(self) -> int:
        return self._dados[0]

    @property
    def estagio(self) -> int:
        return self._dados[1]

    @estagio.setter
    def estagio(self, e: int):
        self._dados[1] = e

    @property
    def coeficiente(self) -> int:
        return self._dados[2]

    @coeficiente.setter
    def coeficiente(self, c: float):
        self._dados[2] = c


class LeituraDadger(LeituraRegistros):
    """
    Classe com utilidades gerais para leitura de arquivos
    do DECOMP com comentários.
    """

    def __init__(self, diretorio: str):
        super().__init__(diretorio)

    def _cria_registros_leitura(self) -> List[RegistroDecomp]:
        """
        Método que cria a lista de registros a serem lidos no arquivo.
        Implementa o Factory Pattern.
        """
        MAX_UHE = 200
        MAX_UTE = 200
        MAX_UE = 10
        MAX_RE = 200
        MAX_ESTAGIOS = 7
        MAX_SUBSIS = 5
        MAX_AC_UHE = 10
        MAX_REE = 12
        MAX_RELATORIOS = 10
        te: List[RegistroDecomp] = [TE()]
        rt: List[RegistroDecomp] = [RT(), RT()]
        sb: List[RegistroDecomp] = [SB() for _ in range(MAX_SUBSIS)]
        uh: List[RegistroDecomp] = [UH() for _ in range(MAX_UHE)]
        ct: List[RegistroDecomp] = [CT() for _ in range(MAX_UTE)]
        ue: List[RegistroDecomp] = [UE() for _ in range(MAX_UE)]
        dp: List[RegistroDecomp] = [
            DP() for _ in range(MAX_SUBSIS * MAX_ESTAGIOS)
        ]
        cd: List[RegistroDecomp] = [
            CD() for _ in range(MAX_SUBSIS * MAX_ESTAGIOS)
        ]
        pq: List[RegistroDecomp] = [
            PQ() for _ in range(MAX_SUBSIS * MAX_ESTAGIOS)
        ]
        ri: List[RegistroDecomp] = [RI() for _ in range(MAX_ESTAGIOS)]
        ia: List[RegistroDecomp] = [
            IA() for _ in range(MAX_SUBSIS * MAX_SUBSIS)
        ]
        tx: List[RegistroDecomp] = [TX()]
        gp: List[RegistroDecomp] = [GP()]
        ni: List[RegistroDecomp] = [NI()]
        dt: List[RegistroDecomp] = [DT()]
        mp: List[RegistroDecomp] = [MP() for _ in range(MAX_UHE)]
        mt: List[RegistroDecomp] = [MT() for _ in range(MAX_UTE)]
        fd: List[RegistroDecomp] = [FD() for _ in range(MAX_UHE)]
        ve: List[RegistroDecomp] = [VE() for _ in range(MAX_UHE)]
        re: List[RegistroDecomp] = [RE() for _ in range(MAX_RE)]
        lu: List[RegistroDecomp] = [LU() for _ in range(MAX_RE * MAX_ESTAGIOS)]
        fu: List[RegistroDecomp] = [FU() for _ in range(MAX_RE)]
        ft: List[RegistroDecomp] = [FT() for _ in range(MAX_RE)]
        vi: List[RegistroDecomp] = [VI(), VI()]
        ac: List[RegistroDecomp] = [AC() for _ in range(MAX_UHE * MAX_AC_UHE)]
        ir: List[RegistroDecomp] = [IR() for _ in range(MAX_RELATORIOS)]
        fc: List[RegistroDecomp] = [FC(), FC()]
        ti: List[RegistroDecomp] = [TI() for _ in range(MAX_UHE)]
        rq: List[RegistroDecomp] = [RQ() for _ in range(MAX_REE)]
        ez: List[RegistroDecomp] = [EZ() for _ in range(MAX_UHE)]
        hv: List[RegistroDecomp] = [HV() for _ in range(MAX_UHE)]
        lv: List[RegistroDecomp] = [
            LV() for _ in range(MAX_UHE * MAX_ESTAGIOS)
        ]
        cv: List[RegistroDecomp] = [CV() for _ in range(MAX_UHE)]
        hq: List[RegistroDecomp] = [HQ() for _ in range(MAX_UHE)]
        lq: List[RegistroDecomp] = [
            LQ() for _ in range(MAX_UHE * MAX_ESTAGIOS)
        ]
        cq: List[RegistroDecomp] = [
            CQ() for _ in range(MAX_UHE * MAX_ESTAGIOS)
        ]
        ar: List[RegistroDecomp] = [AR()]
        ev: List[RegistroDecomp] = [EV()]
        fj: List[RegistroDecomp] = [FJ()]
        he: List[RegistroDecomp] = [
            HE() for _ in range(MAX_REE * MAX_ESTAGIOS)
        ]
        cm: List[RegistroDecomp] = [
            CM() for _ in range(MAX_REE * MAX_ESTAGIOS)
        ]
        fp: List[RegistroDecomp] = [FP() for _ in range(MAX_UHE)]
        return (
            te
            + rt
            + sb
            + uh
            + ct
            + ue
            + dp
            + cd
            + pq
            + ri
            + ia
            + tx
            + gp
            + ni
            + dt
            + mp
            + mt
            + fd
            + ve
            + re
            + lu
            + fu
            + ft
            + vi
            + ac
            + ir
            + fc
            + ti
            + rq
            + ez
            + hv
            + lv
            + cv
            + hq
            + lq
            + cq
            + ar
            + ev
            + fj
            + he
            + cm
            + fp
        )
