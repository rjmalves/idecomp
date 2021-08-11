from typing import IO, List, Dict, Type
import os
from traceback import print_exc

from idecomp._utils.utils import formata_numero
from idecomp._utils.registros import RegistroAn, RegistroFn, RegistroIn
from idecomp._utils.registrodadger import RegistroDadger
from idecomp._utils.registrodadger import TipoRegistroAC
from idecomp._utils.dadosdadger import DadosDadger


class TE(RegistroDadger):
    """
    Registro que contém o nome do estudo do DECOMP.
    """
    mnemonico = "TE"

    def __init__(self):
        super().__init__(TE.mnemonico, True)
        self._dados: str = ""

    def le(self):
        reg_linha = RegistroAn(75)
        self._dados = reg_linha.le_registro(self._linha, 4)

    def escreve(self, arq: IO):
        linha = f"{TE.mnemonico}".ljust(4) + self.dados + "\n"
        arq.write(linha)

    @property
    def titulo(self) -> str:
        return self._dados

    @titulo.setter
    def titulo(self, t: str):
        self._dados = t


class SB(RegistroDadger):
    """
    Registro que contém o cadastro dos subsistemas.
    """
    mnemonico = "SB"

    def __init__(self):
        super().__init__(SB.mnemonico, True)
        self._dados = [0, ""]

    def le(self):
        reg_indice = RegistroIn(2)
        reg_mnemonico = RegistroAn(2)
        self._dados[0] = reg_indice.le_registro(self._linha, 4)
        self._dados[1] = reg_mnemonico.le_registro(self._linha, 9)

    def escreve(self, arq: IO):
        linha = (f"{SB.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(2) + "   " +
                 f"{self._dados[1]}".ljust(2) + "\n")
        arq.write(linha)

    @property
    def codigo(self) -> int:
        return self._dados[0]

    @property
    def nome(self) -> str:
        return self._dados[1]


class UH(RegistroDadger):
    """
    Registro que contém o cadastro das UHEs, com os seus volumes
    iniciais no estudo.
    """
    mnemonico = "UH"

    def __init__(self):
        super().__init__(UH.mnemonico, True)
        self._dados = [0, 0, 0.0, True, -1.0]

    def le(self):
        reg_indice = RegistroIn(3)
        reg_ree = RegistroIn(2)
        reg_vini = RegistroFn(6)
        reg_evap = RegistroIn(1)
        reg_vert = RegistroFn(10)
        self._dados[0] = reg_indice.le_registro(self._linha, 4)
        self._dados[1] = reg_ree.le_registro(self._linha, 9)
        self._dados[2] = reg_vini.le_registro(self._linha, 18)
        self._dados[3] = bool(reg_evap.le_registro(self._linha, 39))
        if self._linha[59:69].strip().isnumeric():
            self._dados[4] = reg_vert.le_registro(self._linha, 59)

    def escreve(self, arq: IO):
        linha = (f"{UH.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "       " +
                 f"{round(self._dados[2], 2)}".rjust(6) + "               " +
                 f"{int(self._dados[3])}")
        if self._dados[4] != -1.0:
            linha += "                   "
            linha += f"{round(self._dados[4], 2)}".rjust(10)
        linha += "\n"
        arq.write(linha)

    @property
    def codigo(self) -> int:
        return self._dados[0]

    @property
    def ree(self) -> int:
        return self._dados[1]

    @property
    def volume_inicial(self) -> float:
        return self._dados[2]

    @volume_inicial.setter
    def volume_inicial(self, v: float):
        self._dados[2] = v

    @property
    def evaporacao(self) -> bool:
        return self._dados[3]

    @evaporacao.setter
    def evaporacao(self, e: bool):
        self._dados[3] = e


