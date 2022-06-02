from cfinterface.files.registerfile import RegisterFile
from idecomp.decomp.modelos.dadgnl import TG, GS, NL, GL
from typing import Type, List, Optional, TypeVar, Any


class DadGNL(RegisterFile):
    """
    Armazena os dados de entrada gerais do DECOMP.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP no `dadger.rvx`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    Atualmente, são suportados os registros:
    `TE`, `SB`, `UH`, `CT`, `DP`, `TX`, `GP`, `NI`, `DT`, `RE`, `LU`,
    `VI`, `IR`, `FC`, `TI`, `HV`, `LV`, `HQ`, `LQ` `HE`, `EV` e `FJ`.

    É possível ler as informações existentes em arquivos a partir do
    método `le_arquivo()` e escreve um novo arquivo a partir do método
    `escreve_arquivo()`.

    """

    T = TypeVar("T")

    REGISTERS = [TG, GS, NL, GL]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="dadgnl.rv0") -> "DadGNL":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="dadgnl.rv0"):
        self.write(diretorio, nome_arquivo)

    def __registros_por_tipo(self, registro: Type[T]) -> List[T]:
        """
        Obtém um gerador de blocos de um tipo, se houver algum no arquivo.
        :param bloco: Um tipo de bloco para ser lido
        :type bloco: T
        :param indice: O índice do bloco a ser acessado, dentre os do tipo
        :type indice: int
        """
        return [b for b in self.data.of_type(registro)]

    def __obtem_registro_com_codigo(
        self, tipo: Type[T], codigo: int
    ) -> Optional[T]:
        regs: List[Any] = self.__registros_por_tipo(tipo)
        for r in regs:
            if r.codigo == codigo:
                return r
        return None

    def __obtem_registro_do_estagio(
        self, tipo: Type[T], codigo: int, estagio: int
    ) -> Optional[T]:
        regs: List[Any] = self.__registros_por_tipo(tipo)
        for r in regs:
            if all([r.codigo == codigo, r.estagio == estagio]):
                return r
        return None

    def __obtem_registros(self, tipo: Type[T]) -> List[T]:
        return self.__registros_por_tipo(tipo)

    def tg(self, codigo: int, estagio: int) -> Optional[TG]:
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
        return self.__obtem_registro_do_estagio(TG, codigo, estagio)

    def gs(self, mes: int) -> Optional[GS]:
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
        return None

    def nl(self, codigo: int) -> Optional[NL]:
        """
        Obtém um registro que define o número de lags para o despacho
        de uma UTE.

        :param codigo: código da UTE
        :type codigo: int

        :return: Um registro do tipo :class:`NL`
        """
        return self.__obtem_registro_com_codigo(NL, codigo)

    def gl(self, codigo: int, estagio: int) -> Optional[GL]:
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
        return self.__obtem_registro_do_estagio(GL, codigo, estagio)
