from idecomp.decomp.modelos.custos import BlocoRelatorioCustos

from cfinterface.components.block import Block
from cfinterface.files.blockfile import BlockFile
from typing import List, TypeVar, Optional
import pandas as pd  # type: ignore


class Custos(BlockFile):
    """
    Armazena os dados de saída do DECOMP referentes aos
    custos associados à solução do problema.

    Esta classe lida com as informações de saída do
    DECOMP reproduzidas no `custos.rvx`.

    """

    T = TypeVar("T")

    BLOCKS = [
        BlocoRelatorioCustos,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)
        self.__relatorios_variaveis_duais = None
        self.__relatorios_fcf = None

    def __concatena_blocos(
        self, blocos, indice_data: int
    ) -> Optional[pd.DataFrame]:
        """
        Adiciona uma coluna com o estágio de cada bloco, assumindo
        a mesma ordem das séries de energia.
        :param blocos: Os blocos a serem concatenados
        :type bloco: List[Type[T]]
        :return: O DataFrame com os estágios
        :rtype: pd.DataFrame
        """
        df = None
        for b in blocos:
            if not isinstance(b, Block):
                continue
            df_estagio = b.data[indice_data]
            if df is None:
                df = df_estagio
            else:
                df = pd.concat([df, df_estagio], ignore_index=True)
        if df is not None:
            return df
        return None

    @property
    def relatorio_variaveis_duais(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela das variáveis duais do armazenamento de cada
        UHE, nos problemas resolvidos pelo DECOMP.

        - estagio (`int`)
        - cenario (`int`)
        - usina (`str`)
        - pih (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        if self.__relatorios_variaveis_duais is None:
            blocos_custos: List[BlocoRelatorioCustos] = []
            for b in self.data.of_type(BlocoRelatorioCustos):
                blocos_custos.append(b)
            self.__relatorios_variaveis_duais = self.__concatena_blocos(
                blocos_custos, 0
            )
        return self.__relatorios_variaveis_duais

    @property
    def relatorio_fcf(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela dos cortes da FCF nos quais o DECOMP acoplou durante
        a resolução dos seus problemas.

        - estagio (`int`)
        - cenario (`int`)
        - indice_corte (`int`)
        - parcela_pi (`float`)

        :return: O DataFrame com os valores
        :rtype: pd.DataFrame | None
        """
        if self.__relatorios_fcf is None:
            blocos_custos: List[BlocoRelatorioCustos] = []
            for b in self.data.of_type(BlocoRelatorioCustos):
                blocos_custos.append(b)
            self.__relatorios_fcf = self.__concatena_blocos(blocos_custos, 1)
        return self.__relatorios_fcf
