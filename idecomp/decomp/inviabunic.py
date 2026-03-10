from typing import Any, TypeVar

import pandas as pd  # type: ignore[import-untyped]
from cfinterface.files.blockfile import BlockFile

from idecomp.decomp.modelos.inviabunic import (
    BlocoInviabilidadesIteracoes,
    BlocoInviabilidadesSimFinal,
)


class InviabUnic(BlockFile):
    """
    Armazena os dados de saída do DECOMP referentes às inviabilidades
    ocorridas durante o processo de execução.

    Esta classe lida com as informações de saída fornecidas pelo
    DECOMP e reproduzidas no `inviab_unic.rvx`.
    """

    T = TypeVar("T")

    BLOCKS = [
        BlocoInviabilidadesIteracoes,
        BlocoInviabilidadesSimFinal,
    ]

    def __init__(self, data: Any = ...) -> None:
        super().__init__(data)

    @property
    def inviabilidades_iteracoes(self) -> pd.DataFrame | None:
        """
        Tabela das inviabilidades visitadas pelo modelo durante
        as iterações. As colunas são:

        - iteracao (`int`): iteração de ocorrência da inviabilidade
        - etapa (`int`): momento de ocorrência da inviabilidade (0 fwd / 1 bkd)
        - estagio (`int`): estágio da ocorrência da inviabilidade
        - cenario (`int`): cenário da ocorrência da inviabilidade
        - restricao (`str`): mensagem da restrição como no arquivo
        - violacao (`float`): quantidade de violação da restrição
        - unidade (`str`): unidade de medição da restrição violada

        :return: Tabela das inviabilidades
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoInviabilidadesIteracoes)
        if isinstance(b, BlocoInviabilidadesIteracoes):
            return b.data
        return None

    @property
    def inviabilidades_simulacao_final(self) -> pd.DataFrame | None:
        """
        Tabela das inviabilidades visitadas pelo modelo durante
        a simulação final. As colunas são:

        - estagio (`int`): estágio da ocorrência da inviabilidade
        - cenario (`int`): cenário da ocorrência da inviabilidade
        - restricao (`str`): mensagem da restrição como impressa
        - violacao (`float`): quantidade de violação da restrição
        - unidade (`str`): unidade de medição da restrição violada

        :return: Tabela das inviabilidades
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_blocks_of_type(BlocoInviabilidadesSimFinal)
        if isinstance(b, BlocoInviabilidadesSimFinal):
            return b.data
        return None
