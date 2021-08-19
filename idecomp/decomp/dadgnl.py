from idecomp.decomp.modelos.dadgnl import LeituraDadGNL
from idecomp.decomp.modelos.dadgnl import TG, GS, NL, GL
from idecomp._utils.arquivo import ArquivoRegistros
from idecomp._utils.dadosarquivo import DadosArquivoRegistros
from idecomp._utils.escritaregistros import EscritaRegistros

from typing import Type, List, Optional, TypeVar, Any


class DadGNL(ArquivoRegistros):
    """
    Armazena os dados de entrada das térmicas de
    despacho antecipado do DECOMP.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP no `dadgnl.rvx`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    É possível ler as informações existentes em arquivos a partir do
    método `le_arquivo()` e escreve um novo arquivo a partir do método
    `escreve_arquivo()`.

    """

    T = TypeVar("T")

    def __init__(self,
                 dados: DadosArquivoRegistros) -> None:
        """
        Construtor padrão
        """
        super().__init__(dados)

    # Override
    @classmethod
    def le_arquivo(cls,
                   diretorio: str,
                   nome_arquivo="dadgnl.rv0") -> 'DadGNL':
        """
        Realiza a leitura de um arquivo "dadgnl.rvx" existente em
        um diretório.

        :param diretorio: O caminho relativo ou completo para o diretório
            onde se encontra o arquivo
        :type diretorio: str
        :param nome_arquivo: Nome do arquivo a ser lido, potencialmente
            especificando a revisão. Tem como valor default "dadgnl.rv0"
        :type nome_arquivo: str, optional
        :return: Um objeto :class:`DadGNL` com informações do arquivo lido
        """
        leitor = LeituraDadGNL(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    def escreve_arquivo(self,
                        diretorio: str,
                        nome_arquivo="dadgnl.rv0"):
        """
        Realiza a escrita de um arquivo com as informações do
        objeto :class:`DadGNL`

        :param diretorio: O caminho relativo ou completo para o diretório
            onde será escrito o arquivo.
        :type diretorio: str
        :param nome_arquivo: Nome do arquivo a ser escrito.Tem como valor
            default "dadgnl.rv0"
        :type nome_arquivo: str, optional
        """
        escritor = EscritaRegistros(diretorio)
        escritor.escreve_arquivo(self._dados, nome_arquivo)

    def __obtem_registro(self,
                         tipo: Type[T]) -> T:
        """
        """
        for b in self._registros:
            if isinstance(b, tipo):
                return b
        raise ValueError(f"Não foi encontrado um registro do tipo {tipo}")

    def __obtem_registro_do_estagio(self,
                                    tipo: Type[T],
                                    codigo: int,
                                    estagio: int) -> Optional[T]:
        regs: List[Any] = self.__obtem_registros(tipo)
        for r in regs:
            if all([r.codigo == codigo,
                    r.estagio == estagio]):
                return r
        return None

    def __obtem_registros(self,
                          tipo: Type[T]) -> List[T]:
        registros = []
        for b in self._registros:
            if isinstance(b, tipo):
                registros.append(b)
        return registros

    def tg(self, codigo: int, estagio: int) -> TG:
        """
        Obtém um registro que define uma usina termelétrica existente
        no estudo descrito pelo :class:`DadGNL`.

        :param codigo: código que especifica o registro
            da UTE
        :type codigo: int
        :param estagio: Índice do estágio para o qual foi cadastrado
            o despacho da UTE
        :type estagio: int
        :return: Um registro do tipo :class:`TG`
        """
        reg = self.__obtem_registro_do_estagio(TG,
                                               codigo,
                                               estagio)
        if reg is None:
            raise ValueError("Não foi encontrado registro TG com" +
                             f" código {codigo} no estágio {estagio}")
        return reg

    def gs(self, mes: int) -> GS:
        """
        Obtém um registro que define o número de semanas em cada
        mês de estudo no :class:`DadGNL`.

        :param mes: índice do mês no estudo
        :type mes: int

        :return: Um registro do tipo :class:`GS`
        """
        regs: List[GS] = self.__obtem_registros(GS)
        for r in regs:
            if r.mes == mes:
                return r
        raise ValueError("Não foi encontrado registro GS" +
                         f" para o mês {mes}")

    def nl(self, codigo: int) -> NL:
        """
        Obtém um registro que define o número de lags para o despacho
        de uma UTE.

        :param codigo: código da UTE
        :type codigo: int

        :return: Um registro do tipo :class:`NL`
        """
        regs: List[NL] = self.__obtem_registros(NL)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro GS" +
                         f" para o código {codigo}")

    def gl(self, codigo: int, estagio: int) -> GL:
        """
        Obtém um registro que define o despacho por patamar
        e a duração dos patamares para uma UTE GNL.

        :param codigo: código que especifica o registro
            da UTE
        :type codigo: int
        :param estagio: Índice do estágio para o qual foi cadastrado
            o despacho da UTE
        :type estagio: int
        :return: Um registro do tipo :class:`GL`
        """
        reg = self.__obtem_registro_do_estagio(GL,
                                               codigo,
                                               estagio)
        if reg is None:
            raise ValueError("Não foi encontrado registro GL com" +
                             f" código {codigo} no estágio {estagio}")
        return reg
