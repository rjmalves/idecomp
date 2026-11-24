from typing import Any, TypeVar

import pandas as pd  # type: ignore[import-untyped]
from cfinterface.files.blockfile import BlockFile

from idecomp.decomp.modelos.decomptim import BlocoTemposEtapas


class Decomptim(BlockFile):
    """
    Armazena os dados de saída do DECOMP referentes ao
    tempo de execução das etapas do programa.

    Esta classe lida com as informações de saída do
    DECOMP e reproduzidas no `decomp.tim`.

    """

    T = TypeVar("T")

    BLOCKS = [
        BlocoTemposEtapas,
    ]

    def __init__(self, data: Any = ...) -> None:
        super().__init__(data)

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
