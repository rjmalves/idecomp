from idecomp.decomp.modelos.arquivos import BlocoNomesArquivos

from cfinterface.files.sectionfile import SectionFile
from typing import TypeVar, Optional, List


class Arquivos(SectionFile):
    """
    Armazena os dados de entrada do DECOMP referentes ao arquivo
    geralmente denominado `rvX`, que contém os arquivos.

    Esta classe lida com informações de entrada do DECOMP e
    que deve se referir aos nomes dos demais arquivos de entrada
    utilizados para o caso em questão.

    """

    T = TypeVar("T")

    SECTIONS = [BlocoNomesArquivos]

    def __le_nome_por_indice(self, indice: int) -> Optional[str]:
        b = self.data.get_sections_of_type(BlocoNomesArquivos)
        if isinstance(b, BlocoNomesArquivos):
            if indice in b.data.index:
                dado = b.data.iloc[indice, 0]
                if isinstance(dado, str):
                    return dado
        return None

    def __atualiza_nome_por_indice(self, indice: int, nome: str):
        b = self.data.get_sections_of_type(BlocoNomesArquivos)
        if isinstance(b, BlocoNomesArquivos):
            if indice in b.data.index:
                b.data.iloc[indice, 0] = nome

    @property
    def arquivos(self) -> List[str]:
        """
        Os nomes dos arquivos utilizados.

        :return: Os arquivos na mesma ordem em que são declarados
        :rtype: List[str]
        """
        b = self.data.get_sections_of_type(BlocoNomesArquivos)
        return (
            [] if not isinstance(b, BlocoNomesArquivos) else b.data.iloc[:, 0]
        )

    @property
    def dadger(self) -> Optional[str]:
        """
        Nome do arquivo de dados gerais utilizado pelo DECOMP.
        """
        return self.__le_nome_por_indice(0)

    @dadger.setter
    def dadger(self, arq: str):
        self.__atualiza_nome_por_indice(0, arq)

    @property
    def vazoes(self) -> Optional[str]:
        """
        Nome do arquivo de vazões incrementais afluentes.
        """
        return self.__le_nome_por_indice(1)

    @vazoes.setter
    def vazoes(self, arq: str):
        self.__atualiza_nome_por_indice(1, arq)

    @property
    def hidr(self) -> Optional[str]:
        """
        Nome do arquivo de cadastro dos dados das hidrelétricas.
        """
        return self.__le_nome_por_indice(2)

    @hidr.setter
    def hidr(self, arq: str):
        self.__atualiza_nome_por_indice(2, arq)

    @property
    def mlt(self) -> Optional[str]:
        """
        Nome do arquivo com as médias mensais de longo termo (MLT).
        """
        return self.__le_nome_por_indice(3)

    @mlt.setter
    def mlt(self, arq: str):
        self.__atualiza_nome_por_indice(3, arq)

    @property
    def perdas(self) -> Optional[str]:
        """
        Nome do arquivo com as perdas no sistema.
        """
        return self.__le_nome_por_indice(4)

    @perdas.setter
    def perdas(self, arq: str):
        self.__atualiza_nome_por_indice(4, arq)

    @property
    def dadgnl(self) -> Optional[str]:
        """
        Nome do arquivo com os dados das usinas térmicas GNL.
        """
        return self.__le_nome_por_indice(5)

    @dadgnl.setter
    def dadgnl(self, arq: str):
        self.__atualiza_nome_por_indice(5, arq)

    @property
    def caminho(self) -> Optional[str]:
        """
        Caminho para os executáveis do DECOMP.
        """
        return self.__le_nome_por_indice(6)

    @caminho.setter
    def caminho(self, arq: str):
        self.__atualiza_nome_por_indice(6, arq)
