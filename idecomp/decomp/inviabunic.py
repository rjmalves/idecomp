from idecomp.decomp.modelos.inviabunic import BlocoInviabilidadesIteracoes
from idecomp.decomp.modelos.inviabunic import BlocoInviabilidadesSimFinal

from cfinterface.files.blockfile import BlockFile
from typing import Type, TypeVar, Optional
import pandas as pd  # type: ignore


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
        return cls.read(diretorio, nome_arquivo)

    def __bloco_por_tipo(self, bloco: Type[T], indice: int) -> Optional[T]:
        """
        Obtém um gerador de blocos de um tipo, se houver algum no arquivo.

        :param bloco: Um tipo de bloco para ser lido
        :type bloco: T
        :param indice: O índice do bloco a ser acessado, dentre os do tipo
        :type indice: int
        :return: O gerador de blocos, se houver
        :rtype: Optional[Generator[T], None, None]
        """
        try:
            return next(
                b
                for i, b in enumerate(self.data.of_type(bloco))
                if i == indice
            )
        except StopIteration:
            return None

    @property
    def inviabilidades_iteracoes(self) -> Optional[pd.DataFrame]:
        """
        Tabela das inviabilidades visitadas pelo modelo durante
        as iterações. As colunas são:

        - Iteração (`int`): iteração de ocorrência da inviabilidade
        - FWD/BWD (`int`): momento de ocorrência da inviabilidade (0/1)
        - Estágio (`int`): estágio da ocorrência da inviabilidade
        - Cenário (`int`): cenário da ocorrência da inviabilidade
        - Restrição (`str`): mensagem da restrição como no arquivo
        - Violação (`float`): quantidade de violação da restrição
        - Unidade (`str`): unidade de medição da restrição violada

        :return: Tabela das inviabilidades
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoInviabilidadesIteracoes, 0)
        if b is not None:
            return b.data
        return None

    @property
    def inviabilidades_simulacao_final(self) -> Optional[pd.DataFrame]:
        """
        Tabela das inviabilidades visitadas pelo modelo durante
        a simulação final. As colunas são:

        - Estágio (`int`): estágio da ocorrência da inviabilidade
        - Cenário (`int`): cenário da ocorrência da inviabilidade
        - Restrição (`str`): mensagem da restrição como impressa
        - Violação (`float`): quantidade de violação da restrição
        - Unidade (`str`): unidade de medição da restrição violada

        :return: Tabela das inviabilidades
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoInviabilidadesSimFinal, 0)
        if b is not None:
            return b.data
        return None
