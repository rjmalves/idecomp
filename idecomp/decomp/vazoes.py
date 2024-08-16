from cfinterface.files.sectionfile import SectionFile
from idecomp.decomp.modelos.vazoes import SecaoVazoesPostos
import pandas as pd  # type: ignore
import numpy as np  # type: ignore


from typing import TypeVar, Optional, List


class Vazoes(SectionFile):
    """
    Armazena os dados de entrada do DECOMP referentes às vazões previstas
    e cenários gerados pelos modelos satélites.
    """

    T = TypeVar("T")

    SECTIONS = [SecaoVazoesPostos]
    STORAGE = "BINARY"

    def __init__(self, data=...) -> None:
        super().__init__(data)
        self.__df_probabilidades: Optional[pd.DataFrame] = None
        self.__df_previsoes_semanais: Optional[pd.DataFrame] = None
        self.__df_cenarios_mensais_gerados: Optional[pd.DataFrame] = None
        self.__df_previsoes_semanais_com_postos_artificiais: Optional[
            pd.DataFrame
        ] = None
        self.__df_cenarios_mensais_calculados_com_postos_artificiais: Optional[
            pd.DataFrame
        ] = None
        self.__df_observacoes_mensais: Optional[pd.DataFrame] = None
        self.__df_observacoes_semanais: Optional[pd.DataFrame] = None

    def __obtem_secao_vazoes(self) -> Optional[SecaoVazoesPostos]:
        s = self.data.get_sections_of_type(SecaoVazoesPostos)
        return s if not isinstance(s, list) else None

    @property
    def numero_aberturas_estagios(self) -> Optional[List[int]]:
        """
        Obtém a lista com o número de aberturas por estágio da árvore.

        :return: A lista das aberturas por estágio
        :rtype: List[int] | None
        """
        dados = self.__obtem_secao_vazoes()
        if dados is not None:
            return dados.numero_aberturas_estagios
        else:
            return None

    @numero_aberturas_estagios.setter
    def numero_aberturas_estagios(self, a: List[int]):
        dados = self.__obtem_secao_vazoes()
        if dados is not None:
            dados.numero_aberturas_estagios = a

    @property
    def probabilidades(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela com as probabilidades de cada nó da árvore de cenários
        que foi gerada para o modelo.

        - estagio (`int`)
        - no (`int`)
        - cenario (`int`)
        - probabilidade (`float`)

        :return: A tabela com as probabilidades por nó
        :rtype: pd.DataFrame | None
        """
        if self.__df_probabilidades is None:
            dados = self.__obtem_secao_vazoes()
            if dados is not None:
                probs = dados.probabilidades_nos
                numero_estagios = dados.numero_estagios
                df = pd.DataFrame(
                    data={
                        "estagio": list(range(1, numero_estagios))
                        + [numero_estagios]
                        * dados.numero_cenarios_estocasticos,
                        "no": list(range(1, len(probs) + 1)),
                        "cenario": [1] * dados.numero_semanas_completas
                        + list(
                            range(1, dados.numero_cenarios_estocasticos + 1)
                        ),
                        "probabilidade": probs,
                    }
                )
                self.__df_probabilidades = df
        return self.__df_probabilidades

    @probabilidades.setter
    def probabilidades(self, df: pd.DataFrame):
        dados = self.__obtem_secao_vazoes()
        if dados is not None:
            dados.probabilidades_nos = df["probabilidade"].tolist()
            self.__df_probabilidades = None

    @property
    def previsoes(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela com as vazões previstas de cada nó da árvore de
        cenários, para a etapa determinística da execução, por posto.

        - estagio (`int`)
        - 1 (`int`)
        - ...
        - N (`int`) : número de postos

        :return: A tabela com as previsões por estágio e posto
        :rtype: pd.DataFrame | None
        """
        if self.__df_previsoes_semanais is None:
            dados = self.__obtem_secao_vazoes()
            if dados is not None:
                prevs = dados.previsoes
                n_postos = dados.numero_postos
                numero_estagios = dados.numero_semanas_completas
                cols_postos = [str(p) for p in range(1, n_postos + 1)]
                df = pd.DataFrame(
                    np.array(prevs).reshape((-1, n_postos)),
                    columns=cols_postos,
                )
                df["estagio"] = list(range(1, numero_estagios + 1))
                self.__df_previsoes_semanais = df[["estagio"] + cols_postos]
        return self.__df_previsoes_semanais

    @previsoes.setter
    def previsoes(self, df: pd.DataFrame):
        dados = self.__obtem_secao_vazoes()
        if dados is not None:
            n_postos = dados.numero_postos
            n_prevs = len(dados.previsoes)
            cols_dados = [c for c in df.columns if c not in ["estagio"]]
            if df[cols_dados].size != n_prevs:
                raise ValueError(
                    f"São esperados {n_prevs} valores de previsões."
                )
            cols_postos = [str(p) for p in range(1, n_postos + 1)]
            dados.previsoes = df[cols_postos].to_numpy().flatten().tolist()
            self.__df_previsoes_semanais = None

    @property
    def previsoes_com_postos_artificiais(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela com as vazões previstas de cada nó da árvore de
        cenários, para a etapa determinística da execução, por posto.
        Considera também os postos artificiais (usados para acoplamento).

        - estagio (`int`)
        - 1 (`int`)
        - ...
        - N (`int`) : número de postos

        :return: A tabela com as previsões por estágio e posto
        :rtype: pd.DataFrame | None
        """
        if self.__df_previsoes_semanais_com_postos_artificiais is None:
            dados = self.__obtem_secao_vazoes()
            if dados is not None:
                prevs = dados.previsoes_com_postos_artificiais
                n_postos = dados.numero_postos
                numero_estagios = dados.numero_semanas_completas
                cols_postos = [str(p) for p in range(1, n_postos + 1)]
                df = pd.DataFrame(
                    np.array(prevs).reshape((-1, n_postos)),
                    columns=cols_postos,
                )
                df["estagio"] = list(range(1, numero_estagios + 1))
                self.__df_previsoes_semanais_com_postos_artificiais = df[
                    ["estagio"] + cols_postos
                ]
        return self.__df_previsoes_semanais_com_postos_artificiais

    @previsoes_com_postos_artificiais.setter
    def previsoes_com_postos_artificiais(self, df: pd.DataFrame):
        dados = self.__obtem_secao_vazoes()
        if dados is not None:
            n_postos = dados.numero_postos
            n_prevs = len(dados.previsoes_com_postos_artificiais)
            cols_dados = [c for c in df.columns if c not in ["estagio"]]
            if df[cols_dados].size != n_prevs:
                raise ValueError(
                    f"São esperados {n_prevs} valores de previsões."
                )
            cols_postos = [str(p) for p in range(1, n_postos + 1)]
            dados.previsoes_com_postos_artificiais = (
                df[cols_postos].to_numpy().flatten().tolist()
            )
            self.__df_previsoes_semanais_com_postos_artificiais = None

    @property
    def cenarios_gerados(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela com as cenários gerados de cada nó da árvore de
        cenários, para a etapa estocástica da execução, por posto.

        - estagio (`int`)
        - cenario (`int`)
        - 1 (`int`)
        - ...
        - N (`int`) : número de postos

        :return: A tabela com os cenários por estágio e posto
        :rtype: pd.DataFrame | None
        """
        if self.__df_cenarios_mensais_gerados is None:
            dados = self.__obtem_secao_vazoes()
            if dados is not None:
                cens = dados.cenarios_gerados
                n_postos = dados.numero_postos
                numero_semanas = dados.numero_semanas_completas
                estagios_estocasticos = list(
                    range(1, dados.numero_estagios + 1)
                )[numero_semanas:]
                aberturas_por_estagio = dados.numero_aberturas_estagios
                cols_postos = [str(p) for p in range(1, n_postos + 1)]
                df = pd.DataFrame(
                    np.array(cens).reshape((-1, n_postos)),
                    columns=cols_postos,
                )
                estagios = []
                cenarios = []
                for _, e in enumerate(estagios_estocasticos):
                    estagios += [e] * aberturas_por_estagio[e - 1]
                    cenarios += list(
                        range(1, aberturas_por_estagio[e - 1] + 1)
                    )
                df["estagio"] = estagios
                df["cenario"] = cenarios
                self.__df_cenarios_mensais_gerados = df[
                    ["estagio", "cenario"] + cols_postos
                ]
        return self.__df_cenarios_mensais_gerados

    @cenarios_gerados.setter
    def cenarios_gerados(self, df: pd.DataFrame):
        dados = self.__obtem_secao_vazoes()
        if dados is not None:
            n_postos = dados.numero_postos
            cols_postos = [str(p) for p in range(1, n_postos + 1)]
            dados.cenarios_gerados = (
                df[cols_postos].to_numpy().flatten().tolist()
            )
            self.__df_cenarios_mensais_gerados = None

    @property
    def cenarios_calculados_com_postos_artificiais(
        self,
    ) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela com as cenários gerados de cada nó da árvore de
        cenários, para a etapa estocástica da execução, por posto.
        Considera também os postos artificiais (usados para acoplamento).

        - estagio (`int`)
        - cenario (`int`)
        - 1 (`int`)
        - ...
        - N (`int`) : número de postos

        :return: A tabela com os cenários por estágio e posto
        :rtype: pd.DataFrame | None
        """
        if (
            self.__df_cenarios_mensais_calculados_com_postos_artificiais
            is None
        ):
            dados = self.__obtem_secao_vazoes()
            if dados is not None:
                cens = dados.cenarios_calculados_com_postos_artificiais
                n_postos = dados.numero_postos
                numero_semanas = dados.numero_semanas_completas
                estagios_estocasticos = list(
                    range(1, dados.numero_estagios + 1)
                )[numero_semanas:]
                aberturas_por_estagio = dados.numero_aberturas_estagios
                cols_postos = [str(p) for p in range(1, n_postos + 1)]
                df = pd.DataFrame(
                    np.array(cens).reshape((-1, n_postos)),
                    columns=cols_postos,
                )
                estagios = []
                cenarios = []
                for _, e in enumerate(estagios_estocasticos):
                    estagios += [e] * aberturas_por_estagio[e - 1]
                    cenarios += list(
                        range(1, aberturas_por_estagio[e - 1] + 1)
                    )
                df["estagio"] = estagios
                df["cenario"] = cenarios
                self.__df_cenarios_mensais_calculados_com_postos_artificiais = df[
                    ["estagio", "cenario"] + cols_postos
                ]
        return self.__df_cenarios_mensais_calculados_com_postos_artificiais

    @cenarios_calculados_com_postos_artificiais.setter
    def cenarios_calculados_com_postos_artificiais(self, df: pd.DataFrame):
        dados = self.__obtem_secao_vazoes()
        if dados is not None:
            n_postos = dados.numero_postos
            cols_postos = [str(p) for p in range(1, n_postos + 1)]
            dados.cenarios_calculados_com_postos_artificiais = (
                df[cols_postos].to_numpy().flatten().tolist()
            )
            self.__df_cenarios_mensais_calculados_com_postos_artificiais = None

    @property
    def observacoes_semanais(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela com as observações semanais de cada nó da árvore de
        cenários, por posto.

        - semana (`int`)
        - 1 (`int`)
        - ...
        - N (`int`) : número de postos

        :return: A tabela com as observações semanais por estágio e posto
        :rtype: pd.DataFrame | None
        """
        if self.__df_observacoes_semanais is None:
            dados = self.__obtem_secao_vazoes()
            if dados is not None:
                obs = dados.observacoes_semanais
                n_postos = dados.numero_postos
                numero_semanas = dados.numero_semanas_observadas
                cols_postos = [str(p) for p in range(1, n_postos + 1)]
                df = pd.DataFrame(
                    np.array(obs).reshape((-1, n_postos)),
                    columns=cols_postos,
                )
                df["semana"] = list(range(1, numero_semanas + 1))
                self.__df_observacoes_semanais = df[["semana"] + cols_postos]
        return self.__df_observacoes_semanais

    @observacoes_semanais.setter
    def observacoes_semanais(self, df: pd.DataFrame):
        dados = self.__obtem_secao_vazoes()
        if dados is not None:
            n_postos = dados.numero_postos
            n_obs = len(dados.observacoes_semanais)
            cols_dados = [c for c in df.columns if c not in ["semana"]]
            if df[cols_dados].size != n_obs:
                raise ValueError(
                    f"São esperados {n_obs} valores de observações."
                )
            cols_postos = [str(p) for p in range(1, n_postos + 1)]
            dados.observacoes_semanais = (
                df[cols_postos].to_numpy().flatten().tolist()
            )
            self.__df_observacoes_semanais = None

    @property
    def observacoes_mensais(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela com as observações mensais de cada nó da árvore de
        cenários, por posto.

        - mes (`int`)
        - 1 (`int`)
        - ...
        - N (`int`) : número de postos

        :return: A tabela com as observações mensais por estágio e posto
        :rtype: pd.DataFrame | None
        """
        if self.__df_observacoes_mensais is None:
            dados = self.__obtem_secao_vazoes()
            if dados is not None:
                obs = dados.observacoes_mensais
                n_postos = dados.numero_postos
                numero_meses = dados.numero_meses_observados
                cols_postos = [str(p) for p in range(1, n_postos + 1)]
                df = pd.DataFrame(
                    np.array(obs).reshape((-1, n_postos)),
                    columns=cols_postos,
                )
                df["mes"] = list(range(1, numero_meses + 1))
                self.__df_observacoes_mensais = df[["mes"] + cols_postos]
        return self.__df_observacoes_mensais

    @observacoes_mensais.setter
    def observacoes_mensais(self, df: pd.DataFrame):
        dados = self.__obtem_secao_vazoes()
        if dados is not None:
            n_postos = dados.numero_postos
            n_obs = len(dados.observacoes_mensais)
            cols_dados = [c for c in df.columns if c not in ["mes"]]
            if df[cols_dados].size != n_obs:
                raise ValueError(
                    f"São esperados {n_obs} valores de observações."
                )
            cols_postos = [str(p) for p in range(1, n_postos + 1)]
            dados.observacoes_mensais = (
                df[cols_postos].to_numpy().flatten().tolist()
            )
            self.__df_observacoes_mensais = None
