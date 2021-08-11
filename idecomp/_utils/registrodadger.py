from abc import abstractmethod
from typing import Any, IO, Optional


class RegistroDadger:
    """
    Registro genérico do arquivo dadger do DECOMP,
    especificado através de uma string de início e uma
    de terminação, com estados de leitura.
    """
    def __init__(self,
                 mnemonico: str,
                 obrigatorio: bool):
        self._mnemonico = mnemonico
        self._obrigatorio = obrigatorio
        self._dados: Any = None
        self._encontrado = False
        self._ordem = 0.
        self._lido = False
        self._linha = ""

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, RegistroDadger):
            return False
        bloco: RegistroDadger = o
        return self.dados == bloco.dados

    def e_inicio_de_registro(self, linha: str) -> bool:
        """
        Verifica se uma linha é início do registro.
        """
        return (self._mnemonico in linha[0:2]
                and linha[0] != "&"
                and not self._encontrado)

    def inicia_registro(self,
                        linha: str,
                        ordem: float) -> bool:
        """
        Inicia um registro com uma linha.
        """
        if not self._encontrado:
            self._encontrado = True
            self._linha = linha
            self._ordem = ordem
        return self._encontrado and not self._lido

    def le_registro(self) -> Optional[bool]:
        """
        """
        self._lido = True
        return self.le()

    @abstractmethod
    def le(self):
        pass

    @abstractmethod
    def escreve(self, arq: IO):
        pass

    @property
    def concluido(self):
        if self._obrigatorio:
            return self._lido
        else:
            return True

    @property
    def encontrado(self):
        return self._encontrado and not self._lido

    @property
    def dados(self) -> Any:
        """
        Retorna os dados lidos pelo registro.
        """
        return self._dados

    @dados.setter
    def dados(self, d: Any):
        self._dados = d


class TipoRegistroAC:
    """
    Classe base para os diferentes tipos possíveis de
    registros AC, baseados nos diferentes mnemônicos.
    """
    mnemonico = ""

    def __init__(self,
                 linha: str) -> None:
        self._linha = linha
        self._dados: Any = []

    @abstractmethod
    def le(self):
        pass

    @property
    @abstractmethod
    def linha_escrita(self) -> str:
        pass