class CT(RegistroDadger):
    """
    Registro que contém o cadastro das usinas termelétricas com
    os seus custos e capacidades.
    """
    mnemonico = "CT"

    def __init__(self):
        super().__init__(CT.mnemonico, True)
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
        self._dados[4] = reg_inflex.le_registro(self._linha, 29)
        self._dados[5] = reg_disp.le_registro(self._linha, 34)
        self._dados[6] = reg_cvu.le_registro(self._linha, 39)
        self._dados[7] = reg_inflex.le_registro(self._linha, 49)
        self._dados[8] = reg_disp.le_registro(self._linha, 54)
        self._dados[9] = reg_cvu.le_registro(self._linha, 59)
        self._dados[10] = reg_inflex.le_registro(self._linha, 69)
        self._dados[11] = reg_disp.le_registro(self._linha, 74)
        self._dados[12] = reg_cvu.le_registro(self._linha, 79)

    def escreve(self, arq: IO):

        linha = (f"{CT.mnemonico}".ljust(4) +
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
        return self._dados[0]

    @property
    def subsistema(self) -> int:
        return self._dados[1]

    @property
    def nome(self) -> str:
        return self._dados[2]

    @nome.setter
    def nome(self, nome: str):
        self._dados[2] = nome

    @property
    def inflexibilidades(self) -> List[float]:
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
        return self._dados[6::3]

    @cvus.setter
    def cvus(self, cvu: List[float]):
        novas = len(cvu)
        atuais = len(self.cvus)
        if novas != atuais:
            raise ValueError("Número de CVUs incompatível. De" +
                             f"vem ser fornecidas {atuais}, mas foram {novas}")
        self._dados[6::3] = cvu


class UE(RegistroDadger):
    """
    Registro que contém o cadastro das estações de bombeamento
    (usinas elevatórias).
    """
    mnemonico = "UE"

    def __init__(self):
        super().__init__(UE.mnemonico, True)
        self._dados = [0, 0, "", 0, 0, 0.0, 0.0, 0.0]

    def le(self):
        reg_codigo = RegistroIn(3)
        reg_subsis = RegistroIn(2)
        reg_nome = RegistroAn(12)
        reg_montante = RegistroIn(3)
        reg_jusante = RegistroIn(3)
        reg_bomb = RegistroFn(10)
        self._dados[0] = reg_codigo.le_registro(self._linha, 4)
        self._dados[1] = reg_subsis.le_registro(self._linha, 9)
        self._dados[2] = reg_nome.le_registro(self._linha, 14)
        self._dados[3] = reg_montante.le_registro(self._linha, 29)
        self._dados[4] = reg_jusante.le_registro(self._linha, 34)
        self._dados[5] = reg_bomb.le_registro(self._linha, 39)
        self._dados[6] = reg_bomb.le_registro(self._linha, 49)
        self._dados[7] = reg_bomb.le_registro(self._linha, 59)

    def escreve(self, arq: IO):
        linha = (f"{UE.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".zfill(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".ljust(12) + "   " +
                 f"{self._dados[3]}".rjust(3) + "  " +
                 f"{self._dados[4]}".rjust(3) + "  " +
                 f"{self._dados[5]:10.1f}" +
                 f"{self._dados[6]:10.1f}" +
                 f"{self._dados[7]:10.2f}" + "\n")
        arq.write(linha)


class DP(RegistroDadger):
    """
    Registro que contém o cadastro das durações dos patamares.
    """
    mnemonico = "DP"

    def __init__(self):
        super().__init__(DP.mnemonico, True)
        self._dados = [0, 0, 0,
                       0.0, 0.0,
                       0.0, 0.0,
                       0.0, 0.0]

    def le(self):
        reg_estagio = RegistroIn(2)
        reg_subsis = RegistroIn(2)
        reg_num = RegistroIn(1)
        reg_carga = RegistroFn(10)
        reg_duracao = RegistroFn(10)
        self._dados[0] = reg_estagio.le_registro(self._linha, 4)
        self._dados[1] = reg_subsis.le_registro(self._linha, 9)
        self._dados[2] = reg_num.le_registro(self._linha, 14)
        if len(self._linha[19:29].strip()) > 0:
            self._dados[3] = reg_carga.le_registro(self._linha, 19)
        self._dados[4] = reg_duracao.le_registro(self._linha, 29)
        if len(self._linha[39:49].strip()) > 0:
            self._dados[5] = reg_carga.le_registro(self._linha, 39)
        self._dados[6] = reg_duracao.le_registro(self._linha, 49)
        if len(self._linha[59:69].strip()) > 0:
            self._dados[7] = reg_carga.le_registro(self._linha, 59)
        self._dados[8] = reg_duracao.le_registro(self._linha, 69)

    def escreve(self, arq: IO):
        linha = (f"{DP.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(2) + "   " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".rjust(1) + "    ")
        if self._dados[3] != 0.0:
            linha += f"{self._dados[3]:10.1f}"
        else:
            linha += "          "
        linha += f"{self._dados[4]:10.1f}"
        if self._dados[5] != 0.0:
            linha += f"{self._dados[5]:10.1f}"
        else:
            linha += "          "
        linha += f"{self._dados[6]:10.1f}"
        if self._dados[7] != 0.0:
            linha += f"{self._dados[7]:10.1f}"
        else:
            linha += "          "
        linha += f"{self._dados[8]:10.1f}"
        arq.write(linha + "\n")

    @property
    def estagio(self) -> int:
        return self._dados[0]

    @property
    def subsistema(self) -> int:
        return self._dados[1]

    @property
    def num_patamares(self) -> int:
        return self._dados[2]

    @property
    def cargas(self) -> List[float]:
        return self._dados[3::2]

    @cargas.setter
    def cargas(self, c: List[float]):
        novas = len(c)
        atuais = len(self.cargas)
        if novas != atuais:
            raise ValueError("Número de cargas incompatível. De" +
                             f"vem ser fornecidas {atuais}, mas foram {novas}")
        self._dados[3::2] = c

    @property
    def duracoes(self) -> List[float]:
        return self._dados[4::2]

    @duracoes.setter
    def duracoes(self, d: List[float]):
        novas = len(d)
        atuais = len(self.duracoes)
        if novas != atuais:
            raise ValueError("Número de durações incompatível. De" +
                             f"vem ser fornecidas {atuais}, mas foram {novas}")
        self._dados[4::2] = d


class CD(RegistroDadger):
    """
    Registro que contém o cadastro dos custos de déficit.
    """
    mnemonico = "CD"

    def __init__(self):
        super().__init__(CD.mnemonico, True)
        self._dados = [0, 0, "", 0,
                       0.0, 0.0,
                       0.0, 0.0,
                       0.0, 0.0]

    def le(self):
        reg_num_curva = RegistroIn(2)
        reg_subsis = RegistroIn(2)
        reg_nome = RegistroAn(10)
        reg_estagio = RegistroIn(2)
        reg_limite = RegistroFn(5)
        reg_custo = RegistroFn(10)
        self._dados[0] = reg_num_curva.le_registro(self._linha, 4)
        self._dados[1] = reg_subsis.le_registro(self._linha, 9)
        self._dados[2] = reg_nome.le_registro(self._linha, 14)
        self._dados[3] = reg_estagio.le_registro(self._linha, 24)
        self._dados[4] = reg_limite.le_registro(self._linha, 29)
        self._dados[5] = reg_custo.le_registro(self._linha, 34)
        self._dados[6] = reg_limite.le_registro(self._linha, 44)
        self._dados[7] = reg_custo.le_registro(self._linha, 49)
        self._dados[8] = reg_limite.le_registro(self._linha, 59)
        self._dados[9] = reg_custo.le_registro(self._linha, 64)

    def escreve(self, arq: IO):
        linha = (f"{CD.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(2) + "   " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".ljust(10) +
                 f"{self._dados[3]}".rjust(2) + "   " +
                 f"{self._dados[4]:5.0f}" +
                 f"{self._dados[5]:10.2f}" +
                 f"{self._dados[6]:5.0f}" +
                 f"{self._dados[7]:10.2f}" +
                 f"{self._dados[8]:5.0f}" +
                 f"{self._dados[9]:10.2f}" + "\n")
        arq.write(linha)


class PQ(RegistroDadger):
    """
    Registro que contém as gerações de pequenas usinas, não
    incluídas no despacho.
    """
    mnemonico = "PQ"

    def __init__(self):
        super().__init__(PQ.mnemonico, True)
        self._dados = ["", 0, 0, 0.0, 0.0, 0.0]

    def le(self):
        reg_nome = RegistroAn(10)
        reg_subsis = RegistroIn(2)
        reg_estagio = RegistroIn(2)
        reg_custo = RegistroFn(5)
        self._dados[0] = reg_nome.le_registro(self._linha, 4)
        self._dados[1] = reg_subsis.le_registro(self._linha, 15)
        self._dados[2] = reg_estagio.le_registro(self._linha, 19)
        self._dados[3] = reg_custo.le_registro(self._linha, 24)
        self._dados[4] = reg_custo.le_registro(self._linha, 29)
        self._dados[5] = reg_custo.le_registro(self._linha, 34)

    def escreve(self, arq: IO):
        linha = (f"{PQ.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".ljust(10) + " " +
                 f"{self._dados[1]}".rjust(1) + "   " +
                 f"{self._dados[2]}".rjust(2) + "   " +
                 f"{self._dados[3]:5.0f}" +
                 f"{self._dados[4]:5.0f}" +
                 f"{self._dados[5]:5.0f}" + "\n")
        arq.write(linha)


class RI(RegistroDadger):
    """
    Registro que contém as restrições de Itaipu.
    """
    mnemonico = "RI"

    def __init__(self):
        super().__init__(RI.mnemonico, True)
        self._dados = [0, 0, 0,
                       0.0, 0.0, 0.0, 0.0, 0.0,
                       0.0, 0.0, 0.0, 0.0, 0.0,
                       0.0, 0.0, 0.0, 0.0, 0.0]

    def le(self):
        reg_uhe = RegistroIn(3)
        reg_estagio = RegistroIn(2)
        reg_subsis = RegistroIn(3)
        reg_minmax = RegistroFn(7)
        self._dados[0] = reg_uhe.le_registro(self._linha, 4)
        self._dados[1] = reg_estagio.le_registro(self._linha, 9)
        self._dados[2] = reg_subsis.le_registro(self._linha, 13)
        tab = reg_minmax.le_linha_tabela(self._linha, 16, 0, 15)
        for i, t in enumerate(tab, start=3):
            self._dados[i] = t

    def escreve(self, arq: IO):
        linha = (f"{RI.mnemonico}".ljust(3) +
                 f"{self._dados[0]}".rjust(3) + "   " +
                 f"{self._dados[1]}".rjust(2) + "  " +
                 f"{self._dados[2]}".rjust(2) + " ")
        for i in range(3, len(self._dados)):
            linha += f"{self._dados[i]:7.0f}"
        linha += "\n"
        arq.write(linha)


class IA(RegistroDadger):
    """
    Registro que contém os limites de intercâmbio entre os subsistemas.
    """
    mnemonico = "IA"

    def __init__(self):
        super().__init__(IA.mnemonico, True)
        self._dados = [0, "", "",
                       0.0, 0.0,
                       0.0, 0.0,
                       0.0, 0.0]

    def le(self):
        reg_estagio = RegistroIn(2)
        reg_subsis = RegistroAn(2)
        reg_limite = RegistroFn(10)
        self._dados[0] = reg_estagio.le_registro(self._linha, 4)
        self._dados[1] = reg_subsis.le_registro(self._linha, 9)
        self._dados[2] = reg_subsis.le_registro(self._linha, 14)
        tab = reg_limite.le_linha_tabela(self._linha, 19, 0, 6)
        for i, t in enumerate(tab, start=3):
            self._dados[i] = t

    def escreve(self, arq: IO):
        linha = (f"{IA.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(2) + "   " +
                 f"{self._dados[1]}".ljust(2) + "   " +
                 f"{self._dados[2]}".ljust(2) + "   ")
        for i in range(3, len(self._dados)):
            linha += f"{self._dados[i]:10.0f}"
        linha += "\n"
        arq.write(linha)


class TX(RegistroDadger):
    """
    Registro que contém a taxa de desconto anual do modelo.
    """
    mnemonico = "TX"

    def __init__(self):
        super().__init__(TX.mnemonico, True)
        self._dados: float = 0.0

    def le(self):
        reg_linha = RegistroFn(5)
        self._dados = reg_linha.le_registro(self._linha, 4)

    def escreve(self, arq: IO):
        linha = (f"{TX.mnemonico}".ljust(4) +
                 f"{round(self.dados, 2)}".rjust(5) +
                 "\n")
        arq.write(linha)

    @property
    def taxa(self) -> float:
        return self._dados

    @taxa.setter
    def taxa(self, t: float):
        self._dados = t


class GP(RegistroDadger):
    """
    Registro que contém o gap de tolerância para convergência.
    """
    mnemonico = "GP"

    def __init__(self):
        super().__init__(GP.mnemonico, True)
        self._dados: float = 0.0

    def le(self):
        reg_linha = RegistroFn(10)
        self._dados = reg_linha.le_registro(self._linha, 4)

    def escreve(self, arq: IO):
        linha = (f"{GP.mnemonico}".ljust(4) +
                 f"{round(self.dados, 8)}".rjust(10) +
                 "\n")
        arq.write(linha)

    @property
    def gap(self) -> float:
        return self._dados

    @gap.setter
    def gap(self, g: float):
        self._dados = g


class NI(RegistroDadger):
    """
    Registro que contém o número máximo de iterações do modelo.
    """
    mnemonico = "NI"

    def __init__(self):
        super().__init__(NI.mnemonico, True)
        self._dados: int = 0

    def le(self):
        reg_linha = RegistroIn(3)
        self._dados = reg_linha.le_registro(self._linha, 4)

    def escreve(self, arq: IO):
        linha = f"{NI.mnemonico}".ljust(4) + f"{self.dados}".rjust(3) + "\n"
        arq.write(linha)

    @property
    def iteracoes(self) -> int:
        return self._dados

    @iteracoes.setter
    def iteracoes(self, i: int):
        self._dados = i


class DT(RegistroDadger):
    """
    Registro que contém a data de referência do estudo.
    """
    mnemonico = "DT"

    def __init__(self):
        super().__init__(DT.mnemonico, True)
        self._dados = [0, 0, 0]

    def le(self):
        reg_diames = RegistroIn(2)
        reg_ano = RegistroIn(4)
        self._dados[0] = reg_diames.le_registro(self._linha, 4)
        self._dados[1] = reg_diames.le_registro(self._linha, 9)
        self._dados[2] = reg_ano.le_registro(self._linha, 14)

    def escreve(self, arq: IO):
        linha = (f"{DT.mnemonico}".ljust(4) +
                 f"{self.dados[0]}".rjust(2) + "   " +
                 f"{self.dados[1]}".zfill(2) + "   " +
                 f"{self.dados[2]}".rjust(4) + "\n")
        arq.write(linha)

    @property
    def dia(self) -> int:
        return self._dados[0]

    @dia.setter
    def dia(self, d: int):
        self._dados[0] = d

    @property
    def mes(self) -> int:
        return self._dados[1]

    @mes.setter
    def mes(self, m: int):
        self._dados[1] = m

    @property
    def ano(self) -> int:
        return self._dados[2]

    @ano.setter
    def ano(self, a: int):
        self._dados[2] = a


class MP(RegistroDadger):
    """
    Registro que contém as manutenções programadas das UHEs.
    """
    mnemonico = "MP"

    def __init__(self):
        super().__init__(MP.mnemonico, True)
        self._dados = [0, 0]

    def le(self):
        reg_uhe = RegistroIn(3)
        reg_frequencia = RegistroIn(2)
        reg_manutencao = RegistroFn(5)
        self._dados[0] = reg_uhe.le_registro(self._linha, 4)
        if self._linha[7:9].strip().isnumeric():
            self._dados[1] = reg_frequencia.le_registro(self._linha, 7)
        ci = 9
        for i in range(2, 26):
            cf = ci + 5
            if len(self._linha[ci:cf].strip()) < 5:
                break
            self._dados.append(reg_manutencao.le_registro(self._linha, ci))
            ci = cf

    def escreve(self, arq: IO):
        linha = (f"{MP.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3))
        linha += "  " if self._dados[1] == 0 else f"{self._dados[1]}"
        for i in range(2, len(self._dados)):
            linha += f"{self._dados[i]:1.3f}"
        linha += "\n"
        arq.write(linha)


class MT(RegistroDadger):
    """
    Registro que contém as manutenções programadas das UTEs.
    """
    mnemonico = "MT"

    def __init__(self):
        super().__init__(MT.mnemonico, True)
        self._dados = [0, 0]

    def le(self):
        reg_ute = RegistroIn(3)
        reg_subsis = RegistroIn(2)
        reg_manutencao = RegistroFn(5)
        self._dados[0] = reg_ute.le_registro(self._linha, 4)
        self._dados[1] = reg_subsis.le_registro(self._linha, 9)
        ci = 14
        for i in range(2, 26):
            cf = ci + 5
            if len(self._linha[ci:cf].strip()) < 5:
                break
            self._dados.append(reg_manutencao.le_registro(self._linha, ci))
            ci = cf

    def escreve(self, arq: IO):
        linha = (f"{MT.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   ")
        for i in range(2, len(self._dados)):
            linha += f"{self._dados[i]:1.3f}"
        linha += "\n"
        arq.write(linha)


class FD(RegistroDadger):
    """
    Registro que contém os fatores de disponibilidade das UHEs.
    """
    mnemonico = "FD"

    def __init__(self):
        super().__init__(FD.mnemonico, True)
        self._dados = [0, 0]

    def le(self):
        reg_uhe = RegistroIn(3)
        reg_manutencao = RegistroFn(5)
        reg_frequencia = RegistroIn(2)
        self._dados[0] = reg_uhe.le_registro(self._linha, 4)
        if self._linha[7:9].strip().isnumeric():
            self._dados[1] = reg_frequencia.le_registro(self._linha, 7)
        ci = 9
        for i in range(2, 25):
            cf = ci + 5
            if len(self._linha[ci:cf].strip()) < 5:
                break
            self._dados.append(reg_manutencao.le_registro(self._linha, ci))
            ci = cf

    def escreve(self, arq: IO):
        linha = (f"{FD.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3))
        linha += "  " if self._dados[1] == 0 else f"{self._dados[1]}"
        for i in range(2, len(self._dados)):
            linha += f"{self._dados[i]:1.3f}"
        linha += "\n"
        arq.write(linha)


class VE(RegistroDadger):
    """
    Registro que contém os volumes de espera das UHEs.
    """
    mnemonico = "VE"

    def __init__(self):
        super().__init__(VE.mnemonico, True)
        self._dados = [0]

    def le(self):
        reg_uhe = RegistroIn(3)
        reg_manutencao = RegistroFn(5)
        self._dados[0] = reg_uhe.le_registro(self._linha, 4)
        ci = 9
        for i in range(1, 25):
            cf = ci + 5
            if len(self._linha[ci:cf].strip()) < 5:
                break
            self._dados.append(reg_manutencao.le_registro(self._linha, ci))
            ci = cf

    def escreve(self, arq: IO):
        linha = (f"{VE.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  ")
        for i in range(1, len(self._dados)):
            linha += f"{round(self._dados[i], 2)}"
        linha += "\n"
        arq.write(linha)


class RE(RegistroDadger):
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
        linha = (f"{RE.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".rjust(2) + "\n")
        arq.write(linha)

    @property
    def codigo(self) -> int:
        return self._dados[0]

    @property
    def estagio_inicial(self) -> int:
        return self._dados[1]

    @property
    def estagio_final(self) -> int:
        return self._dados[2]


class LU(RegistroDadger):
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
        linha = (f"{LU.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   ")
        for i in range(2, len(self._dados)):
            if self._dados[i] != LU.default:
                linha += f"{round(self._dados[i], 2)}".rjust(10)
            else:
                linha += "          "

        arq.write(linha + "\n")

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
    def limites_inferiores(self) -> List[float]:
        return self._dados[2::2]

    @limites_inferiores.setter
    def limites_inferiores(self, lim: List[float]):
        novos = len(lim)
        atuais = len(self.limites_inferiores)
        if novos != atuais:
            raise ValueError("Número de limites incompatível. De" +
                             f"vem ser fornecidos {atuais}, mas foram {novos}")
        self._dados[2::2] = lim

    @property
    def limites_superiores(self) -> List[float]:
        return self._dados[3::2]

    @limites_superiores.setter
    def limites_superiores(self, lim: List[float]):
        novos = len(lim)
        atuais = len(self.limites_superiores)
        if novos != atuais:
            raise ValueError("Número de limites incompatível. De" +
                             f"vem ser fornecidos {atuais}, mas foram {novos}")
        self._dados[3::2] = lim


class FU(RegistroDadger):
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
        linha = (f"{FU.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".rjust(3) + "  " +
                 f"{round(self._dados[3], 2)}".rjust(10))
        if self._dados[4] != 0:
            linha += f" {self._dados[4]}"
        linha += "\n"
        arq.write(linha)


class FT(RegistroDadger):
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
        linha = (f"{FT.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".rjust(3) + "  " +
                 f"{self._dados[3]}".rjust(2) + "   " +
                 f"{round(self._dados[4], 2)}".rjust(10))
        linha += "\n"
        arq.write(linha)


class FI(RegistroDadger):
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
        linha = (f"{FI.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".rjust(2) + "   " +
                 f"{self._dados[3]}".rjust(2) + "   " +
                 f"{round(self._dados[4], 2)}".rjust(10))
        linha += "\n"
        arq.write(linha)


class VI(RegistroDadger):
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
        linha = (f"{VI.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(3) + "  ")
        for i in range(2, len(self._dados)):
            linha += f"{round(self._dados[i], 2)}".rjust(5)
        linha += "\n"
        arq.write(linha)

    @property
    def uhe(self) -> int:
        return self._dados[0]

    @property
    def duracao(self) -> int:
        return self._dados[1]

    @duracao.setter
    def duracao(self, d: int):
        self._dados[1] = d

    @property
    def vazoes(self) -> List[float]:
        return self._dados[2:]

    @vazoes.setter
    def vazoes(self, v: List[float]):
        novos = len(v)
        atuais = len(self.vazoes)
        if novos != atuais:
            raise ValueError("Número de vazões incompatível. De" +
                             f"vem ser fornecidos {atuais}, mas foram {novos}")
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
        linha = (f"{self._dados[0]}".rjust(5) +
                 f"{round(self._dados[1], 2)}".rjust(10))
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
        linha = (f"{self._dados[0]}".rjust(5) +
                 f"{round(self._dados[1], 3)}".rjust(15))
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
        linha = (f"{self._dados[0]}".rjust(5) +
                 f"{round(self._dados[1], 3)}".rjust(15))
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
        self._dados[1] = reg_coef.le_registro(self._linha, 29)

    @property
    def linha_escrita(self) -> str:
        linha = (f"{self._dados[0]}".rjust(5) +
                 f"{self._dados[1]}".rjust(5) +
                 f"{round(self._dados[2], 3)}".rjust(15))
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
        linha = (f"{self._dados[0]}".rjust(5) +
                 f"{self._dados[1]}".rjust(5))
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
        linha = (f"{self._dados[0]}".rjust(5) +
                 f"{self._dados[1]}".rjust(5))
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
        linha = (f"{self._dados[0]}".rjust(5) +
                 f"{round(self._dados[1], 1)}".rjust(10))
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
        if len(self._linha[19:24]) == 5:
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


class AC(RegistroDadger):
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
                                                 ACCOTVAZ,
                                                 ACCOFEVA,
                                                 ACNUMCON,
                                                 ACNUMMAQ,
                                                 ACPOTEFE,
                                                 ACJUSMED,
                                                 ACVERTJU,
                                                 ACVAZMIN,
                                                 ACJUSENA,
                                                 ACVSVERT,
                                                 ACVMDESV,
                                                 ACNPOSNW
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
            raise ValueError(f"Mnemônico {self._dados[1]} não" +
                             " suportado para registro AC")

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
        linha = (f"{AC.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(6))
        linha = linha.ljust(19)
        linha += self._modificacao.linha_escrita
        if any([
                self._dados[2] != "",
                self._dados[3] != 0,
                self._dados[4] != 0
               ]):
            linha = linha.ljust(69)
            linha += self._dados[2]
            if self._dados[3] != 0:
                linha += f"  {self._dados[3]}"
            if self._dados[4] != 0:
                linha += f" {self._dados[4]}"

        linha += "\n"
        arq.write(linha)


class IR(RegistroDadger):
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
        linha = (f"{IR.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".ljust(7))
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
        return self._dados[0]


class CI(RegistroDadger):
    """
    Registro que define contratos de importação de energia.
    """
    mnemonico = "CI"

    def __init__(self):
        super().__init__(CI.mnemonico, True)
        self._dados = [0, 0, "", 0,
                       0.0, 0.0, 0.0,
                       0.0, 0.0, 0.0,
                       0.0, 0.0, 0.0,
                       0.0]

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
            self._dados[4 + i * 3] = reg_limite.le_registro(self._linha,
                                                            29 + i * 20)
            self._dados[5 + i * 3] = reg_limite.le_registro(self._linha,
                                                            34 + i * 20)
            self._dados[6 + i * 3] = reg_custo.le_registro(self._linha,
                                                           39 + i * 20)
        if self._linha[89:94].strip().isnumeric():
            self._dados[13] = reg_fator.le_registro(self._linha, 89)

    def escreve(self, arq: IO):
        linha = (f"{CI.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".zfill(3) + " " +
                 f"{self._dados[1]}".rjust(2) + " " +
                 f"{self._dados[2]}".ljust(10) + "   " +
                 f"{self._dados[3]}".rjust(2) + "   ")
        for i in range(3):
            linha += f"{round(self._dados[4 + i * 3], 1)}".rjust(5)
            linha += f"{round(self._dados[5 + i * 3], 1)}".rjust(5)
            linha += f"{round(self._dados[6 + i * 3], 2)}".rjust(10)
        if self._dados[13] != 0.0:
            linha += f"{round(self._dados[13], 2)}".rjust(5)
        linha += "\n"
        arq.write(linha)


class CE(RegistroDadger):
    """
    Registro que define contratos de importação de energia.
    """
    mnemonico = "CE"

    def __init__(self):
        super().__init__(CE.mnemonico, True)
        self._dados = [0, 0, "", 0,
                       0.0, 0.0, 0.0,
                       0.0, 0.0, 0.0,
                       0.0, 0.0, 0.0,
                       0.0]

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
            self._dados[4 + i * 3] = reg_limite.le_registro(self._linha,
                                                            29 + i * 20)
            self._dados[5 + i * 3] = reg_limite.le_registro(self._linha,
                                                            34 + i * 20)
            self._dados[6 + i * 3] = reg_custo.le_registro(self._linha,
                                                           39 + i * 20)
        if self._linha[89:94].strip().isnumeric():
            self._dados[13] = reg_fator.le_registro(self._linha, 89)

    def escreve(self, arq: IO):
        linha = (f"{CE.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".zfill(3) + " " +
                 f"{self._dados[1]}".rjust(2) + " " +
                 f"{self._dados[2]}".ljust(10) + "   " +
                 f"{self._dados[3]}".rjust(2) + "   ")
        for i in range(3):
            linha += f"{round(self._dados[4 + i * 3], 1)}".rjust(5)
            linha += f"{round(self._dados[5 + i * 3], 1)}".rjust(5)
            linha += f"{round(self._dados[6 + i * 3], 2)}".rjust(10)
        if self._dados[13] != 0.0:
            linha += f"{round(self._dados[13], 2)}".rjust(5)
        linha += "\n"
        arq.write(linha)


class FC(RegistroDadger):
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
        reg_nome = RegistroAn(60)
        self._dados[0] = reg_mne.le_registro(self._linha, 4)
        self._dados[1] = reg_nome.le_registro(self._linha, 14)

    def escreve(self, arq: IO):
        linha = (f"{FC.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".ljust(6) + "    " +
                 self._dados[1] + "\n")
        arq.write(linha)

    @property
    def tipo(self) -> str:
        return self._dados[0]

    @property
    def caminho(self) -> str:
        return self._dados[1]

    @caminho.setter
    def caminho(self, c: str):
        self._dados[1] = c


class TI(RegistroDadger):
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
        linha = (f"{TI.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  ")
        for i in range(1, len(self._dados)):
            linha += f"{round(self._dados[i], 2)}".rjust(5)
        linha += "\n"
        arq.write(linha)

    @property
    def codigo(self) -> int:
        return self._dados[0]

    @property
    def taxas(self) -> List[float]:
        return self._dados[1:]

    @taxas.setter
    def taxas(self, tx: List[float]):
        novas = len(tx)
        atuais = len(self.taxas)
        if novas != atuais:
            raise ValueError("Número de taxas incompatível. De" +
                             f"vem ser fornecidas {atuais}, mas foram {novas}")
        self._dados[1:] = tx


class RQ(RegistroDadger):
    """
    Registro que contém as vazões mínimas históricas.
    """
    mnemonico = "RQ"

    def __init__(self):
        super().__init__(RQ.mnemonico, True)
        self._dados = [0]

    def le(self):
        reg_ree = RegistroIn(2)
        reg_irrig = RegistroFn(5)
        self._dados[0] = reg_ree.le_registro(self._linha, 4)
        ci = 9
        for i in range(24):
            cf = ci + 5
            if len(self._linha[ci:cf].strip()) == 0:
                break
            self._dados.append(reg_irrig.le_registro(self._linha, ci))
            ci = cf

    def escreve(self, arq: IO):
        linha = (f"{RQ.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(2) + "   ")
        for i in range(1, len(self._dados)):
            linha += f"{round(self._dados[i], 2)}".rjust(5)
        linha += "\n"
        arq.write(linha)


class EZ(RegistroDadger):
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
        linha = (f"{EZ.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{round(self._dados[1], 2)}".rjust(5) + "\n")
        arq.write(linha)


class HV(RegistroDadger):
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
        linha = (f"{HV.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".rjust(2) + "\n")
        arq.write(linha)

    @property
    def codigo(self) -> int:
        return self._dados[0]

    @property
    def estagio_inicial(self) -> int:
        return self._dados[1]

    @property
    def estagio_final(self) -> int:
        return self._dados[2]


class LV(RegistroDadger):
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
        linha = (f"{LV.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   ")
        for i in range(2, len(self._dados)):
            if self._dados[i] != LV.default:
                linha += f"{round(self._dados[i], 2)}".rjust(10)
            else:
                linha += "          "

        arq.write(linha + "\n")

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
    def limite_inferior(self) -> float:
        return self._dados[2]

    @limite_inferior.setter
    def limite_inferior(self, lim: float):
        self._dados[2] = lim

    @property
    def limites_superior(self) -> float:
        return self._dados[3]

    @limites_superior.setter
    def limites_superior(self, lim: float):
        self._dados[3] = lim


class CV(RegistroDadger):
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
        linha = (f"{CV.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".rjust(3) + "  " +
                 f"{round(self._dados[3], 8)}".rjust(10))
        linha = linha.ljust(34)
        linha += self._dados[4]
        linha += "\n"
        arq.write(linha)


class HQ(RegistroDadger):
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
        linha = (f"{HQ.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "  " +
                 f"{self._dados[2]}".rjust(2) + "\n")
        arq.write(linha)

    @property
    def codigo(self) -> int:
        return self._dados[0]

    @property
    def estagio_inicial(self) -> int:
        return self._dados[1]

    @property
    def estagio_final(self) -> int:
        return self._dados[2]


class LQ(RegistroDadger):
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
        linha = (f"{LQ.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   ")
        for i in range(2, len(self._dados)):
            if self._dados[i] != LQ.default:
                linha += f"{round(self._dados[i], 2)}".rjust(10)
            else:
                linha += "          "

        arq.write(linha + "\n")

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
    def limites_inferiores(self) -> List[float]:
        return self._dados[2::2]

    @limites_inferiores.setter
    def limites_inferiores(self, lim: List[float]):
        novos = len(lim)
        atuais = len(self.limites_inferiores)
        if novos != atuais:
            raise ValueError("Número de limites incompatível. De" +
                             f"vem ser fornecidos {atuais}, mas foram {novos}")
        self._dados[2::2] = lim

    @property
    def limites_superiores(self) -> List[float]:
        return self._dados[3::2]

    @limites_superiores.setter
    def limites_superiores(self, lim: List[float]):
        novos = len(lim)
        atuais = len(self.limites_superiores)
        if novos != atuais:
            raise ValueError("Número de limites incompatível. De" +
                             f"vem ser fornecidos {atuais}, mas foram {novos}")
        self._dados[3::2] = lim


class CQ(RegistroDadger):
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
        linha = (f"{CQ.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(2) + "   " +
                 f"{self._dados[2]}".rjust(3) + "  " +
                 f"{round(self._dados[3], 2)}".rjust(10))
        linha = linha.ljust(34)
        linha += self._dados[4]
        linha += "\n"
        arq.write(linha)


class AR(RegistroDadger):
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
        linha = (f"{AR.mnemonico}".ljust(4) + " " +
                 f"{self.dados}".rjust(3) + "\n")
        arq.write(linha)


class EV(RegistroDadger):
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
        linha = (f"{EV.mnemonico}".ljust(4) +
                 f"{self._dados[0]}" + "    " +
                 f"{self._dados[1]}".rjust(3) + "\n")
        arq.write(linha)


class FJ(RegistroDadger):
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
        linha = (f"{FJ.mnemonico}".ljust(4) +
                 f"{self.dados}".rjust(12) + "\n")
        arq.write(linha)


class HE(RegistroDadger):
    """
    Registro que contém o cadastro de uma restrição de volume
    mínimo armazenado.
    """
    mnemonico = "HE"

    def __init__(self):
        super().__init__(HE.mnemonico, True)
        self._dados = [0, 0, 0.0, 0, 0.0, 0]

    def le(self):
        reg_cod = RegistroIn(3)
        reg_tipo_limite = RegistroIn(1)
        reg_limite = RegistroFn(10)
        reg_estagio = RegistroIn(2)
        reg_penal = RegistroFn(10)
        reg_inviab = RegistroIn(1)
        self._dados[0] = reg_cod.le_registro(self._linha, 4)
        self._dados[1] = reg_tipo_limite.le_registro(self._linha, 9)
        self._dados[2] = reg_limite.le_registro(self._linha, 14)
        self._dados[3] = reg_estagio.le_registro(self._linha, 25)
        self._dados[4] = reg_penal.le_registro(self._linha, 28)
        if self._linha[43].isnumeric():
            self._dados[5] = reg_inviab.le_registro(self._linha, 43)

    def escreve(self, arq: IO):
        linha = (f"{HE.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}" + "    " +
                 f"{round(self._dados[2], 2)}".rjust(10) + " " +
                 f"{self._dados[3]}".rjust(2) + " " +
                 f"{round(self._dados[4], 2)}".rjust(10) + "     " +
                 f"{self._dados[5]}")
        linha += "\n"
        arq.write(linha)

    @property
    def codigo(self) -> int:
        return self._dados[0]

    @property
    def tipo_limite(self) -> int:
        return self._dados[1]

    @tipo_limite.setter
    def tipo_limite(self, t: int):
        self._dados[1] = t

    @property
    def limite(self) -> float:
        return self._dados[2]

    @limite.setter
    def limite(self, lim: float):
        self._dados[2] = lim

    @property
    def estagio(self) -> int:
        return self._dados[3]

    @estagio.setter
    def estagio(self, e: int):
        self._dados[3] = e

    @property
    def penalidade(self) -> float:
        return self._dados[4]

    @penalidade.setter
    def penalidade(self, p: float):
        self._dados[4] = p

    @property
    def tipo_penalidade(self) -> int:
        return self._dados[5]

    @tipo_penalidade.setter
    def tipo_penalidade(self, t: int):
        self._dados[5] = t


class CM(RegistroDadger):
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
        linha = (f"{CM.mnemonico}".ljust(4) +
                 f"{self._dados[0]}".rjust(3) + "  " +
                 f"{self._dados[1]}".rjust(3) + "  " +
                 f"{formata_numero(self._dados[2], 2, 10)}")
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


class LeituraDadger:
    """
    Classe com utilidades gerais para leitura de arquivos
    do DECOMP com comentários.
    """
    def __init__(self,
                 diretorio: str):
        self._usa_backup = False
        self._linha_backup = ""
        self._diretorio = diretorio
        self._linhas_fora_registros: Dict[float, str] = {}
        self._registros: List[RegistroDadger] = []
        self._registros_encontrados: List[RegistroDadger] = []
        self._registros_lidos: List[RegistroDadger] = []

    def _le_linha_com_backup(self, arq: IO) -> str:
        """
        Faz uma leitura de linha de um arquivo, mas com a opção de usar
        um backup de leitura anterior sinalizado anteriormente.
        """
        linha = ""
        if self._usa_backup:
            self._usa_backup = False
            linha = self._linha_backup
        else:
            linha = arq.readline()
            self._linha_backup = linha
        return linha

    def _configura_backup(self):
        """
        Prepara a próxima leitura para ser uma feita a partir de um
        backup armazenado.
        """
        self._usa_backup = True

    def _lista_arquivos_por_chave(self, chave: str) -> List[str]:
        """
        Retorna a lista de caminhos completos para os arquivos em um
        diretório, desde que tenham uma certa chave no nome.
        """
        return [f for f in os.listdir(self._diretorio) if chave in f]

    def _verifica_inicio_registros(self,
                                   linha: str,
                                   ordem: int,
                                   registros: List[RegistroDadger]) -> bool:
        """
        Verifica se a linha atual é a linha de início de algum
        dos registros a serem lidos.
        """
        for i, b in enumerate(registros):
            if b.e_inicio_de_registro(linha):
                b.inicia_registro(linha, ordem)
                self._registros_encontrados.append(registros.pop(i))
                return True

        self._linhas_fora_registros[ordem] = linha
        return False

    def _le_registros_encontrados(self,
                                  registros: List[RegistroDadger]):
        """
        Faz a leitura dos registros encontrados até o momento e que
        ainda não foram lidos.
        """
        for i, b in enumerate(registros):
            if b.encontrado:
                res = b.le_registro()
                self._registros_lidos.append(registros.pop(i))
                return res

    def _le_registros_arquivo(self, arq: IO):
        """
        Faz a leitura dos registros de dados do arquivo.
        """
        self._registros = self._cria_registros_leitura()
        linha = ""
        i = 0
        while True:
            # Decide se lê uma linha nova ou usa a última lida
            linha = self._le_linha_com_backup(arq)
            if self._fim_arquivo(linha):
                self._prepara_dados_saida()
                break

            self._verifica_inicio_registros(linha, i, self._registros)
            # Caso a função de leitura retorne True, é configurado
            #  o backup da linha atual.
            bkp = self._le_registros_encontrados(self._registros_encontrados)
            if bkp:
                self._linha_backup = bkp
                self._configura_backup()
            i += 1

    def _le_arquivo_em_diretorio(self,
                                 diretorio: str,
                                 nome_arquivo: str) -> None:
        """
        Faz a leitura do arquivo em um diretorio.
        """
        try:
            caminho = os.path.join(diretorio, nome_arquivo)
            with open(caminho, "r") as arq:
                self._le_registros_arquivo(arq)
        except Exception:
            print_exc()

    def _cria_registros_leitura(self) -> List[RegistroDadger]:
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
        te: List[RegistroDadger] = [TE()]
        sb: List[RegistroDadger] = [SB() for _ in range(MAX_SUBSIS)]
        uh: List[RegistroDadger] = [UH() for _ in range(MAX_UHE)]
        ct: List[RegistroDadger] = [CT() for _ in range(MAX_UTE)]
        ue: List[RegistroDadger] = [UE() for _ in range(MAX_UE)]
        dp: List[RegistroDadger] = [DP() for _ in
                                    range(MAX_SUBSIS * MAX_ESTAGIOS)]
        cd: List[RegistroDadger] = [CD() for _ in range(MAX_SUBSIS)]
        pq: List[RegistroDadger] = [PQ() for _ in
                                    range(MAX_SUBSIS * MAX_ESTAGIOS)]
        ri: List[RegistroDadger] = [RI() for _ in range(MAX_ESTAGIOS)]
        ia: List[RegistroDadger] = [IA() for _ in
                                    range(MAX_SUBSIS * MAX_SUBSIS)]
        tx: List[RegistroDadger] = [TX()]
        gp: List[RegistroDadger] = [GP()]
        ni: List[RegistroDadger] = [NI()]
        dt: List[RegistroDadger] = [DT()]
        mp: List[RegistroDadger] = [MP() for _ in range(MAX_UHE)]
        mt: List[RegistroDadger] = [MT() for _ in range(MAX_UTE)]
        fd: List[RegistroDadger] = [FD() for _ in range(MAX_UHE)]
        ve: List[RegistroDadger] = [VE() for _ in range(MAX_UHE)]
        re: List[RegistroDadger] = [RE() for _ in range(MAX_RE)]
        lu: List[RegistroDadger] = [LU() for _ in
                                    range(MAX_RE * MAX_ESTAGIOS)]
        fu: List[RegistroDadger] = [FU() for _ in range(MAX_RE)]
        ft: List[RegistroDadger] = [FT() for _ in range(MAX_RE)]
        vi: List[RegistroDadger] = [VI(), VI()]
        ac: List[RegistroDadger] = [AC() for _ in
                                    range(MAX_UHE * MAX_AC_UHE)]
        ir: List[RegistroDadger] = [IR() for _ in range(MAX_RELATORIOS)]
        fc: List[RegistroDadger] = [FC(), FC()]
        ti: List[RegistroDadger] = [TI() for _ in range(MAX_UHE)]
        rq: List[RegistroDadger] = [RE() for _ in range(MAX_REE)]
        ez: List[RegistroDadger] = [EZ() for _ in range(MAX_UHE)]
        hv: List[RegistroDadger] = [HV() for _ in range(MAX_UHE)]
        lv: List[RegistroDadger] = [LV() for _ in
                                    range(MAX_UHE * MAX_ESTAGIOS)]
        cv: List[RegistroDadger] = [CV() for _ in range(MAX_UHE)]
        hq: List[RegistroDadger] = [HQ() for _ in range(MAX_UHE)]
        lq: List[RegistroDadger] = [LQ() for _ in
                                    range(MAX_UHE * MAX_ESTAGIOS)]
        cq: List[RegistroDadger] = [CQ() for _ in
                                    range(MAX_UHE * MAX_ESTAGIOS)]
        ar: List[RegistroDadger] = [AR()]
        ev: List[RegistroDadger] = [EV()]
        fj: List[RegistroDadger] = [FJ()]
        he: List[RegistroDadger] = [HE() for _ in
                                    range(MAX_REE * MAX_ESTAGIOS)]
        cm: List[RegistroDadger] = [CM() for _ in
                                    range(MAX_REE * MAX_ESTAGIOS)]
        return (te + sb + uh + ct + ue + dp + cd + pq +
                ri + ia + tx + gp + ni + dt + mp + mt +
                fd + ve + re + lu + fu + ft + vi + ac +
                ir + fc + ti + rq + ez + hv + lv + cv +
                hq + lq + cq + ar + ev + fj + he + cm)

    def _prepara_dados_saida(self):
        """
        Trata os dados obtidos do arquivo para ser retornado.
        """
        self._registros = self._registros_lidos

    def _fim_arquivo(self, linha: str) -> bool:
        """
        Método que deve ser implementado para cada arquivo, com o
        conteúdo da linha que indica o fim do próprio, para impedir loops
        de leitura eterna.
        """
        return len(linha) == 0

    def le_arquivo(self, nome_arquivo: str) -> DadosDadger:
        """
        Método para ler um arquivo e retornar o objeto
        devido da classe em particular.
        """
        self._le_arquivo_em_diretorio(self._diretorio,
                                      nome_arquivo)
        return DadosDadger(self._registros,
                           self._linhas_fora_registros)


class EscritaDadger:
    """
    Classe com utilidades gerais para a escrita de arquivos
    do DECOMP.
    """
    def __init__(self,
                 diretorio: str):
        self._diretorio = diretorio

    def _escreve_blocos_e_linhas(self,
                                 arq: IO,
                                 blocos: List[RegistroDadger],
                                 linhas: Dict[float, str]):

        ordem_blocos = [b._ordem for b in blocos]
        ordem_linhas = list(linhas.keys())
        itens = ordem_blocos + ordem_linhas
        itens.sort()
        for i in itens:
            if i in ordem_blocos:
                blocos[ordem_blocos.index(i)].escreve(arq)
            elif i in ordem_linhas:
                arq.write(linhas[i])

    def escreve_arquivo(self,
                        dados: DadosDadger,
                        nome_arquivo: str):
        """
        """
        try:
            if not os.path.exists(self._diretorio):
                os.makedirs(self._diretorio)
            caminho = os.path.join(self._diretorio, nome_arquivo)
            with open(caminho, "w") as arq:
                self._escreve_blocos_e_linhas(arq,
                                              dados.registros,
                                              dados.linhas_fora_registros)
        except Exception as e:
            print_exc()
            raise e
