from idecomp._utils.blocobinario import BlocoBinario
from .registrodecomp import RegistroDecomp
from .bloco import Bloco
from typing import Dict, List


class DadosArquivoBlocos:
    """
    """
    def __init__(self,
                 blocos: List[Bloco],
                 linhas_fora_blocos: Dict[int, str]) -> None:
        self.__blocos = blocos
        self.__linhas_fora_blocos = linhas_fora_blocos
        pass

    @property
    def blocos(self) -> List[Bloco]:
        return self.__blocos

    @property
    def linhas_fora_blocos(self) -> Dict[int, str]:
        return self.__linhas_fora_blocos


class DadosArquivoRegistros:
    """
    """
    def __init__(self,
                 registros: List[RegistroDecomp],
                 linhas_fora_registros: Dict[float, str]) -> None:
        self.__registros = registros
        self.__linhas_fora_registros = linhas_fora_registros
        pass

    @property
    def registros(self) -> List[RegistroDecomp]:
        return self.__registros

    @property
    def linhas_fora_registros(self) -> Dict[float, str]:
        return self.__linhas_fora_registros


class DadosArquivoBinarios:
    """
    """
    def __init__(self,
                 blocos: List[BlocoBinario]) -> None:
        self.__blocos = blocos

    @property
    def blocos(self) -> List[BlocoBinario]:
        return self.__blocos
