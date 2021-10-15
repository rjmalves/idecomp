from abc import abstractmethod
import numpy as np  # type: ignore
from io import BufferedReader
from typing import Any, List


class RegistroBinario:
    """
    Classe geral que modela os registros existentes
    nos arquivos binários do DECOMP.
    """
    def __init__(self, tamanho: int):
        self.tamanho = tamanho

    @abstractmethod
    def le_registro(self,
                    arq: BufferedReader) -> Any:
        """
        Função genérica para leitura de um valor de registro
        binário em um arquivo
        """
        pass

    @abstractmethod
    def le_linha_tabela(self,
                        arq: BufferedReader,
                        num_colunas: int) -> List[Any]:
        """
        Função genérica para leitura de uma linha de uma
        tabela com vários registros iguais.
        """
        pass


class RegistroAnBinario(RegistroBinario):
    """
    Registro de strings em arquivos binários do DECOMP.
    """
    def __init__(self,
                 tamanho: int,
                 encoding: str = "ISO-8859-1"):
        super().__init__(tamanho)
        self._encoding = encoding

    def le_registro(self,
                    arq: BufferedReader) -> str:
        """
        Lê o conteúdo de uma string existente em posições de um
        arquivo binário e retorna o valor sem espaços adicionais.
        """
        return arq.read(self.tamanho).decode(self._encoding).strip()

    def le_linha_tabela(self,
                        arq: BufferedReader,
                        num_colunas: int) -> List[str]:
        """
        Lê o conteúdo de uma linha de tabela com strings.
        """
        lista_valores: List[str] = []
        # Gera a lista com as colunas de início de cada valor
        for i in range(num_colunas):
            lista_valores.append(self.le_registro(arq))
        return lista_valores


class RegistroInBinario(RegistroBinario):
    """
    Registro de números inteiros nos arquivos binários do DECOMP.
    """
    def __init__(self,
                 num_bits: int = 8):
        super().__init__(int(num_bits / 8))
        if num_bits == 8:
            self._tipo = np.int8  # type: ignore
        elif num_bits == 16:
            self._tipo = np.int16  # type: ignore
        elif num_bits == 32:
            self._tipo = np.int32  # type: ignore
        else:
            self._tipo = np.int64  # type: ignore

    def le_registro(self,
                    arq: BufferedReader) -> int:
        """
        Lê o conteúdo de um inteiro existente em posições de um arquivo
        binário do DECOMP e retorna o valor já convertido.
        """
        return int(np.fromfile(arq,
                               dtype=self._tipo,
                               count=1)[0])

    def le_linha_tabela(self,
                        arq: BufferedReader,
                        num_colunas: int) -> List[int]:
        """
        Lê o conteúdo de uma linha de tabela com inteiros.
        """
        lista_valores: List[int] = np.fromfile(arq,
                                               dtype=self._tipo,
                                               count=num_colunas)
        return [int(v) for v in lista_valores]


class RegistroFnBinario(RegistroBinario):
    """
    Registro de números reais existentes nos arquivos binários
    do DECOMP.
    """
    def __init__(self,
                 num_bits: int = 32):
        super().__init__(int(num_bits / 8))
        if num_bits == 32:
            self._tipo = np.float32  # type: ignore
        elif num_bits == 64:
            self._tipo = np.float64  # type: ignore

    def le_registro(self,
                    arq: BufferedReader) -> float:
        """
        Lê o conteúdo de um inteiro existente em posições de um arquivo
        binário do DECOMP e retorna o valor já convertido.
        """
        return float(np.fromfile(arq,
                                 dtype=self._tipo,
                                 count=1)[0])

    def le_linha_tabela(self,
                        arq: BufferedReader,
                        num_colunas: int) -> List[float]:
        """
        Lê o conteúdo de uma linha de tabela com valores reais.
        """
        lista_valores: List[float] = np.fromfile(arq,
                                                 dtype=self._tipo,
                                                 count=num_colunas)
        return [float(v) for v in lista_valores]
