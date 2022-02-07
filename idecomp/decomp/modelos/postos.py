from typing import List, BinaryIO
import numpy as np  # type: ignore
from io import BufferedReader

from idecomp._utils.registrosbinario import RegistroAnBinario
from idecomp._utils.registrosbinario import RegistroInBinario
from idecomp._utils.leiturabinario import LeituraBinario
from idecomp._utils.blocobinario import BlocoBinario


class BlocoBinarioPosto(BlocoBinario):
    def __init__(self):
        super().__init__()
        self._dados = []

    # Override
    def le(self, arq: BufferedReader):
        """ """
        reg_nome = RegistroAnBinario(12)
        reg_ano = RegistroInBinario(32)
        nome = reg_nome.le_registro(arq)
        anos = reg_ano.le_linha_tabela(arq, 2)
        self._dados = [nome, *anos]

    # Override
    def escreve(self, arq: BinaryIO):
        """ """
        arq.write(self._dados[0].ljust(12).encode("ISO-8859-1"))
        anos = np.array(self._dados[1:]).astype("int32")
        anos.tofile(arq)
        pass


class LeituraPostos(LeituraBinario):
    """
    Classe com utilidades gerais para leitura de arquivos
    do DECOMP com comentários.
    """

    def __init__(self, diretorio: str):
        super().__init__(diretorio)

    def _cria_blocos_leitura(self) -> List[BlocoBinario]:
        """
        Método que cria a lista de blocos a serem lidos no arquivo.
        Implementa o Factory Pattern.
        """
        MAX_BLOCOS = 600

        b: List[BlocoBinario] = [BlocoBinarioPosto() for _ in range(MAX_BLOCOS)]

        return b
