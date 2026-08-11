from typing import Any, TypeVar

import pandas as pd  # type: ignore[import-untyped]
from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile

from idecomp.libs.modelos.renovaveis import (
    PEECadastro,
    PEEConfiguracaoPeriodo,
    PEEGeracaoPeriodoPatamarCenario,
    PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal,
    PEEPotenciaInstaladaPeriodo,
    PEESubmercado,
)


class Renovaveis(RegisterFile):
    """
    Armazena os dados de entrada do DECOMP referentes aos dados
    das usinas renováveis (parques eólicos equivalentes) do problema.
    """

    T = TypeVar("T", bound=Register)

    REGISTERS = [
        PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal,
        PEEGeracaoPeriodoPatamarCenario,
        PEEPotenciaInstaladaPeriodo,
        PEEConfiguracaoPeriodo,
        PEESubmercado,
        PEECadastro,
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

    def pee_cad(
        self,
        codigo_pee: int | None = None,
        nome_pee: str | None = None,
        df: bool = False,
    ) -> PEECadastro | list[PEECadastro] | pd.DataFrame | None:
        """
        Obtém registros que cadastram um parque eólico equivalente.
        Opcionalmente, o retorno pode ser transformado em um `DataFrame`,
        apenas para leitura das informações.

        :param codigo_pee: código que especifica o parque
        :type codigo_pee: int | None
        :param nome_pee: nome do parque
        :type nome_pee: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: `PEECadastro` | list[`PEECadastro`] | `None` | `DataFrame`
        """
        return self.__registros_ou_df(
            PEECadastro,
            codigo_pee=codigo_pee,
            nome_pee=nome_pee,
            df=df,
        )

    def pee_subm(
        self,
        codigo_pee: int | None = None,
        codigo_submercado: int | None = None,
        df: bool = False,
    ) -> PEESubmercado | list[PEESubmercado] | pd.DataFrame | None:
        """
        Obtém registros que relacionam um parque eólico equivalente
        a um submercado. Opcionalmente, o retorno pode ser transformado
        em um `DataFrame`, apenas para leitura das informações.

        :param codigo_pee: código que especifica o parque
        :type codigo_pee: int | None
        :param codigo_submercado: código do submercado
        :type codigo_submercado: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: `PEESubmercado` | list[`PEESubmercado`] | `None` | `DataFrame`
        """
        return self.__registros_ou_df(
            PEESubmercado,
            codigo_pee=codigo_pee,
            codigo_submercado=codigo_submercado,
            df=df,
        )

    def pee_config_per(
        self,
        codigo_pee: int | None = None,
        estagio_inicial: int | None = None,
        estagio_final: int | None = None,
        estado_operacao: str | None = None,
        df: bool = False,
    ) -> (
        PEEConfiguracaoPeriodo
        | list[PEEConfiguracaoPeriodo]
        | pd.DataFrame
        | None
    ):
        """
        Obtém registros que definem a configuração de operação de um
        parque eólico equivalente por período. Opcionalmente, o retorno
        pode ser transformado em um `DataFrame`, apenas para leitura das
        informações.

        :param codigo_pee: código que especifica o parque
        :type codigo_pee: int | None
        :param estagio_inicial: estágio inicial de validade
        :type estagio_inicial: int | None
        :param estagio_final: estágio final de validade
        :type estagio_final: int | None
        :param estado_operacao: estado de operação do parque
        :type estado_operacao: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: `PEEConfiguracaoPeriodo` | list[`PEEConfiguracaoPeriodo`] |
            `None` | `DataFrame`
        """
        return self.__registros_ou_df(
            PEEConfiguracaoPeriodo,
            codigo_pee=codigo_pee,
            estagio_inicial=estagio_inicial,
            estagio_final=estagio_final,
            estado_operacao=estado_operacao,
            df=df,
        )

    def pee_pot_inst_per(
        self,
        codigo_pee: int | None = None,
        estagio_inicial: int | None = None,
        estagio_final: int | None = None,
        potencia_instalada: float | None = None,
        df: bool = False,
    ) -> (
        PEEPotenciaInstaladaPeriodo
        | list[PEEPotenciaInstaladaPeriodo]
        | pd.DataFrame
        | None
    ):
        """
        Obtém registros que definem a potência instalada de um parque
        eólico equivalente por período. Opcionalmente, o retorno pode ser
        transformado em um `DataFrame`, apenas para leitura das
        informações.

        :param codigo_pee: código que especifica o parque
        :type codigo_pee: int | None
        :param estagio_inicial: estágio inicial de validade
        :type estagio_inicial: int | None
        :param estagio_final: estágio final de validade
        :type estagio_final: int | None
        :param potencia_instalada: potência instalada do parque
        :type potencia_instalada: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: `PEEPotenciaInstaladaPeriodo` |
            list[`PEEPotenciaInstaladaPeriodo`] | `None` | `DataFrame`
        """
        return self.__registros_ou_df(
            PEEPotenciaInstaladaPeriodo,
            codigo_pee=codigo_pee,
            estagio_inicial=estagio_inicial,
            estagio_final=estagio_final,
            potencia_instalada=potencia_instalada,
            df=df,
        )

    def pee_ger_per_pat_cen(
        self,
        codigo_pee: int | None = None,
        estagio: int | None = None,
        patamar: int | None = None,
        cenario: int | None = None,
        geracao: float | None = None,
        df: bool = False,
    ) -> (
        list[
            PEEGeracaoPeriodoPatamarCenario
            | PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal
        ]
        | pd.DataFrame
        | None
    ):
        """
        Obtém registros que definem a geração de um parque eólico
        equivalente por período, patamar e cenário. Opcionalmente, o
        retorno pode ser transformado em um `DataFrame`, apenas para
        leitura das informações.

        O card `PEE-GER-PER-PAT-CEN` possui dois layouts, distinguidos pela
        quantidade de campos da linha: o de período único (5 campos) e o de
        intervalo de períodos (6 campos, com `PerFin`). Ambos são lidos e
        combinados neste método, expondo sempre as colunas
        `codigo_pee, estagio, patamar, cenario, geracao` e, quando o layout
        de intervalo está presente, também `estagio_final`.

        :param codigo_pee: código que especifica o parque
        :type codigo_pee: int | None
        :param estagio: estágio (período) de validade
        :type estagio: int | None
        :param patamar: índice do patamar de carga
        :type patamar: int | None
        :param cenario: índice do cenário
        :type cenario: int | None
        :param geracao: geração do parque
        :type geracao: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Os registros, se existirem.
        :rtype: list[`PEEGeracaoPeriodoPatamarCenario` |
            `PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal`] |
            `None` | `DataFrame`
        """
        tipos: tuple[type[Register], ...] = (
            PEEGeracaoPeriodoPatamarCenario,
            PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal,
        )
        if df:
            frames = [f for f in (self._as_df(t) for t in tipos) if not f.empty]
            if len(frames) == 0:
                return pd.DataFrame()
            if len(frames) == 1:
                return frames[0]
            return pd.concat(frames, ignore_index=True)
        registros: list[
            PEEGeracaoPeriodoPatamarCenario
            | PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal
        ] = []
        periodo_unico = self.data.get_registers_of_type(
            PEEGeracaoPeriodoPatamarCenario,
            codigo_pee=codigo_pee,
            estagio=estagio,
            patamar=patamar,
            cenario=cenario,
            geracao=geracao,
        )
        if periodo_unico is not None:
            registros.extend(
                periodo_unico
                if isinstance(periodo_unico, list)
                else [periodo_unico]
            )
        com_periodo_final = self.data.get_registers_of_type(
            PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal,
            codigo_pee=codigo_pee,
            estagio=estagio,
            patamar=patamar,
            cenario=cenario,
            geracao=geracao,
        )
        if com_periodo_final is not None:
            registros.extend(
                com_periodo_final
                if isinstance(com_periodo_final, list)
                else [com_periodo_final]
            )
        return registros if len(registros) > 0 else None
