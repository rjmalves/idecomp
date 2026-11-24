from datetime import datetime
from typing import Any, TypeVar

import pandas as pd  # type: ignore[import-untyped]
from cfinterface.components.block import Block
from cfinterface.files.blockfile import BlockFile

from idecomp.decomp.modelos.decomptim import (
    BlocoCaso,
    BlocoData,
    BlocoHora,
    BlocoNumeroProcessadores,
    BlocoPacoteOtimizacao,
    BlocoPlataforma,
    BlocoTemposEtapas,
    BlocoVersaoModelo,
)


class Decomptim(BlockFile):
    """
    Armazena os dados de saída do DECOMP referentes ao
    tempo de execução das etapas do programa.

    Esta classe lida com as informações de saída do
    DECOMP e reproduzidas no `decomp.tim`.

    """

    T = TypeVar("T")

    BLOCKS = [
        BlocoVersaoModelo,
        BlocoCaso,
        BlocoData,
        BlocoHora,
        BlocoNumeroProcessadores,
        BlocoPlataforma,
        BlocoPacoteOtimizacao,
        BlocoTemposEtapas,
    ]

    def __init__(self, data: Any = ...) -> None:
        super().__init__(data)

    def _dado_cabecalho(self, tipo: type[Block]) -> Any:
        b = self.data.get_blocks_of_type(tipo)
        return b.data if isinstance(b, tipo) else None

    @property
    def versao_modelo(self) -> str | None:
        """
        Obtém a versão do DECOMP que gerou o arquivo, isto é, o primeiro
        termo após `Versao` no cabeçalho, incluindo o sufixo de
        compilação quando existir (por exemplo `32.15.2_gurobi`).

        :return: A versão, ou `None` se a linha não existe no arquivo
        :rtype: str | None
        """
        return self._dado_cabecalho(BlocoVersaoModelo)

    @property
    def caso(self) -> str | None:
        """
        Obtém o nome do caso existente no cabeçalho do arquivo, como
        escrito (sem os espaços ao final).

        :return: O nome do caso, ou `None` se a linha não existe no
            arquivo
        :rtype: str | None
        """
        return self._dado_cabecalho(BlocoCaso)

    @property
    def data_hora_inicio(self) -> datetime | None:
        """
        Obtém a data e hora de início da execução do DECOMP, como escritas
        no cabeçalho do arquivo, sem fuso horário.

        :return: O instante de início, ou `None` se alguma das linhas
            `Data` e `Hora` não existe no arquivo
        :rtype: datetime | None
        """
        data = self._dado_cabecalho(BlocoData)
        hora = self._dado_cabecalho(BlocoHora)
        if data is None or hora is None:
            return None
        return datetime.combine(data, hora)

    @property
    def numero_processadores(self) -> int | None:
        """
        Obtém o número de processadores utilizados na execução do DECOMP.

        :return: O número de processadores, ou `None` se a linha não
            existe no arquivo
        :rtype: int | None
        """
        return self._dado_cabecalho(BlocoNumeroProcessadores)

    @property
    def plataforma(self) -> str | None:
        """
        Obtém a plataforma do executável do DECOMP, como escrita no
        cabeçalho do arquivo (por exemplo `LINUX (L)`).

        :return: A plataforma, ou `None` se a linha não existe no arquivo
        :rtype: str | None
        """
        return self._dado_cabecalho(BlocoPlataforma)

    @property
    def pacote_otimizacao(self) -> str | None:
        """
        Obtém o pacote de otimização do executável do DECOMP, como
        escrito no cabeçalho do arquivo (por exemplo `LIBSLV`).

        :return: O pacote de otimização, ou `None` se a linha não existe
            no arquivo
        :rtype: str | None
        """
        return self._dado_cabecalho(BlocoPacoteOtimizacao)

    @property
    def tempos_etapas(self) -> pd.DataFrame | None:
        """
        Obtém a tabela dos tempos de execução do DECOMP existente no
        :class:`Decomptim`

        - Etapa (`str`)
        - Tempo (`timedelta`)

        Possui sempre cinco linhas, na mesma ordem nos dois layouts do
        arquivo: `Leitura de Dados`, `Convergencia` (envio inicial mais
        os totais das iterações), `Simulacao Final`, `Impressao` (zero
        quando o arquivo não possui essa linha) e `Tempo Total`.

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None.
        """
        b = self.data.get_blocks_of_type(BlocoTemposEtapas)
        if isinstance(b, BlocoTemposEtapas):
            return b.data
        return None

    @property
    def tempos_iteracoes(self) -> pd.DataFrame | None:
        """
        Obtém a tabela dos tempos de cada iteração do processo iterativo
        do DECOMP existente no :class:`Decomptim`

        - iteracao (`int`)
        - envio_variaveis (`timedelta`)
        - descida_1a_parte (`timedelta`)
        - descida_2a_parte (`timedelta`)
        - retorno (`timedelta`)
        - total (`timedelta`)

        Possui uma linha por iteração concluída, isto é, com a linha
        `Total:` presente no arquivo. A iteração final truncada é
        descartada e uma fase ausente em uma iteração concluída vale
        zero. O envio de variáveis inicial e o grupo final
        (`Impressao` ou `Sim. Final`) não são linhas desta tabela: o
        tempo deles compõe :attr:`tempos_etapas`.

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None.
        """
        b = self.data.get_blocks_of_type(BlocoTemposEtapas)
        if isinstance(b, BlocoTemposEtapas):
            return b.tempos_iteracoes
        return None
