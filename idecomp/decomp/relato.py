from idecomp._utils.bloco import Bloco
from idecomp.decomp.modelos.relato import BlocoDadosGeraisRelato
from idecomp.decomp.modelos.relato import BlocoBalancoEnergeticoRelato
from idecomp.decomp.modelos.relato import BlocoCMORelato
from idecomp.decomp.modelos.relato import BlocoGeracaoTermicaSubsistemaRelato
from idecomp.decomp.modelos.relato import BlocoEnergiaArmazenadaREERelato
from idecomp.decomp.modelos.relato import BlocoEnergiaArmazenadaSubsistemaRelato  # noqa
from idecomp.decomp.modelos.relato import BlocoENAPreEstudoSemanalSubsistemaRelato  # noqa
from idecomp.decomp.modelos.relato import LeituraRelato
from idecomp._utils.arquivo import Arquivo
from idecomp._utils.dadosarquivo import DadosArquivo
from typing import Dict, Type
import numpy as np  # type: ignore
import pandas as pd  # type: ignore


class Relato(Arquivo):
    """
    Armazena os dados de saída do DECOMP referentes ao
    acompanhamento do programa.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP e reproduzidas no `relato.rvx`, bem como as saídas finais
    da execução: custos de operação, despacho de térmicas, etc.

    """
    def __init__(self,
                 dados: DadosArquivo) -> None:
        super().__init__(dados)

    # Override
    @classmethod
    def le_arquivo(cls,
                   diretorio: str,
                   nome_arquivo="relato.rv0") -> 'Relato':
        """
        """
        leitor = LeituraRelato(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    def __obtem_bloco_por_tipo(self, tipo: Type[Bloco]) -> Bloco:
        """
        """
        for b in self._blocos:
            if isinstance(b, tipo):
                return b
        raise ValueError(f"Não foi encontrado um bloco do tipo {tipo}")

    @property
    def cmo_medio_subsistema(self) -> pd.DataFrame:
        """
        Custo Marginal de Operação (CMO) médio por subsistema
        e por semana.

        **Retorna**

        `pd.DataFrame`

        **Sobre**

        """
        b: BlocoCMORelato = self.__obtem_bloco_por_tipo(BlocoCMORelato)
        return b.dados

    # @property
    # def geracao_termica_subsistema(self) -> Dict[str, np.ndarray]:
    #     """
    #     Geração Térmica (MWmed) por subsistema e por semana
    #     como fornecido no arquivo relato.rvX do DECOMP.

    #     **Retorna**

    #     `Dict[str, np.ndarray]`

    #     **Sobre**

    #     O acesso é feito com `[subsistema]` e é retornada um
    #     array onde a posição [i - 1] contém os dados do período
    #     i do DECOMP.
    #     """
    #     return self._geracao_termica_subsistema.geracao_subsistema

    # @property
    # def energia_armazenada_inicial_ree(self) -> Dict[str, float]:
    #     """
    #     Energia Armazenada inicial (% EARMax) por REE
    #     como fornecido no arquivo relato.rvX do DECOMP.

    #     **Retorna**

    #     `Dict[str, np.ndarray]`

    #     **Sobre**

    #     O acesso é feito com `[ree]`.
    #     """
    #     return self._earm_ree.armazenamento_inicial_ree

    # @property
    # def energia_armazenada_inicial_subsistema(self) -> Dict[str, float]:
    #     """
    #     Energia Armazenada inicial (% EARMax) por subsistema
    #     como fornecido no arquivo relato.rvX do DECOMP.

    #     **Retorna**

    #     `Dict[str, np.ndarray]`

    #     **Sobre**

    #     O acesso é feito com `[subsistema]`.
    #     """
    #     return self._earm_subsistema.armazenamento_inicial_subsistema

    # @property
    # def energia_armazenada_subsistema(self) -> Dict[str, np.ndarray]:
    #     """
    #     Energia Armazenada (% EARMax) por subsistema e por
    #     período de execução como fornecido no arquivo
    #     relato.rvX do DECOMP.

    #     **Retorna**

    #     `Dict[str, np.ndarray]`

    #     **Sobre**

    #     O acesso é feito com `[subsistema]` e é retornada uma
    #     `np.ndarray` onde a entrada [i - 1] possui o valor
    #     referente ap período i do DECOMP.
    #     """
    #     return self._earm_subsistema.armazenamento_subsistema

    # @property
    # def energia_armazenada_ree(self) -> Dict[str, np.ndarray]:
    #     """
    #     Energia Armazenada (% EARMax) por REE e por
    #     período de execução como fornecido no arquivo
    #     relato.rvX do DECOMP.

    #     **Retorna**

    #     `Dict[str, np.ndarray]`

    #     **Sobre**

    #     O acesso é feito com `[ree]` e é retornada uma
    #     `np.ndarray` onde a entrada [i - 1] possui o valor
    #     referente ap período i do DECOMP.
    #     """
    #     return self._earm_ree.armazenamento_ree

    # @property
    # def armazenamento_maximo_subsistema(self) -> Dict[str, float]:
    #     """
    #     Armazenamento máximo (EARMax) por subsistema com referência
    #     no final do estudo, como fornecido no arquivo
    #     relato.rvX do DECOMP.

    #     **Retorna**

    #     `Dict[str, float]`

    #     **Sobre**

    #     O acesso é feito com `[subsistema]` e é retornado um float.
    #     """
    #     earmax = (self._ena_pre_semanal_subsistema.
    #               armazenamento_maximo_subsistema)
    #     return earmax

    # @property
    # def energia_afluente_pre_estudo_semanal_subsistema(self
    #                                                    ) -> Dict[str,
    #                                                              np.ndarray]:
    #     """
    #     Energia natural afluente (ENA) pré-estudo por semana (em MWmed) e
    #     por subsistema, como fornecido no arquivo relato.rvX do DECOMP.

    #     **Retorna**

    #     `Dict[str, np.ndarray]`

    #     **Sobre**

    #     O acesso é feito com `[subsistema]` e é retornada uma
    #     `np.ndarray` onde a entrada [i - 1] possui o valor
    #     referente à `i`-ésima semana pré-estudo. `Atenção`, pois a
    #     ordem das semanas pré-estudo é [..., 4ª, 3ª, 2ª, 1ª], então
    #     a lista deve ser invertida para estar em ordem cronológica.
    #     """
    #     ena = (self._ena_pre_semanal_subsistema.
    #            energia_afluente_pre_estudo_semanal)
    #     return ena

    # @property
    # def mercado_subsistema(self) -> Dict[str, np.ndarray]:
    #     """
    #     Mercado médio por subsistema
    #     e por semana, em MWmed.

    #     **Retorna**

    #     `Dict[str, np.ndarray]`

    #     **Sobre**

    #     O acesso é feito com `[subsistema]` e é retornada um
    #     array onde a posição [i - 1] contém os dados do período
    #     i do DECOMP.
    #     """
    #     return self.balanco_energetico.mercado_subsistema

    # @property
    # def bacia_subsistema(self) -> Dict[str, np.ndarray]:
    #     """
    #     Bacia média por subsistema
    #     e por semana, em MWmed.

    #     **Retorna**

    #     `Dict[str, np.ndarray]`

    #     **Sobre**

    #     O acesso é feito com `[subsistema]` e é retornada um
    #     array onde a posição [i - 1] contém os dados do período
    #     i do DECOMP.
    #     """
    #     return self.balanco_energetico.bacia_subsistema

    # @property
    # def cbomba_subsistema(self) -> Dict[str, np.ndarray]:
    #     """
    #     Cbomba médio por subsistema
    #     e por semana, em MWmed.

    #     **Retorna**

    #     `Dict[str, np.ndarray]`

    #     **Sobre**

    #     O acesso é feito com `[subsistema]` e é retornada um
    #     array onde a posição [i - 1] contém os dados do período
    #     i do DECOMP.
    #     """
    #     return self.balanco_energetico.cbomba_subsistema

    # @property
    # def geracao_hidraulica_subsistema(self) -> Dict[str, np.ndarray]:
    #     """
    #     Geração Hidráulica (Ghid) médio por subsistema
    #     e por semana, em MWmed.

    #     **Retorna**

    #     `Dict[str, np.ndarray]`

    #     **Sobre**

    #     O acesso é feito com `[subsistema]` e é retornada um
    #     array onde a posição [i - 1] contém os dados do período
    #     i do DECOMP.
    #     """
    #     return self.balanco_energetico.geracao_hidraulica_subsistema

    # @property
    # def geracao_termica_antecipada_subsistema(self) -> Dict[str,
    #                                                         np.ndarray]:
    #     """
    #     Geração térmica antecipada média por subsistema
    #     e por semana, em MWmed.

    #     **Retorna**

    #     `Dict[str, np.ndarray]`

    #     **Sobre**

    #     O acesso é feito com `[subsistema]` e é retornada um
    #     array onde a posição [i - 1] contém os dados do período
    #     i do DECOMP.
    #     """
    #     return self.balanco_energetico.geracao_termica_antecipada_subsistema

    # @property
    # def deficit_subsistema(self) -> Dict[str, np.ndarray]:
    #     """
    #     Déficit médio por subsistema e por semana, em MWmed.

    #     **Retorna**

    #     `Dict[str, np.ndarray]`

    #     **Sobre**

    #     O acesso é feito com `[subsistema]` e é retornada um
    #     array onde a posição [i - 1] contém os dados do período
    #     i do DECOMP.
    #     """
    #     return self.balanco_energetico.deficit_subsistema
