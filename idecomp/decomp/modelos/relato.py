from typing import Dict, List
import numpy as np  # type: ignore


class DadosGeraisRelato:
    """
    Armazena os dados de saída existentes no relato do DECOMP
    referentes aos dados gerais fornecidos ao programa.

    **Parâmetros**

    - numero_semanas_1_mes: `int`

    """
    def __init__(self,
                 numero_semanas_1_mes: int):
        self.numero_semanas_1_mes = numero_semanas_1_mes

    def __eq__(self, o: object) -> bool:
        """
        A igualdade entre DadosGeraisRelato avalia todos os campos.
        """
        if not isinstance(o, DadosGeraisRelato):
            return False
        rel: DadosGeraisRelato = o
        dif = False
        for (k, u), (_, v) in zip(self.__dict__.items(),
                                  rel.__dict__.items()):
            if u != v:
                dif = True
                break
        return not dif


class CMORelato:
    """
    Armazena os dados de saída existentes no relato do DECOMP
    referentes ao Custo Marginal de Operação (CMO).

    Esta classe armazena a tabela de CMO por subsistema em cada
    patamar de carga e os valores médios por submercado.

    **Parâmetros**

    - subsistema: `List[str]`
    - tabela: `np.ndarray`

    """
    def __init__(self,
                 subsistema: List[str],
                 tabela: np.ndarray):
        self.subsistema = subsistema
        self.tabela = tabela

    def __eq__(self, o: object) -> bool:
        """
        A igualdade entre CMORelato avalia todos os campos.
        """
        if not isinstance(o, CMORelato):
            return False
        cmo: CMORelato = o
        eq_subsistema = self.subsistema == cmo.subsistema
        eq_tabela = np.array_equal(self.tabela, cmo.tabela)
        return all([eq_subsistema, eq_tabela])

    @property
    def custo_medio_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Custo Marginal de Operação (CMO) médio por subsistema
        e por semana.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        dict_cmo: Dict[str, np.ndarray] = {}
        for i, ssis in enumerate(self.subsistema):
            if "Med" in ssis:
                str_subsistema = ssis.split("_")[1]
                dict_cmo[str_subsistema] = self.tabela[i, :]
        return dict_cmo


class Relato:
    """
    Armazena os dados de saída do DECOMP referentes ao
    acompanhamento do programa.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP e reproduzidas no `relato.rvx`, bem como as saídas finais
    da execução: custos de operação, despacho de térmicas, etc.

    Em versões futuras, esta classe pode passar a ler os dados
    de execução intermediárias do programa.

    **Parâmetros**

    - dados_gerais: `DadosGeraisRelato`
    - cmo: `CMORelato`

    """
    def __init__(self,
                 dados_gerais: DadosGeraisRelato,
                 cmo: CMORelato):
        self.dados_gerais = dados_gerais
        self.cmo = cmo

    def __eq__(self, o: object) -> bool:
        """
        A igualdade entre Relato avalia todos os campos.
        """
        if not isinstance(o, Relato):
            return False
        rel: Relato = o
        dif = False
        for (k, u), (_, v) in zip(self.__dict__.items(),
                                  rel.__dict__.items()):
            if u != v:
                dif = True
                break
        return not dif
