from idecomp.config import SUBSISTEMAS
from typing import Dict, List
from copy import deepcopy
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


class GeracaoTermicaSubsistemaRelato:
    """
    Armazena os dados de saída existentes no relato do DECOMP
    referentes à geração de térmicas (MWmed) por subsistema.

    Esta classe armazena a tabela de Geração por subsistema
    e por semana do DECOMP.

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
        A igualdade entre GeracaoTermicaSubsistemaRelato
        avalia todos os campos.
        """
        if not isinstance(o, GeracaoTermicaSubsistemaRelato):
            return False
        gt: GeracaoTermicaSubsistemaRelato = o
        eq_subsistema = self.subsistema == gt.subsistema
        eq_tabela = np.array_equal(self.tabela, gt.tabela)
        return all([eq_subsistema, eq_tabela])

    @property
    def geracao_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Geração Térmica (MWmed) por subsistema e por semana
        como fornecido no arquivo relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        dict_gt: Dict[str, np.ndarray] = {}
        for i, ssis in enumerate(self.subsistema):
            dict_gt[ssis] = self.tabela[i, :]
        return dict_gt


class EnergiaArmazenadaREERelato:
    """
    Armazena os dados de saída existentes no relato do DECOMP
    referentes à energia armazenada (% EARMax) por REE.

    Esta classe armazena a tabela de armazenamento por REE
    inicial e por semana do DECOMP.

    **Parâmetros**

    - subsistema: `List[str]`
    - tabela: `np.ndarray`

    """
    def __init__(self,
                 ree: List[str],
                 tabela: np.ndarray):
        self.ree = ree
        self.tabela = tabela

    def __eq__(self, o: object) -> bool:
        """
        A igualdade entre EnergiaArmazenadaREERelato
        avalia todos os campos.
        """
        if not isinstance(o, EnergiaArmazenadaREERelato):
            return False
        earm: EnergiaArmazenadaREERelato = o
        eq_ree = self.ree == earm.ree
        eq_tabela = np.array_equal(self.tabela, earm.tabela)
        return all([eq_ree, eq_tabela])

    @property
    def armazenamento_inicial_ree(self) -> Dict[str, float]:
        """
        Energia Armazenada inicial (% EARMax) por REE
        como fornecido no arquivo relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, float]`

        **Sobre**

        O acesso é feito com `[subsistema]`.
        """
        dict_gt: Dict[str, float] = {}
        for i, ssis in enumerate(self.ree):
            dict_gt[ssis] = self.tabela[i, 0]
        return dict_gt

    @property
    def armazenamento_ree(self) -> Dict[str, np.ndarray]:
        """
        Energia Armazenada (% EARMax) por REE e por
        período de execução como fornecido no arquivo
        relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[ree]` e é retornada uma
        `np.ndarray` onde a entrada [i - 1] possui o valor
        referente ao período i do DECOMP.
        """
        dict_earm: Dict[str, np.ndarray] = {}
        for i, ssis in enumerate(self.ree):
            dict_earm[ssis] = self.tabela[i, 1:]
        return dict_earm


