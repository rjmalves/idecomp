from cfinterface.files.sectionfile import SectionFile
from idecomp.decomp.modelos.mapcut import SecaoDadosMapcut
import pandas as pd  # type: ignore
from typing import List
from datetime import datetime


from typing import TypeVar, Optional


class Mapcut(SectionFile):
    """
    Armazena os dados de saída do DECOMP referentes ao
    cabeçalho dos cortes de Benders.
    """

    T = TypeVar("T")

    SECTIONS = [SecaoDadosMapcut]
    STORAGE = "BINARY"

    def __init__(self, data=...) -> None:
        super().__init__(data)

    def __obtem_dados(self) -> Optional[SecaoDadosMapcut]:
        s = self.data.get_sections_of_type(SecaoDadosMapcut)
        return s if not isinstance(s, list) else None

    @property
    def numero_iteracoes(self) -> Optional[int]:
        """
        O número de iterações.

        :return: O número de iterações
        :rtype: int | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.numero_iteracoes
        return None

    @property
    def numero_cortes(self) -> Optional[int]:
        """
        O número de cortes de Benders.

        :return: O número de cortes
        :rtype: int | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.numero_cortes
        return None

    @property
    def numero_submercados(self) -> Optional[int]:
        """
        O número de submercados.

        :return: O número de submercados
        :rtype: int | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.numero_submercados
        return None

    @property
    def numero_uhes(self) -> Optional[int]:
        """
        O número de usinas hidrelétricas.

        :return: O número de usinas hidrelétricas
        :rtype: int | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.numero_uhes
        return None

    @property
    def numero_cenarios(self) -> Optional[int]:
        """
        O número de cenarios.

        :return: O número de cenarios
        :rtype: int | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.numero_cenarios
        return None

    @property
    def registro_ultimo_corte_no(self) -> Optional[pd.DataFrame]:
        """
        Retorna os dados dos índices do último registro
        de cortes para cada estágio, para leitura do
        arquivo `cortdeco`.

        - no (`int`)
        - estagio (`int`)
        - indice_ultimo_corte (`int`)

        :return: Os dados dos índices dos cortes em uma tabela.
        :rtype: pd.DataFrame
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.registro_ultimo_corte_no
        return None

    @property
    def tamanho_corte(self) -> Optional[int]:
        """
        O tamanho do corte (tamanho do registro no
        arquivo cortdeco).

        :return: O tamanho do corte
        :rtype: int | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.tamanho_corte
        return None

    @property
    def data_inicio(self) -> Optional[datetime]:
        """
        A data de início do estudo.

        :return: A data
        :rtype: datetime | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.data_inicio
        return None

    @property
    def codigos_uhes(self) -> Optional[List[int]]:
        """
        Os códigos das usinas hidráulicas.

        :return: Os códigos das usinas
        :rtype: list | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.codigos_uhes
        return None

    @property
    def codigos_uhes_jusante(self) -> Optional[List[int]]:
        """
        Os códigos das usinas hidráulicas a jusante.

        :return: Os códigos das usinas
        :rtype: list | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.codigos_uhes_jusante
        return None

    @property
    def indice_no_arvore(self) -> Optional[list]:
        """
        Os índice do nó pai na árvore de cenários
        para cada nó da árvore.

        :return: Os índices
        :rtype: list | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.indice_no_arvore
        return None

    @property
    def numero_estagios(self) -> Optional[int]:
        """
        O número de estágios.

        :return: O número de estágios
        :rtype: int | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.numero_estagios
        return None

    @property
    def numero_semanas(self) -> Optional[int]:
        """
        O número de semanas.

        :return: O número de semanas
        :rtype: int | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.numero_semanas
        return None

    @property
    def numero_uhes_tempo_viagem(self) -> Optional[int]:
        """
        O número de usinas hidraúlicas com tempo
        de viagem da água.

        :return: O número de usinas
        :rtype: int | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.numero_uhes_tempo_viagem
        return None

    @property
    def maximo_lag_tempo_viagem(self) -> Optional[int]:
        """
        O máximo lag de tempo de viagem.

        :return: O máximo lag de tempo de viagem
        :rtype: int | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.maximo_lag_tempo_viagem
        return None

    @property
    def indice_primeiro_no_estagio(self) -> Optional[list]:
        """
        O índice do primeiro nó de cada estágio.

        :return: O número de patamares por estágio
        :rtype: list | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.indice_primeiro_no_estagio
        return None

    @property
    def patamares_por_estagio(self) -> Optional[list]:
        """
        O número de patamares de carga por estágio.

        :return: O número de patamares por estágio
        :rtype: list | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.patamares_por_estagio
        return None

    @property
    def lag_tempo_viagem_por_uhe(self) -> Optional[list]:
        """
        O lag (em estágios) de uma usina para cada período.

        :return: O lag por usina e estágio
        :rtype: list | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.lag_tempo_viagem_por_uhe
        return None

    @property
    def codigos_uhes_tempo_viagem(self) -> Optional[List[int]]:
        """
        Os códigos das usinas hidráulicas com tempo de viagem.

        :return: Os códigos das usinas com tempo de viagem
        :rtype: list | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.codigos_uhes_tempo_viagem
        return None

    @property
    def dados_tempo_viagem(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela com os dados de tempo de viagem.

        - codigo_usina (`int`)
        - numero_horas (`int`)
        - estagio (`int`)
        - indice_lag (`int`)
        - coeficiente_amortecimento (`float`)

        :return: A tabela com os dados de tempo de viagem
        :rtype: pd.DataFrame | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.dados_tempo_viagem
        return None

    @property
    def codigos_submercados_gnl(self) -> Optional[List[int]]:
        """
        Os códigos das usinas térmicas com despacho
         antecipado (GNL).

        :return: Os códigos das usinas
        :rtype: list | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.codigos_submercados_gnl
        return None

    @property
    def dados_gnl(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela com os dados de usinas GNL.

        - estagio (`int`)
        - numero_utes_gnl (`int`)
        - codigo_submercado (`int`)
        - indice_lag (`int`)
        - numero_patamares (`int`)

        :return: A tabela com os dados de usinas GNL
        :rtype: pd.DataFrame | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.dados_gnl
        return None

    @property
    def dados_custos(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela com os dados de custos.

        - estagio (`int`)
        - taxa_desconto (`float`)
        - parcela_custo_geracao_termica_minima (`float`)
        - parcela_custo_contrato_importacao_minimo (`float`)
        - parcela_custo_contrato_exportacao_minimo (`float`)
        - geracao_termica_minima_sinalizada_gnl (`float`)
        - geracao_termica_minima_gerada_gnl (`float`)

        :return: A tabela com os dados de custos
        :rtype: pd.DataFrame | None
        """
        dados = self.__obtem_dados()
        if dados is not None:
            return dados.dados_custos
        return None
