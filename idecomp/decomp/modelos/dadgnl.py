from typing import IO, List

from idecomp._utils.utils import formata_numero
from idecomp._utils.registros import RegistroAn, RegistroFn, RegistroIn
from idecomp._utils.registrodecomp import RegistroDecomp
from idecomp._utils.leituraregistros import LeituraRegistros


class TG(RegistroDecomp):
    """
    Registro que contém o cadastro das térmicas a GNL
    """
    mnemonico = "TG"

    def __init__(self):
        super().__init__(TG.mnemonico, True)
        self._dados = [0, 0, "", 0,
                       0.0, 0.0, 0.0,
                       0.0, 0.0, 0.0,
                       0.0, 0.0, 0.0]

    def le(self):
        reg_codigo = RegistroIn(3)
        reg_subsis = RegistroIn(2)
        reg_nome = RegistroAn(10)
        reg_estagio = RegistroIn(2)
        reg_inflex = RegistroFn(5)
        reg_disp = RegistroFn(5)
        reg_cvu = RegistroFn(10)
        self._dados[0] = reg_codigo.le_registro(self._linha, 4)
        self._dados[1] = reg_subsis.le_registro(self._linha, 9)
        self._dados[2] = reg_nome.le_registro(self._linha, 14)
        self._dados[3] = reg_estagio.le_registro(self._linha, 24)
        for j in range(3):
            self._dados[4 + 3 * j] = reg_inflex.le_registro(self._linha,
                                                            29 + 20 * j)
            self._dados[5 + 3 * j] = reg_disp.le_registro(self._linha,
                                                          34 + 20 * j)
            self._dados[6 + 3 * j] = reg_cvu.le_registro(self._linha,
                                                         39 + 20 * j)

    def escreve(self, arq: IO):

        linha = (f"{TG.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".ljust(10) +
                 f"{self._dados[3]}".rjust(2) + "   " +
                 formata_numero(self._dados[4], 2, 5) +
                 formata_numero(self._dados[5], 2, 5) +
                 f"{self._dados[6]:10.2f}" +
                 formata_numero(self._dados[7], 2, 5) +
                 formata_numero(self._dados[8], 2, 5) +
                 f"{self._dados[9]:10.2f}" +
                 formata_numero(self._dados[10], 2, 5) +
                 formata_numero(self._dados[11], 2, 5) +
                 f"{self._dados[12]:10.2f}" + "\n")
        arq.write(linha)

    @property
    def codigo(self) -> int:
        """
        O código de cadastro da UTE.

        :return: O código como um `int`.
        """
        return self._dados[0]

    @property
    def subsistema(self) -> int:
        """
        O subsistema de cadastro da UTE.

        :return: O subsistema como um `int`.
        """
        return self._dados[1]

    @property
    def nome(self) -> str:
        """
        O nome de cadastro da UTE.

        :return: O nome como uma `str`.
        """
        return self._dados[2]

    @nome.setter
    def nome(self, nome: str):
        self._dados[2] = nome

    @property
    def estagio(self) -> int:
        """
        O estágio do despacho da UTE.

        :return: O estágio como um `int`.
        """
        return self._dados[3]

    @estagio.setter
    def estagio(self, estagio: int):
        self._dados[3] = estagio

    @property
    def inflexibilidades(self) -> List[float]:
        """
        As inflexibilidades da UTE por patamar.

        :return: As inflexibilidades como `list[float]`.
        """
        return self._dados[4::3]

    @inflexibilidades.setter
    def inflexibilidades(self, inflex: List[float]):
        novas = len(inflex)
        atuais = len(self.inflexibilidades)
        if novas != atuais:
            raise ValueError("Número de inflexibilidades incompatível. De" +
                             f"vem ser fornecidas {atuais}, mas foram {novas}")
        self._dados[4::3] = inflex

    @property
    def disponibilidades(self) -> List[float]:
        """
        As disponibilidades da UTE por patamar.

        :return: As disponibilidades como `list[float]`.
        """
        return self._dados[5::3]

    @disponibilidades.setter
    def disponibilidades(self, disp: List[float]):
        novas = len(disp)
        atuais = len(self.disponibilidades)
        if novas != atuais:
            raise ValueError("Número de disponibilidades incompatível. De" +
                             f"vem ser fornecidas {atuais}, mas foram {novas}")
        self._dados[5::3] = disp

    @property
    def cvus(self) -> List[float]:
        """
        Os CVUs da UTE por patamar.

        :return: Os CVUs como `list[float]`.
        """
        return self._dados[6::3]

    @cvus.setter
    def cvus(self, cvu: List[float]):
        novas = len(cvu)
        atuais = len(self.cvus)
        if novas != atuais:
            raise ValueError("Número de CVUs incompatível. De" +
                             f"vem ser fornecidas {atuais}, mas foram {novas}")
        self._dados[6::3] = cvu


