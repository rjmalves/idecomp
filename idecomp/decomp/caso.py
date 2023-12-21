from idecomp.decomp.modelos.caso import NomeCaso

from cfinterface.files.sectionfile import SectionFile
from typing import TypeVar, Optional


class Caso(SectionFile):
    """
    Armazena os dados de entrada do DECOMP referentes ao nome do arquivo
    que define os arquivos do caso.

    Esta classe lida com informações de entrada fornecidas ao DECOMP e
    que podem ser modificadas através do arquivo `caso.dat`.

    """

    T = TypeVar("T")

    SECTIONS = [NomeCaso]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @property
    def arquivos(self) -> Optional[str]:
        """
        Caminho para o arquivo `arquivos.dat` de entrada do DECOMP.

        :return: O caminho para o arquivo
        :rtype: str | None
        """
        b = self.data.get_sections_of_type(NomeCaso)
        if isinstance(b, NomeCaso):
            return b.data
        return None

    @arquivos.setter
    def arquivos(self, a: str):
        b = self.data.get_sections_of_type(NomeCaso)
        if isinstance(b, NomeCaso):
            b.data = a
