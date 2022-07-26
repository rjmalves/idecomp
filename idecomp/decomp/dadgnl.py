from cfinterface.files.registerfile import RegisterFile
from cfinterface.components.register import Register
from idecomp.decomp.modelos.dadgnl import TG, GS, NL, GL
from typing import Type, List, Optional, TypeVar, Union


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

    def __obtem_registro(self, tipo: Type[T]) -> Optional[T]:
        """ """
        r = self.__obtem_registros(tipo)
        return r[0] if len(r) > 0 else None

    def __obtem_registros(self, tipo: Type[T]) -> List[T]:
        return self.__registros_por_tipo(tipo)

    def __obtem_registros_com_filtros(
        self, tipo_registro: Type[T], **kwargs
    ) -> Optional[Union[T, List[T]]]:
        def __atende(r) -> bool:
            condicoes: List[bool] = []
            for k, v in kwargs.items():
                if v is not None:
                    condicoes.append(getattr(r, k) == v)
            return all(condicoes)

        regs_filtro = [
            r for r in self.__obtem_registros(tipo_registro) if __atende(r)
        ]
        if len(regs_filtro) == 0:
            return None
        elif len(regs_filtro) == 1:
            return regs_filtro[0]
        else:
            return regs_filtro

    def cria_registro(self, anterior: Register, registro: Register):
        """
        Adiciona um registro ao arquivo após um outro registro previamente
        existente.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.add_after(anterior, registro)

    def deleta_registro(self, registro: Register):
        """
        Remove um registro existente no arquivo.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.remove(registro)

    def lista_registros(self, tipo: Type[T]) -> List[T]:
        """
        Lista todos os registros presentes no arquivo que tenham o tipo `T`.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        return [r for r in self.data.of_type(tipo)]

    def append_registro(self, registro: Register):
        """
        Adiciona um registro ao arquivo na última posição.


        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.append(registro)

    def preppend_registro(self, registro: Register):
        """
        Adiciona um registro ao arquivo na primeira posição.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.preppend(registro)

    def tg(
        self,
        codigo: Optional[int] = None,
        subsistema: Optional[int] = None,
        nome: Optional[str] = None,
        estagio: Optional[int] = None,
    ) -> Optional[Union[TG, List[TG]]]:
        """
        Obtém um registro que define uma usina termelétrica existente
        no estudo descrito pelo :class:`DadGNL`.

        :param codigo: código que especifica o registro
            da UTE
        :type codigo: int | None
        :param subsistema: código que especifica o subsistema
            da UTE
        :type subsistema: int | None
        :param nome: nome da UTE
        :type nome: str | None
        :param estagio: Índice do estágio para o qual foi cadastrado
            o despacho da UTE
        :type estagio: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`TG` | list[:class:`TG`] | None
        """
        return self.__obtem_registros_com_filtros(
            TG,
            codigo=codigo,
            subsistema=subsistema,
            nome=nome,
            estagio=estagio,
        )

    def gs(
        self, mes: Optional[int] = None, semanas: Optional[int] = None
    ) -> Optional[Union[GS, List[GS]]]:
        """
        Obtém um registro que define o número de semanas em cada
        mês de estudo no :class:`DadGNL`.

        :param mes: índice do mês no estudo
        :type mes: int | None
        :param semanas: número de semanas do mês
        :type semanas: int | None

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`GS` | list[:class:`GS`] | None
        """
        return self.__obtem_registros_com_filtros(
            GS,
            mes=mes,
            semanas=semanas,
        )

    def nl(
        self,
        codigo: Optional[int] = None,
        subsistema: Optional[int] = None,
        lag: Optional[int] = None,
    ) -> Optional[Union[NL, List[NL]]]:
        """
        Obtém um registro que define o número de lags para o despacho
        de uma UTE.

        :param codigo: código da UTE
        :type codigo: int | None
        :param subsistema: subsistema da UTE
        :type subsistema: int | None
        :param lag: número de lags da UTE
        :type lag: int | None

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`NL` | list[:class:`NL`] | None
        """
        return self.__obtem_registros_com_filtros(
            NL,
            codigo=codigo,
            subsistema=subsistema,
            lag=lag,
        )

    def gl(
        self,
        codigo: Optional[int] = None,
        subsistema: Optional[int] = None,
        estagio: Optional[int] = None,
        data_inicio: Optional[str] = None,
    ) -> Optional[Union[GL, List[GL]]]:
        """
        Obtém um registro que define o despacho por patamar
        e a duração dos patamares para uma UTE GNL.

        :param codigo: código que especifica o registro
            da UTE
        :type codigo: int | None
        :param subsistema: subsistema da UTE
        :type subsistema: int | None
        :param estagio: estágio do despacho da UTE
        :type estagio: int | None
        :param data_inicio: data de início do estágio
            do despacho da UTE
        :type data_inicio: str | None

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`GL` | list[:class:`GL`] | None
        """
        return self.__obtem_registros_com_filtros(
            GL,
            codigo=codigo,
            subsistema=subsistema,
            estagio=estagio,
            data_inicio=data_inicio,
        )
