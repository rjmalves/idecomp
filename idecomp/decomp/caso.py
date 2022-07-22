from idecomp.decomp.modelos.caso import NomeCaso

from cfinterface.files.sectionfile import SectionFile
from typing import Type, TypeVar, Optional


class Caso(SectionFile):
    """
    Armazena os dados de entrada do NEWAVE referentes ao nome do arquivo
    que define os arquivos do caso.

    Esta classe lida com informações de entrada fornecidas ao NEWAVE e
    que podem ser modificadas através do arquivo `caso.dat`.

    """

    T = TypeVar("T")

    SECTIONS = [NomeCaso]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="caso.dat") -> "Caso":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="caso.dat"):
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

    @property
    def arquivos(self) -> Optional[str]:
        """
        Caminho para o arquivo `arquivos.dat` de entrada do DECOMP.

        :return: O caminho para o arquivo
        :rtype: str | None
        """
        b = self.__bloco_por_tipo(NomeCaso, 0)
        if b is not None:
            return b.data
        return None

    @arquivos.setter
    def arquivos(self, a: str):
        b = self.__bloco_por_tipo(NomeCaso, 0)
        if b is not None:
            b.data = a
