from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile
from idecomp.decomp.modelos.dadgnl import TG, GS, NL, GL
from typing import Type, List, Optional, TypeVar, Union
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class DadGNL(RegisterFile):
    """
    Armazena os dados de entrada gerais do DECOMP.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP no `dadgnl.rvx`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    Atualmente, são suportados os registros:
    `TG`, `GS`, `NL` e `GL`

    É possível ler as informações existentes em arquivos a partir do
    método `le_arquivo()` e escreve um novo arquivo a partir do método
    `escreve_arquivo()`.

    """

    T = TypeVar("T", bound=Register)

    REGISTERS = [TG, GS, NL, GL]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="dadgnl.rv0") -> "DadGNL":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="dadgnl.rv0"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    def __registros_ou_df(
        self, t: Type[T], **kwargs
    ) -> Optional[Union[T, List[T], pd.DataFrame]]:
        if kwargs.get("df"):
            return self._as_df(t)
        else:
            kwargs_sem_df = {k: v for k, v in kwargs.items() if k != "df"}
            return self.data.get_registers_of_type(t, **kwargs_sem_df)

    def tg(
        self,
        codigo: Optional[int] = None,
        subsistema: Optional[int] = None,
        nome: Optional[str] = None,
        estagio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[TG, List[TG], pd.DataFrame]]:
        """
        Obtém um registro que define uma usina termelétrica existente
        no estudo descrito pelo :class:`DadGNL`.

        :param codigo: código que especifica o registro
            da UTE
        :type codigo: int | None
        :param subsistema: código que especifica o subsistema
            da UTE
        :type subsistema: int | None
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
            codigo=codigo,
            subsistema=subsistema,
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
        mês de estudo no :class:`DadGNL`.

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
        codigo: Optional[int] = None,
        subsistema: Optional[int] = None,
        lag: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[NL, List[NL], pd.DataFrame]]:
        """
        Obtém um registro que define o número de lags para o despacho
        de uma UTE.

        :param codigo: código da UTE
        :type codigo: int | None
        :param subsistema: subsistema da UTE
        :type subsistema: int | None
        :param lag: número de lags da UTE
        :type lag: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`NL` | list[:class:`NL`] | :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            NL, codigo=codigo, subsistema=subsistema, lag=lag, df=df
        )

    def gl(
        self,
        codigo: Optional[int] = None,
        subsistema: Optional[int] = None,
        estagio: Optional[int] = None,
        data_inicio: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[GL, List[GL], pd.DataFrame]]:
        """
        Obtém um registro que define o despacho por patamar
        e a duração dos patamares para uma UTE GNL.

        :param codigo: código que especifica o registro
            da UTE
        :type codigo: int | None
        :param subsistema: subsistema da UTE
        :type subsistema: int | None
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
            codigo=codigo,
            subsistema=subsistema,
            estagio=estagio,
            data_inicio=data_inicio,
            df=df,
        )
