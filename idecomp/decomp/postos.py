from cfinterface.files.registerfile import RegisterFile
from idecomp.decomp.modelos.postos import RegistroPostos
import pandas as pd  # type: ignore


from typing import TypeVar, List, Optional, Union, IO


class Postos(RegisterFile):
    """
    Armazena os dados de entrada do DECOMP referentes ao postos
    e seus históricos.
    """

    T = TypeVar("T")

    REGISTERS = [RegistroPostos]
    POSTOS = 320
    STORAGE = "BINARY"

    def __init__(self, data=...) -> None:
        super().__init__(data)
        self.__df: Optional[pd.DataFrame] = None
        RegistroPostos.set_postos(self.POSTOS)

    def write(self, to: Union[str, IO], *args, **kwargs):
        self.__atualiza_registros()
        super().write(to, *args, **kwargs)

    def __monta_df_de_registros(self) -> Optional[pd.DataFrame]:
        registros: List[RegistroPostos] = [
            r for r in self.data.of_type(RegistroPostos)
        ]
        if len(registros) == 0:
            return None
        df = pd.DataFrame(
            data={
                "nome": [r.data[0] for r in registros],
                "ano_inicio_historico": [r.data[1] for r in registros],
                "ano_fim_historico": [r.data[2] for r in registros],
            }
        )

        df = df.astype(
            {
                "nome": str,
                "ano_inicio_historico": int,
                "ano_fim_historico": int,
            }
        )
        return df

    def __atualiza_registros(self):
        registros: List[RegistroPostos] = [r for r in self.data][1:]
        n_registros = len(registros)
        n_meses = self.postos.shape[0]
        # Deleta os registros que sobraram
        for i in range(n_meses, n_registros):
            self.data.remove(registros[i])
        # Cria registros se faltaram
        for i in range(n_registros, n_meses):
            self.data.append(RegistroPostos())
        # Atualiza os dados
        for (_, linha), r in zip(self.postos.iterrows(), registros):
            r.data = linha.tolist()

    @property
    def postos(self) -> pd.DataFrame:
        """
        Obtém a tabela com os dados dos postos existentes no arquivo
        binário.

        - nome (`str`)
        - ano_inicio_historico (`int`)
        - ano_fim_historico (`int`)

        :return: A tabela com os postos
        :rtype: pd.DataFrame
        """
        if self.__df is None:
            self.__df = self.__monta_df_de_registros()
        return self.__df

    @postos.setter
    def postos(self, df: pd.DataFrame):
        self.__df = df
