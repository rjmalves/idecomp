from idecomp.decomp.modelos.dadger import LeituraDadger
from idecomp.decomp.modelos.dadger import TE, SB, UH, CT, UE, DP, CD, PQ  # noqa
from idecomp.decomp.modelos.dadger import RI, IA, TX, GP, NI, DT, MP, MT  # noqa
from idecomp.decomp.modelos.dadger import FD, VE, RE, LU, FU, FT, FI, VI  # noqa
from idecomp.decomp.modelos.dadger import AC, IR, CI, CE, FC, TI, RQ, EZ  # noqa
from idecomp.decomp.modelos.dadger import HV, LV, CV, HQ, LQ, CQ, AR, EV  # noqa
from idecomp.decomp.modelos.dadger import FJ, HE, CM  # noqa
from idecomp._utils.arquivo import ArquivoRegistros
from idecomp._utils.dadosarquivo import DadosArquivoRegistros
from idecomp._utils.escritaregistros import EscritaRegistros

from copy import deepcopy
from typing import Type, List, Optional, TypeVar, Any


class Dadger(ArquivoRegistros):
    """
    Armazena os dados de entrada gerais do DECOMP.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP no `dadger.rvx`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    Atualmente, são suportados os registros:
    `TE`, `SB`, `UH`, `CT`, `DP`, `TX`, `GP`, `NI`, `DT`, `RE`, `LU`,
    `VI`, `IR`, `FC`, `TI`, `HV`, `LV`, `HQ`, `LQ` e `HE`.

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
                   nome_arquivo="dadger.rv0") -> 'Dadger':
        """
        Realiza a leitura de um arquivo "dadger.rvx" existente em
        um diretório.

        :param diretorio: O caminho relativo ou completo para o diretório
            onde se encontra o arquivo
        :type diretorio: str
        :param nome_arquivo: Nome do arquivo a ser lido, potencialmente
            especificando a revisão. Tem como valor default "dadger.rv0"
        :type nome_arquivo: str, optional
        :return: Um objeto :class:`Dadger` com informações do arquivo lido
        """
        leitor = LeituraDadger(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    def escreve_arquivo(self,
                        diretorio: str,
                        nome_arquivo="dadger.rv0"):
        """
        Realiza a escrita de um arquivo com as informações do
        objeto :class:`Dadger`

        :param diretorio: O caminho relativo ou completo para o diretório
            onde será escrito o arquivo.
        :type diretorio: str
        :param nome_arquivo: Nome do arquivo a ser escrito.Tem como valor
            default "dadger.rv0"
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

    @property
    def te(self) -> TE:
        """
        Obtém o (único) registro que define o nome do estudo no
        :class:`Dadger`

        :return: Um registro do tipo :class:`TE`.
        """
        r = self.__obtem_registro(TE)
        return r

    def sb(self, codigo: int) -> SB:
        """
        Obtém um registro que define os subsistemas existentes
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            do subsistema
        :type codigo: int
        :return: Um registro do tipo :class:`SB`
        """
        regs: List[SB] = self.__obtem_registros(SB)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro SB" +
                         f" para o código {codigo}")

    def uh(self, codigo: int) -> UH:
        """
        Obtém um registro que define uma usina hidrelétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da UHE
        :type codigo: int
        :return: Um registro do tipo :class:`UH`
        """
        regs: List[UH] = self.__obtem_registros(UH)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro UH" +
                         f" para a UHE {codigo}")

    def ct(self, codigo: int) -> CT:
        """
        Obtém um registro que define uma usina termelétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da UTE
        :type codigo: int
        :return: Um registro do tipo :class:`CT`
        """
        regs: List[CT] = self.__obtem_registros(CT)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro CT" +
                         f" para a UTE {codigo}")

    def dp(self, estagio: int, subsistema: int) -> DP:
        """
        Obtém um registro que define as durações dos patamares
        no estudo descrito pelo :class:`Dadger`.

        :param estagio: Índice do estágio sobre o qual serão
            definidas as durações dos patamares
        :type estagio: int
        :param subsistema: Índice do subsistema para o qual
            valerão os patamares.
        :type subsistema: int
        :return: Um registro do tipo :class:`DP`
        """
        regs: List[DP] = self.__obtem_registros(DP)
        for r in regs:
            if all([r.estagio == estagio,
                    r.subsistema == subsistema]):
                return r
        raise ValueError("Não foi encontrado registro DP" +
                         f" para o subsistema {subsistema}" +
                         f" no estágio {estagio})")

    @property
    def tx(self) -> TX:
        """
        Obtém o (único) registro que define a taxa de desconto
        aplicada no estudo definido no :class:`Dadger`

        :return: Um registro do tipo :class:`TX`.
        """
        return self.__obtem_registro(TX)

    @property
    def gp(self) -> GP:
        """
        Obtém o (único) registro que define o gap para convergência
        considerado no estudo definido no :class:`Dadger`

        :return: Um registro do tipo :class:`GP`.
        """
        return self.__obtem_registro(GP)

    @property
    def ni(self) -> NI:
        """
        Obtém o (único) registro que define o número máximo de iterações
        do DECOMP no estudo definido no :class:`Dadger`

        :return: Um registro do tipo :class:`NI`.
        """
        return self.__obtem_registro(NI)

    @property
    def dt(self) -> DT:
        """
        Obtém o (único) registro que define a data de referência do
        estudo definido no :class:`Dadger`

        :return: Um registro do tipo :class:`DT`.
        """
        return self.__obtem_registro(DT)

    def re(self, codigo: int) -> RE:
        """
        Obtém um registro que cadastra uma restrição elétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição elétrica
        :type codigo: int
        :return: Um registro do tipo :class:`RE`
        """
        regs: List[RE] = self.__obtem_registros(RE)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro RE" +
                         f" com código {codigo}")

    def lu(self, codigo: int, estagio: int) -> LU:
        """
        Obtém um registro que especifica os limites inferiores e
        superiores por patamar de uma restrição elétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição elétrica
        :type codigo: int
        :param estagio: Estágio sobre o qual valerão os limites da
            restrição elétricas
        :type estagio: int
        :return: Um registro do tipo :class:`LU`

        **Exemplos**

        Para um objeto :class:`Dadger` que possua uma restrição RE
        de código 1, definida para os estágios de 1 a 5, com limites
        LU definidos apenas para o estágio 1, estes podem ser acessados com:

        >>> lu = dadger.lu(1, 1)
        >>> lu
            <idecomp.decomp.modelos.dadger.LU object at 0x0000026E5C269550>

        Se for acessado o registro LU de um estágio fora dos limites da
        restrição RE, isso resultará em um erro:

        >>> dadger.lu(1, 7)
            Traceback (most recent call last):
            ...
            ValueError: Estágio 7 fora dos limites do registro RE

        Por outro lado, se for acessado o registro LU em um estágio dentro
        dos limites do registro RE, porém sem limites próprios definidos,
        será criado um registro idêntico ao do último estágio existente,
        e este será retornado:

        >>> lu2 = dadger.lu(1, 5)
        >>> lu.limites_inferiores == lu2.limites_inferiores
            True

        """

        def cria_registro(modelo: LU,
                          estagio_final: int) -> LU:
            copia = deepcopy(modelo)
            copia.estagio = estagio
            # Procura pelo registro do próximo estágio
            proximo = None
            for est in range(estagio, estagio_final + 1):
                r = self.__obtem_registro_do_estagio(LU, codigo, est)
                if r is not None:
                    proximo = r
                    break
            if proximo is not None:
                delta = (proximo._ordem - modelo._ordem) / 2.0
            else:
                delta = 0.1
            copia._ordem += delta
            self._registros.append(copia)
            return copia

        # Obtém o registro RE associado
        re = self.re(codigo)
        # Confere se o estágio pedido está no intervalo
        # do registro RE
        if not (re.estagio_inicial <= estagio <= re.estagio_final):
            raise ValueError(f"Estágio {estagio} fora dos limites" +
                             " do registro RE")
        # Tenta obter um registro já existente
        reg = self.__obtem_registro_do_estagio(LU, codigo, estagio)
        if reg is not None:
            return reg
        # Se não conseguir, cria mais um registro, idêntico ao do
        # último estágio existente, e retorna.
        for est in range(re.estagio_inicial, estagio):
            r = self.__obtem_registro_do_estagio(LU, codigo, est)
            if r is not None:
                reg = r
        if reg is None:
            raise ValueError("Registro não encontrado")
        return cria_registro(reg, re.estagio_final)

    def vi(self, uhe: int) -> VI:
        """
        Obtém um registro que especifica os tempos de viagem da
        água em uma UHE existente no no estudo descrito
        pelo :class:`Dadger`.

        :param uhe: Índice da UHE associada aos tempos de viagem
        :type uhe: int
        :return: Um registro do tipo :class:`VI`
        """
        regs: List[VI] = self.__obtem_registros(VI)
        for r in regs:
            if r.uhe == uhe:
                return r
        raise ValueError("Não foi encontrado registro VI" +
                         f" para a UHE {uhe}")

    def ir(self, tipo: str) -> IR:
        """
        Obtém um registro que especifica os relatórios de saída
        a serem produzidos pelo DECOMP após a execução do estudo
        descrito no :class:`Dadger`.

        :param tipo: Mnemônico do tipo de relatório especificado
            no registro
        :type tipo: str
        :return: Um registro do tipo :class:`IR`
        """
        regs: List[IR] = self.__obtem_registros(IR)
        for r in regs:
            if r.tipo == tipo:
                return r
        raise ValueError("Não foi encontrado registro IR" +
                         f" com mnemônico {tipo}")

    def fc(self, tipo: str) -> FC:
        """
        Obtém um registro que especifica os caminhos para os
        arquivos com a FCF do NEWAVE.

        :param tipo: Mnemônico do tipo de FCF especificado
            no registro
        :type tipo: str
        :return: Um registro do tipo :class:`FC`
        """
        regs: List[FC] = self.__obtem_registros(FC)
        for r in regs:
            if r.tipo == tipo:
                return r
        raise ValueError("Não foi encontrado registro FC" +
                         f" com mnemônico {tipo}")

    def ti(self, codigo: int) -> TI:
        """
        Obtém um registro que especifica as taxas de irrigação
        por posto (UHE) existente no estudo especificado no :class:`Dadger`

        :param codigo: Código do posto da UHE associada
            no registro
        :type codigo: int
        :return: Um registro do tipo :class:`TI`
        """
        regs: List[TI] = self.__obtem_registros(TI)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro TI" +
                         f" para a UHE {codigo}")

    def ve(self, codigo: int) -> VE:
        """
        Obtém um registro que especifica os volumes de espera
        por posto (UHE) existente no estudo especificado no :class:`Dadger`

        :param codigo: Código do posto da UHE associada
        :type codigo: int
        :return: Um registro do tipo :class:`VE`
        """
        regs: List[VE] = self.__obtem_registros(VE)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro VE" +
                         f" para a UHE {codigo}")

    def hv(self, codigo: int) -> HV:
        """
        Obtém um registro que cadastra uma restrição de volume mínimo
        armazenado existente no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição de volume mínimo
        :type codigo: int
        :return: Um registro do tipo :class:`HV`
        """
        regs: List[HV] = self.__obtem_registros(HV)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro HV" +
                         f" para UHE {codigo}")

    def lv(self, codigo: int, estagio: int) -> LV:
        """
        Obtém um registro que especifica os limites inferior e
        superior de uma restrição de volume mínimo existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição de volume mínimo
        :type codigo: int
        :param estagio: Estágio sobre o qual valerão os limites da
            restrição
        :type estagio: int
        :return: Um registro do tipo :class:`LV`

        **Exemplos**

        Para um objeto :class:`Dadger` que possua uma restrição HV
        de código 1, definida para os estágios de 1 a 5, com limites
        LV definidos apenas para o estágio 1, estes podem ser acessados com:

        >>> lv = dadger.lv(1, 1)
        >>> lv
            <idecomp.decomp.modelos.dadger.LV object at 0x0000026E5C269550>

        Se for acessado o registro LV de um estágio fora dos limites da
        restrição HV, isso resultará em um erro:

        >>> dadger.lv(1, 7)
            Traceback (most recent call last):
            ...
            ValueError: Estágio 7 fora dos limites do registro HV

        Por outro lado, se for acessado o registro LV em um estágio dentro
        dos limites do registro HV, porém sem limites próprios definidos,
        será criado um registro idêntico ao do último estágio existente,
        e este será retornado:

        >>> lv2 = dadger.lv(1, 5)
        >>> lv.limite_inferior == lv2.limite_inferior
            True

        """
        def cria_registro(modelo: LV,
                          estagio_final: int) -> LV:
            copia = deepcopy(modelo)
            copia.estagio = estagio
            # Procura pelo registro do próximo estágio
            proximo = None
            for est in range(estagio, estagio_final + 1):
                r = self.__obtem_registro_do_estagio(LV, codigo, est)
                if r is not None:
                    proximo = r
                    break
            if proximo is not None:
                delta = (proximo._ordem - modelo._ordem) / 2.0
            else:
                delta = 0.1
            copia._ordem += delta
            self._registros.append(copia)
            return copia

        # Obtém o registro HV associado
        hv = self.hv(codigo)
        # Confere se o estágio pedido está no intervalo
        # do registro HV
        if not (hv.estagio_inicial <= estagio <= hv.estagio_final):
            raise ValueError(f"Estágio {estagio} fora dos limites" +
                             " do registro HV")
        # Tenta obter um registro já existente
        reg = self.__obtem_registro_do_estagio(LV, codigo, estagio)
        if reg is not None:
            return reg
        # Se não conseguir, cria mais um registro, idêntico ao do
        # último estágio existente, e retorna.
        for est in range(hv.estagio_inicial, estagio):
            r = self.__obtem_registro_do_estagio(LV, codigo, est)
            if r is not None:
                reg = r
        if reg is None:
            raise ValueError("Registro não encontrado")
        return cria_registro(reg, hv.estagio_final)

    def hq(self, codigo: int) -> HQ:
        """
        Obtém um registro que cadastra uma restrição de vazão
        existente no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição de vazão
        :type codigo: int
        :return: Um registro do tipo :class:`HQ`
        """
        regs: List[HQ] = self.__obtem_registros(HQ)
        for r in regs:
            if r.codigo == codigo:
                return r
        raise ValueError("Não foi encontrado registro HQ" +
                         f" com o código {codigo}")

    def lq(self, codigo: int, estagio: int) -> LQ:
        """
        Obtém um registro que especifica os limites inferiores e
        superiores por patamar de uma restrição de vazão existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição de vazão
        :type codigo: int
        :param estagio: Estágio sobre o qual valerão os limites da
            restrição de vazão
        :type estagio: int
        :return: Um registro do tipo :class:`LQ`

        **Exemplos**

        Para um objeto :class:`Dadger` que possua uma restrição HQ
        de código 1, definida para os estágios de 1 a 5, com limites
        LQ definidos apenas para o estágio 1, estes podem ser acessados com:

        >>> lq = dadger.lq(1, 1)
        >>> lq
            <idecomp.decomp.modelos.dadger.LQ object at 0x0000026E5C269550>

        Se for acessado o registro LQ de um estágio fora dos limites da
        restrição HQ, isso resultará em um erro:

        >>> dadger.lq(1, 7)
            Traceback (most recent call last):
            ...
            ValueError: Estágio 7 fora dos limites do registro HQ

        Por outro lado, se for acessado o registro LQ em um estágio dentro
        dos limites do registro HQ, porém sem limites próprios definidos,
        será criado um registro idêntico ao do último estágio existente,
        e este será retornado:

        >>> lq2 = dadger.lq(1, 5)
        >>> lq.limites_inferiores == lq2.limites_inferiores
            True

        """
        def cria_registro(modelo: LQ,
                          estagio_final: int) -> LQ:
            copia = deepcopy(modelo)
            copia.estagio = estagio
            # Procura pelo registro do próximo estágio
            proximo = None
            for est in range(estagio, estagio_final + 1):
                r = self.__obtem_registro_do_estagio(LQ, codigo, est)
                if r is not None:
                    proximo = r
                    break
            if proximo is not None:
                delta = (proximo._ordem - modelo._ordem) / 2.0
            else:
                delta = 0.1
            copia._ordem += delta
            self._registros.append(copia)
            return copia

        # Obtém o registro HQ associado
        hq = self.hq(codigo)
        # Confere se o estágio pedido está no intervalo
        # do registro HQ
        if not (hq.estagio_inicial <= estagio <= hq.estagio_final):
            raise ValueError(f"Estágio {estagio} fora dos limites" +
                             " do registro HQ")
        # Tenta obter um registro já existente
        reg = self.__obtem_registro_do_estagio(LQ, codigo, estagio)
        if reg is not None:
            return reg
        # Se não conseguir, cria mais um registro, idêntico ao do
        # último estágio existente, e retorna.
        for est in range(hq.estagio_inicial, estagio):
            r = self.__obtem_registro_do_estagio(LQ, codigo, est)
            if r is not None:
                reg = r
        if reg is None:
            raise ValueError("Registro não encontrado")
        return cria_registro(reg, hq.estagio_final)

    def he(self, codigo: int, estagio: int) -> HE:
        """
        Obtém um registro que cadastra uma restrição de energia
        armazenada existente no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição de energia armazenada
        :type codigo: int
        :param estagio: Índice do estágio para o qual vale a
            restrição de energia armazenada
        :type estagio: int
        :return: Um registro do tipo :class:`HE`
        """
        r = self.__obtem_registro_do_estagio(HE,
                                             codigo,
                                             estagio)
        if r is not None:
            return r
        else:
            raise ValueError("Registro não encontrado")
