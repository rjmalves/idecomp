
from typing import Dict, List

from.registrodadger import RegistroDadger


class DadosDadger:
    """
    """
    def __init__(self,
                 registros: List[RegistroDadger],
                 linhas_fora_registros: Dict[float, str]) -> None:
        self.__registros = registros
        self.__linhas_fora_registros = linhas_fora_registros
        pass

    @property
    def registros(self) -> List[RegistroDadger]:
        return self.__registros

    @property
    def linhas_fora_registros(self) -> Dict[float, str]:
        return self.__linhas_fora_registros
