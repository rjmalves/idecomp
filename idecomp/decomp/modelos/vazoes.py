from cfinterface.components.section import Section
from typing import List, IO
import numpy as np  # type: ignore


class SecaoVazoesPostos(Section):
    """
    Registro com os dados associados às vazões dos postos.
    """

    __slots__ = []

    TAMANHO_REGISTRO = 320

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.data = {
            "dados_gerais": [],
            "codigos_uhes": [],
            "dados_caso": [],
            "dados_cenarios": [],
            "previsoes": [],
            "cenarios_gerados": [],
            "previsoes_com_postos_artificiais": [],
            "cenarios_calculados_com_postos_artificiais": [],
            "observacoes_mensais": [],
            "observacoes_semanais": [],
        }

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, SecaoVazoesPostos):
            return False
        bloco: SecaoVazoesPostos = o
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
        # Leitura do segundo registro (códigos UHEs)
        self.__le_segundo_registro(file)
        # Leitura do terceiro registro (dados do caso)
        self.__le_terceiro_registro(file)
        # Leitura do quarto registro (dados dos cenários)
        self.__le_quarto_registro(file)
        # Leitura do quinto registro (dados de vazões incrementais
        # semanais previstas)
        self.__le_quinto_registro(file)
        # Leitura do sexto registro (dados de vazões incrementais
        # mensais geradas)
        self.__le_sexto_registro(file)
        # Leitura do sétimo registro (dados de vazões incrementais
        # semanais previstas com postos artificiais)
        self.__le_setimo_registro(file)
        # Leitura do oitavo registro (dados de vazões incrementais
        # mensais calculadas com postos artificiais)
        self.__le_oitavo_registro(file)
        # Leitura do nono registro (dados de vazões incrementais
        # mensais observadas)
        self.__le_nono_registro(file)
        # Leitura do décimo registro (dados de vazões incrementais
        # semanais observadas)
        self.__le_decimo_registro(file)

    def __le_primeiro_registro(self, file: IO):
        dados = np.frombuffer(
            file.read(SecaoVazoesPostos.TAMANHO_REGISTRO * 4),
            dtype=np.int32,
            count=SecaoVazoesPostos.TAMANHO_REGISTRO,
        )
        self.data["dados_gerais"] = list(dados)

    def __le_segundo_registro(self, file: IO):
        dados = np.frombuffer(
            file.read(
                SecaoVazoesPostos.TAMANHO_REGISTRO
                * self.__numero_blocos_postos()
                * 4
            ),
            dtype=np.int32,
            count=SecaoVazoesPostos.TAMANHO_REGISTRO
            * self.__numero_blocos_postos(),
        )
        self.data["codigos_uhes"] = list(dados)

    def __le_terceiro_registro(self, file: IO):
        dados_caso = np.frombuffer(
            file.read(SecaoVazoesPostos.TAMANHO_REGISTRO * 4),
            dtype=np.int32,
            count=SecaoVazoesPostos.TAMANHO_REGISTRO,
        )
        self.data["dados_caso"] = list(dados_caso)

    def __le_quarto_registro(self, file: IO):
        dados_cenarios = np.frombuffer(
            file.read(
                SecaoVazoesPostos.TAMANHO_REGISTRO
                * self.__numero_blocos_cenarios()
                * 4
            ),
            dtype=np.float32,
            count=SecaoVazoesPostos.TAMANHO_REGISTRO
            * self.__numero_blocos_cenarios(),
        )
        self.data["dados_cenarios"] = list(dados_cenarios)

    def __le_quinto_registro(self, file: IO):
        for _ in range(self.numero_semanas_completas):
            dados_cenarios = np.frombuffer(
                file.read(SecaoVazoesPostos.TAMANHO_REGISTRO * 4),
                dtype=np.int32,
                count=SecaoVazoesPostos.TAMANHO_REGISTRO,
            )
            self.data["previsoes"] += list(dados_cenarios)

    def __le_sexto_registro(self, file: IO):
        for _ in range(self.numero_cenarios_estocasticos):
            dados_cenarios = np.frombuffer(
                file.read(SecaoVazoesPostos.TAMANHO_REGISTRO * 4),
                dtype=np.int32,
                count=SecaoVazoesPostos.TAMANHO_REGISTRO,
            )
            self.data["cenarios_gerados"] += list(dados_cenarios)

    def __le_setimo_registro(self, file: IO):
        for _ in range(self.numero_semanas_completas):
            dados_cenarios = np.frombuffer(
                file.read(SecaoVazoesPostos.TAMANHO_REGISTRO * 4),
                dtype=np.int32,
                count=SecaoVazoesPostos.TAMANHO_REGISTRO,
            )
            self.data["previsoes_com_postos_artificiais"] += list(
                dados_cenarios
            )

    def __le_oitavo_registro(self, file: IO):
        for _ in range(self.numero_cenarios_estocasticos):
            dados_cenarios = np.frombuffer(
                file.read(SecaoVazoesPostos.TAMANHO_REGISTRO * 4),
                dtype=np.int32,
                count=SecaoVazoesPostos.TAMANHO_REGISTRO,
            )
            self.data["cenarios_calculados_com_postos_artificiais"] += list(
                dados_cenarios
            )

    def __le_nono_registro(self, file: IO):
        for _ in range(self.numero_meses_observados):
            dados_cenarios = np.frombuffer(
                file.read(SecaoVazoesPostos.TAMANHO_REGISTRO * 4),
                dtype=np.int32,
                count=SecaoVazoesPostos.TAMANHO_REGISTRO,
            )
            self.data["observacoes_mensais"] += list(dados_cenarios)

    def __le_decimo_registro(self, file: IO):
        for _ in range(self.numero_semanas_observadas):
            dados_cenarios = np.frombuffer(
                file.read(SecaoVazoesPostos.TAMANHO_REGISTRO * 4),
                dtype=np.int32,
                count=SecaoVazoesPostos.TAMANHO_REGISTRO,
            )
            self.data["observacoes_semanais"] += list(dados_cenarios)

    def write(self, file: IO, *args, **kwargs):
        # Escrita do primeiro registro (dados gerais)
        self.__escreve_primeiro_registro(file)
        # Escrita do segundo registro (códigos UHEs)
        self.__escreve_segundo_registro(file)
        # Escrita do terceiro registro (dados do caso)
        self.__escreve_terceiro_registro(file)
        # Escrita do quarto registro (dados dos cenários)
        self.__escreve_quarto_registro(file)
        # Escrita do quinto registro (dados de vazões incrementais
        # semanais previstas)
        self.__escreve_quinto_registro(file)
        # Escrita do sexto registro (dados de vazões incrementais
        # mensais geradas)
        self.__escreve_sexto_registro(file)
        # Escrita do sétimo registro (dados de vazões incrementais
        # semanais previstas com postos artificiais)
        self.__escreve_setimo_registro(file)
        # Escrita do oitavo registro (dados de vazões incrementais
        # mensais calculadas com postos artificiais)
        self.__escreve_oitavo_registro(file)
        # Escrita do nono registro (dados de vazões incrementais
        # mensais observadas)
        self.__escreve_nono_registro(file)
        # Escrita do décimo registro (dados de vazões incrementais
        # semanais observadas)
        self.__escreve_decimo_registro(file)

    def __escreve_primeiro_registro(self, file: IO):
        file.write(
            np.array(self.data["dados_gerais"], dtype=np.int32).tobytes()
        )

    def __escreve_segundo_registro(self, file: IO):
        file.write(
            np.array(self.data["codigos_uhes"], dtype=np.int32).tobytes()
        )

    def __escreve_terceiro_registro(self, file: IO):
        file.write(np.array(self.data["dados_caso"], dtype=np.int32).tobytes())

    def __escreve_quarto_registro(self, file: IO):
        num_entradas = len(self.data["dados_cenarios"])
        num_valores = (
            self.__numero_blocos_cenarios()
            * SecaoVazoesPostos.TAMANHO_REGISTRO
        )
        if num_entradas < num_valores:
            self.data["dados_cenarios"] += [0] * (num_valores - num_entradas)
        file.write(
            np.array(self.data["dados_cenarios"], dtype=np.float32).tobytes()
        )

    def __escreve_quinto_registro(self, file: IO):
        file.write(np.array(self.data["previsoes"], dtype=np.int32).tobytes())

    def __escreve_sexto_registro(self, file: IO):
        file.write(
            np.array(self.data["cenarios_gerados"], dtype=np.int32).tobytes()
        )

    def __escreve_setimo_registro(self, file: IO):
        file.write(
            np.array(
                self.data["previsoes_com_postos_artificiais"], dtype=np.int32
            ).tobytes()
        )

    def __escreve_oitavo_registro(self, file: IO):
        file.write(
            np.array(
                self.data["cenarios_calculados_com_postos_artificiais"],
                dtype=np.int32,
            ).tobytes()
        )

    def __escreve_nono_registro(self, file: IO):
        file.write(
            np.array(
                self.data["observacoes_mensais"], dtype=np.int32
            ).tobytes()
        )

    def __escreve_decimo_registro(self, file: IO):
        file.write(
            np.array(
                self.data["observacoes_semanais"], dtype=np.int32
            ).tobytes()
        )

    def __numero_blocos_postos(self) -> int:
        return int(
            np.ceil(
                float(self.numero_postos) / SecaoVazoesPostos.TAMANHO_REGISTRO
            )
        )

    def __numero_blocos_cenarios(self) -> int:
        return int(
            np.ceil(
                float(np.sum(self.numero_aberturas_estagios))
                / SecaoVazoesPostos.TAMANHO_REGISTRO
            )
        )

    @property
    def numero_meses_observados(self) -> int:
        return 11

    @property
    def numero_uhes(self) -> int:
        return self.data["dados_gerais"][0]

    @numero_uhes.setter
    def numero_uhes(self, n: int):
        self.data["dados_gerais"][0] = n

    @property
    def numero_estagios(self) -> int:
        return self.data["dados_gerais"][1]

    @numero_estagios.setter
    def numero_estagios(self, n: int):
        self.data["dados_gerais"][1] = n

    @property
    def numero_aberturas_estagios(self) -> List[int]:
        return self.data["dados_gerais"][2 : 2 + self.numero_estagios]

    @numero_aberturas_estagios.setter
    def numero_aberturas_estagios(self, n: List[int]):
        self.data["dados_gerais"][2 : 2 + self.numero_estagios] = n

    @property
    def numero_postos(self) -> int:
        valor_arquivo = self.data["dados_gerais"][2 + self.numero_estagios]
        return 320 if valor_arquivo == 0 else valor_arquivo

    @numero_postos.setter
    def numero_postos(self, n: int):
        self.data["dados_gerais"][2 + self.numero_estagios] = n

    @property
    def codigos_uhes(self) -> List[int]:
        return self.data["codigos_uhes"][: self.numero_uhes]

    @codigos_uhes.setter
    def codigos_uhes(self, n: List[int]):
        self.data["codigos_uhes"][: self.numero_uhes] = n

    @property
    def numero_semanas_completas(self) -> int:
        return self.data["dados_caso"][0]

    @property
    def numero_dias_excluidos_estagio_apos_mes_inicial(self) -> int:
        return self.data["dados_caso"][1]

    @property
    def mes_inicial(self) -> int:
        return self.data["dados_caso"][2]

    @property
    def ano_mes_inicial(self) -> int:
        return self.data["dados_caso"][3]

    @property
    def numero_semanas_observadas(self) -> int:
        return self.data["dados_caso"][5]

    @property
    def numero_cenarios_estocasticos(self) -> int:
        return (
            sum(self.numero_aberturas_estagios) - self.numero_semanas_completas
        )

    @property
    def versao_modelo(self) -> int:
        return self.data["dados_caso"][5]

    @property
    def probabilidades_nos(self) -> List[float]:
        return self.data["dados_cenarios"][
            : sum(self.numero_aberturas_estagios)
        ]

    @probabilidades_nos.setter
    def probabilidades_nos(self, probs: List[float]):
        self.data["dados_cenarios"] = probs

    @property
    def previsoes(self) -> List[int]:
        return self.data["previsoes"]

    @previsoes.setter
    def previsoes(self, prevs: List[int]):
        self.data["previsoes"] = prevs

    @property
    def cenarios_gerados(self) -> List[int]:
        return self.data["cenarios_gerados"]

    @cenarios_gerados.setter
    def cenarios_gerados(self, cens: List[int]):
        self.data["cenarios_gerados"] = cens

    @property
    def previsoes_com_postos_artificiais(self) -> List[int]:
        return self.data["previsoes_com_postos_artificiais"]

    @previsoes_com_postos_artificiais.setter
    def previsoes_com_postos_artificiais(self, prevs: List[int]):
        self.data["previsoes_com_postos_artificiais"] = prevs

    @property
    def cenarios_calculados_com_postos_artificiais(self) -> List[int]:
        return self.data["cenarios_calculados_com_postos_artificiais"]

    @cenarios_calculados_com_postos_artificiais.setter
    def cenarios_calculados_com_postos_artificiais(self, cens: List[int]):
        self.data["cenarios_calculados_com_postos_artificiais"] = cens

    @property
    def observacoes_mensais(self) -> List[int]:
        return self.data["observacoes_mensais"]

    @observacoes_mensais.setter
    def observacoes_mensais(self, obs: List[int]):
        self.data["observacoes_mensais"] = obs

    @property
    def observacoes_semanais(self) -> List[int]:
        return self.data["observacoes_semanais"]

    @observacoes_semanais.setter
    def observacoes_semanais(self, obs: List[int]):
        self.data["observacoes_semanais"] = obs
