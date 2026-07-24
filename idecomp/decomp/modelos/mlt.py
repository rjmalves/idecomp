from typing import IO, Any

import numpy as np
from cfinterface.components.section import Section


class SecaoMlt(Section):
    """
    Registro com os dados das médias mensais de longo termo (MLT)
    de cada posto, por mês do ano.
    """

    __slots__: list[str] = []

    NUMERO_MESES = 12
    NUMERO_POSTOS = 320

    def __init__(
        self,
        previous: Any = None,
        next: Any = None,
        data: Any = None,
    ) -> None:
        super().__init__(previous, next, data)
        self.data = []

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, SecaoMlt):
            return False
        bloco: SecaoMlt = o
        return self.data == bloco.data

    def read(self, file: IO[Any], *args: Any, **kwargs: Any) -> None:  # type: ignore[override]
        dados = np.frombuffer(
            file.read(SecaoMlt.NUMERO_MESES * SecaoMlt.NUMERO_POSTOS * 4),
            dtype=np.int32,
            count=SecaoMlt.NUMERO_MESES * SecaoMlt.NUMERO_POSTOS,
        )
        self.data = list(dados)

    def write(self, file: IO[Any], *args: Any, **kwargs: Any) -> None:  # type: ignore[override]
        file.write(np.array(self.data, dtype=np.int32).tobytes())
