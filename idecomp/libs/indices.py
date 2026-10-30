from typing import Any, Literal, TypeVar, overload

import pandas as pd  # type: ignore[import-untyped]
from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile

from idecomp.libs.modelos.indices import RegistroIndice


class Indices(RegisterFile):
    """
    Armazena os dados do arquivo de índices das LIBS (``indices.csv``,
    nome definido pelo registro ``FA`` do ``dadger``), que associa cada
    identificador de card das LIBS ao arquivo que contém os seus
    registros.

    Regras de leitura e escrita:

    - toda linha que contém ``;`` e não começa com ``&`` (após os
      espaços iniciais) é um registro :class:`RegistroIndice`, no
      formato ``IDENTIFICADOR;DESCRICAO;ARQUIVO``;
    - as linhas iniciadas por ``&`` são comentários, mesmo quando
      contêm ``;``, e são reescritas sem alterações;
    - os espaços em torno dos valores são removidos e os identificadores
      não são convertidos para maiúsculas;
    - um campo vazio é lido como ``""``, e não como ``None``;
    - identificadores repetidos são mantidos como registros separados,
      na ordem do arquivo, sem gerar erro;
    - na escrita, os registros são reescritos como
      ``IDENTIFICADOR;DESCRICAO;ARQUIVO``.
    """

    T = TypeVar("T", bound=Register)

    REGISTERS = [RegistroIndice]

    def __init__(self, data: Any = ...) -> None:
        super().__init__(data)

    def __registros_ou_df(
        self, t: type[T], **kwargs: Any
    ) -> T | list[T] | pd.DataFrame | None:
        if kwargs.get("df"):
            return self._as_df(t)
        else:
            kwargs_sem_df = {k: v for k, v in kwargs.items() if k != "df"}
            return self.data.get_registers_of_type(t, **kwargs_sem_df)

    @overload
    def indices(
        self,
        identificador: str | None = None,
        arquivo: str | None = None,
        *,
        df: Literal[True],
    ) -> pd.DataFrame: ...
    @overload
    def indices(
        self,
        identificador: str | None = None,
        arquivo: str | None = None,
        df: Literal[False] = False,
    ) -> RegistroIndice | list[RegistroIndice] | None: ...
    @overload
    def indices(
        self,
        identificador: str | None = None,
        arquivo: str | None = None,
        df: bool = False,
    ) -> RegistroIndice | list[RegistroIndice] | pd.DataFrame | None: ...
    def indices(
        self,
        identificador: str | None = None,
        arquivo: str | None = None,
        df: bool = False,
    ) -> RegistroIndice | list[RegistroIndice] | pd.DataFrame | None:
        """
        Obtém registros que associam os identificadores dos cards das
        LIBS aos arquivos que contêm os seus registros.
        Opcionalmente, o retorno pode ser transformado em um `DataFrame`,
        com as colunas ``arquivo``, ``descricao`` e ``identificador``.

        :param identificador: o identificador do card das LIBS
        :type identificador: str | None
        :param arquivo: o arquivo que contém os registros do card
        :type arquivo: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Os registros, se existirem.
        :rtype: :class:`RegistroIndice` | list[:class:`RegistroIndice`] |
            :class:`pd.DataFrame` | None
        """
        return self.__registros_ou_df(
            RegistroIndice,
            identificador=identificador,
            arquivo=arquivo,
            df=df,
        )
