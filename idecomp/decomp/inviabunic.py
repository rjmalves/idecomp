from idecomp.decomp.modelos.inviabunic import BlocoInviabilidadesIteracoes
from idecomp.decomp.modelos.inviabunic import BlocoInviabilidadesSimFinal

from cfinterface.files.blockfile import BlockFile
from typing import TypeVar, Optional
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


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

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="inviab_unic.rv0"
    ) -> "InviabUnic":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    @property
    def inviabilidades_iteracoes(self) -> Optional[pd.DataFrame]:
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
    def inviabilidades_simulacao_final(self) -> Optional[pd.DataFrame]:
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
