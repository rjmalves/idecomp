from typing import Type, TypeVar, List, Optional, Union
from datetime import datetime
import pandas as pd  # type: ignore
from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile
from idecomp.libs.modelos.restricoes import (
    RegistroRE,
    RegistroREHorizPer,
    RegistroREHorizData,
    RegistroREPerPat,
    RegistroREDataPat,
    RegistroRELimFormPerPat,
    RegistroRELimFormDataPat,
    RegistroAliasElet,
    RegistroAliasEletValPerPat,
    RegistroRERegraAtiva,
    RegistroREHabilita,
    RegistroRETratViol,
    RegistroRETratViolPer,
)


class Restricoes(RegisterFile):
    """
    Armazena os dados de entrada do DECOMP referentes aos dados
    das restrições do problema informadas no ambiente LIBS.
    """

    T = TypeVar("T", bound=Register)

    REGISTERS = [
        RegistroREHorizPer,
        RegistroREHorizData,
        RegistroREPerPat,
        RegistroREDataPat,
        RegistroRELimFormPerPat,
        RegistroRELimFormDataPat,
        RegistroAliasEletValPerPat,
        RegistroAliasElet,
        RegistroRERegraAtiva,
        RegistroREHabilita,
        RegistroRETratViolPer,
        RegistroRETratViol,
        RegistroRE,
    ]

    def __registros_ou_df(
        self, t: Type[T], **kwargs
    ) -> Optional[Union[T, List[T], pd.DataFrame]]:
        if kwargs.get("df"):
            return self._as_df(t)
        else:
            kwargs_sem_df = {k: v for k, v in kwargs.items() if k != "df"}
            return self.data.get_registers_of_type(t, **kwargs_sem_df)

    def re(
        self,
        codigo_restricao: Optional[int] = None,
        formula: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[RegistroRE, List[RegistroRE], pd.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição elétrica (RE).

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param formula: equação da restrição
        :type formula: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRE` |
            list[:class:`RegistroRE`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRE,
            codigo_restricao=codigo_restricao,
            formula=formula,
            df=df,
        )

    def re_horiz_per(
        self,
        codigo_restricao: Optional[int] = None,
        periodo_inicio: Optional[int] = None,
        periodo_fim: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroREHorizPer, List[RegistroREHorizPer], pd.DataFrame]
    ]:
        """
        Obtém um registro que cadastra o horizonte de validade de uma
        restrição elétrica com intervalo de data.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param periodo_inicio: período inicial de validade da restrição
        :type periodo_inicio: int | None
        :param periodo_fim: período final de validade da restrição
        :type periodo_fim: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroREHorizPer` |
            list[:class:`RegistroREHorizPer`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroREHorizPer,
            codigo_restricao=codigo_restricao,
            periodo_inicio=periodo_inicio,
            periodo_fim=periodo_fim,
            df=df,
        )

    def re_horiz_data(
        self,
        codigo_restricao: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroREHorizData, List[RegistroREHorizData], pd.DataFrame]
    ]:
        """
        Obtém um registro que cadastra o horizonte de validade de uma
        restrição elétrica com intervalo de data.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param data_inicio: data inicial de validade da restrição
        :type data_inicio: datetime | None
        :param data_fim: data final de validade da restrição
        :type data_fim: datetime | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroREHorizData` |
            list[:class:`RegistroREHorizData`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroREHorizData,
            codigo_restricao=codigo_restricao,
            data_inicio=data_inicio,
            data_fim=data_fim,
            df=df,
        )

    def re_per_pat(
        self,
        codigo_restricao: Optional[int] = None,
        periodo_inicio: Optional[int] = None,
        periodo_fim: Optional[int] = None,
        patamar: Optional[int] = None,
        formula: Optional[str] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroREPerPat, List[RegistroREPerPat], pd.DataFrame]
    ]:
        """
        Obtém um registro que cadastra uma restrição elétrica (RE)
        que varia ao longo do tempo, informada por intervalo de período.


        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param periodo_inicio: período inicial de validade da restrição
        :type periodo_inicio: int | None
        :param periodo_fim: período final de validade da restrição
        :type periodo_fim: int | None
        :param patamar: patamar de carga de validade da restrição
        :type patamar: int | None
        :param formula: equação da restrição
        :type formula: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroREPerPat` |
            list[:class:`RegistroREPerPat`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroREPerPat,
            codigo_restricao=codigo_restricao,
            periodo_inicio=periodo_inicio,
            periodo_fim=periodo_fim,
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
        Union[RegistroREDataPat, List[RegistroREDataPat], pd.DataFrame]
    ]:
        """
        Obtém um registro que cadastra uma restrição elétrica (RE)
        que varia ao longo do tempo, informada por intervalo de data.


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
        :rtype: :class:`RegistroREDataPat` |
            list[:class:`RegistroREDataPat`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroREDataPat,
            codigo_restricao=codigo_restricao,
            data_inicio=data_inicio,
            data_fim=data_fim,
            patamar=patamar,
            formula=formula,
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
            RegistroRELimFormDataPat,
            List[RegistroRELimFormDataPat],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que cadastra os limites por horizonte, definido
        por intervalo de data, e por patamar para uma restrição elétrica.

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
        :rtype: :class:`RegistroRELimFormDataPat` |
            list[:class:`RegistroRELimFormDataPat`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRELimFormDataPat,
            codigo_restricao=codigo_restricao,
            data_inicio=data_inicio,
            data_fim=data_fim,
            patamar=patamar,
            limite_inferior=limite_inferior,
            limite_superior=limite_superior,
            df=df,
        )

    def re_lim_form_per_pat(
        self,
        codigo_restricao: Optional[int] = None,
        periodo_inicio: Optional[int] = None,
        periodo_fim: Optional[int] = None,
        patamar: Optional[int] = None,
        limite_inferior: Optional[float] = None,
        limite_superior: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            RegistroRELimFormPerPat,
            List[RegistroRELimFormPerPat],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém um registro que cadastra os limites por horizonte, definido
        por intervalo de período, e por patamar para uma restrição elétrica.

        :param codigo_restricao: código que especifica a restrição
        :type codigo_restricao: int | None
        :param periodo_inicio: periodo inicial de validade dos limites
        :type periodo_inicio: int | None
        :param periodo_fim: periodo final de validade dos limites
        :type periodo_fim: int | None
        :param patamar: patamar de validade dos limites
        :type patamar: int | None
        :param limite_inferior: limite inferior da restrição
        :type limite_inferior: float | None
        :param limite_superior: limite superior da restrição
        :type limite_superior: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRELimFormPerPat` |
            list[:class:`RegistroRELimFormPerPat`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRELimFormPerPat,
            codigo_restricao=codigo_restricao,
            periodo_inicio=periodo_inicio,
            periodo_fim=periodo_fim,
            patamar=patamar,
            limite_inferior=limite_inferior,
            limite_superior=limite_superior,
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
        Obtém um registro que cadastra um alias elétrico.

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

    def alias_elet_val_per_pat(
        self,
        codigo_alias: Optional[int] = None,
        periodo_inicio: Optional[int] = None,
        periodo_fim: Optional[int] = None,
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
        alias para cada período e patamar.

        :param codigo_alias: código que especifica o alias
        :type codigo_alias: int | None
        :param periodo_inicio: periodo inicial de validade do dado
        :type periodo_inicio: datetime | None
        :param periodo_fim: periodo final de validade do dado
        :type periodo_fim: datetime | None
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
            periodo_inicio=periodo_inicio,
            periodo_fim=periodo_fim,
            patamar=patamar,
            valor=valor,
            df=df,
        )

    def re_regra_ativa(
        self,
        codigo_regra_ativacao: Optional[int] = None,
        regra_ativacao: Optional[str] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroRERegraAtiva, List[RegistroRERegraAtiva], pd.DataFrame]
    ]:
        """
        Obtém um registro que define uma regra para ativação e
        desativação de restrições elétricas.

        :param codigo_regra_ativacao: código que especifica a regra de ativação
        :type codigo_regra_ativacao: int | None
        :param regra_ativacao: texto que define a regra condicional para ativação
        :type regra_ativacao: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRERegraAtiva` |
            list[:class:`RegistroRERegraAtiva`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRERegraAtiva,
            codigo_regra_ativacao=codigo_regra_ativacao,
            regra_ativacao=regra_ativacao,
            df=df,
        )

    def re_habilita(
        self,
        codigo_restricao: Optional[int] = None,
        codigo_regra_ativacao: Optional[int] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroREHabilita, List[RegistroREHabilita], pd.DataFrame]
    ]:
        """
        Obtém um registro que contém a associação entre uma regra
        de ativação e uma restrição elétrica.

        :param codigo_restricao: código que especifica a restrição elétrica
        :type codigo_restricao: int | None
        :param codigo_regra_ativacao: código que especifica a regra de ativação
        :type codigo_regra_ativacao: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroREHabilita` |
            list[:class:`RegistroREHabilita`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroREHabilita,
            codigo_restricao=codigo_restricao,
            codigo_regra_ativacao=codigo_regra_ativacao,
            df=df,
        )

    def re_trat_viol(
        self,
        codigo_restricao: Optional[int] = None,
        tipo_violacao: Optional[str] = None,
        custo_violacao: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroRETratViol, List[RegistroRETratViol], pd.DataFrame]
    ]:
        """
        Obtém um registro que contém definição do tipo de violação e o
        valor do custo de violação de uma restrição elétrica.

        :param codigo_restricao: código que especifica a restrição elétrica
        :type codigo_restricao: int | None
        :param tipo_violacao: define o tipo de violação da restrição elétrica
        :type tipo_violacao: str | None
        :param custo_violacao: define o custo de violação da restrição elétrica
        :type custo_violacao: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRETratViol` |
            list[:class:`RegistroRETratViol`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRETratViol,
            codigo_restricao=codigo_restricao,
            tipo_violacao=tipo_violacao,
            custo_violacao=custo_violacao,
            df=df,
        )

    def re_trat_viol_per(
        self,
        codigo_restricao: Optional[int] = None,
        periodo_inicio: Optional[int] = None,
        periodo_fim: Optional[int] = None,
        tipo_violacao: Optional[str] = None,
        custo_violacao: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[RegistroRETratViolPer, List[RegistroRETratViolPer], pd.DataFrame]
    ]:
        """
        Obtém um registro que contém definição do tipo de violação e o
        valor do custo de violação de uma restrição elétrica definida para um
        intervalo de período.

        :param codigo_restricao: código que especifica a restrição elétrica
        :type codigo_restricao: int | None
        :param periodo_inicio: periodo inicial de validade do dado
        :type periodo_inicio: int | None
        :param periodo_fim: periodo final de validade do dado
        :type periodo_fim: int | None
        :param tipo_violacao: define o tipo de violação da restrição elétrica
        :type tipo_violacao: str | None
        :param custo_violacao: define o custo de violação da restrição elétrica
        :type custo_violacao: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroRETratViolPer` |
            list[:class:`RegistroRETratViolPer`] | `pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroRETratViol,
            codigo_restricao=codigo_restricao,
            periodo_inicio=periodo_inicio,
            periodo_fim=periodo_fim,
            tipo_violacao=tipo_violacao,
            custo_violacao=custo_violacao,
            df=df,
        )
