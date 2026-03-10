from typing import Any, TypeVar

import pandas as pd  # type: ignore[import-untyped]
from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile

from idecomp.libs.modelos.usinas_hidreletricas import (
    HidreletricaCurvaJusante,
    HidreletricaCurvaJusanteAfogamentoExplicitoPadrao,
    HidreletricaCurvaJusanteAfogamentoExplicitoUsina,
    HidreletricaCurvaJusantePolinomioPorPartes,
    HidreletricaCurvaJusantePolinomioPorPartesSegmento,
)


class UsinasHidreletricas(RegisterFile):
    """
    Armazena os dados de entrada do DECOMP referentes aos dados
    das usinas hidrelétricas do problema.
    """

    T = TypeVar("T", bound=Register)

    REGISTERS = [
        HidreletricaCurvaJusanteAfogamentoExplicitoUsina,
        HidreletricaCurvaJusanteAfogamentoExplicitoPadrao,
        HidreletricaCurvaJusantePolinomioPorPartesSegmento,
        HidreletricaCurvaJusantePolinomioPorPartes,
        HidreletricaCurvaJusante,
    ]

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

    def hidreletrica_curvajusante(
        self,
        codigo_usina: int | None = None,
        indice_familia: int | None = None,
        nivel_montante_referencia: float | None = None,
        df: bool = False,
    ) -> (
        HidreletricaCurvaJusante
        | list[HidreletricaCurvaJusante]
        | pd.DataFrame
        | None
    ):
        """
        Obtém registros que cadastram uma família de curvas
        de jusante para uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas
        para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param indice_familia: índice da família de polinômios
        :type indice_familia: int | None
        :param nivel_montante_referencia: nível de montante de usina de
            jusante para cálculo da queda
        :type nivel_montante_referencia: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: `HidreletricaCurvaJusante` |
            List[`HidreletricaCurvaJusante`] | `None` | `DataFrame`
        """
        return self.__registros_ou_df(
            HidreletricaCurvaJusante,
            codigo_usina=codigo_usina,
            indice_familia=indice_familia,
            nivel_montante_referencia=nivel_montante_referencia,
            df=df,
        )

    def hidreletrica_curvajusante_polinomio(
        self,
        codigo_usina: int | None = None,
        indice_familia: int | None = None,
        numero_polinomios: int | None = None,
        df: bool = False,
    ) -> (
        HidreletricaCurvaJusantePolinomioPorPartes
        | list[HidreletricaCurvaJusantePolinomioPorPartes]
        | pd.DataFrame
        | None
    ):
        """
        Obtém registros que cadastram uma família de curvas
        de jusante para uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas
        para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param indice_familia: índice da família de polinômios
        :type indice_familia: int | None
        :param numero_polinomios: número de polinômios da família
        :type numero_polinomios: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: `HidreletricaCurvaJusantePolinomioPorPartes` |
            List[`HidreletricaCurvaJusantePolinomioPorPartes`] | `None` | `DataFrame`
        """
        return self.__registros_ou_df(
            HidreletricaCurvaJusantePolinomioPorPartes,
            codigo_usina=codigo_usina,
            indice_familia=indice_familia,
            numero_polinomios=numero_polinomios,
            df=df,
        )

    def hidreletrica_curvajusante_polinomio_segmento(
        self,
        codigo_usina: int | None = None,
        indice_familia: int | None = None,
        indice_polinomio: int | None = None,
        limite_inferior_vazao_jusante: float | None = None,
        limite_superior_vazao_jusante: float | None = None,
        coeficiente_a0: float | None = None,
        coeficiente_a1: float | None = None,
        coeficiente_a2: float | None = None,
        coeficiente_a3: float | None = None,
        coeficiente_a4: float | None = None,
        df: bool = False,
    ) -> (
        HidreletricaCurvaJusantePolinomioPorPartesSegmento
        | list[HidreletricaCurvaJusantePolinomioPorPartesSegmento]
        | pd.DataFrame
        | None
    ):
        """
        Obtém registros que cadastram os polinômios para cada família de curvas
        de jusante para uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas
        para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param indice_familia: índice da família de polinômios
        :type indice_familia: int | None
        :param indice_polinomio: índice do polinômio da família
        :type indice_polinomio: int | None
        :param limite_inferior_vazao_jusante: limite inferior de vazão de
            jusante para janela de validade do polinômio
        :type limite_inferior_vazao_jusante: float | None
        :param limite_superior_vazao_jusante: limite superior de vazão de
            jusante para janela de validade do polinômio
        :type limite_superior_vazao_jusante: float | None
        :param coeficiente_a0: coeficiente de grau 0 do polinômio
        :type coeficiente_a0: float | None
        :param coeficiente_a1: coeficiente de grau 1 do polinômio
        :type coeficiente_a1: float | None
        :param coeficiente_a2: coeficiente de grau 2 do polinômio
        :type coeficiente_a2: float | None
        :param coeficiente_a3: coeficiente de grau 3 do polinômio
        :type coeficiente_a3: float | None
        :param coeficiente_a4: coeficiente de grau 4 do polinômio
        :type coeficiente_a4: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`HidreletricaCurvaJusantePolinomioPorPartesSegmento` |
            list[:class:`HidreletricaCurvaJusantePolinomioPorPartesSegmento`] |
            None
        """
        return self.__registros_ou_df(
            HidreletricaCurvaJusantePolinomioPorPartesSegmento,
            codigo_usina=codigo_usina,
            indice_familia=indice_familia,
            indice_polinomio=indice_polinomio,
            limite_inferior_vazao_jusante=limite_inferior_vazao_jusante,
            limite_superior_vazao_jusante=limite_superior_vazao_jusante,
            coeficiente_a0=coeficiente_a0,
            coeficiente_a1=coeficiente_a1,
            coeficiente_a2=coeficiente_a2,
            coeficiente_a3=coeficiente_a3,
            coeficiente_a4=coeficiente_a4,
            df=df,
        )

    def hidreletrica_curvajusante_afogamentoexplicito_usina(
        self,
        codigo_usina: int | None = None,
        considera_afogamento: str | None = None,
        df: bool = False,
    ) -> (
        HidreletricaCurvaJusanteAfogamentoExplicitoUsina
        | list[HidreletricaCurvaJusanteAfogamentoExplicitoUsina]
        | pd.DataFrame
        | None
    ):
        """
        Obtém registros que habilitam ou desabilitam a consideração
        do tratamento do afogamento explícito por usina. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas
        para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param considera_afogamento: habilitação do afogamento
        :type considera_afogamento: str | None
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: `HidreletricaCurvaJusante` |
            List[`HidreletricaCurvaJusante`] | `None` | `DataFrame`
        """
        return self.__registros_ou_df(
            HidreletricaCurvaJusanteAfogamentoExplicitoUsina,
            codigo_usina=codigo_usina,
            considera_afogamento=considera_afogamento,
            df=df,
        )

    def hidreletrica_curvajusante_afogamentoexplicito_padrao(
        self, considera_afogamento: str | None = None, df: bool = False
    ) -> (
        HidreletricaCurvaJusanteAfogamentoExplicitoPadrao
        | list[HidreletricaCurvaJusanteAfogamentoExplicitoPadrao]
        | pd.DataFrame
        | None
    ):
        """
        Obtém registros que habilitam ou desabilitam a consideração
        do tratamento do afogamento explícito padrão.

        :param considera_afogamento: habilitação do afogamento
        :type considera_afogamento: str | None
        """
        return self.__registros_ou_df(
            HidreletricaCurvaJusanteAfogamentoExplicitoPadrao,
            considera_afogamento=considera_afogamento,
            df=df,
        )
