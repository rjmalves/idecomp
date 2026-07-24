from typing import IO, Any, TypeVar

import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from cfinterface.files.sectionfile import SectionFile

from idecomp.decomp.modelos.mlt import SecaoMlt


class Mlt(SectionFile):
    """
    Armazena os dados de entrada do DECOMP referentes às médias
    mensais de longo termo (MLT) de cada posto.
    """

    T = TypeVar("T")

    SECTIONS = [SecaoMlt]
    STORAGE = "BINARY"

    def __init__(self, data: Any = ...) -> None:
        super().__init__(data)
        self.__df: pd.DataFrame | None = None

    def write(self, to: str | IO[Any], *args: Any, **kwargs: Any) -> None:
        self.__atualiza_secao()
        super().write(to, *args, **kwargs)

    def __obtem_secao_mlt(self) -> SecaoMlt | None:
        s = self.data.get_sections_of_type(SecaoMlt)
        return s if not isinstance(s, list) else None

    def __atualiza_secao(self) -> None:
        dados = self.__obtem_secao_mlt()
        if dados is not None and self.__df is not None:
            cols_postos = [str(p) for p in range(1, SecaoMlt.NUMERO_POSTOS + 1)]
            dados.data = self.__df[cols_postos].to_numpy().flatten().tolist()

    @property
    def valores(self) -> pd.DataFrame | None:
        """
        Obtém a tabela com as médias mensais de longo termo (MLT) de
        cada posto, por mês do ano.

        - mes (`int`)
        - 1 (`int`)
        - ...
        - N (`int`) : número de postos

        :return: A tabela com as médias por mês e posto
        :rtype: pd.DataFrame | None
        """
        if self.__df is None:
            dados = self.__obtem_secao_mlt()
            if dados is not None:
                cols_postos = [
                    str(p) for p in range(1, SecaoMlt.NUMERO_POSTOS + 1)
                ]
                df = pd.DataFrame(
                    np.array(dados.data).reshape(
                        (SecaoMlt.NUMERO_MESES, SecaoMlt.NUMERO_POSTOS)
                    ),
                    columns=cols_postos,
                )
                df["mes"] = list(range(1, SecaoMlt.NUMERO_MESES + 1))
                self.__df = df[["mes"] + cols_postos]
        return self.__df

    @valores.setter
    def valores(self, df: pd.DataFrame) -> None:
        dados = self.__obtem_secao_mlt()
        if dados is not None:
            cols_postos = [str(p) for p in range(1, SecaoMlt.NUMERO_POSTOS + 1)]
            dados.data = df[cols_postos].to_numpy().flatten().tolist()
            self.__df = None
