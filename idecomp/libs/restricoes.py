from typing import Type, TypeVar, List, Optional, Union
from datetime import datetime
import pandas as pd  # type: ignore
from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile
from idecomp.libs.modelos.restricoes import (
    RegistroRe,
    RegistroReHorizPer,
    RegistroReHorizData,
    RegistroRePerPat,
    RegistroReDataPat,
    RegistroReLimFormPerPat,
    RegistroReLimFormDataPat,
    RegistroReRegraAtiva,
    RegistroReHabilita,
    RegistroReTratViol,
    RegistroReTratViolPer,
    RegistroAliasElet,
    RegistroAliasEletValPerPat,
)
from idecomp.libs.modelos.restricoes import (
    RegistroRestricaoEletricaFormula,
    RegistroRestricaoEletricaFormulaDataPatamar,
    RegistroRestricaoEletricaFormulaPeriodoPatamar,
    RegistroRestricaoEletricaHabilita,
    RegistroRestricaoEletricaHorizonteData,
    RegistroRestricaoEletricaHorizontePeriodo,
    RegistroRestricaoEletricaLimitesFormulaDataPatamar,
    RegistroRestricaoEletricaLimitesFormulaPeriodoPatamar,
    RegistroRestricaoEletricaRegraAtivacao,
    RegistroRestricaoEletricaTratamentoViolacao,
    RegistroRestricaoEletricaTratamentoViolacaoPeriodo,
    RegistroAliasEletrico,
    RegistroAliasEletricoValorPeriodoPatamar,
)