class GS(RegistroDecomp):
    """
    Registro que contém o número de semanas dos meses envolvidos
    no estudo.
    """
    mnemonico = "GS"

    def __init__(self):
        super().__init__(GS.mnemonico, True)
        self._dados = [0, 0]

    def le(self):
        reg_mes = RegistroIn(2)
        reg_semanas = RegistroIn(1)
        self._dados[0] = reg_mes.le_registro(self._linha, 4)
        self._dados[1] = reg_semanas.le_registro(self._linha, 9)

    def escreve(self, arq: IO):
        linha = (f"{GS.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(2) + "   " +
                 f"{self._dados[1]}".rjust(1) + "\n")
        arq.write(linha)

    @property
    def mes(self) -> int:
        """
        O índice do mês associado ao registro GS

        :return: O índice como `int`.
        """
        return self._dados[0]

    @mes.setter
    def mes(self, m: int):
        self._dados[0] = m

    @property
    def semanas(self) -> int:
        """
        O número de semanas do mês associado ao registro GS

        :return: O número de semanas como `int`.
        """
        return self._dados[1]

    @semanas.setter
    def semanas(self, s: int):
        self._dados[1] = s


class NL(RegistroDecomp):
    """
    Registro que contém o número de lags para o despacho de cada térmica
    de despacho antecipado em cada subsistema.
    """
    mnemonico = "NL"

    def __init__(self):
        super().__init__(NL.mnemonico, True)
        self._dados = [0, 0, 0]

    def le(self):
        reg_codigo = RegistroIn(3)
        reg_subsis = RegistroIn(2)
        reg_lag = RegistroIn(1)
        self._dados[0] = reg_codigo.le_registro(self._linha, 4)
        self._dados[1] = reg_subsis.le_registro(self._linha, 9)
        self._dados[2] = reg_lag.le_registro(self._linha, 14)

    def escreve(self, arq: IO):
        linha = (f"{NL.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".rjust(1) + "\n")
        arq.write(linha)

    @property
    def codigo(self) -> int:
        """
        O código da UTE associada ao registro NL

        :return: O código como `int`.
        """
        return self._dados[0]

    @codigo.setter
    def codigo(self, c: int):
        self._dados[0] = c

    @property
    def subsistema(self) -> int:
        """
        O índice do subsistema de despacho da UTE

        :return: O índice do subsistema como `int`.
        """
        return self._dados[1]

    @subsistema.setter
    def subsistema(self, s: int):
        self._dados[1] = s

    @property
    def lag(self) -> int:
        """
        O lag de despacho da UTE

        :return: O lag como `int`.
        """
        return self._dados[2]

    @lag.setter
    def lag(self, lag: int):
        self._dados[2] = lag