class EnergiaArmazenadaSubsistemaRelato:
    """
    Armazena os dados de saída existentes no relato do DECOMP
    referentes à energia armazenada (% EARMax) por subsistema.

    Esta classe armazena a tabela de armazenamento por subsistema
    inicial e por semana do DECOMP.

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
        A igualdade entre EnergiaArmazenadaSubsistemaRelato
        avalia todos os campos.
        """
        if not isinstance(o, EnergiaArmazenadaSubsistemaRelato):
            return False
        earm: EnergiaArmazenadaSubsistemaRelato = o
        eq_subsistema = self.subsistema == earm.subsistema
        eq_tabela = np.array_equal(self.tabela, earm.tabela)
        return all([eq_subsistema, eq_tabela])

    @property
    def armazenamento_inicial_subsistema(self) -> Dict[str, float]:
        """
        Energia Armazenada inicial (% EARMax) por subsistema
        como fornecido no arquivo relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, float]`

        **Sobre**

        O acesso é feito com `[subsistema]`.
        """
        dict_gt: Dict[str, float] = {}
        for i, ssis in enumerate(self.subsistema):
            dict_gt[ssis] = self.tabela[i, 0]
        return dict_gt

    @property
    def armazenamento_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Energia Armazenada (% EARMax) por subsistema e por
        período de execução como fornecido no arquivo
        relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada uma
        `np.ndarray` onde a entrada [i - 1] possui o valor
        referente ao período i do DECOMP.
        """
        dict_earm: Dict[str, np.ndarray] = {}
        for i, ssis in enumerate(self.subsistema):
            dict_earm[ssis] = self.tabela[i, 1:]
        return dict_earm


class ENAPreEstudoSemanalSubsistemaRelato:
    """
    Armazena os dados de saída existentes no relato do DECOMP
    referentes à energia natural afluente pré-estudo por subsistema,
    em valores semanais (MWmed).

    Esta classe armazena a tabela de energias afluentes por subsistema
    e em cada semana anterior ao estudo do DECOMP, bem como o valor
    de EARMax (em MWmes) por subsistema ao final do estudo.

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
        A igualdade entre BalancoEnergeticoRelato
        avalia todos os campos.
        """
        if not isinstance(o, ENAPreEstudoSemanalSubsistemaRelato):
            return False
        earm: ENAPreEstudoSemanalSubsistemaRelato = o
        eq_subsistema = self.subsistema == earm.subsistema
        eq_tabela = np.array_equal(self.tabela, earm.tabela)
        return all([eq_subsistema, eq_tabela])

    @property
    def armazenamento_maximo_subsistema(self) -> Dict[str, float]:
        """
        Armazenamento máximo (EARMax) por subsistema com referência
        no final do estudo, como fornecido no arquivo
        relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, float]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornado um float.
        """
        dict_earm: Dict[str, float] = {}
        for i, ssis in enumerate(self.subsistema):
            dict_earm[ssis] = self.tabela[i, 0]
        return dict_earm

    @property
    def energia_afluente_pre_estudo_semanal(self) -> Dict[str, np.ndarray]:
        """
        Energia natural afluente (ENA) pré-estudo por semana (em MWmed) e
        por subsistema, como fornecido no arquivo relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada uma
        `np.ndarray` onde a entrada [i - 1] possui o valor
        referente à `i`-ésima semana pré-estudo. `Atenção`, pois a
        ordem das semanas pré-estudo é [..., 4ª, 3ª, 2ª, 1ª], então
        a lista deve ser invertida para estar em ordem cronológica.
        """
        dict_earm: Dict[str, np.ndarray] = {}
        for i, ssis in enumerate(self.subsistema):
            dict_earm[ssis] = self.tabela[i, 1:]
        return dict_earm


class BalancoEnergeticoRelato:
    """
    Armazena os dados de saída existentes no relato do DECOMP
    referentes ao balanço energético para o primeiro mês.

    Esta classe armazena as tabelas do balanço por subsistema
    em cada patamar de carga e os valores médios.

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
        A igualdade entre ENAPreEstudoSemanalRelato
        avalia todos os campos.
        """
        if not isinstance(o, BalancoEnergeticoRelato):
            return False
        bal: BalancoEnergeticoRelato = o
        eq_subsistema = self.subsistema == bal.subsistema
        eq_tabela = np.array_equal(self.tabela, bal.tabela)
        return all([eq_subsistema, eq_tabela])

    @property
    def mercado_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Mercado médio por subsistema
        e por semana, em MWmed.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        col_merc = 0
        dict_merc: Dict[str, np.ndarray] = {}
        for i, sub in enumerate(SUBSISTEMAS):
            dict_merc[sub] = self.tabela[:, i, col_merc]
        return dict_merc

    @property
    def bacia_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Bacia média por subsistema
        e por semana, em MWmed.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        col_bacia = 1
        dict_bacia: Dict[str, np.ndarray] = {}
        for i, sub in enumerate(SUBSISTEMAS):
            dict_bacia[sub] = self.tabela[:, i, col_bacia]
        return dict_bacia

    @property
    def cbomba_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Cbomba médio por subsistema
        e por semana, em MWmed.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        col_cbomba = 2
        dict_cbomba: Dict[str, np.ndarray] = {}
        for i, sub in enumerate(SUBSISTEMAS):
            dict_cbomba[sub] = self.tabela[:, i, col_cbomba]
        return dict_cbomba

    @property
    def geracao_hidraulica_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Geração Hidráulica (Ghid) médio por subsistema
        e por semana, em MWmed.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        col_ghid = 3
        dict_ghid: Dict[str, np.ndarray] = {}
        for i, sub in enumerate(SUBSISTEMAS):
            ghid = deepcopy(self.tabela[:, i, col_ghid])
            ghid += self.tabela[:, i, 15]
            ghid += self.tabela[:, i, 16]
            dict_ghid[sub] = ghid
        return dict_ghid

    @property
    def geracao_termica_antecipada_subsistema(self) -> Dict[str,
                                                            np.ndarray]:
        """
        Geração térmica antecipada média por subsistema
        e por semana, em MWmed.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        col_gterat = 5
        dict_gterat: Dict[str, np.ndarray] = {}
        for i, sub in enumerate(SUBSISTEMAS):
            dict_gterat[sub] = self.tabela[:, i, col_gterat]
        return dict_gterat

    @property
    def deficit_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Déficit médio por subsistema e por semana, em MWmed.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        col_def = 6
        dict_def: Dict[str, np.ndarray] = {}
        for i, sub in enumerate(SUBSISTEMAS):
            dict_def[sub] = self.tabela[:, i, col_def]
        return dict_def


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
    - geracao_termica_subsistema: `GeracaoTermicaSubsistemaRelato`
    - earm_ree: `EnergiaArmazenadaREERelato`
    - earm_subsistema: `EnergiaArmazenadaSubsistemaRelato`
    - ena_pre_semanal: `ENAPreEstudoSemanalSubsistemaRelato`
    - balanco_energetico: `BalancoEnergeticoRelato`

    """
    def __init__(self,
                 dados_gerais: DadosGeraisRelato,
                 cmo: CMORelato,
                 geracao_termica_subsistema: GeracaoTermicaSubsistemaRelato,
                 earm_ree: EnergiaArmazenadaREERelato,
                 earm_subsistema: EnergiaArmazenadaSubsistemaRelato,
                 ena_pre_sem_subsistema: ENAPreEstudoSemanalSubsistemaRelato,
                 balanco_energetico: BalancoEnergeticoRelato):
        self.dados_gerais = dados_gerais
        self._cmo = cmo
        self._geracao_termica_subsistema = geracao_termica_subsistema
        self._earm_ree = earm_ree
        self._earm_subsistema = earm_subsistema
        self._ena_pre_semanal_subsistema = ena_pre_sem_subsistema
        self.balanco_energetico = balanco_energetico

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

    @property
    def cmo_medio_subsistema(self) -> Dict[str, np.ndarray]:
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
        return self._cmo.custo_medio_subsistema

    @property
    def geracao_termica_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Geração Térmica (MWmed) por subsistema e por semana
        como fornecido no arquivo relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        return self._geracao_termica_subsistema.geracao_subsistema

    @property
    def energia_armazenada_inicial_ree(self) -> Dict[str, float]:
        """
        Energia Armazenada inicial (% EARMax) por REE
        como fornecido no arquivo relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[ree]`.
        """
        return self._earm_ree.armazenamento_inicial_ree

    @property
    def energia_armazenada_inicial_subsistema(self) -> Dict[str, float]:
        """
        Energia Armazenada inicial (% EARMax) por subsistema
        como fornecido no arquivo relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]`.
        """
        return self._earm_subsistema.armazenamento_inicial_subsistema

    @property
    def energia_armazenada_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Energia Armazenada (% EARMax) por subsistema e por
        período de execução como fornecido no arquivo
        relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada uma
        `np.ndarray` onde a entrada [i - 1] possui o valor
        referente ap período i do DECOMP.
        """
        return self._earm_subsistema.armazenamento_subsistema

    @property
    def energia_armazenada_ree(self) -> Dict[str, np.ndarray]:
        """
        Energia Armazenada (% EARMax) por REE e por
        período de execução como fornecido no arquivo
        relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[ree]` e é retornada uma
        `np.ndarray` onde a entrada [i - 1] possui o valor
        referente ap período i do DECOMP.
        """
        return self._earm_ree.armazenamento_ree

    @property
    def armazenamento_maximo_subsistema(self) -> Dict[str, float]:
        """
        Armazenamento máximo (EARMax) por subsistema com referência
        no final do estudo, como fornecido no arquivo
        relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, float]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornado um float.
        """
        earmax = (self._ena_pre_semanal_subsistema.
                  armazenamento_maximo_subsistema)
        return earmax

    @property
    def energia_afluente_pre_estudo_semanal_subsistema(self
                                                       ) -> Dict[str,
                                                                 np.ndarray]:
        """
        Energia natural afluente (ENA) pré-estudo por semana (em MWmed) e
        por subsistema, como fornecido no arquivo relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada uma
        `np.ndarray` onde a entrada [i - 1] possui o valor
        referente à `i`-ésima semana pré-estudo. `Atenção`, pois a
        ordem das semanas pré-estudo é [..., 4ª, 3ª, 2ª, 1ª], então
        a lista deve ser invertida para estar em ordem cronológica.
        """
        ena = (self._ena_pre_semanal_subsistema.
               energia_afluente_pre_estudo_semanal)
        return ena

    @property
    def mercado_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Mercado médio por subsistema
        e por semana, em MWmed.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        return self.balanco_energetico.mercado_subsistema

    @property
    def bacia_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Bacia média por subsistema
        e por semana, em MWmed.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        return self.balanco_energetico.bacia_subsistema

    @property
    def cbomba_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Cbomba médio por subsistema
        e por semana, em MWmed.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        return self.balanco_energetico.cbomba_subsistema

    @property
    def geracao_hidraulica_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Geração Hidráulica (Ghid) médio por subsistema
        e por semana, em MWmed.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        return self.balanco_energetico.geracao_hidraulica_subsistema

    @property
    def geracao_termica_antecipada_subsistema(self) -> Dict[str,
                                                            np.ndarray]:
        """
        Geração térmica antecipada média por subsistema
        e por semana, em MWmed.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        return self.balanco_energetico.geracao_termica_antecipada_subsistema

    @property
    def deficit_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Déficit médio por subsistema e por semana, em MWmed.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        return self.balanco_energetico.deficit_subsistema