class Restricoes(RegisterFile):
    """
    Armazena os dados de entrada do DECOMP referentes aos dados
    das restrições do problema informadas no ambiente LIBS.
    """

    T = TypeVar("T", bound=Register)

    REGISTERS = [
        RegistroRestricaoEletricaHorizontePeriodo,
        RegistroRestricaoEletricaHorizonteData,
        RegistroRestricaoEletricaFormulaPeriodoPatamar,
        RegistroRestricaoEletricaFormulaDataPatamar,
        RegistroRestricaoEletricaFormula,
        RegistroRestricaoEletricaHabilita,
        RegistroRestricaoEletricaLimitesFormulaDataPatamar,
        RegistroRestricaoEletricaLimitesFormulaPeriodoPatamar,
        RegistroRestricaoEletricaRegraAtivacao,
        RegistroRestricaoEletricaTratamentoViolacaoPeriodo,
        RegistroRestricaoEletricaTratamentoViolacao,
        RegistroAliasEletricoValorPeriodoPatamar,
        RegistroAliasEletrico,
        RegistroReHorizPer,
        RegistroReHorizData,
        RegistroRePerPat,
        RegistroReDataPat,
        RegistroReLimFormPerPat,
        RegistroReLimFormDataPat,
        RegistroAliasEletValPerPat,
        RegistroAliasElet,
        RegistroReRegraAtiva,
        RegistroReHabilita,
        RegistroReTratViolPer,
        RegistroReTratViol,
        RegistroRe,
    ]

    def __registros_ou_df(
        self, t: Type[T], **kwargs
    ) -> Optional[Union[T, List[T], pd.DataFrame]]:
        if kwargs.get("df"):
            return self._as_df(t)
        else:
            kwargs_sem_df = {k: v for k, v in kwargs.items() if k != "df"}
            return self.data.get_registers_of_type(t, **kwargs_sem_df)

    def restricao_eletrica_formula(
        self,
        codigo_restricao: Optional[int] = None,
        formula: Optional[str] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroRestricaoEletricaFormula,
            List[RegistroRestricaoEletricaFormula],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que cadastra uma restrição elétrica (RE),
        definido através do nome completo do card.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param formula: equação da restrição
        :type formula: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRestricaoEletricaFormula` |
            list[:class:`RegistroRestricaoEletricaFormula`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRestricaoEletricaFormula,
            codigo_restricao=codigo_restricao,
            formula=formula,
            df=df,
        )

    def re(
        self,
        codigo_restricao: Optional[int] = None,
        formula: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[RegistroRe, List[RegistroRe], pd.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição elétrica (RE),
        definido através do nome alternativo (apelido) do card.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param formula: equação da restrição
        :type formula: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRe` |
            list[:class:`RegistroRe`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRe,
            codigo_restricao=codigo_restricao,
            formula=formula,
            df=df,
        )

    def restricao_eletrica_horizonte_periodo(
        self,
        codigo_restricao: Optional[int] = None,
        estagio_inicio: Optional[int] = None,
        estagio_fim: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroRestricaoEletricaHorizontePeriodo,
            List[RegistroRestricaoEletricaHorizontePeriodo],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que cadastra o horizonte de validade de uma
        restrição elétrica com intervalo de estágios,
        definido através do nome completo do card.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param estagio_inicio: estágio inicial de validade da restrição
        :type estagio_inicio: int | None
        :param estagio_fim: estágio final de validade da restrição
        :type estagio_fim: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRestricaoEletricaHorizontePeriodo` |
            list[:class:`RegistroRestricaoEletricaHorizontePeriodo`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRestricaoEletricaHorizontePeriodo,
            codigo_restricao=codigo_restricao,
            estagio_inicio=estagio_inicio,
            estagio_fim=estagio_fim,
            df=df,
        )

    def re_horiz_per(
        self,
        codigo_restricao: Optional[int] = None,
        estagio_inicio: Optional[int] = None,
        estagio_fim: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroReHorizPer, List[RegistroReHorizPer], pd.DataFrame]
    ]:
        """
        Obtém um registro que cadastra o horizonte de validade de uma
        restrição elétrica com intervalo de estágios,
        definido através do nome alternativo (apelido) do card.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param estagio_inicio: estágio inicial de validade da restrição
        :type estagio_inicio: int | None
        :param estagio_fim: estágio final de validade da restrição
        :type estagio_fim: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroReHorizPer` |
            list[:class:`RegistroReHorizPer`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroReHorizPer,
            codigo_restricao=codigo_restricao,
            estagio_inicio=estagio_inicio,
            estagio_fim=estagio_fim,
            df=df,
        )

    def restricao_eletrica_horizonte_data(
        self,
        codigo_restricao: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroRestricaoEletricaHorizonteData,
            List[RegistroRestricaoEletricaHorizonteData],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que cadastra o horizonte de validade de uma
        restrição elétrica com intervalo de data,
        definido através do nome completo do card.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param data_inicio: data inicial de validade da restrição
        :type data_inicio: datetime | None
        :param data_fim: data final de validade da restrição
        :type data_fim: datetime | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRestricaoEletricaHorizonteData` |
            list[:class:`RegistroRestricaoEletricaHorizonteData`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRestricaoEletricaHorizonteData,
            codigo_restricao=codigo_restricao,
            data_inicio=data_inicio,
            data_fim=data_fim,
            df=df,
        )

    def re_horiz_data(
        self,
        codigo_restricao: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroReHorizData, List[RegistroReHorizData], pd.DataFrame]
    ]:
        """
        Obtém um registro que cadastra o horizonte de validade de uma
        restrição elétrica com intervalo de data,
        definido através do nome alternativo (apelido) do card.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param data_inicio: data inicial de validade da restrição
        :type data_inicio: datetime | None
        :param data_fim: data final de validade da restrição
        :type data_fim: datetime | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroReHorizData` |
            list[:class:`RegistroReHorizData`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroReHorizData,
            codigo_restricao=codigo_restricao,
            data_inicio=data_inicio,
            data_fim=data_fim,
            df=df,
        )

    def restricao_eletrica_formula_periodo_patamar(
        self,
        codigo_restricao: Optional[int] = None,
        estagio_inicio: Optional[int] = None,
        estagio_fim: Optional[int] = None,
        patamar: Optional[int] = None,
        formula: Optional[str] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroRestricaoEletricaFormulaPeriodoPatamar,
            List[RegistroRestricaoEletricaFormulaPeriodoPatamar],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que cadastra uma restrição elétrica (RE)
        que varia ao longo do tempo, informada por intervalo de estágios,
        definido através do nome completo do card.


        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param estagio_inicio: estágio inicial de validade da restrição
        :type estagio_inicio: int | None
        :param estagio_fim: estágio final de validade da restrição
        :type estagio_fim: int | None
        :param patamar: patamar de carga de validade da restrição
        :type patamar: int | None
        :param formula: equação da restrição
        :type formula: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRestricaoEletricaFormulaPeriodoPatamar` |
            list[:class:`RegistroRestricaoEletricaFormulaPeriodoPatamar`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRestricaoEletricaFormulaPeriodoPatamar,
            codigo_restricao=codigo_restricao,
            estagio_inicio=estagio_inicio,
            estagio_fim=estagio_fim,
            patamar=patamar,
            formula=formula,
            df=df,
        )

    def re_per_pat(
        self,
        codigo_restricao: Optional[int] = None,
        estagio_inicio: Optional[int] = None,
        estagio_fim: Optional[int] = None,
        patamar: Optional[int] = None,
        formula: Optional[str] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroRePerPat, List[RegistroRePerPat], pd.DataFrame]
    ]:
        """
        Obtém um registro que cadastra uma restrição elétrica (RE)
        que varia ao longo do tempo, informada por intervalo de estágios,
        definido através do nome alternativo (apelido) do card.


        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param estagio_inicio: estágio inicial de validade da restrição
        :type estagio_inicio: int | None
        :param estagio_fim: estágio final de validade da restrição
        :type estagio_fim: int | None
        :param patamar: patamar de carga de validade da restrição
        :type patamar: int | None
        :param formula: equação da restrição
        :type formula: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRePerPat` |
            list[:class:`RegistroRePerPat`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRePerPat,
            codigo_restricao=codigo_restricao,
            estagio_inicio=estagio_inicio,
            estagio_fim=estagio_fim,
            patamar=patamar,
            formula=formula,
            df=df,
        )

    def restricao_eletrica_formula_data_patamar(
        self,
        codigo_restricao: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        patamar: Optional[int] = None,
        formula: Optional[str] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroRestricaoEletricaFormulaDataPatamar,
            List[RegistroRestricaoEletricaFormulaDataPatamar],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que cadastra uma restrição elétrica (RE)
        que varia ao longo do tempo, informada por intervalo de data,
        definido através do nome completo do card.


        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param data_inicio: data inicial de validade da restrição
        :type data_inicio: datetime | None
        :param data_fim: data final de validade da restrição
        :type data_fim: datetime | None
        :param patamar: patamar de carga de validade da restrição
        :type patamar: int | None
        :param formula: equação da restrição
        :type formula: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRestricaoEletricaFormulaDataPatamar` |
            list[:class:`RegistroRestricaoEletricaFormulaDataPatamar`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRestricaoEletricaFormulaDataPatamar,
            codigo_restricao=codigo_restricao,
            data_inicio=data_inicio,
            data_fim=data_fim,
            patamar=patamar,
            formula=formula,
            df=df,
        )

    def re_data_pat(
        self,
        codigo_restricao: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        patamar: Optional[int] = None,
        formula: Optional[str] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroReDataPat, List[RegistroReDataPat], pd.DataFrame]
    ]:
        """
        Obtém um registro que cadastra uma restrição elétrica (RE)
        que varia ao longo do tempo, informada por intervalo de data,
        definido através do nome alternativo (apelido) do card.


        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param data_inicio: data inicial de validade da restrição
        :type data_inicio: datetime | None
        :param data_fim: data final de validade da restrição
        :type data_fim: datetime | None
        :param patamar: patamar de carga de validade da restrição
        :type patamar: int | None
        :param formula: equação da restrição
        :type formula: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroReDataPat` |
            list[:class:`RegistroReDataPat`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroReDataPat,
            codigo_restricao=codigo_restricao,
            data_inicio=data_inicio,
            data_fim=data_fim,
            patamar=patamar,
            formula=formula,
            df=df,
        )

    def restricao_eletrica_limites_formula_data_patamar(
        self,
        codigo_restricao: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        patamar: Optional[int] = None,
        limite_inferior: Optional[float] = None,
        limite_superior: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroRestricaoEletricaLimitesFormulaDataPatamar,
            List[RegistroRestricaoEletricaLimitesFormulaDataPatamar],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que cadastra os limites por horizonte, definido
        por intervalo de data, e por patamar para uma restrição elétrica,
        definido através do nome completo do card.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param data_inicio: data inicial de validade dos limites
        :type data_inicio: datetime | None
        :param data_fim: data final de validade dos limites
        :type data_fim: datetime | None
        :param patamar: patamar de validade dos limites
        :type patamar: int | None
        :param limite_inferior: limite inferior da restrição
        :type limite_inferior: float | None
        :param limite_superior: limite superior da restrição
        :type limite_superior: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRestricaoEletricaLimitesFormulaDataPatamar` |
            list[:class:`RegistroRestricaoEletricaLimitesFormulaDataPatamar`] |
            `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRestricaoEletricaLimitesFormulaDataPatamar,
            codigo_restricao=codigo_restricao,
            data_inicio=data_inicio,
            data_fim=data_fim,
            patamar=patamar,
            limite_inferior=limite_inferior,
            limite_superior=limite_superior,
            df=df,
        )

    def re_lim_form_data_pat(
        self,
        codigo_restricao: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        patamar: Optional[int] = None,
        limite_inferior: Optional[float] = None,
        limite_superior: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroReLimFormDataPat,
            List[RegistroReLimFormDataPat],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que cadastra os limites por horizonte, definido
        por intervalo de data, e por patamar para uma restrição elétrica,
        definido através do nome alternativo (apelido) do card.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param data_inicio: data inicial de validade dos limites
        :type data_inicio: datetime | None
        :param data_fim: data final de validade dos limites
        :type data_fim: datetime | None
        :param patamar: patamar de validade dos limites
        :type patamar: int | None
        :param limite_inferior: limite inferior da restrição
        :type limite_inferior: float | None
        :param limite_superior: limite superior da restrição
        :type limite_superior: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroReLimFormDataPat` |
            list[:class:`RegistroReLimFormDataPat`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroReLimFormDataPat,
            codigo_restricao=codigo_restricao,
            data_inicio=data_inicio,
            data_fim=data_fim,
            patamar=patamar,
            limite_inferior=limite_inferior,
            limite_superior=limite_superior,
            df=df,
        )

    def restricao_eletrica_limite_formula_periodo_patamar(
        self,
        codigo_restricao: Optional[int] = None,
        estagio_inicio: Optional[int] = None,
        estagio_fim: Optional[int] = None,
        patamar: Optional[int] = None,
        limite_inferior: Optional[float] = None,
        limite_superior: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroRestricaoEletricaLimitesFormulaPeriodoPatamar,
            List[RegistroRestricaoEletricaLimitesFormulaPeriodoPatamar],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que cadastra os limites por horizonte, definido
        por intervalo de estágios, e por patamar para uma restrição elétrica,
        definido através do nome completo do card.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param estagio_inicio: estágio inicial de validade dos limites
        :type estagio_inicio: int | None
        :param estagio_fim: estágio final de validade dos limites
        :type estagio_fim: int | None
        :param patamar: patamar de validade dos limites
        :type patamar: int | None
        :param limite_inferior: limite inferior da restrição
        :type limite_inferior: float | None
        :param limite_superior: limite superior da restrição
        :type limite_superior: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRestricaoEletricaLimitesFormulaPeriodoPatamar` |
            list[:class:`RegistroRestricaoEletricaLimitesFormulaPeriodoPatamar`] |
            `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRestricaoEletricaLimitesFormulaPeriodoPatamar,
            codigo_restricao=codigo_restricao,
            estagio_inicio=estagio_inicio,
            estagio_fim=estagio_fim,
            patamar=patamar,
            limite_inferior=limite_inferior,
            limite_superior=limite_superior,
            df=df,
        )

    def re_lim_form_per_pat(
        self,
        codigo_restricao: Optional[int] = None,
        estagio_inicio: Optional[int] = None,
        estagio_fim: Optional[int] = None,
        patamar: Optional[int] = None,
        limite_inferior: Optional[float] = None,
        limite_superior: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroReLimFormPerPat,
            List[RegistroReLimFormPerPat],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que cadastra os limites por horizonte, definido
        por intervalo de estágios, e por patamar para uma restrição elétrica,
        definido através do nome alternativo (apelido) do card.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param estagio_inicio: estágio inicial de validade dos limites
        :type estagio_inicio: int | None
        :param estagio_fim: estágio final de validade dos limites
        :type estagio_fim: int | None
        :param patamar: patamar de validade dos limites
        :type patamar: int | None
        :param limite_inferior: limite inferior da restrição
        :type limite_inferior: float | None
        :param limite_superior: limite superior da restrição
        :type limite_superior: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroReLimFormPerPat` |
            list[:class:`RegistroReLimFormPerPat`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroReLimFormPerPat,
            codigo_restricao=codigo_restricao,
            estagio_inicio=estagio_inicio,
            estagio_fim=estagio_fim,
            patamar=patamar,
            limite_inferior=limite_inferior,
            limite_superior=limite_superior,
            df=df,
        )

    def alias_eletrico(
        self,
        codigo_alias: Optional[int] = None,
        identificador_alias: Optional[str] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroAliasEletrico, List[RegistroAliasEletrico], pd.DataFrame]
    ]:
        """
        Obtém um registro que cadastra um alias elétrico,
        definido através do nome completo do card.

        :param codigo_alias: código que especifica o alias
        :type codigo_alias: int | None
        :param identificador_alias: o nome identificador do alias
        :type identificador_alias: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroAliasEletrico` |
            list[:class:`RegistroAliasEletrico`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroAliasEletrico,
            codigo_alias=codigo_alias,
            identificador_alias=identificador_alias,
            df=df,
        )

    def alias_elet(
        self,
        codigo_alias: Optional[int] = None,
        identificador_alias: Optional[str] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroAliasElet, List[RegistroAliasElet], pd.DataFrame]
    ]:
        """
        Obtém um registro que cadastra um alias elétrico,
        definido através do nome alternativo (apelido) do card.

        :param codigo_alias: código que especifica o alias
        :type codigo_alias: int | None
        :param identificador_alias: o nome identificador do alias
        :type identificador_alias: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroAliasElet` |
            list[:class:`RegistroAliasElet`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroAliasElet,
            codigo_alias=codigo_alias,
            identificador_alias=identificador_alias,
            df=df,
        )

    def alias_eletrico_valor_periodo_patamar(
        self,
        codigo_alias: Optional[int] = None,
        estagio_inicio: Optional[int] = None,
        estagio_fim: Optional[int] = None,
        patamar: Optional[int] = None,
        valor: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroAliasEletricoValorPeriodoPatamar,
            List[RegistroAliasEletricoValorPeriodoPatamar],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que contém os valores assumidos pelo
        alias para cada período e patamar,
        definido através do nome completo do card.

        :param codigo_alias: código que especifica o alias
        :type codigo_alias: int | None
        :param estagio_inicio: estágio inicial de validade do dado
        :type estagio_inicio: datetime | None
        :param estagio_fim: estágio final de validade do dado
        :type estagio_fim: datetime | None
        :param patamar: patamar de validade do dado
        :type patamar: int | None
        :param valor: valor do dado
        :type valor: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroAliasEletricoValorPeriodoPatamar` |
            list[:class:`RegistroAliasEletricoValorPeriodoPatamar`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroAliasEletricoValorPeriodoPatamar,
            codigo_alias=codigo_alias,
            estagio_inicio=estagio_inicio,
            estagio_fim=estagio_fim,
            patamar=patamar,
            valor=valor,
            df=df,
        )

    def alias_elet_val_per_pat(
        self,
        codigo_alias: Optional[int] = None,
        estagio_inicio: Optional[int] = None,
        estagio_fim: Optional[int] = None,
        patamar: Optional[int] = None,
        valor: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroAliasEletValPerPat,
            List[RegistroAliasEletValPerPat],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que contém os valores assumidos pelo
        alias para cada período e patamar,
        definido através do nome alternativo (apelido) do card.

        :param codigo_alias: código que especifica o alias
        :type codigo_alias: int | None
        :param estagio_inicio: estágio inicial de validade do dado
        :type estagio_inicio: datetime | None
        :param estagio_fim: estágio final de validade do dado
        :type estagio_fim: datetime | None
        :param patamar: patamar de validade do dado
        :type patamar: int | None
        :param valor: valor do dado
        :type valor: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroAliasEletValPerPat` |
            list[:class:`RegistroAliasEletValPerPat`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroAliasEletValPerPat,
            codigo_alias=codigo_alias,
            estagio_inicio=estagio_inicio,
            estagio_fim=estagio_fim,
            patamar=patamar,
            valor=valor,
            df=df,
        )

    def restricao_eletrica_regra_ativacao(
        self,
        codigo_regra_ativacao: Optional[int] = None,
        regra_ativacao: Optional[str] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroRestricaoEletricaRegraAtivacao,
            List[RegistroRestricaoEletricaRegraAtivacao],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que define uma regra para ativação e
        desativação de restrições elétricas,
        definido através do nome completo do card.

        :param codigo_regra_ativacao: código que especifica a regra de ativação
        :type codigo_regra_ativacao: int | None
        :param regra_ativacao: texto que define a regra condicional para ativação
        :type regra_ativacao: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRestricaoEletricaRegraAtivacao` |
            list[:class:`RegistroRestricaoEletricaRegraAtivacao`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRestricaoEletricaRegraAtivacao,
            codigo_regra_ativacao=codigo_regra_ativacao,
            regra_ativacao=regra_ativacao,
            df=df,
        )

    def re_regra_ativa(
        self,
        codigo_regra_ativacao: Optional[int] = None,
        regra_ativacao: Optional[str] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroReRegraAtiva, List[RegistroReRegraAtiva], pd.DataFrame]
    ]:
        """
        Obtém um registro que define uma regra para ativação e
        desativação de restrições elétricas,
        definido através do nome alternativo (apelido) do card.

        :param codigo_regra_ativacao: código que especifica a regra de ativação
        :type codigo_regra_ativacao: int | None
        :param regra_ativacao: texto que define a regra condicional para ativação
        :type regra_ativacao: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroReRegraAtiva` |
            list[:class:`RegistroReRegraAtiva`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroReRegraAtiva,
            codigo_regra_ativacao=codigo_regra_ativacao,
            regra_ativacao=regra_ativacao,
            df=df,
        )

    def restricao_eletrica_habilita(
        self,
        codigo_restricao: Optional[int] = None,
        codigo_regra_ativacao: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroRestricaoEletricaHabilita,
            List[RegistroRestricaoEletricaHabilita],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que contém a associação entre uma regra
        de ativação e uma restrição elétrica,
        definido através do nome completo do card.

        :param codigo_restricao: código que especifica a restrição elétrica
        :type codigo_restricao: int | None
        :param codigo_regra_ativacao: código que especifica a regra de ativação
        :type codigo_regra_ativacao: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRestricaoEletricaHabilita` |
            list[:class:`RegistroRestricaoEletricaHabilita`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRestricaoEletricaHabilita,
            codigo_restricao=codigo_restricao,
            codigo_regra_ativacao=codigo_regra_ativacao,
            df=df,
        )

    def re_habilita(
        self,
        codigo_restricao: Optional[int] = None,
        codigo_regra_ativacao: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroReHabilita, List[RegistroReHabilita], pd.DataFrame]
    ]:
        """
        Obtém um registro que contém a associação entre uma regra
        de ativação e uma restrição elétrica,
        definido através do nome alternativo (apelido) do card.

        :param codigo_restricao: código que especifica a restrição elétrica
        :type codigo_restricao: int | None
        :param codigo_regra_ativacao: código que especifica a regra de ativação
        :type codigo_regra_ativacao: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroReHabilita` |
            list[:class:`RegistroReHabilita`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroReHabilita,
            codigo_restricao=codigo_restricao,
            codigo_regra_ativacao=codigo_regra_ativacao,
            df=df,
        )

    def restricao_eletrica_tratamento_violacao(
        self,
        codigo_restricao: Optional[int] = None,
        tipo_violacao: Optional[str] = None,
        custo_violacao: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroRestricaoEletricaTratamentoViolacao,
            List[RegistroRestricaoEletricaTratamentoViolacao],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que contém definição do tipo de violação e o
        valor do custo de violação de uma restrição elétrica,
        definido através do nome completo do card.

        :param codigo_restricao: código que especifica a restrição elétrica
        :type codigo_restricao: int | None
        :param tipo_violacao: define o tipo de violação da restrição elétrica
        :type tipo_violacao: str | None
        :param custo_violacao: define o custo de violação da restrição elétrica
        :type custo_violacao: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRestricaoEletricaTratamentoViolacao` |
            list[:class:`RegistroRestricaoEletricaTratamentoViolacao`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRestricaoEletricaTratamentoViolacao,
            codigo_restricao=codigo_restricao,
            tipo_violacao=tipo_violacao,
            custo_violacao=custo_violacao,
            df=df,
        )

    def re_trat_viol(
        self,
        codigo_restricao: Optional[int] = None,
        tipo_violacao: Optional[str] = None,
        custo_violacao: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroReTratViol, List[RegistroReTratViol], pd.DataFrame]
    ]:
        """
        Obtém um registro que contém definição do tipo de violação e o
        valor do custo de violação de uma restrição elétrica,
        definido através do nome alternativo (apelido) do card.

        :param codigo_restricao: código que especifica a restrição elétrica
        :type codigo_restricao: int | None
        :param tipo_violacao: define o tipo de violação da restrição elétrica
        :type tipo_violacao: str | None
        :param custo_violacao: define o custo de violação da restrição elétrica
        :type custo_violacao: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroReTratViol` |
            list[:class:`RegistroReTratViol`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroReTratViol,
            codigo_restricao=codigo_restricao,
            tipo_violacao=tipo_violacao,
            custo_violacao=custo_violacao,
            df=df,
        )

    def restricao_eletrica_tratamento_violacao_periodo(
        self,
        codigo_restricao: Optional[int] = None,
        estagio_inicio: Optional[int] = None,
        estagio_fim: Optional[int] = None,
        tipo_violacao: Optional[str] = None,
        custo_violacao: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroRestricaoEletricaTratamentoViolacaoPeriodo,
            List[RegistroRestricaoEletricaTratamentoViolacaoPeriodo],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que contém definição do tipo de violação e o
        valor do custo de violação de uma restrição elétrica definida para um
        intervalo de estágios,
        definido através do nome completo do card.

        :param codigo_restricao: código que especifica a restrição elétrica
        :type codigo_restricao: int | None
        :param estagio_inicio: estágio inicial de validade do dado
        :type estagio_inicio: int | None
        :param estagio_fim: estágio final de validade do dado
        :type estagio_fim: int | None
        :param tipo_violacao: define o tipo de violação da restrição elétrica
        :type tipo_violacao: str | None
        :param custo_violacao: define o custo de violação da restrição elétrica
        :type custo_violacao: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRestricaoEletricaTratamentoViolacaoPeriodo` |
            list[:class:`RegistroRestricaoEletricaTratamentoViolacaoPeriodo`] |
            `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRestricaoEletricaTratamentoViolacaoPeriodo,
            codigo_restricao=codigo_restricao,
            estagio_inicio=estagio_inicio,
            estagio_fim=estagio_fim,
            tipo_violacao=tipo_violacao,
            custo_violacao=custo_violacao,
            df=df,
        )

    def re_trat_viol_per(
        self,
        codigo_restricao: Optional[int] = None,
        estagio_inicio: Optional[int] = None,
        estagio_fim: Optional[int] = None,
        tipo_violacao: Optional[str] = None,
        custo_violacao: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroReTratViolPer, List[RegistroReTratViolPer], pd.DataFrame]
    ]:
        """
        Obtém um registro que contém definição do tipo de violação e o
        valor do custo de violação de uma restrição elétrica definida para um
        intervalo de estágios,
        definido através do nome alternativo (apelido) do card.

        :param codigo_restricao: código que especifica a restrição elétrica
        :type codigo_restricao: int | None
        :param estagio_inicio: estágio inicial de validade do dado
        :type estagio_inicio: int | None
        :param estagio_fim: estágio final de validade do dado
        :type estagio_fim: int | None
        :param tipo_violacao: define o tipo de violação da restrição elétrica
        :type tipo_violacao: str | None
        :param custo_violacao: define o custo de violação da restrição elétrica
        :type custo_violacao: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroReTratViolPer` |
            list[:class:`RegistroReTratViolPer`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroReTratViol,
            codigo_restricao=codigo_restricao,
            estagio_inicio=estagio_inicio,
            estagio_fim=estagio_fim,
            tipo_violacao=tipo_violacao,
            custo_violacao=custo_violacao,
            df=df,
        )
