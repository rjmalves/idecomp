from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile
from idecomp.decomp.modelos.dadgnl import TG, GS, NL, GL
from typing import Type, List, Optional, TypeVar, Union
import pandas as pd  # type: ignore


class Dadgnl(RegisterFile):
    """
    Armazena os dados de entrada gerais do DECOMP.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP no `dadgnl.rvx`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    Atualmente, são suportados os registros:
    `TG`, `GS`, `NL` e `GL`


    """

    T = TypeVar("T", bound=Register)

    REGISTERS = [TG, GS, NL, GL]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    def __expande_colunas_df(self, df: pd.DataFrame) -> pd.DataFrame:
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
    ) -> Optional[Union[T, List[T], pd.DataFrame]]:
        if kwargs.get("df"):
            return self.__expande_colunas_df(self._as_df(t))
        else:
            kwargs_sem_df = {k: v for k, v in kwargs.items() if k != "df"}
            return self.data.get_registers_of_type(t, **kwargs_sem_df)

    def tg(
        self,
        codigo_usina: Optional[int] = None,
        codigo_submercado: Optional[int] = None,
        nome: Optional[str] = None,
        estagio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[TG, List[TG], pd.DataFrame]]:
        """
        Obtém um registro que define uma usina termelétrica existente
        no estudo descrito pelo :class:`Dadgnl`.

        :param codigo_usina: código que especifica o registro
            da UTE
        :type codigo_usina: int | None
        :param codigo_submercado: código que especifica o submercado
            da UTE
        :type codigo_submercado: int | None
        :param nome: nome da UTE
        :type nome: str | None
        :param estagio: Índice do estágio para o qual foi cadastrado
            o despacho da UTE
        :type estagio: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`TG` | list[:class:`TG`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            TG,
            codigo_usina=codigo_usina,
            codigo_submercado=codigo_submercado,
            nome=nome,
            estagio=estagio,
            df=df,
        )

    def gs(
        self,
        mes: Optional[int] = None,
        semanas: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[GS, List[GS], pd.DataFrame]]:
        """
        Obtém um registro que define o número de semanas em cada
        mês de estudo no :class:`Dadgnl`.

        :param mes: índice do mês no estudo
        :type mes: int | None
        :param semanas: número de semanas do mês
        :type semanas: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`GS` | list[:class:`GS`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(GS, mes=mes, semanas=semanas, df=df)

    def nl(
        self,
        codigo_usina: Optional[int] = None,
        codigo_submercado: Optional[int] = None,
        lag: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[NL, List[NL], pd.DataFrame]]:
        """
        Obtém um registro que define o número de lags para o despacho
        de uma UTE.

        :param codigo_usina: código da UTE
        :type codigo_usina: int | None
        :param codigo_submercado: código do submercado da UTE
        :type codigo_submercado: int | None
        :param lag: número de lags da UTE
        :type lag: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`NL` | list[:class:`NL`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            NL,
            codigo_usina=codigo_usina,
            codigo_submercado=codigo_submercado,
            lag=lag,
            df=df,
        )

    def gl(
        self,
        codigo_usina: Optional[int] = None,
        codigo_submercado: Optional[int] = None,
        estagio: Optional[int] = None,
        data_inicio: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[GL, List[GL], pd.DataFrame]]:
        """
        Obtém um registro que define o despacho por patamar
        e a duração dos patamares para uma UTE GNL.

        :param codigo_usina: código que especifica o registro
            da UTE
        :type codigo_usina: int | None
        :param codigo_submercado: código do submercado da UTE
        :type codigo_submercado: int | None
        :param estagio: estágio do despacho da UTE
        :type estagio: int | None
        :param data_inicio: data de início do estágio
            do despacho da UTE
        :type data_inicio: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`GL` | list[:class:`GL`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            GL,
            codigo_usina=codigo_usina,
            codigo_submercado=codigo_submercado,
            estagio=estagio,
            data_inicio=data_inicio,
            df=df,
        )
