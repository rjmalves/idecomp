from idecomp.decomp.modelos.arquivos import BlocoNomesArquivos

from cfinterface.files.sectionfile import SectionFile
from typing import Type, TypeVar, Optional, List


class Arquivos(SectionFile):
    """
    Armazena os dados de entrada do NEWAVE referentes ao arquivo
    `arquivos.dat`.

    Esta classe lida com informações de entrada do NEWAVE e
    que deve se referir aos nomes dos demais arquivos de entrada
    utilizados para o caso em questão.

    """

    T = TypeVar("T")

    SECTIONS = [BlocoNomesArquivos]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="arquivos.dat"
    ) -> "Arquivos":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="arquivos.dat"):
        self.write(diretorio, nome_arquivo)

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

    def __le_nome_por_indice(self, indice: int) -> str:
        b = self.__bloco_por_tipo(BlocoNomesArquivos, 0)
        return b.data.iloc[indice, 0] if b is not None else ""

    def __atualiza_nome_por_indice(self, indice: int, nome: str):
        b = self.__bloco_por_tipo(BlocoNomesArquivos, 0)
        if b is not None:
            b.data.iloc[indice, 0] = nome

    @property
    def arquivos(self) -> List[str]:
        """
        Os nomes dos arquivos utilizados.

        :return: Os arquivos na mesma ordem em que são declarados
        :rtype: List[str]
        """
        b = self.__bloco_por_tipo(BlocoNomesArquivos, 0)
        return [] if b is None else b.data.iloc[:, 0].tolist()

    @property
    def dadger(self) -> str:
        """
        Nome do arquivo de dados gerais utilizado pelo DECOMP.
        """
        return self.__le_nome_por_indice(0)

    @dadger.setter
    def dadger(self, arq: str):
        self.__atualiza_nome_por_indice(0, arq)

    @property
    def vazoes(self) -> str:
        """
        Nome do arquivo de vazões incrementais afluentes.
        """
        return self.__le_nome_por_indice(1)

    @vazoes.setter
    def vazoes(self, arq: str):
        self.__atualiza_nome_por_indice(1, arq)

    @property
    def hidr(self) -> str:
        """
        Nome do arquivo de cadastro dos dados das hidrelétricas.
        """
        return self.__le_nome_por_indice(2)

    @hidr.setter
    def hidr(self, arq: str):
        self.__atualiza_nome_por_indice(2, arq)

    @property
    def mlt(self) -> str:
        """
        Nome do arquivo com as médias mensais de longo termo (MLT).
        """
        return self.__le_nome_por_indice(3)

    @mlt.setter
    def mlt(self, arq: str):
        self.__atualiza_nome_por_indice(3, arq)

    @property
    def perdas(self) -> str:
        """
        Nome do arquivo com as perdas no sistema.
        """
        return self.__le_nome_por_indice(4)

    @perdas.setter
    def perdas(self, arq: str):
        self.__atualiza_nome_por_indice(4, arq)

    @property
    def dadgnl(self) -> str:
        """
        Nome do arquivo com os dados das usinas térmicas GNL.
        """
        return self.__le_nome_por_indice(5)

    @dadgnl.setter
    def dadgnl(self, arq: str):
        self.__atualiza_nome_por_indice(5, arq)

    @property
    def caminho(self) -> str:
        """
        Caminho para os executáveis do DECOMP.
        """
        return self.__le_nome_por_indice(6)

    @caminho.setter
    def caminho(self, arq: str):
        self.__atualiza_nome_por_indice(6, arq)
