from idecomp._utils.blocobinario import BlocoBinario
from typing import List


class DadosArquivoBinarios:
    """ """

    def __init__(self, blocos: List[BlocoBinario]) -> None:
        self.__blocos = blocos

    @property
    def blocos(self) -> List[BlocoBinario]:
        return self.__blocos
