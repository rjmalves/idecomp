from abc import abstractmethod
from .dadosarquivo import DadosArquivoBinarios


class ArquivoBinario:
    """ """

    def __init__(self, dados: DadosArquivoBinarios) -> None:
        self._dados = dados

    def __eq__(self, o: object) -> bool:
        """
        A igualdade entre arquivos avalia os dados interpretados e
        também os comentários externos.
        """
        if not isinstance(o, ArquivoBinario):
            return False
        d: ArquivoBinario = o
        dif = False
        for b1, b2 in zip(self._blocos, d._blocos):
            if b1 != b2:
                dif = True
                break
        return not dif

    @property
    def _blocos(self):
        return self._dados.blocos

    @classmethod
    @abstractmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="") -> "ArquivoBinario":
        pass

    @abstractmethod
    def escreve_arquivo(self, diretorio: str, nome_arquivo=""):
        pass
