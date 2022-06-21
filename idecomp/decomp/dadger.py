from idecomp.decomp.modelos.dadger import (
    TE,
    SB,
    UH,
    CT,
    UE,
    DP,
    CD,
    FP,
    RI,
    IA,
    TX,
    GP,
    NI,
    DT,
    MP,
    MT,
    FD,
    VE,
    RE,
    LU,
    FU,
    FT,
    FI,
    VI,
    IR,
    CI,
    CE,
    FC,
    TI,
    RQ,
    EZ,
    RT,
    HV,
    LV,
    CV,
    HQ,
    LQ,
    CQ,
    AR,
    EV,
    FJ,
    HE,
    CM,
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
)


from cfinterface.files.registerfile import RegisterFile
from cfinterface.components.state import ComponentState
from cfinterface.components.register import Register
from typing import Type, List, Optional, TypeVar, Any, Union


class Dadger(RegisterFile):
    """
    Armazena os dados de entrada gerais do DECOMP.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP no `dadger.rvx`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    Atualmente, são suportados os registros:
    `TE`, `SB`, `UH`, `CT`, `DP`, `TX`, `GP`, `NI`, `DT`, `RE`, `LU`,
    `VI`, `IR`, `FC`, `TI`, `HV`, `LV`, `HQ`, `LQ` `HE`, `EV` e `FJ`.

    É possível ler as informações existentes em arquivos a partir do
    método `le_arquivo()` e escreve um novo arquivo a partir do método
    `escreve_arquivo()`.

    """

    T = TypeVar("T")

    AC = Union[
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

    REGISTERS = [
        TE,
        SB,
        UH,
        CT,
        UE,
        DP,
        CD,
        FP,
        RI,
        IA,
        TX,
        GP,
        NI,
        DT,
        MP,
        MT,
        FD,
        VE,
        RE,
        LU,
        FU,
        FT,
        FI,
        VI,
        IR,
        CI,
        CE,
        FC,
        TI,
        RQ,
        EZ,
        RT,
        HV,
        LV,
        CV,
        HQ,
        LQ,
        CQ,
        AR,
        EV,
        FJ,
        HE,
        CM,
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

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="dadger.rv0") -> "Dadger":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="dadger.rv0"):
        self.write(diretorio, nome_arquivo)

    def __registros_por_tipo(self, registro: Type[T]) -> List[T]:
        """
        Obtém um gerador de blocos de um tipo, se houver algum no arquivo.
        :param bloco: Um tipo de bloco para ser lido
        :type bloco: T
        :param indice: O índice do bloco a ser acessado, dentre os do tipo
        :type indice: int
        """
        return [b for b in self.data.of_type(registro)]

    def __obtem_registro(self, tipo: Type[T]) -> Optional[T]:
        """ """
        r = self.__obtem_registros(tipo)
        return r[0] if len(r) > 0 else None

    def __obtem_registro_com_codigo(
        self, tipo: Type[T], codigo: int
    ) -> Optional[T]:
        regs: List[Any] = self.__registros_por_tipo(tipo)
        for r in regs:
            if r.codigo == codigo:
                return r
        return None

    def __obtem_registro_do_estagio(
        self, tipo: Type[T], codigo: int, estagio: int
    ) -> Optional[T]:
        regs: List[Any] = self.__registros_por_tipo(tipo)
        for r in regs:
            if all([r.codigo == codigo, r.estagio == estagio]):
                return r
        return None

    def __obtem_registro_do_subsistema(
        self, tipo: Type[T], codigo: int, subsistema: int
    ) -> Optional[T]:
        regs: List[Any] = self.__registros_por_tipo(tipo)
        for r in regs:
            if all([r.codigo == codigo, r.subsistema == subsistema]):
                return r
        return None

    def __obtem_registro_do_estagio_para_subsistema(
        self, tipo: Type[T], estagio: int, subsistema: int
    ) -> Optional[T]:
        regs: List[Any] = self.__registros_por_tipo(tipo)
        for r in regs:
            if all([r.estagio == estagio, r.subsistema == subsistema]):
                return r
        return None

    def __obtem_registros(self, tipo: Type[T]) -> List[T]:
        return self.__registros_por_tipo(tipo)

    def cria_registro(self, anterior: Register, registro: Register):
        """
        Adiciona um registro ao arquivo após um outro registro previamente
        existente.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.add_after(anterior, registro)

    def deleta_registro(self, registro: Register):
        """
        Remove um registro existente no arquivo.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.remove(registro)

    def lista_registros(self, tipo: Type[T]) -> List[T]:
        """
        Lista todos os registros presentes no arquivo que tenham o tipo `T`.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        return [r for r in self.data.of_type(tipo)]

    @property
    def te(self) -> Optional[TE]:
        """
        Obtém o (único) registro que define o nome do estudo no
        :class:`Dadger`

        :return: Um registro do tipo :class:`TE`.
        """
        return self.__obtem_registro(TE)

    def sb(self, codigo: int) -> Optional[SB]:
        """
        Obtém um registro que define os subsistemas existentes
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            do subsistema
        :type codigo: int
        :return: Um registro do tipo :class:`SB`
        """
        return self.__obtem_registro_com_codigo(SB, codigo)

    def uh(self, codigo: int) -> Optional[UH]:
        """
        Obtém um registro que define uma usina hidrelétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da UHE
        :type codigo: int
        :return: Um registro do tipo :class:`UH`
        """
        return self.__obtem_registro_com_codigo(UH, codigo)

    def ct(self, codigo: int, estagio: int) -> Optional[CT]:
        """
        Obtém um registro que define uma usina termelétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da UTE
        :type codigo: int
        :param estagio: Índice do estágio associado ao registro
        :type estagio: int
        :return: Um registro do tipo :class:`CT`
        """
        return self.__obtem_registro_do_estagio(CT, codigo, estagio)

    def dp(self, estagio: int, subsistema: int) -> Optional[DP]:
        """
        Obtém um registro que define as durações dos patamares
        no estudo descrito pelo :class:`Dadger`.

        :param estagio: Índice do estágio sobre o qual serão
            definidas as durações dos patamares
        :type estagio: int
        :param subsistema: Índice do subsistema para o qual
            valerão os patamares.
        :type subsistema: int
        :return: Um registro do tipo :class:`DP`
        """
        return self.__obtem_registro_do_estagio_para_subsistema(
            DP, estagio, subsistema
        )

    def ac(
        self,
        uhe: int,
        modificacao: Any,
        mes: str = None,
        semana: int = None,
        ano: int = None,
    ) -> Optional[AC]:
        """
        Obtém um registro que define modificações nos parâmetros
        das UHE em um :class:`Dadger`.

        :param uhe: código da UHE modificada
        :type uhe: int
        :param modificacao: classe da modificação realizada
        :type modificacao: subtipos do tipo `AC`
        :return: Um registro do tipo :class:`AC`
        """

        def __atende(r: Dadger.AC) -> bool:
            condicoes: List[bool] = [
                r.uhe == uhe,
            ]
            if mes is not None:
                condicoes.append(r.mes == mes)
            if semana is not None:
                condicoes.append(r.semana == semana)
            if ano is not None:
                condicoes.append(r.ano == ano)
            return all(condicoes)

        regs: List[Dadger.AC] = self.__obtem_registros(modificacao)
        for r in regs:
            if __atende(r):
                return r
        return None

    def cd(self, numero_curva: int, subsistema: int) -> Optional[CD]:
        """
        Obtém um registro que define as curvas de déficit
        no estudo descrito pelo :class:`Dadger`.

        :param numero_curva: Índice da curva de déficit
            descrita
        :type numero_curva: int
        :param subsistema: Índice do subsistema para o qual
            valerá a curva.
        :type subsistema: int
        :return: Um registro do tipo :class:`CD`
        """
        regs: List[CD] = self.__registros_por_tipo(CD)
        for r in regs:
            if all(
                [r.numero_curva == numero_curva, r.subsistema == subsistema]
            ):
                return r
        return None

    @property
    def tx(self) -> Optional[TX]:
        """
        Obtém o (único) registro que define a taxa de desconto
        aplicada no estudo definido no :class:`Dadger`

        :return: Um registro do tipo :class:`TX`.
        """
        return self.__obtem_registro(TX)

    @property
    def gp(self) -> Optional[GP]:
        """
        Obtém o (único) registro que define o gap para convergência
        considerado no estudo definido no :class:`Dadger`

        :return: Um registro do tipo :class:`GP`.
        """
        return self.__obtem_registro(GP)

    @property
    def ni(self) -> Optional[NI]:
        """
        Obtém o (único) registro que define o número máximo de iterações
        do DECOMP no estudo definido no :class:`Dadger`

        :return: Um registro do tipo :class:`NI`.
        """
        return self.__obtem_registro(NI)

    @property
    def dt(self) -> Optional[DT]:
        """
        Obtém o (único) registro que define a data de referência do
        estudo definido no :class:`Dadger`

        :return: Um registro do tipo :class:`DT`.
        """
        return self.__obtem_registro(DT)

    def re(self, codigo: int) -> Optional[RE]:
        """
        Obtém um registro que cadastra uma restrição elétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição elétrica
        :type codigo: int
        :return: Um registro do tipo :class:`RE`
        """
        return self.__obtem_registro_com_codigo(RE, codigo)

    def lu(self, codigo: int, estagio: int) -> Optional[LU]:
        """
        Obtém um registro que especifica os limites inferiores e
        superiores por patamar de uma restrição elétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição elétrica
        :type codigo: int
        :param estagio: Estágio sobre o qual valerão os limites da
            restrição elétricas
        :type estagio: int
        :return: Um registro do tipo :class:`LU`

        **Exemplos**

        Para um objeto :class:`Dadger` que possua uma restrição RE
        de código 1, definida para os estágios de 1 a 5, com limites
        LU definidos apenas para o estágio 1, estes podem ser acessados com:

        >>> lu = dadger.lu(1, 1)
        >>> lu
            <idecomp.decomp.modelos.dadger.LU object at 0x0000026E5C269550>

        Se for acessado o registro LU de um estágio fora dos limites da
        restrição RE, isso resultará em um erro:

        >>> dadger.lu(1, 7)
            Traceback (most recent call last):
            ...
            ValueError: Estágio 7 fora dos limites do registro RE

        Por outro lado, se for acessado o registro LU em um estágio dentro
        dos limites do registro RE, porém sem limites próprios definidos,
        será criado um registro idêntico ao do último estágio existente,
        e este será retornado:

        >>> lu2 = dadger.lu(1, 5)
        >>> lu.limites_inferiores == lu2.limites_inferiores
            True

        """

        def cria_registro() -> Optional[LU]:
            re = self.__obtem_registro_com_codigo(RE, codigo)
            if re is None:
                return re
            ei = re.estagio_inicial
            ef = re.estagio_final
            ultimo_registro = None
            if ei is not None and ef is not None:
                for e in range(ei, ef + 1):
                    registro_estagio = self.__obtem_registro_do_estagio(
                        LU, codigo, e
                    )
                    if registro_estagio is not None:
                        ultimo_registro = registro_estagio
            if isinstance(ultimo_registro, LU):
                novo_registro = LU(
                    state=ComponentState.READ_SUCCESS,
                    data=[None] * len(ultimo_registro.data),
                )
                novo_registro.codigo = ultimo_registro.codigo
                novo_registro.limites_inferiores = (
                    ultimo_registro.limites_inferiores
                )
                novo_registro.limites_superiores = (
                    ultimo_registro.limites_superiores
                )
                novo_registro.estagio = estagio
                self.data.add_after(ultimo_registro, novo_registro)
                return novo_registro
            return None

        lu = self.__obtem_registro_do_estagio(LU, codigo, estagio)
        if lu is None:
            lu = cria_registro()
        return lu

    def vi(self, uhe: int) -> Optional[VI]:
        """
        Obtém um registro que especifica os tempos de viagem da
        água em uma UHE existente no no estudo descrito
        pelo :class:`Dadger`.

        :param uhe: Índice da UHE associada aos tempos de viagem
        :type uhe: int
        :return: Um registro do tipo :class:`VI`
        """
        regs: List[VI] = self.__obtem_registros(VI)
        for r in regs:
            if r.uhe == uhe:
                return r
        return None

    def ir(self, tipo: str) -> Optional[IR]:
        """
        Obtém um registro que especifica os relatórios de saída
        a serem produzidos pelo DECOMP após a execução do estudo
        descrito no :class:`Dadger`.

        :param tipo: Mnemônico do tipo de relatório especificado
            no registro
        :type tipo: str
        :return: Um registro do tipo :class:`IR`
        """
        regs: List[IR] = self.__obtem_registros(IR)
        for r in regs:
            if r.tipo == tipo:
                return r
        return None

    def rt(self, mnemonico: str) -> Optional[RT]:
        """
        Obtém um registro que especifica uma retirada de restrição
        de soleira de vertedouro ou canal de desvio.

        :param mnemonico: Mnemônico da restrição retirada (CRISTA ou
            DESVIO)
        :type mnemonico: str
        :return: Um registro do tipo :class:`RT`
        """
        regs: List[RT] = self.__obtem_registros(RT)
        for r in regs:
            if r.restricao == mnemonico:
                return r
        return None

    def fc(self, tipo: str) -> Optional[FC]:
        """
        Obtém um registro que especifica os caminhos para os
        arquivos com a FCF do NEWAVE.

        :param tipo: Mnemônico do tipo de FCF especificado
            no registro
        :type tipo: str
        :return: Um registro do tipo :class:`FC`
        """
        regs: List[FC] = self.__obtem_registros(FC)
        for r in regs:
            if r.tipo == tipo:
                return r
        return None

    def ti(self, codigo: int) -> Optional[TI]:
        """
        Obtém um registro que especifica as taxas de irrigação
        por posto (UHE) existente no estudo especificado no :class:`Dadger`

        :param codigo: Código do posto da UHE associada
            no registro
        :type codigo: int
        :return: Um registro do tipo :class:`TI`
        """
        regs: List[TI] = self.__obtem_registros(TI)
        for r in regs:
            if r.codigo == codigo:
                return r
        return None

    def fp(self, codigo: int, estagio: int) -> Optional[FP]:
        """
        Obtém um registro que especifica as taxas de irrigação
        por posto (UHE) existente no estudo especificado no :class:`Dadger`

        :param codigo: Código do posto da UHE associada
            no registro
        :type codigo: int
        :param estagio: Estágio de definição da FP da UHE
        :type estagio: int
        :return: Um registro do tipo :class:`FP`
        """
        r = self.__obtem_registro_do_estagio(FP, codigo, estagio)
        if r is not None:
            return r
        else:
            return None

    def rq(self, ree: int) -> Optional[RQ]:
        """
        Obtém um registro que especifica as vazões mínimas históricas
        por REE existentes no estudo especificado no :class:`Dadger`

        :param ree: Código do REE
        :type ree: int
        :return: Um registro do tipo :class:`RQ`
        """
        regs: List[RQ] = self.__obtem_registros(RQ)
        for r in regs:
            if r.ree == ree:
                return r
        return None

    def ve(self, codigo: int) -> Optional[VE]:
        """
        Obtém um registro que especifica os volumes de espera
        por posto (UHE) existente no estudo especificado no :class:`Dadger`

        :param codigo: Código do posto da UHE associada
        :type codigo: int
        :return: Um registro do tipo :class:`VE`
        """
        regs: List[VE] = self.__obtem_registros(VE)
        for r in regs:
            if r.codigo == codigo:
                return r
        return None

    def hv(self, codigo: int) -> Optional[HV]:
        """
        Obtém um registro que cadastra uma restrição de volume mínimo
        armazenado existente no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição de volume mínimo
        :type codigo: int
        :return: Um registro do tipo :class:`HV`
        """
        regs: List[HV] = self.__obtem_registros(HV)
        for r in regs:
            if r.codigo == codigo:
                return r
        return None

    def lv(self, codigo: int, estagio: int) -> Optional[LV]:
        """
        Obtém um registro que especifica os limites inferior e
        superior de uma restrição de volume mínimo existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição de volume mínimo
        :type codigo: int
        :param estagio: Estágio sobre o qual valerão os limites da
            restrição
        :type estagio: int
        :return: Um registro do tipo :class:`LV`

        **Exemplos**

        Para um objeto :class:`Dadger` que possua uma restrição HV
        de código 1, definida para os estágios de 1 a 5, com limites
        LV definidos apenas para o estágio 1, estes podem ser acessados com:

        >>> lv = dadger.lv(1, 1)
        >>> lv
            <idecomp.decomp.modelos.dadger.LV object at 0x0000026E5C269550>

        Se for acessado o registro LV de um estágio fora dos limites da
        restrição HV, isso resultará em um erro:

        >>> dadger.lv(1, 7)
            Traceback (most recent call last):
            ...
            ValueError: Estágio 7 fora dos limites do registro HV

        Por outro lado, se for acessado o registro LV em um estágio dentro
        dos limites do registro HV, porém sem limites próprios definidos,
        será criado um registro idêntico ao do último estágio existente,
        e este será retornado:

        >>> lv2 = dadger.lv(1, 5)
        >>> lv.limite_inferior == lv2.limite_inferior
            True

        """

        def cria_registro() -> Optional[LV]:
            hv = self.__obtem_registro_com_codigo(HV, codigo)
            if hv is None:
                return hv
            ei = hv.estagio_inicial
            ef = hv.estagio_final
            ultimo_registro = None
            if ei is not None and ef is not None:
                for e in range(ei, ef + 1):
                    registro_estagio = self.__obtem_registro_do_estagio(
                        LV, codigo, e
                    )
                    if registro_estagio is not None:
                        ultimo_registro = registro_estagio
            if isinstance(ultimo_registro, LV):
                novo_registro = LV(
                    state=ComponentState.READ_SUCCESS,
                    data=[None] * len(ultimo_registro.data),
                )
                novo_registro.codigo = codigo
                novo_registro.limite_inferior = ultimo_registro.limite_inferior
                novo_registro.limite_superior = ultimo_registro.limite_superior
                novo_registro.estagio = estagio
                self.data.add_after(ultimo_registro, novo_registro)
                return novo_registro
            return None

        lv = self.__obtem_registro_do_estagio(LV, codigo, estagio)
        if lv is None:
            lv = cria_registro()
        return lv

    def hq(self, codigo: int) -> Optional[HQ]:
        """
        Obtém um registro que cadastra uma restrição de vazão
        existente no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição de vazão
        :type codigo: int
        :return: Um registro do tipo :class:`HQ`
        """
        regs: List[HQ] = self.__obtem_registros(HQ)
        for r in regs:
            if r.codigo == codigo:
                return r
        return None

    def lq(self, codigo: int, estagio: int) -> Optional[LQ]:
        """
        Obtém um registro que especifica os limites inferiores e
        superiores por patamar de uma restrição de vazão existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição de vazão
        :type codigo: int
        :param estagio: Estágio sobre o qual valerão os limites da
            restrição de vazão
        :type estagio: int
        :return: Um registro do tipo :class:`LQ`

        **Exemplos**

        Para um objeto :class:`Dadger` que possua uma restrição HQ
        de código 1, definida para os estágios de 1 a 5, com limites
        LQ definidos apenas para o estágio 1, estes podem ser acessados com:

        >>> lq = dadger.lq(1, 1)
        >>> lq
            <idecomp.decomp.modelos.dadger.LQ object at 0x0000026E5C269550>

        Se for acessado o registro LQ de um estágio fora dos limites da
        restrição HQ, isso resultará em um erro:

        >>> dadger.lq(1, 7)
            Traceback (most recent call last):
            ...
            ValueError: Estágio 7 fora dos limites do registro HQ

        Por outro lado, se for acessado o registro LQ em um estágio dentro
        dos limites do registro HQ, porém sem limites próprios definidos,
        será criado um registro idêntico ao do último estágio existente,
        e este será retornado:

        >>> lq2 = dadger.lq(1, 5)
        >>> lq.limites_inferiores == lq2.limites_inferiores
            True

        """

        def cria_registro() -> Optional[LQ]:
            hq = self.__obtem_registro_com_codigo(HQ, codigo)
            if hq is None:
                return hq
            ei = hq.estagio_inicial
            ef = hq.estagio_final
            ultimo_registro = None
            if ei is not None and ef is not None:
                for e in range(ei, ef + 1):
                    registro_estagio = self.__obtem_registro_do_estagio(
                        LQ, codigo, e
                    )
                    if registro_estagio is not None:
                        ultimo_registro = registro_estagio
            if isinstance(ultimo_registro, LQ):
                novo_registro = LQ(
                    state=ComponentState.READ_SUCCESS,
                    data=[None] * len(ultimo_registro.data),
                )
                novo_registro.codigo = codigo
                novo_registro.limites_superiores = (
                    ultimo_registro.limites_superiores
                )
                novo_registro.limites_inferiores = (
                    ultimo_registro.limites_inferiores
                )
                novo_registro.estagio = estagio
                self.data.add_after(ultimo_registro, novo_registro)
                return novo_registro
            return None

        lq = self.__obtem_registro_do_estagio(LQ, codigo, estagio)
        if lq is None:
            lq = cria_registro()
        return lq

    def he(self, codigo: int, estagio: int) -> Optional[HE]:
        """
        Obtém um registro que cadastra uma restrição de energia
        armazenada existente no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição de energia armazenada
        :type codigo: int
        :param estagio: Índice do estágio para o qual vale a
            restrição de energia armazenada
        :type estagio: int
        :return: Um registro do tipo :class:`HE`
        """
        r = self.__obtem_registro_do_estagio(HE, codigo, estagio)
        if r is not None:
            return r
        else:
            return None

    def cm(self, codigo: int) -> Optional[CM]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        de energia armazenada.

        :param codigo: Índice do código que especifica o registro
        :type codigo: int
        :return: Um registro do tipo :class:`CM`
        """
        regs: List[CM] = self.__obtem_registros(CM)
        for r in regs:
            if r.codigo == codigo:
                return r
        return None

    @property
    def ev(self) -> Optional[EV]:
        """
        Obtém o (único) registro que define a evaporação
        :class:`Dadger`

        :return: Um registro do tipo :class:`EV`.
        """
        return self.__obtem_registro(EV)

    @property
    def fj(self) -> Optional[FJ]:
        """
        Obtém o (único) registro que define o arquivo `polinjus`
        :class:`Dadger`

        :return: Um registro do tipo :class:`FJ`.
        """
        return self.__obtem_registro(FJ)
