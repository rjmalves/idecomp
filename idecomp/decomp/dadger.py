from idecomp.decomp.modelos.dadger import (
    TE,
    SB,
    UH,
    CT,
    UE,
    DP,
    PQ,
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
    EA,
    ES,
    QI,
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
    PD,
    PU,
    RC,
    PE,
    TS,
    PV,
    CX,
    FA,
    VT,
    CS,
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
    VL,
    VA,
    VU,
    DA,
)

import pandas  # type: ignore
from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile
from typing import Type, List, Optional, TypeVar, Any, Union


class Dadger(RegisterFile):
    """
    Armazena os dados de entrada gerais do DECOMP.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP no `dadger.rvx`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.


    """

    T = TypeVar("T", bound=Register)

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
        PQ,
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
        EA,
        ES,
        QI,
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
        HE,
        CM,
        FA,
        VT,
        FJ,
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
        VL,
        VA,
        VU,
        DA,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    def __expande_colunas_df(self, df: pandas.DataFrame) -> pandas.DataFrame:
        colunas_com_listas = df.applymap(
            lambda linha: isinstance(linha, list)
        ).all()
        nomes_colunas = [
            c for c in colunas_com_listas[colunas_com_listas].index
        ]
        for c in nomes_colunas:
            num_elementos = len(df.at[0, c])
            particoes_coluna = [
                f"{c}_{i}" for i in range(1, num_elementos + 1)
            ]
            df[particoes_coluna] = df.apply(
                lambda linha: linha[c], axis=1, result_type="expand"
            )
            df.drop(columns=[c], inplace=True)
        return df

    def __registros_ou_df(
        self, t: Type[T], **kwargs
    ) -> Optional[Union[T, List[T], pandas.DataFrame]]:
        if kwargs.get("df"):
            return self.__expande_colunas_df(self._as_df(t))
        else:
            kwargs_sem_df = {k: v for k, v in kwargs.items() if k != "df"}
            return self.data.get_registers_of_type(t, **kwargs_sem_df)

    @property
    def te(self) -> Optional[TE]:
        """
        Obtém o (único) registro que define o nome do estudo no
        :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`TE` | None.
        """
        r = self.data.get_registers_of_type(TE)
        if isinstance(r, TE):
            return r
        else:
            return None

    def sb(
        self,
        codigo_submercado: Optional[int] = None,
        nome_submercado: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[SB, List[SB], pandas.DataFrame]]:
        """
        Obtém um registro que define os submercados existentes
        no estudo descrito pelo :class:`Dadger`.

        :param codigo_submercado: código que especifica o registro do submercado
        :type codigo_submercado: int | None
        :param nome_submercado: nome do submercado
        :type nome_submercado: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`SB` | list[:class:`SB`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            SB,
            codigo_submercado=codigo_submercado,
            nome_submercado=nome_submercado,
            df=df,
        )

    def uh(
        self,
        codigo_usina: Optional[int] = None,
        codigo_ree: Optional[int] = None,
        volume_inicial: Optional[float] = None,
        evaporacao: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[UH, List[UH], pandas.DataFrame]]:
        """
        Obtém um registro que define uma usina hidrelétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo_usina: índice do código que especifica o registro da UHE
        :type codigo_usina: int | None
        :param codigo_ree: índice do ree da UHE
        :type codigo_ree: int | None
        :param volume_inicial: volume inicial da UHE
        :type volume_inicial: float | None
        :param evaporacao: consideração da evaporação na UHE
        :type evaporacao: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`UH` | list[:class:`UH`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            UH,
            codigo_usina=codigo_usina,
            codigo_ree=codigo_ree,
            volume_inicial=volume_inicial,
            evaporacao=evaporacao,
            df=df,
        )

    def ue(
        self,
        codigo_usina: Optional[int] = None,
        codigo_submercado: Optional[int] = None,
        nome_usina: Optional[str] = None,
        codigo_usina_montante: Optional[int] = None,
        codigo_usina_jusante: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[UE, List[UE], pandas.DataFrame]]:
        """
        Obtém um registro que define uma usina elevatória existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo_usina: índice do código que especifica o registro da UHE
        :type codigo_usina: int | None
        :param codigo_submercado: índice do submercado da UHE
        :type codigo_submercado: int | None
        :param nome_usina: nome da UHE
        :type nome_usina: int | None
        :param codigo_usina_montante: código da UHE a montante
        :type codigo_usina_montante: int | None
        :param codigo_usina_jusante: código da UHE a jusante
        :type codigo_usina_jusante: int | None

        :param evaporacao: consideração da evaporação na UHE
        :type evaporacao: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`UE` | list[:class:`UE`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            UH,
            codigo_usina=codigo_usina,
            codigo_submercado=codigo_submercado,
            nome_usina=nome_usina,
            codigo_usina_montante=codigo_usina_montante,
            codigo_usina_jusante=codigo_usina_jusante,
            df=df,
        )

    def ct(
        self,
        codigo_usina: Optional[int] = None,
        estagio: Optional[int] = None,
        codigo_submercado: Optional[int] = None,
        nome_usina: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[CT, List[CT], pandas.DataFrame]]:
        """
        Obtém um registro que define uma usina termelétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo_usina: código que especifica o registro da UTE
        :type codigo_usina: int | None
        :param estagio: estágio associado ao registro
        :type estagio: int | None
        :param codigo_submercado: submercado da UTE
        :type codigo_submercado: str | None
        :param nome_usina: nome da UTE
        :type nome_usina: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`CT` | list[:class:`CT`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            CT,
            codigo_usina=codigo_usina,
            estagio=estagio,
            codigo_submercado=codigo_submercado,
            nome_usina=nome_usina,
            df=df,
        )

    def dp(
        self,
        estagio: Optional[int] = None,
        codigo_submercado: Optional[int] = None,
        numero_patamares: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[DP, List[DP], pandas.DataFrame]]:
        """
        Obtém um registro que define as durações dos patamares
        no estudo descrito pelo :class:`Dadger`.

        :param estagio: estágio sobre o qual serão
            definidas as durações dos patamares
        :type estagio: int | None
        :param codigo_submercado: submercado para o qual
            valerão os patamares.
        :type codigo_submercado: int | None
        :param numero_patamares: número de patamares
        :type numero_patamares: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`DP` | list[:class:`DP`] |
            :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            DP,
            estagio=estagio,
            codigo_submercado=codigo_submercado,
            numero_patamares=numero_patamares,
            df=df,
        )

    def pq(
        self,
        nome: Optional[str] = None,
        codigo_submercado: Optional[int] = None,
        estagio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[PQ, List[PQ], pandas.DataFrame]]:
        """
        Obtém um registro que define as gerações das pequenas usinas
        no estudo descrito pelo :class:`Dadger`.

        :param nome: o nome das gerações
        :param codigo_submercado: submercado para o qual
            valerão as gerações
        :type codigo_submercado: int | None
        :param estagio: estágio sobre o qual serão
            definidas as gerações
        :type estagio: int | None
        :type codigo_submercado: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`PQ` | list[:class:`PQ`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            PQ,
            nome=nome,
            estagio=estagio,
            codigo_submercado=codigo_submercado,
            df=df,
        )

    def ac(
        self,
        codigo_usina: int,
        modificacao: Any,
        df: bool = False,
        **kwargs,
    ) -> Optional[Union[AC, List[AC], pandas.DataFrame]]:
        """
        Obtém um registro que define modificações nos parâmetros
        das UHE em um :class:`Dadger`.

        :param codigo_usina: código da UHE modificada
        :type codigo_usina: int
        :param modificacao: classe da modificação realizada
        :type modificacao: subtipos do tipo `AC`
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: `AC` | list[`AC`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            modificacao, **{"codigo_usina": codigo_usina, **kwargs, "df": df}
        )

    def cd(
        self,
        codigo_curva: Optional[int] = None,
        codigo_submercado: Optional[int] = None,
        nome_curva: Optional[str] = None,
        estagio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[CD, List[CD], pandas.DataFrame]]:
        """
        Obtém um registro que define as curvas de déficit
        no estudo descrito pelo :class:`Dadger`.

        :param codigo_curva: Índice da curva de déficit descrita
        :type codigo_curva: int | None
        :param codigo_submercado: submercado para o qual valerá a curva.
        :type codigo_submercado: int | None
        :param nome_curva: nome da curva.
        :type nome_curva: str | None
        :param estagio: estagio para o qual valerá a curva.
        :type estagio: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`LU` | list[:class:`LU`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            CD,
            codigo_curva=codigo_curva,
            codigo_submercado=codigo_submercado,
            nome_curva=nome_curva,
            estagio=estagio,
            df=df,
        )

    @property
    def tx(self) -> Optional[TX]:
        """
        Obtém o (único) registro que define a taxa de desconto
        aplicada no estudo definido no :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`TX` | None.
        """
        r = self.data.get_registers_of_type(TX)
        if isinstance(r, TX):
            return r
        else:
            return None

    @property
    def gp(self) -> Optional[GP]:
        """
        Obtém o (único) registro que define o gap para convergência
        considerado no estudo definido no :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`GP` | None.
        """
        r = self.data.get_registers_of_type(GP)
        if isinstance(r, GP):
            return r
        else:
            return None

    @property
    def ni(self) -> Optional[NI]:
        """
        Obtém o (único) registro que define o número máximo de iterações
        do DECOMP no estudo definido no :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`NI` | None.
        """
        r = self.data.get_registers_of_type(NI)
        if isinstance(r, NI):
            return r
        else:
            return None

    @property
    def dt(self) -> Optional[DT]:
        """
        Obtém o (único) registro que define a data de referência do
        estudo definido no :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`DT` | None.
        """
        r = self.data.get_registers_of_type(DT)
        if isinstance(r, DT):
            return r
        else:
            return None

    def re(
        self,
        codigo_restricao: Optional[int] = None,
        estagio_inicial: Optional[int] = None,
        estagio_final: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[RE, List[RE], pandas.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição elétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo_restricao: código que especifica o registro
            da restrição elétrica
        :type codigo_restricao: int | None
        :param estagio_inicial: estágio inicial da restrição elétrica
        :type estagio_inicial: int | None
        :param estagio_final: estágio final da restrição elétrica
        :type estagio_final: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RE` | list[:class:`RE`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            RE,
            codigo_restricao=codigo_restricao,
            estagio_inicial=estagio_inicial,
            estagio_final=estagio_final,
            df=df,
        )

    def lu(  # noqa
        self,
        codigo_restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[LU, List[LU], pandas.DataFrame]]:
        """
        Obtém um registro que especifica os limites inferiores e
        superiores por patamar de uma restrição elétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo_restricao: Índice do código que especifica o registro
            da restrição elétrica
        :type codigo_restricao: int | None
        :param estagio: Estágio sobre o qual valerão os limites da
            restrição elétricas
        :type estagio: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`LU` | list[:class:`LU`] | :class:`pandas.DataFrame` | None

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
            re = self.re(codigo_restricao=codigo_restricao)
            if isinstance(re, list) or re is None:
                return None
            ei = re.estagio_inicial
            ef = re.estagio_final
            if any([estagio is None, ei is None, ef is None]):
                return None
            ultimo_registro = None
            if ei is not None and estagio <= ef:  # type: ignore
                for e in range(ei, estagio + 1):  # type: ignore
                    registro_estagio = self.data.get_registers_of_type(
                        LU, codigo_restricao=codigo_restricao, estagio=e
                    )
                    if registro_estagio is not None:
                        ultimo_registro = registro_estagio
            if isinstance(ultimo_registro, LU):
                novo_registro = LU(
                    data=[None] * len(ultimo_registro.data),
                )
                novo_registro.codigo_restricao = (
                    ultimo_registro.codigo_restricao
                )
                novo_registro.limite_inferior = ultimo_registro.limite_inferior
                novo_registro.limite_superior = ultimo_registro.limite_superior
                novo_registro.estagio = estagio
                self.data.add_after(ultimo_registro, novo_registro)
                return novo_registro
            return None

        if df:
            return self.__expande_colunas_df(self._as_df(LU))
        else:
            lu = self.data.get_registers_of_type(
                LU, codigo_restricao=codigo_restricao, estagio=estagio
            )
            if isinstance(lu, list):
                return lu
            if lu is None:
                lu = cria_registro()
            return lu

    def fu(
        self,
        codigo_restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        codigo_usina: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FU, List[FU], pandas.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        elétricas.

        :param codigo_restricao: código que especifica o registro
        :type codigo_restricao: int | None
        :param estagio: o estágio do coeficiente
        :type estagio: int | None
        :param codigo_usina: o código da UHE para a restrição
        :type codigo_usina: int | None
        :param coeficiente: valor do coeficiente para a usina
            na restrição
        :type coeficiente: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FU` | list[:class:`FU`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            FU,
            codigo_restricao=codigo_restricao,
            codigo_usina=codigo_usina,
            estagio=estagio,
            coeficiente=coeficiente,
            df=df,
        )

    def ft(
        self,
        codigo_restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        codigo_usina: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FT, List[FT], pandas.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        elétricas.

        :param codigo_restricao: código que especifica o registro
        :type codigo_restricao: int | None
        :param estagio: o estágio do coeficiente
        :type estagio: int | None
        :param codigo_usina: o código da UTE para a restrição
        :type codigo_usina: int | None
        :param coeficiente: valor do coeficiente para a usina
            na restrição
        :type coeficiente: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FT` | list[:class:`FT`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            FT,
            codigo_restricao=codigo_restricao,
            codigo_usina=codigo_usina,
            estagio=estagio,
            coeficiente=coeficiente,
            df=df,
        )

    def fi(
        self,
        codigo_restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        codigo_submercado_de: Optional[int] = None,
        codigo_submercado_para: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FI, List[FI], pandas.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        elétricas.

        :param codigo_restricao: código que especifica o registro
        :type codigo_restricao: int | None
        :param estagio: o estágio do coeficiente
        :type estagio: int | None
        :param codigo_submercado_de: o código do submercado DE
        :type codigo_submercado_de: int | None
        :param codigo_submercado_para: o código do submercado PARA
        :type codigo_submercado_para: int | None
        :param coeficiente: valor do coeficiente para a interligação
            na restrição
        :type coeficiente: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FI` | list[:class:`FI`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            FI,
            codigo_restricao=codigo_restricao,
            estagio=estagio,
            codigo_submercado_de=codigo_submercado_de,
            codigo_submercado_para=codigo_submercado_para,
            coeficiente=coeficiente,
            df=df,
        )

    def vi(
        self,
        codigo_usina: Optional[int] = None,
        duracao: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[VI, List[VI], pandas.DataFrame]]:
        """
        Obtém um registro que especifica os tempos de viagem da
        água em uma UHE existente no no estudo descrito
        pelo :class:`Dadger`.

        :param codigo_usina: Índice da UHE associada aos tempos de viagem
        :type codigo_usina: int | None
        :param duracao: duração, em horas, da viagem da água
        :type duracao: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`VI` | list[:class:`VI`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            VI, codigo_usina=codigo_usina, duracao=duracao, df=df
        )

    def ir(
        self, tipo: Optional[str] = None, df: bool = False
    ) -> Optional[Union[IR, List[IR], pandas.DataFrame]]:
        """
        Obtém um registro que especifica os relatórios de saída
        a serem produzidos pelo DECOMP após a execução do estudo
        descrito no :class:`Dadger`.

        :param tipo: Mnemônico do tipo de relatório especificado
            no registro
        :type tipo: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`IR` | list[:class:`IR`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(IR, tipo=tipo, df=df)

    def rt(
        self, restricao: Optional[str] = None, df: bool = False
    ) -> Optional[Union[RT, List[RT], pandas.DataFrame]]:
        """
        Obtém um registro que especifica uma retirada de restrição
        de soleira de vertedouro ou canal de desvio.

        :param restricao: Mnemônico da restrição retirada (CRISTA ou
            DESVIO)
        :type restricao: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RT` | list[:class:`RT`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(RT, restricao=restricao, df=df)

    def fc(
        self,
        tipo: Optional[str] = None,
        caminho: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[FC, List[FC], pandas.DataFrame]]:
        """
        Obtém um registro que especifica os caminhos para os
        arquivos com a FCF do NEWAVE.

        :param tipo: Mnemônico do tipo de FCF especificado
            no registro
        :type tipo: str | None
        :param caminho: caminho para o arquivo com a FCF
        :type caminho: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`FC` | list[:class:`FC`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(FC, tipo=tipo, caminho=caminho, df=df)

    def ea(
        self, codigo_ree: Optional[int] = None, df: bool = False
    ) -> Optional[Union[EA, List[EA], pandas.DataFrame]]:
        """
        Obtém um registro que especifica a ENA dos meses anteriores
        ao estudo.

        :param codigo_ree: Código do REE
        :type codigo_ree: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`EA` | list[:class:`EA`] | :class:`pandas.DataFrame` | None
        """
        return self.data.get_registers_of_type(
            EA, codigo_ree=codigo_ree, df=df
        )

    def es(
        self,
        codigo_ree: Optional[int] = None,
        numero_semanas: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[ES, List[ES], pandas.DataFrame]]:
        """
        Obtém um registro que especifica a ENA das semanas anteriores
        ao estudo.

        :param codigo_ree: Código do REE
        :type codigo_ree: int | None
        :param numero_semanas: Número de semanas do mês anterior
        :type numero_semanas: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`ES` | list[:class:`ES`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            ES, codigo_ree=codigo_ree, numero_semanas=numero_semanas, df=df
        )

    def qi(
        self, codigo_usina: Optional[int] = None, df: bool = False
    ) -> Optional[Union[QI, List[QI], pandas.DataFrame]]:
        """
        Obtém um registro que especifica o tempo de viagem
        para cálculo da ENA.

        :param codigo_usina: Código da UHE
        :type codigo_usina: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`QI` | list[:class:`QI`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(QI, codigo_usina=codigo_usina, df=df)

    def ti(
        self, codigo_usina: Optional[int] = None, df: bool = False
    ) -> Optional[Union[TI, List[TI], pandas.DataFrame]]:
        """
        Obtém um registro que especifica as taxas de irrigação
        por posto (UHE) existente no estudo especificado no :class:`Dadger`

        :param codigo_usina: Código da UHE associada ao registro
        :type codigo_usina: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`TI` | list[:class:`TI`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(TI, codigo_usina=codigo_usina, df=df)

    def da(
        self,
        codigo_usina_retirada: Optional[int] = None,
        codigo_usina_retorno: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[DA, List[DA], pandas.DataFrame]]:
        """
        Obtém um registro que especifica as retiradas de água para
        outros usos (desvios de água) por usina (UHE) existente no
        estudo especificado no :class:`Dadger`

        :param codigo_usina_retirada: Código da UHE a montante da qual será feita a retirada
        :type codigo_usina_retirada: int | None
        :param codigo_usina_retorno: Código da UHE a montante da qual se derá o retorno.
        :type codigo_usina_retorno: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`DA` | list[:class:`DA`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            DA,
            codigo_usina_retirada=codigo_usina_retirada,
            codigo_usina_retorno=codigo_usina_retorno,
            df=df,
        )

    def mp(
        self,
        codigo_usina: Optional[int] = None,
        frequencia: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[MP, List[MP], pandas.DataFrame]]:
        """
        Obtém um registro que especifica as manutenções programadas
        por UHE existente no estudo especificado no :class:`Dadger`

        :param codigo_usina: Código da UHE associada ao registro
        :type codigo_usina: int | None
        :param frequencia: Frequência da UHE, quando for Itaipu
        :type frequencia: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`MP` | list[:class:`MP`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            MP, codigo_usina=codigo_usina, frequencia=frequencia, df=df
        )

    def mt(
        self,
        codigo_usina: Optional[int] = None,
        codigo_submercado: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[MT, List[MT], pandas.DataFrame]]:
        """
        Obtém um registro que especifica as manutenções programadas
        por UTE existente no estudo especificado no :class:`Dadger`

        :param codigo_usina: Código da UTE associada ao registro
        :type codigo_usina: int | None
        :param codigo_submercado: Código do submercado da UTE
        :type codigo_submercado: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`MT` | list[:class:`MT`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            MT,
            codigo_usina=codigo_usina,
            codigo_submercado=codigo_submercado,
            df=df,
        )

    def fd(
        self,
        codigo_usina: Optional[int] = None,
        frequencia: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[FD, List[FD], pandas.DataFrame]]:
        """
        Obtém um registro que especifica os fatores de disponibilidade
        por UHE existente no estudo especificado no :class:`Dadger`

        :param codigo_usina: Código da UHE associada ao registro
        :type codigo_usina: int | None
        :param frequencia: Frequência da UHE, quando for Itaipu
        :type frequencia: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`FD` | list[:class:`FD`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            FD, codigo_usina=codigo_usina, frequencia=frequencia, df=df
        )

    def fp(
        self,
        codigo_usina: Optional[int] = None,
        estagio: Optional[int] = None,
        tipo_entrada_janela_turbinamento: Optional[int] = None,
        numero_pontos_turbinamento: Optional[int] = None,
        limite_inferior_janela_turbinamento: Optional[float] = None,
        limite_superior_janela_turbinamento: Optional[float] = None,
        tipo_entrada_janela_volume: Optional[int] = None,
        numero_pontos_volume: Optional[int] = None,
        limite_inferior_janela_volume: Optional[float] = None,
        limite_superior_janela_volume: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FP, List[FP], pandas.DataFrame]]:
        """
        Obtém um registro que especifica as taxas de irrigação
        por posto (UHE) existente no estudo especificado no :class:`Dadger`

        :param codigo_usina: Código da UHE associada ao registro
        :type codigo_usina: int | None
        :param estagio: Estágio de definição da FP da UHE
        :type estagio: int | None
        :param tipo_entrada_janela_turbinamento: unidade de entrada
            dos valores da janela de turbinamento
        :type tipo_entrada_janela_turbinamento: int | None
        :param numero_pontos_turbinamento: número de pontos para
            discretização da janela
        :type numero_pontos_turbinamento: int | None
        :param limite_inferior_janela_turbinamento: limite inferior
            da janela
        :type limite_inferior_janela_turbinamento: float | None
        :param limite_superior_janela_turbinamento: limite superior
            da janela
        :type limite_superior_janela_turbinamento: float | None
        :param tipo_entrada_janela_volume: unidade de entrada
            dos valores da janela de volume
        :type tipo_entrada_janela_volume: int | None
        :param numero_pontos_volume: número de pontos para
            discretização da janela
        :type numero_pontos_volume: int | None
        :param limite_inferior_janela_volume: limite inferior
            da janela
        :type limite_inferior_janela_volume: float | None
        :param limite_superior_janela_volume: limite superior
            da janela
        :type limite_superior_janela_volume: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`FP` | list[:class:`FP`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            FP,
            codigo_usina=codigo_usina,
            estagio=estagio,
            tipo_entrada_janela_turbinamento=tipo_entrada_janela_turbinamento,
            numero_pontos_turbinamento=numero_pontos_turbinamento,
            limite_inferior_janela_turbinamento=limite_inferior_janela_turbinamento,
            limite_superior_janela_turbinamento=limite_superior_janela_turbinamento,
            tipo_entrada_janela_volume=tipo_entrada_janela_volume,
            numero_pontos_volume=numero_pontos_volume,
            limite_inferior_janela_volume=limite_inferior_janela_volume,
            limite_superior_janela_volume=limite_superior_janela_volume,
            df=df,
        )

    def rq(
        self, codigo_ree: Optional[int] = None, df: bool = False
    ) -> Optional[Union[RQ, List[RQ], pandas.DataFrame]]:
        """
        Obtém um registro que especifica as vazões mínimas históricas
        por REE existentes no estudo especificado no :class:`Dadger`

        :param codigo_ree: Código do REE
        :type codigo_ree: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RQ` | list[:class:`RQ`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(RQ, codigo_ree=codigo_ree, df=df)

    def ve(
        self, codigo_usina: Optional[int] = None, df: bool = False
    ) -> Optional[Union[VE, List[VE], pandas.DataFrame]]:
        """
        Obtém um registro que especifica os volumes de espera
        por posto (UHE) existente no estudo especificado no :class:`Dadger`

        :param codigo_usina: Código da UHE associada
        :type codigo_usina: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`VE` | list[:class:`VE`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(VE, codigo_usina=codigo_usina, df=df)

    def hv(
        self,
        codigo_restricao: Optional[int] = None,
        estagio_inicial: Optional[int] = None,
        estagio_final: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[HV, List[HV], pandas.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição de volume mínimo
        armazenado existente no estudo descrito pelo :class:`Dadger`.

        :param codigo_restricao: código que especifica o registro
            da restrição de volume
        :type codigo_restricao: int | None
        :param estagio_inicial: estágio inicial da restrição de volume
        :type estagio_inicial: int | None
        :param estagio_final: estágio final da restrição de volume
        :type estagio_final: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`HV` | list[:class:`HV`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            HV,
            codigo_restricao=codigo_restricao,
            estagio_inicial=estagio_inicial,
            estagio_final=estagio_final,
            df=df,
        )

    def lv(  # noqa
        self,
        codigo_restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[LV, List[LV], pandas.DataFrame]]:
        """
        Obtém um registro que especifica os limites inferior e
        superior de uma restrição de volume mínimo existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo_restricao: Índice do código que especifica o registro
            da restrição de volume
        :type codigo_restricao: int | None
        :param estagio: Estágio sobre o qual valerão os limites da
            restrição de volume
        :type estagio: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`LV` | list[:class:`LV`] | :class:`pandas.DataFrame` | None

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
            hv = self.hv(codigo_restricao=codigo_restricao)
            if isinstance(hv, list) or hv is None:
                return None
            ei = hv.estagio_inicial
            ef = hv.estagio_final
            if any([estagio is None, ei is None, ef is None]):
                return None
            ultimo_registro = None
            if ei is not None and estagio <= ef:  # type: ignore
                for e in range(ei, estagio + 1):  # type: ignore
                    registro_estagio = self.data.get_registers_of_type(
                        LV, codigo_restricao=codigo_restricao, estagio=e
                    )
                    if registro_estagio is not None:
                        ultimo_registro = registro_estagio
            if isinstance(ultimo_registro, LV):
                novo_registro = LV(
                    data=[None] * len(ultimo_registro.data),
                )
                novo_registro.codigo_restricao = codigo_restricao
                novo_registro.limite_inferior = ultimo_registro.limite_inferior
                novo_registro.limite_superior = ultimo_registro.limite_superior
                novo_registro.estagio = estagio
                self.data.add_after(ultimo_registro, novo_registro)
                return novo_registro
            return None

        if df:
            return self.__expande_colunas_df(self._as_df(LV))
        else:
            lv = self.data.get_registers_of_type(
                LV, codigo_restricao=codigo_restricao, estagio=estagio
            )
            if isinstance(lv, list):
                return lv
            if lv is None:
                lv = cria_registro()
            return lv

    def cv(
        self,
        codigo_restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        codigo_usina: Optional[int] = None,
        coeficiente: Optional[float] = None,
        tipo: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[CV, List[CV], pandas.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        de volume.

        :param codigo_restricao: código que especifica o registro
        :type codigo_restricao: int | None
        :param estagio: o estágio do coeficiente
        :type estagio: int | None
        :param codigo_usina: o código da UHE para a restrição
        :type codigo_usina: int | None
        :param coeficiente: valor do coeficiente para a usina
            na restrição
        :type coeficiente: float | None
        :param tipo: o mnemônico de tipo da restrição
        :type tipo: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`CV` | list[:class:`CV`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            CV,
            codigo_restricao=codigo_restricao,
            codigo_usina=codigo_usina,
            estagio=estagio,
            coeficiente=coeficiente,
            tipo=tipo,
            df=df,
        )

    def hq(
        self,
        codigo_restricao: Optional[int] = None,
        estagio_inicial: Optional[int] = None,
        estagio_final: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[HQ, List[HQ], pandas.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição de vazão
        existente no estudo descrito pelo :class:`Dadger`.

        :param codigo_restricao: código que especifica o registro
            da restrição de vazão
        :type codigo_restricao: int | None
        :param estagio_inicial: estágio inicial da restrição de vazão
        :type estagio_inicial: int | None
        :param estagio_final: estágio final da restrição de vazão
        :type estagio_final: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`HQ` | list[:class:`HQ`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            HQ,
            codigo_restricao=codigo_restricao,
            estagio_inicial=estagio_inicial,
            estagio_final=estagio_final,
            df=df,
        )

    def lq(  # noqa
        self,
        codigo_restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[LQ, List[LQ], pandas.DataFrame]]:
        """
        Obtém um registro que especifica os limites inferiores e
        superiores por patamar de uma restrição de vazão existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo_restricao: Índice do código que especifica o registro
            da restrição de vazão
        :type codigo_restricao: int | None
        :param estagio: Estágio sobre o qual valerão os limites da
            restrição de vazão
        :type estagio: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`LQ` | list[:class:`LQ`] | :class:`pandas.DataFrame` | None

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
            hq = self.hq(codigo_restricao=codigo_restricao)
            if isinstance(hq, list) or hq is None:
                return None
            ei = hq.estagio_inicial
            ef = hq.estagio_final
            if any([estagio is None, ei is None, ef is None]):
                return None
            ultimo_registro = None
            if ei is not None and estagio <= ef:  # type: ignore
                for e in range(ei, estagio + 1):  # type: ignore
                    registro_estagio = self.data.get_registers_of_type(
                        LQ, codigo_restricao=codigo_restricao, estagio=e
                    )
                    if registro_estagio is not None:
                        ultimo_registro = registro_estagio
            if isinstance(ultimo_registro, LQ):
                novo_registro = LQ(
                    data=[None] * len(ultimo_registro.data),
                )
                novo_registro.codigo_restricao = codigo_restricao
                novo_registro.limite_superior = ultimo_registro.limite_superior
                novo_registro.limite_inferior = ultimo_registro.limite_inferior
                novo_registro.estagio = estagio
                self.data.add_after(ultimo_registro, novo_registro)
                return novo_registro
            return None

        if df:
            return self.__expande_colunas_df(self._as_df(LQ))
        else:
            lq = self.data.get_registers_of_type(
                LQ, codigo_restricao=codigo_restricao, estagio=estagio
            )
            if isinstance(lq, list):
                return lq
            if lq is None:
                lq = cria_registro()
            return lq

    def cq(
        self,
        codigo_restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        codigo_usina: Optional[int] = None,
        coeficiente: Optional[float] = None,
        tipo: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[CQ, List[CQ], pandas.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        de vazão.

        :param codigo_restricao: código que especifica o registro
        :type codigo_restricao: int | None
        :param estagio: o estágio do coeficiente
        :type estagio: int | None
        :param codigo_usina: o código da UHE para a restrição
        :type codigo_usina: int | None
        :param coeficiente: valor do coeficiente para a usina
            na restrição
        :type coeficiente: float | None
        :param tipo: o mnemônico de tipo da restrição
        :type tipo: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`CQ` | list[:class:`CQ`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            CQ,
            codigo_restricao=codigo_restricao,
            codigo_usina=codigo_usina,
            estagio=estagio,
            coeficiente=coeficiente,
            tipo=tipo,
            df=df,
        )

    def he(
        self,
        codigo_restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        tipo_limite: Optional[int] = None,
        forma_calculo_produtibilidades: Optional[int] = None,
        tipo_valores_produtibilidades: Optional[int] = None,
        tipo_penalidade: Optional[int] = None,
        valor_penalidade: Optional[float] = None,
        arquivo_produtibilidades: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[HE, List[HE], pandas.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição de energia
        armazenada existente no estudo descrito pelo :class:`Dadger`.

        :param codigo_restricao: código que especifica o registro
            da restrição de energia armazenada
        :type codigo_restricao: int | None
        :param estagio: estágio para o qual vale a
            restrição de energia armazenada
        :type estagio: int | None
        :param tipo_limite: flag para o tipo de limite considerado
        :type tipo_limite: int | None
        :param forma_calculo_produtibilidades: flag para a forma
            do cálculo das probutibilidades
        :type forma_calculo_produtibilidades: int | None
        :param tipo_valores_produtibilidades: flag para o tipo de
            valores das probutibilidades
        :type tipo_valores_produtibilidades: int | None
        :param tipo_penalidade: flag para o tipo de
            penalidade aplicada
        :type tipo_penalidade: int | None
        :param valor_penalidade: valor de penalidade aplicada
        :type valor_penalidade: float | None
        :param arquivo_produtibilidades: nome do arquivo com as
            produtibilidades das usinas
        :type arquivo_produtibilidades: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`HE` | list[:class:`HE`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            HE,
            codigo_restricao=codigo_restricao,
            estagio=estagio,
            tipo_limite=tipo_limite,
            forma_calculo_produtibilidades=forma_calculo_produtibilidades,
            tipo_valores_produtibilidades=tipo_valores_produtibilidades,
            tipo_penalidade=tipo_penalidade,
            valor_penalidade=valor_penalidade,
            arquivo_produtibilidades=arquivo_produtibilidades,
            df=df,
        )

    def cm(
        self,
        codigo_restricao: Optional[int] = None,
        codigo_ree: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[CM, List[CM], pandas.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        de energia armazenada.

        :param codigo_restricao: código que especifica o registro
        :type codigo_restricao: int | None
        :param codigo_ree: REE do coeficiente
        :type codigo_ree: int | None
        :param coeficiente: valor do coeficiente para a energia
        :type coeficiente: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`CM` | list[:class:`CM`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            CM,
            codigo_restricao=codigo_restricao,
            codigo_ree=codigo_ree,
            coeficiente=coeficiente,
            df=df,
        )

    @property
    def ev(self) -> Optional[EV]:
        """
        Obtém o (único) registro que define a evaporação
        :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`EV` | None.
        """
        r = self.data.get_registers_of_type(EV)
        if isinstance(r, EV):
            return r
        else:
            return None

    @property
    def fj(self) -> Optional[FJ]:
        """
        Obtém o (único) registro que define o arquivo `polinjus`
        :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`FJ` | None.
        """
        r = self.data.get_registers_of_type(FJ)
        if isinstance(r, FJ):
            return r
        else:
            return None

    @property
    def pu(self) -> Optional[PU]:
        """
        Obtém o (único) registro que define se será usado PL único.

        :return: Um registro, se existir.
        :rtype: :class:`PU` | None.
        """
        r = self.data.get_registers_of_type(PU)
        if isinstance(r, PU):
            return r
        else:
            return None

    @property
    def rc(self) -> Optional[RC]:
        """
        Obtém o (único) registro que insere restrições do tipo
        escada.

        :return: Um registro, se existir.
        :rtype: :class:`RC` | None.
        """
        r = self.data.get_registers_of_type(RC)
        if isinstance(r, RC):
            return r
        else:
            return None

    def pe(
        self,
        codigo_submercado: Optional[int] = None,
        tipo: Optional[int] = None,
        penalidade: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[PE, List[PE], pandas.DataFrame]]:
        """
        Obtém um registro que altera penalidades de vertimento,
            intercâmbio e desvios.

        :param codigo_submercado: Índice do submercado
        :type codigo_submercado: int | None
        :param tipo: tipo de restrição a ser modificada
        :type tipo: int | None
        :param penalidade: valor da penalidade
        :type penalidade: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`PE` | list[:class:`PE`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            PE,
            codigo_submercado=codigo_submercado,
            tipo=tipo,
            penalidade=penalidade,
            df=df,
        )

    def ts(
        self,
        tolerancia_primaria: Optional[float] = None,
        tolerancia_secundaria: Optional[float] = None,
        zera_coeficientes: Optional[int] = None,
        tolerancia_teste_otimalidade: Optional[float] = None,
    ) -> Optional[Union[TS, List[TS]]]:
        """
        Obtém um registro que altera as tolerâncias do solver.

        :param tolerancia_primaria: valor da tolerância primária do solver.
        :type tolerancia_primaria: float | None
        :param tolerancia_secundaria: valor da tolerância secundária do solver.
        :type tolerancia_secundaria: float | None
        :param zera_coeficientes: funcionalidade de zerar os coeficientes de
            cortes não ótimos.
        :type zera_coeficientes: int | None
        :param tolerancia_teste_otimalidade: valor da tolerância usada no
            teste de otimalidade.
        :type tolerancia_teste_otimalidade: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`TS` | list[:class:`TS`] | None
        """
        return self.data.get_registers_of_type(
            TS,
            tolerancia_primaria=tolerancia_primaria,
            tolerancia_secundaria=tolerancia_secundaria,
            zera_coeficientes=zera_coeficientes,
            tolerancia_teste_otimalidade=tolerancia_teste_otimalidade,
        )

    def pv(
        self,
        penalidade_variaveis_folga: Optional[float] = None,
        tolerancia_viabilidade_restricoes: Optional[float] = None,
        iteracoes_atualizacao_penalidade: Optional[int] = None,
        fator_multiplicacao_folga: Optional[float] = None,
        valor_inicial_variaveis_folga: Optional[float] = None,
        valor_final_variaveis_folga: Optional[float] = None,
    ) -> Optional[Union[PV, List[PV]]]:
        """
        Obtém um registro que altera as penalidades das variáveis
            de folga.

        :param penalidade_variaveis_folga: valor da nova penalidade das
            variáveis de folga
        :type penalidade_variaveis_folga: float | None
        :param tolerancia_viabilidade_restricoes: valor da tolerância para
            a viabilidade das restrições
        :type tolerancia_viabilidade_restricoes: float | None
        :param iteracoes_atualizacao_penalidade: número de iterações para
            a atualização da penalidade variável
        :type iteracoes_atualizacao_penalidade: int | None
        :param fator_multiplicacao_folga: o fator para multiplicação da
            folga
        :type fator_multiplicacao_folga: float | None
        :param valor_inicial_variaveis_folga: o valor inicial para as
            variáveis de folga
        :type valor_inicial_variaveis_folga: float | None
        :param valor_final_variaveis_folga: o valor final para as
            variáveis de folga
        :type valor_final_variaveis_folga: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`PV` | list[:class:`PV`] | None
        """
        return self.data.get_registers_of_type(
            PV,
            penalidade_variaveis_folga=penalidade_variaveis_folga,
            tolerancia_viabilidade_restricoes=tolerancia_viabilidade_restricoes,
            iteracoes_atualizacao_penalidade=iteracoes_atualizacao_penalidade,
            fator_multiplicacao_folga=fator_multiplicacao_folga,
            valor_inicial_variaveis_folga=valor_inicial_variaveis_folga,
            valor_final_variaveis_folga=valor_final_variaveis_folga,
        )

    def cx(
        self,
        codigo_newave: Optional[int] = None,
        codigo_decomp: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[CX, List[CX], pandas.DataFrame]]:
        """
        Obtém um registro que altera as tolerâncias do solver.

        :param codigo_newave: código da usina no NEWAVE
        :type codigo_newave: int | None
        :param codigo_decomp: código da usina no DECOMP
        :type codigo_decomp: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`CX` | list[:class:`CX`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            CX, codigo_newave=codigo_newave, codigo_decomp=codigo_decomp, df=df
        )

    @property
    def fa(self) -> Optional[FA]:
        """
        Obtém o (único) registro que define o arquivo de índices.

        :return: Um registro, se existir.
        :rtype: :class:`FA` | None.
        """
        r = self.data.get_registers_of_type(FA)
        if isinstance(r, FA):
            return r
        else:
            return None

    @property
    def vt(self) -> Optional[VT]:
        """
        Obtém o (único) registro que define o arquivo com
            cenários de vento.

        :return: Um registro, se existir.
        :rtype: :class:`VT` | None.
        """
        r = self.data.get_registers_of_type(VT)
        if isinstance(r, VT):
            return r
        else:
            return None

    @property
    def cs(self) -> Optional[CS]:
        """
        Obtém o (único) registro que habilita a
            consistência de dados.

        :return: Um registro, se existir.
        :rtype: :class:`CS` | None.
        """
        r = self.data.get_registers_of_type(CS)
        if isinstance(r, CS):
            return r
        else:
            return None

    def vl(
        self,
        codigo_usina_influenciada: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[VL, List[VL], pandas.DataFrame]]:
        """
        Obtém um registro que define uma usina hidrelétrica que sofre
        influência de vazão lateral na cota de jusante existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo_usina_influenciada: código da UHE influenciada
        :type codigo_usina_influenciada: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`VL` | list[:class:`VL`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            VL,
            codigo_usina_influenciada=codigo_usina_influenciada,
            df=df,
        )

    def vu(
        self,
        codigo_usina_influenciada: Optional[int] = None,
        codigo_usina_influenciadora: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[VU, List[VU], pandas.DataFrame]]:
        """
        Obtém um registro que define uma usina hidrelétrica que tem
        influencia sobre a vazão de jusante da primeira existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo_usina_influenciada: código da UHE influenciada
        :type codigo_usina_influenciada: int | None
        :param codigo_usina_influenciadora: código da UHE influenciadora
        :type codigo_usina_influenciadora: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`VU` | list[:class:`VU`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            VU,
            codigo_usina_influenciada=codigo_usina_influenciada,
            codigo_usina_influenciadora=codigo_usina_influenciadora,
            df=df,
        )

    def va(
        self,
        codigo_usina_influenciada: Optional[int] = None,
        codigo_posto_influenciador: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[VA, List[VA], pandas.DataFrame]]:
        """
        Obtém um registro que define um posto que tem
        influencia sobre a vazão de jusante da primeira existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo_usina_influenciada: código da UHE influenciada
        :type codigo_usina_influenciada: int | None
        :param codigo_posto_influenciador: código do posto influenciador
        :type codigo_posto_influenciador: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`VA` | list[:class:`VA`] | :class:`pandas.DataFrame` | None
        """
        return self.__registros_ou_df(
            VA,
            codigo_usina_influenciada=codigo_usina_influenciada,
            codigo_posto_influenciador=codigo_posto_influenciador,
            df=df,
        )

    def pd(
        self, algoritmo: Optional[str] = None
    ) -> Optional[Union[PD, List[PD]]]:
        """
        Obtém um registro que especifica o algoritmo usado para a solução.

        :param algoritmo: Mnemônico do algoritmo
        :type algoritmo: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`PD` | list[:class:`PD`] | None
        """
        return self.data.get_registers_of_type(PD, algoritmo=algoritmo)
