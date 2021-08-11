from idecomp.decomp.modelos.dadger import LeituraDadger
from idecomp.decomp.modelos.dadger import TE, SB, UH, CT, UE, DP, CD, PQ  # noqa
from idecomp.decomp.modelos.dadger import RI, IA, TX, GP, NI, DT, MP, MT  # noqa
from idecomp.decomp.modelos.dadger import FD, VE, RE, LU, FU, FT, FI, VI  # noqa
from idecomp.decomp.modelos.dadger import AC, IR, CI, CE, FC, TI, RQ, EZ  # noqa
from idecomp.decomp.modelos.dadger import HV, LV, CV, HQ, LQ, CQ, AR, EV  # noqa
from idecomp.decomp.modelos.dadger import FJ, HE, CM  # noqa
from idecomp.decomp.modelos.dadger import EscritaDadger
from idecomp._utils.dadosdadger import DadosDadger

from copy import deepcopy
from typing import Type, List, Optional, TypeVar, Any


class Dadger:
    """
    Armazena os dados de entrada do DECOMP

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP no `dadger.rvx`.

    """

    T = TypeVar("T")

    def __init__(self,
                 dados: DadosDadger) -> None:
        self._dados = dados

    def __eq__(self, o: object) -> bool:
        """
        A igualdade entre arquivos avalia os dados interpretados e
        também os comentários externos.
        """
        if not isinstance(o, Dadger):
            return False
        d: Dadger = o
        dif = False
        for (i1, l1), (i2, l2) in zip(self.linhas_fora_registros.items(),
                                      d.linhas_fora_registros.items()):
            if i1 != i2 or l1 != l2:
                dif = True
                break
        for b1, b2 in zip(self._registros,
                          d._registros):
            if b1 != b2:
                dif = True
                break
        return not dif

    @property
    def linhas_fora_registros(self):
        return self._dados.linhas_fora_registros

    @property
    def _registros(self):
        return self._dados.registros

    # Override
    @classmethod
    def le_arquivo(cls,
                   diretorio: str,
                   nome_arquivo="dadger.rv0") -> 'Dadger':
        """
        """
        leitor = LeituraDadger(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    def escreve_arquivo(self,
                        diretorio: str,
                        nome_arquivo="dadger.rv0"):
        escritor = EscritaDadger(diretorio)
        escritor.escreve_arquivo(self._dados, nome_arquivo)

    def __obtem_registro(self,
                         tipo: Type[T]) -> T:
        """
        """
        for b in self._registros:
            if isinstance(b, tipo):
                return b
        raise ValueError(f"Não foi encontrado um registro do tipo {tipo}")

    def __obtem_registro_do_estagio(self,
                                    tipo: Type[T],
                                    codigo: int,
                                    estagio: int) -> Optional[T]:
        regs: List[Any] = self.__obtem_registros(tipo)
        for r in regs:
            if all([r.codigo == codigo,
                    r.estagio == estagio]):
                return r
        return None

    def __obtem_registros(self,
                          tipo: Type[T]) -> List[T]:
        """
        """
        registros = []
        for b in self._registros:
            if isinstance(b, tipo):
                registros.append(b)
        return registros

    @property
    def te(self) -> TE:
        r = self.__obtem_registro(TE)
        return r

    def sb(self, codigo: int) -> SB:
        regs: List[SB] = self.__obtem_registros(SB)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro SB" +
                         f" para o código {codigo}")

    def uh(self, codigo: int) -> UH:
        regs: List[UH] = self.__obtem_registros(UH)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro UH" +
                         f" para a UHE {codigo}")

    def ct(self, codigo: int) -> CT:
        regs: List[CT] = self.__obtem_registros(CT)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro CT" +
                         f" para a UTE {codigo}")

    def dp(self, estagio: int, subsistema: int) -> DP:
        regs: List[DP] = self.__obtem_registros(DP)
        for r in regs:
            if all([r.estagio == estagio,
                    r.subsistema == subsistema]):
                return r
        raise ValueError("Não foi encontrado registro DP" +
                         f" para o subsistema {subsistema}" +
                         f" no estágio {estagio})")

    @property
    def tx(self) -> TX:
        return self.__obtem_registro(TX)

    @property
    def gp(self) -> GP:
        return self.__obtem_registro(GP)

    @property
    def ni(self) -> NI:
        return self.__obtem_registro(NI)

    @property
    def dt(self) -> DT:
        return self.__obtem_registro(DT)

    def re(self, codigo: int) -> RE:
        regs: List[RE] = self.__obtem_registros(RE)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro RE" +
                         f" com código {codigo}")

    def lu(self, codigo: int, estagio: int) -> LU:

        def cria_registro(modelo: LU,
                          estagio_final: int) -> LU:
            copia = deepcopy(modelo)
            copia.estagio = estagio
            # Procura pelo registro do próximo estágio
            proximo = None
            for est in range(estagio, estagio_final + 1):
                r = self.__obtem_registro_do_estagio(LU, codigo, est)
                if r is not None:
                    proximo = r
                    break
            if proximo is not None:
                delta = (proximo._ordem - modelo._ordem) / 2.0
            else:
                delta = 0.1
            copia._ordem += delta
            self._registros.append(copia)
            return copia

        # Obtém o registro RE associado
        re = self.re(codigo)
        # Confere se o estágio pedido está no intervalo
        # do registro RE
        if not (re.estagio_inicial <= estagio <= re.estagio_final):
            raise ValueError(f"Estágio {estagio} fora dos limites" +
                             " do registro RE")
        # Tenta obter um registro já existente
        reg = self.__obtem_registro_do_estagio(LU, codigo, estagio)
        if reg is not None:
            return reg
        # Se não conseguir, cria mais um registro, idêntico ao do
        # último estágio existente, e retorna.
        for est in range(re.estagio_inicial, estagio):
            r = self.__obtem_registro_do_estagio(LU, codigo, est)
            if r is not None:
                reg = r
        if reg is None:
            raise ValueError("Registro não encontrado")
        return cria_registro(reg, re.estagio_final)

    def vi(self, uhe: int) -> VI:
        regs: List[VI] = self.__obtem_registros(VI)
        for r in regs:
            if r.uhe == uhe:
                return r
        raise ValueError("Não foi encontrado registro VI" +
                         f" para a UHE {uhe}")

    def ir(self, tipo: str) -> IR:
        regs: List[IR] = self.__obtem_registros(IR)
        for r in regs:
            if r.tipo == tipo:
                return r
        raise ValueError("Não foi encontrado registro IR" +
                         f" com mnemônico {tipo}")

    def fc(self, tipo: str) -> FC:
        regs: List[FC] = self.__obtem_registros(FC)
        for r in regs:
            if r.tipo == tipo:
                return r
        raise ValueError("Não foi encontrado registro FC" +
                         f" com mnemônico {tipo}")

    def ti(self, codigo: int) -> TI:
        regs: List[TI] = self.__obtem_registros(TI)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro TI" +
                         f" para a UHE {codigo}")

    def hv(self, codigo: int) -> HV:
        regs: List[HV] = self.__obtem_registros(HV)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro HV" +
                         f" para UHE {codigo}")

    def lv(self, codigo: int, estagio: int) -> LV:

        def cria_registro(modelo: LV,
                          estagio_final: int) -> LV:
            copia = deepcopy(modelo)
            copia.estagio = estagio
            # Procura pelo registro do próximo estágio
            proximo = None
            for est in range(estagio, estagio_final + 1):
                r = self.__obtem_registro_do_estagio(LV, codigo, est)
                if r is not None:
                    proximo = r
                    break
            if proximo is not None:
                delta = (proximo._ordem - modelo._ordem) / 2.0
            else:
                delta = 0.1
            copia._ordem += delta
            self._registros.append(copia)
            return copia

        # Obtém o registro HV associado
        hv = self.hv(codigo)
        # Confere se o estágio pedido está no intervalo
        # do registro HV
        if not (hv.estagio_inicial <= estagio <= hv.estagio_final):
            raise ValueError(f"Estágio {estagio} fora dos limites" +
                             " do registro HV")
        # Tenta obter um registro já existente
        reg = self.__obtem_registro_do_estagio(LV, codigo, estagio)
        if reg is not None:
            return reg
        # Se não conseguir, cria mais um registro, idêntico ao do
        # último estágio existente, e retorna.
        for est in range(hv.estagio_inicial, estagio):
            r = self.__obtem_registro_do_estagio(LV, codigo, est)
            if r is not None:
                reg = r
        if reg is None:
            raise ValueError("Registro não encontrado")
        return cria_registro(reg, hv.estagio_final)

    def hq(self, codigo: int) -> HQ:
        regs: List[HQ] = self.__obtem_registros(HQ)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro HQ" +
                         f" com o código {codigo}")

    def lq(self, codigo: int, estagio: int) -> LQ:

        def cria_registro(modelo: LQ,
                          estagio_final: int) -> LQ:
            copia = deepcopy(modelo)
            copia.estagio = estagio
            # Procura pelo registro do próximo estágio
            proximo = None
            for est in range(estagio, estagio_final + 1):
                r = self.__obtem_registro_do_estagio(LQ, codigo, est)
                if r is not None:
                    proximo = r
                    break
            if proximo is not None:
                delta = (proximo._ordem - modelo._ordem) / 2.0
            else:
                delta = 0.1
            copia._ordem += delta
            self._registros.append(copia)
            return copia

        # Obtém o registro HQ associado
        hq = self.hq(codigo)
        # Confere se o estágio pedido está no intervalo
        # do registro HQ
        if not (hq.estagio_inicial <= estagio <= hq.estagio_final):
            raise ValueError(f"Estágio {estagio} fora dos limites" +
                             " do registro HQ")
        # Tenta obter um registro já existente
        reg = self.__obtem_registro_do_estagio(LQ, codigo, estagio)
        if reg is not None:
            return reg
        # Se não conseguir, cria mais um registro, idêntico ao do
        # último estágio existente, e retorna.
        for est in range(hq.estagio_inicial, estagio):
            r = self.__obtem_registro_do_estagio(LQ, codigo, est)
            if r is not None:
                reg = r
        if reg is None:
            raise ValueError("Registro não encontrado")
        return cria_registro(reg, hq.estagio_final)

    def he(self, codigo: int, estagio: int) -> HE:
        r = self.__obtem_registro_do_estagio(HE,
                                             codigo,
                                             estagio)
        if r is not None:
            return r
        else:
            raise ValueError("Registro não encontrado")