class GL(RegistroDecomp):
    """
    Registro que contém os cadastros de restrições elétricas.
    """
    mnemonico = "GL"

    def __init__(self):
        super().__init__(GL.mnemonico, True)
        self._dados = [0, 0, 0,
                       0.0, 0.0,
                       0.0, 0.0,
                       0.0, 0.0,
                       ""]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_subsistema = RegistroIn(2)
        reg_estagio = RegistroIn(2)
        reg_geracao = RegistroFn(10)
        reg_duracao = RegistroFn(5)
        reg_data = RegistroAn(8)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_subsistema.le_registro(self._linha, 9)
        self._dados[2] = reg_estagio.le_registro(self._linha, 14)
        self._dados[3] = reg_geracao.le_registro(self._linha, 19)
        self._dados[4] = reg_duracao.le_registro(self._linha, 29)
        self._dados[5] = reg_geracao.le_registro(self._linha, 34)
        self._dados[6] = reg_duracao.le_registro(self._linha, 44)
        self._dados[7] = reg_geracao.le_registro(self._linha, 49)
        self._dados[8] = reg_duracao.le_registro(self._linha, 59)
        self._dados[9] = reg_data.le_registro(self._linha, 65)

    def escreve(self, arq: IO):
        linha = (f"{GL.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".rjust(2) + "   " +
                 f"{formata_numero(self._dados[3], 1, 10)}" +
                 f"{formata_numero(self._dados[4], 1, 5)}" +
                 f"{formata_numero(self._dados[5], 1, 10)}" +
                 f"{formata_numero(self._dados[6], 1, 5)}" +
                 f"{formata_numero(self._dados[7], 1, 10)}" +
                 f"{formata_numero(self._dados[8], 1, 5)}" +
                 f" {self._dados[9]}")

        arq.write(linha + "\n")

    @property
    def codigo(self) -> int:
        """
        O código da UTE despachada no registro GL

        :return: O código como `int`.
        """
        return self._dados[0]

    @property
    def subsistema(self) -> int:
        """
        O índice do subsistema de despacho da UTE

        :return: O índice do subsistema como `int`.
        """
        return self._dados[1]

    @subsistema.setter
    def subsistema(self, e: int):
        self._dados[1] = e

    @property
    def estagio(self) -> int:
        """
        O estágio de despacho da UTE

        :return: O estágio como `int`.
        """
        return self._dados[2]

    @estagio.setter
    def estagio(self, e: int):
        self._dados[2] = e

    @property
    def geracoes(self) -> List[float]:
        """
        Os valores de geração por patamar para o despacho
        da UTE

        :return: As geracoes como `list[float]`
        """
        return self._dados[3::2][:-1]

    @geracoes.setter
    def geracoes(self, gers: List[float]):
        novos = len(gers)
        atuais = len(self.geracoes)
        if novos != atuais:
            raise ValueError("Número de gerações incompatível. De" +
                             f"vem ser fornecidos {atuais}, mas foram {novos}")
        self._dados[3::2] = gers

    @property
    def duracoes(self) -> List[float]:
        """
        Os valores de geração por patamar para o despacho
        da UTE

        :return: As durações como `list[float]`
        """
        return self._dados[4::2]

    @duracoes.setter
    def duracoes(self, durs: List[float]):
        novos = len(durs)
        atuais = len(self.duracoes)
        if novos != atuais:
            raise ValueError("Número de durações incompatível. De" +
                             f"vem ser fornecidos {atuais}, mas foram {novos}")
        self._dados[4::2] = durs


class LeituraDadGNL(LeituraRegistros):
    """
    Classe com utilidades gerais para leitura de arquivos
    do DECOMP com comentários.
    """
    def __init__(self,
                 diretorio: str):
        super().__init__(diretorio)

    def _cria_registros_leitura(self) -> List[RegistroDecomp]:
        """
        Método que cria a lista de registros a serem lidos no arquivo.
        Implementa o Factory Pattern.
        """
        MAX_UTE = 200
        MAX_MESES = 5
        MAX_ESTAGIOS = 10
        tg: List[RegistroDecomp] = [TG() for _ in range(MAX_UTE)]
        gs: List[RegistroDecomp] = [GS() for _ in range(MAX_MESES)]
        nl: List[RegistroDecomp] = [NL() for _ in range(MAX_UTE)]
        gl: List[RegistroDecomp] = [GL() for _ in range(MAX_UTE *
                                                        MAX_ESTAGIOS)]
        return (tg + gs + nl + gl)
