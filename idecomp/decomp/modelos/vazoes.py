from typing import BinaryIO, List
import numpy as np  # type: ignore
from io import BufferedReader

from idecomp._utils.registrosbinario import RegistroInBinario
from idecomp._utils.leiturabinario import LeituraBinario
from idecomp._utils.blocobinario import BlocoBinario


class BlocoBinarioVazoes(BlocoBinario):
    def __init__(self):
        super().__init__()
        self._dados = []

    # Override
    def le(self, arq: BufferedReader):
        """
        """
        reg_teste = RegistroInBinario(32)
        vazoes = reg_teste.le_linha_tabela(arq, 600)
        self._dados = vazoes

    # Override
    def escreve(self, arq: BinaryIO):
        """
        """
        np.array(self._dados).astype("int32").tofile(arq)


class LeituraVazoes(LeituraBinario):
    """
    Classe com utilidades gerais para leitura de arquivos
    do DECOMP com comentários.
    """
    def __init__(self,
                 diretorio: str):
        super().__init__(diretorio)

    def _cria_blocos_leitura(self) -> List[BlocoBinario]:
        """
        Método que cria a lista de blocos a serem lidos no arquivo.
        Implementa o Factory Pattern.
        """
        MAX_BLOCOS = 9000

        b: List[BlocoBinario] = [BlocoBinarioVazoes()
                                 for _ in range(MAX_BLOCOS)]

        return b
