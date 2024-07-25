from cfinterface.components.section import Section
from typing import IO
import numpy as np  # type: ignore


class SecaoDadosMapcut(Section):
    """
    Registro com os dados da execução do caso existente no
    arquivo mapcut.
    """

    __slots__ = ["__contador_registro"]

    REGISTER_SIZE = 48020

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.data = {
            "dados_gerais": [],  # 1
            "dados_caso": [],  # 2
            "dados_uhes": [],  # 3
            "dados_uhes_topologia": [],  # 4
            "dados_arvore": [],  # 5
            "dados_estagios": [],  # 6
            "dados_tempo_viagem": [],  # 7 e 8
            "dados_gnl": [],  # 9 e 10
        }
        self.__contador_registro = 1

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, SecaoDadosMapcut):
            return False
        bloco: SecaoDadosMapcut = o
        if not all(
            [
                isinstance(self.data, dict),
                isinstance(o.data, dict),
            ]
        ):
            return False
        else:
            return self.data == bloco.data

    def read(self, file: IO, *args, **kwargs):
        # Leitura do primeiro registro (dados gerais)
        self.__le_primeiro_registro(file)
        # Leitura do segundo registro (dados do caso)
        self.__le_segundo_registro(file)
        # Leitura do terceiro registro (códigos UHEs)
        self.__le_terceiro_registro(file)
        # Leitura do quarto registro (dados cascatas UHEs)
        self.__le_quarto_registro(file)
        # Leitura do quinto registro (dados da árvore de cenários)
        self.__le_quinto_registro(file)
        # Leitura do sexto registro (dados gerais dos estágios)
        self.__le_sexto_registro(file)
        # Leitura do sétimo e oitavo registro (dados de tempo de viagem)
        self.__le_setimo_oitavo_registros(file)
        # Leitura do nono e décimo registro (dados de usinas gnl)
        self.__le_nono_decimo_registros(file)

    def __le_primeiro_registro(self, file: IO):
        tamanho_primeiro_bloco = 5
        dados_primeiro_bloco = np.frombuffer(
            file.read(tamanho_primeiro_bloco * 4),
            dtype=np.int32,
            count=tamanho_primeiro_bloco,
        )
        ncen = list(dados_primeiro_bloco)[-1]
        tamanho_segundo_bloco = ncen
        dados_segundo_bloco = np.frombuffer(
            file.read(tamanho_segundo_bloco * 4),
            dtype=np.int32,
            count=tamanho_segundo_bloco,
        )
        dados = list(dados_primeiro_bloco) + list(dados_segundo_bloco)
        self.data["dados_gerais"] = list(dados)

    def __le_segundo_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho = 4
        dados = np.frombuffer(
            file.read(tamanho * 4),
            dtype=np.int32,
            count=tamanho,
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_caso"] = list(dados)

    def __le_terceiro_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho = self.numero_uhes
        dados = np.frombuffer(
            file.read(tamanho * 4),
            dtype=np.int32,
            count=tamanho,
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_uhes"] = list(dados)

    def __le_quarto_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho = self.numero_uhes
        dados = np.frombuffer(
            file.read(tamanho * 4),
            dtype=np.float32,
            count=tamanho,
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_uhes_topologia"] = list(dados)

    def __le_quinto_registro(self, file: IO):
        self.__contador_registro = self.__contador_registro + 14
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho = self.numero_cenarios
        dados = np.frombuffer(
            file.read(tamanho * 4),
            dtype=np.float32,
            count=tamanho,
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_arvore"] = list(dados)

    def __le_sexto_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho_primeiro_bloco = 5
        dados_primeiro_bloco = np.frombuffer(
            file.read(tamanho_primeiro_bloco * 4),
            dtype=np.int32,
            count=tamanho_primeiro_bloco,
        )
        nper = list(dados_primeiro_bloco)[1]
        nutv = list(dados_primeiro_bloco)[-2]
        tamanho_segundo_bloco = 2 * nper
        dados_segundo_bloco = np.frombuffer(
            file.read(tamanho_segundo_bloco * 4),
            dtype=np.int32,
            count=tamanho_segundo_bloco,
        )
        tamanho_terceiro_bloco = nutv * nper
        dados_terceiro_bloco = np.frombuffer(
            file.read(tamanho_terceiro_bloco * 4),
            dtype=np.int32,
            count=tamanho_terceiro_bloco,
        )
        dados = (
            list(dados_primeiro_bloco)
            + list(dados_segundo_bloco)
            + list(dados_terceiro_bloco)
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_estagios"] = list(dados)

    def __le_setimo_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho_primeiro_bloco = 3
        tamanho_segundo_bloco = 1
        dados_primeiro_bloco = np.frombuffer(
            file.read(tamanho_primeiro_bloco * 4),
            dtype=np.int32,
            count=tamanho_primeiro_bloco,
        )
        dados_segundo_bloco = np.frombuffer(
            file.read(tamanho_segundo_bloco * 8),
            dtype=np.float64,
            count=tamanho_segundo_bloco,
        )
        dados = list(dados_primeiro_bloco) + list(dados_segundo_bloco)
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_tempo_viagem"] += list(dados)

    def __le_oitavo_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho = 1
        dados_primeiro_bloco = np.frombuffer(
            file.read(tamanho * 4),
            dtype=np.int32,
            count=tamanho,
        )
        dados_segundo_bloco = np.frombuffer(
            file.read(tamanho * 8),
            dtype=np.float64,
            count=tamanho,
        )
        dados = list(dados_primeiro_bloco) + list(dados_segundo_bloco)
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_tempo_viagem"] += list(dados)

    def __le_setimo_oitavo_registros(self, file: IO):
        for uhe in range(1, self.numero_uhes_tempo_viagem + 1, 1):
            for est in range(1, self.numero_estagios + 1, 1):
                lags = self.lag_tempo_viagem_por_uhe[(uhe * est) - 1]
                for lag in range(0, lags + 1, 1):
                    if (est == 1) & (lag == 0):
                        self.__le_setimo_registro(file)
                    else:
                        self.__le_oitavo_registro(file)

    def __le_nono_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho_primeiro_bloco = 1
        dados_primeiro_bloco = np.frombuffer(
            file.read(tamanho_primeiro_bloco * 4),
            dtype=np.int32,
            count=tamanho_primeiro_bloco,
        )
        ngnl = list(dados_primeiro_bloco)[0]
        tamanho_segundo_bloco = 3 * ngnl
        dados_segundo_bloco = np.frombuffer(
            file.read(tamanho_segundo_bloco * 4),
            dtype=np.int32,
            count=tamanho_segundo_bloco,
        )
        tamanho_terceiro_bloco = len(self.patamares_por_estagio) * ngnl
        dados_terceiro_bloco = np.frombuffer(
            file.read(tamanho_terceiro_bloco * 8),
            dtype=np.float64,
            count=tamanho_terceiro_bloco,
        )
        dados = (
            list(dados_primeiro_bloco)
            + list(dados_segundo_bloco)
            + list(dados_terceiro_bloco)
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_gnl"] += list(dados)

    def __le_decimo_registro(self, file: IO):
        file.seek(self.__contador_registro * self.REGISTER_SIZE)
        tamanho = 6
        dados = np.frombuffer(
            file.read(tamanho * 8),
            dtype=np.float64,
            count=tamanho,
        )
        self.__contador_registro = self.__contador_registro + 1
        self.data["dados_gnl"] += list(dados)

    def __le_nono_decimo_registros(self, file: IO):
        for _ in range(self.numero_estagios):
            self.__le_nono_registro(file)
            self.__le_decimo_registro(file)

    @property
    def numero_iteracoes(self) -> int:
        return self.data["dados_gerais"][0]

    @property
    def numero_cortes(self) -> int:
        return self.data["dados_gerais"][1]

    @property
    def numero_submercados(self) -> int:
        return self.data["dados_gerais"][2]

    @property
    def numero_uhes(self) -> int:
        return self.data["dados_gerais"][3]

    @property
    def numero_cenarios(self) -> int:
        return self.data["dados_gerais"][4]

    @property
    def tamanho_corte(self) -> int:
        return self.data["dados_caso"][0]

    @property
    def codigos_uhes(self) -> list:
        return self.data["dados_uhes"]

    @property
    def codigos_uhes_jusante(self) -> list:
        return self.data["dados_uhes_topologia"]

    @property
    def indice_no_arvore(self) -> list:
        return self.data["dados_arvore"]

    @property
    def numero_estagios(self) -> int:
        return self.data["dados_estagios"][1]

    @property
    def numero_semanas(self) -> int:
        return self.data["dados_estagios"][2]

    @property
    def numero_uhes_tempo_viagem(self) -> int:
        return self.data["dados_estagios"][3]

    @property
    def maximo_lag_tempo_viagem(self) -> int:
        return self.data["dados_estagios"][4]

    @property
    def indice_primeiro_no_estagio(self) -> list:
        offset = 5
        return self.data["dados_estagios"][
            offset : (offset + self.numero_estagios)
        ]

    @property
    def patamares_por_estagio(self) -> list:
        offset = 4 + self.numero_estagios + 1
        patamares_estagio = self.data["dados_estagios"][
            offset : (offset + self.numero_estagios)
        ]
        return patamares_estagio

    @property
    def lag_tempo_viagem_por_uhe(self) -> list:
        return self.data["dados_estagios"][
            -(self.numero_uhes_tempo_viagem * self.numero_estagios) :
        ]

    @property
    def dados_tempo_viagem(self) -> list:
        return self.data["dados_tempo_viagem"]

    @property
    def dados_gnl(self) -> list:
        return self.data["dados_gnl"]
