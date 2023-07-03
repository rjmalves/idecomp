from cfinterface.components.section import Section
from typing import List, IO
import numpy as np  # type: ignore


class SecaoVazoesPostos(Section):
    """
    Registro com os dados associados às vazões dos postos.
    """

    TAMANHO_REGISTRO = 320

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, SecaoVazoesPostos):
            return False
        bloco: SecaoVazoesPostos = o
        if not all(
            [
                isinstance(self.data, list),
                isinstance(o.data, list),
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
        self.data = list(dados)

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
        self.data += list(dados)

    def __le_terceiro_registro(self, file: IO):
        dados_caso = np.frombuffer(
            file.read(SecaoVazoesPostos.TAMANHO_REGISTRO * 4),
            dtype=np.int32,
            count=SecaoVazoesPostos.TAMANHO_REGISTRO,
        )
        self.data += list(dados_caso)

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
        self.data += list(dados_cenarios)

    def __le_quinto_registro(self, file: IO):
        for _ in range(self.numero_semanas_completas):
            dados_cenarios = np.frombuffer(
                file.read(
                    SecaoVazoesPostos.TAMANHO_REGISTRO
                    * self.__numero_blocos_cenarios()
                    * 4
                ),
                dtype=np.int32,
                count=SecaoVazoesPostos.TAMANHO_REGISTRO
                * self.__numero_blocos_cenarios(),
            )
            self.data += list(dados_cenarios)

    def __le_sexto_registro(self, file: IO):
        for _ in range(self.numero_cenarios_estocasticos):
            dados_cenarios = np.frombuffer(
                file.read(
                    SecaoVazoesPostos.TAMANHO_REGISTRO
                    * self.__numero_blocos_cenarios()
                    * 4
                ),
                dtype=np.int32,
                count=SecaoVazoesPostos.TAMANHO_REGISTRO
                * self.__numero_blocos_cenarios(),
            )
            self.data += list(dados_cenarios)

    def __le_setimo_registro(self, file: IO):
        for _ in range(self.numero_semanas_completas):
            dados_cenarios = np.frombuffer(
                file.read(
                    SecaoVazoesPostos.TAMANHO_REGISTRO
                    * self.__numero_blocos_cenarios()
                    * 4
                ),
                dtype=np.int32,
                count=SecaoVazoesPostos.TAMANHO_REGISTRO
                * self.__numero_blocos_cenarios(),
            )
            self.data += list(dados_cenarios)

    def __le_oitavo_registro(self, file: IO):
        for _ in range(self.numero_cenarios_estocasticos):
            dados_cenarios = np.frombuffer(
                file.read(
                    SecaoVazoesPostos.TAMANHO_REGISTRO
                    * self.__numero_blocos_cenarios()
                    * 4
                ),
                dtype=np.int32,
                count=SecaoVazoesPostos.TAMANHO_REGISTRO
                * self.__numero_blocos_cenarios(),
            )
            self.data += list(dados_cenarios)

    def __le_nono_registro(self, file: IO):
        for _ in range(self.__numero_meses_observados()):
            dados_cenarios = np.frombuffer(
                file.read(
                    SecaoVazoesPostos.TAMANHO_REGISTRO
                    * self.__numero_blocos_cenarios()
                    * 4
                ),
                dtype=np.int32,
                count=SecaoVazoesPostos.TAMANHO_REGISTRO
                * self.__numero_blocos_cenarios(),
            )
            self.data += list(dados_cenarios)

    def __le_decimo_registro(self, file: IO):
        for _ in range(self.numero_semanas_observadas):
            dados_cenarios = np.frombuffer(
                file.read(
                    SecaoVazoesPostos.TAMANHO_REGISTRO
                    * self.__numero_blocos_cenarios()
                    * 4
                ),
                dtype=np.int32,
                count=SecaoVazoesPostos.TAMANHO_REGISTRO
                * self.__numero_blocos_cenarios(),
            )
            self.data += list(dados_cenarios)

    def __offset_primeiro_registro(self) -> int:
        return SecaoVazoesPostos.TAMANHO_REGISTRO

    def __offset_segundo_registro(self) -> int:
        return (
            self.__offset_primeiro_registro()
            + SecaoVazoesPostos.TAMANHO_REGISTRO
            * self.__numero_blocos_postos()
        )

    def __offset_terceiro_registro(self) -> int:
        return (
            self.__offset_segundo_registro()
            + SecaoVazoesPostos.TAMANHO_REGISTRO
        )

    def __offset_quarto_registro(self) -> int:
        return (
            self.__offset_terceiro_registro()
            + SecaoVazoesPostos.TAMANHO_REGISTRO
            * self.__numero_blocos_cenarios()
        )

    def __offset_quinto_registro(self) -> int:
        return (
            self.__offset_quarto_registro()
            + SecaoVazoesPostos.TAMANHO_REGISTRO
            * self.__numero_blocos_cenarios()
            * self.numero_semanas_completas
        )

    def __offset_sexto_registro(self) -> int:
        return (
            self.__offset_quinto_registro()
            + SecaoVazoesPostos.TAMANHO_REGISTRO
            * self.__numero_blocos_cenarios()
            * self.numero_cenarios_estocasticos
        )

    def __offset_setimo_registro(self) -> int:
        return (
            self.__offset_sexto_registro()
            + SecaoVazoesPostos.TAMANHO_REGISTRO
            * self.__numero_blocos_cenarios()
            * self.numero_semanas_completas
        )

    def __offset_oitavo_registro(self) -> int:
        return (
            self.__offset_setimo_registro()
            + SecaoVazoesPostos.TAMANHO_REGISTRO
            * self.__numero_blocos_cenarios()
            * self.numero_cenarios_estocasticos
        )

    def __offset_nono_registro(self) -> int:
        return (
            self.__offset_oitavo_registro()
            + SecaoVazoesPostos.TAMANHO_REGISTRO
            * self.__numero_blocos_cenarios()
            * self.__numero_meses_observados()
        )

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
        offset_fin = self.__offset_primeiro_registro()
        file.write(np.array(self.data[:offset_fin], dtype=np.int32).tobytes())

    def __escreve_segundo_registro(self, file: IO):
        offset_ini = self.__offset_primeiro_registro()
        offset_fin = self.__offset_segundo_registro()
        file.write(
            np.array(
                self.data[offset_ini:offset_fin], dtype=np.int32
            ).tobytes()
        )

    def __escreve_terceiro_registro(self, file: IO):
        offset_ini = self.__offset_segundo_registro()
        offset_fin = self.__offset_terceiro_registro()
        file.write(
            np.array(
                self.data[offset_ini:offset_fin], dtype=np.int32
            ).tobytes()
        )

    def __escreve_quarto_registro(self, file: IO):
        offset_ini = self.__offset_terceiro_registro()
        offset_fin = self.__offset_quarto_registro()
        file.write(
            np.array(
                self.data[offset_ini:offset_fin], dtype=np.float32
            ).tobytes()
        )

    def __escreve_quinto_registro(self, file: IO):
        offset_ini = self.__offset_quarto_registro()
        offset_fin = self.__offset_quinto_registro()
        file.write(
            np.array(
                self.data[offset_ini:offset_fin], dtype=np.int32
            ).tobytes()
        )

    def __escreve_sexto_registro(self, file: IO):
        offset_ini = self.__offset_quinto_registro()
        offset_fin = self.__offset_sexto_registro()
        file.write(
            np.array(
                self.data[offset_ini:offset_fin], dtype=np.int32
            ).tobytes()
        )

    def __escreve_setimo_registro(self, file: IO):
        offset_ini = self.__offset_sexto_registro()
        offset_fin = self.__offset_setimo_registro()
        file.write(
            np.array(
                self.data[offset_ini:offset_fin], dtype=np.int32
            ).tobytes()
        )

    def __escreve_oitavo_registro(self, file: IO):
        offset_ini = self.__offset_setimo_registro()
        offset_fin = self.__offset_oitavo_registro()
        file.write(
            np.array(
                self.data[offset_ini:offset_fin], dtype=np.int32
            ).tobytes()
        )

    def __escreve_nono_registro(self, file: IO):
        offset_ini = self.__offset_oitavo_registro()
        offset_fin = self.__offset_nono_registro()
        file.write(
            np.array(
                self.data[offset_ini:offset_fin], dtype=np.int32
            ).tobytes()
        )

    def __escreve_decimo_registro(self, file: IO):
        offset_ini = self.__offset_nono_registro()
        file.write(np.array(self.data[offset_ini:], dtype=np.int32).tobytes())

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

    def __numero_meses_observados(self) -> int:
        return 11

    @property
    def numero_uhes(self) -> int:
        return self.data[0]

    @property
    def numero_estagios(self) -> int:
        return self.data[1]

    @property
    def numero_aberturas_estagios(self) -> List[int]:
        return self.data[2 : 2 + self.numero_estagios]

    @property
    def numero_postos(self) -> int:
        return self.data[2 + self.numero_estagios]

    @property
    def codigos_uhes(self) -> List[int]:
        offset = self.__offset_primeiro_registro()
        return self.data[offset : offset + self.numero_uhes]

    @property
    def numero_semanas_completas(self) -> int:
        offset = self.__offset_segundo_registro()
        return self.data[offset]

    @property
    def numero_dias_excluidos_estagio_apos_mes_inicial(self) -> int:
        offset = self.__offset_segundo_registro() + 1
        return self.data[offset]

    @property
    def mes_inicial(self) -> int:
        offset = self.__offset_segundo_registro() + 2
        return self.data[offset]

    @property
    def ano_mes_inicial(self) -> int:
        offset = self.__offset_segundo_registro() + 3
        return self.data[offset]

    @property
    def numero_semanas_observadas(self) -> int:
        offset = self.__offset_segundo_registro() + 5
        return self.data[offset]

    @property
    def numero_cenarios_estocasticos(self) -> int:
        return (
            sum(self.numero_aberturas_estagios) - self.numero_semanas_completas
        )

    @property
    def versao_modelo(self) -> int:
        offset = self.__offset_segundo_registro() + 5
        return self.data[offset]

    @property
    def probabilidades_nos(self) -> List[float]:
        offset_ini = self.__offset_terceiro_registro()
        offset_fin = offset_ini + sum(self.numero_aberturas_estagios)
        return self.data[offset_ini:offset_fin]

    @probabilidades_nos.setter
    def probabilidades_nos(self, probs: List[float]):
        offset_ini = self.__offset_terceiro_registro()
        offset_fin = offset_ini + sum(self.numero_aberturas_estagios)
        self.data = self.data[:offset_ini] + probs + self.data[offset_fin:]

    @property
    def previsoes(self) -> List[int]:
        offset_ini = self.__offset_quarto_registro()
        offset_fin = self.__offset_quinto_registro()
        return self.data[offset_ini:offset_fin]

    @previsoes.setter
    def previsoes(self, prevs: List[int]):
        offset_ini = self.__offset_quarto_registro()
        offset_fin = self.__offset_quinto_registro()
        self.data = self.data[:offset_ini] + prevs + self.data[offset_fin:]

    @property
    def cenarios_gerados(self) -> List[int]:
        offset_ini = self.__offset_quinto_registro()
        offset_fin = self.__offset_sexto_registro()
        return self.data[offset_ini:offset_fin]

    @cenarios_gerados.setter
    def cenarios_gerados(self, cens: List[int]):
        offset_ini = self.__offset_quinto_registro()
        offset_fin = self.__offset_sexto_registro()
        self.data = self.data[:offset_ini] + cens + self.data[offset_fin:]

    @property
    def previsoes_com_postos_artificiais(self) -> List[int]:
        offset_ini = self.__offset_sexto_registro()
        offset_fin = self.__offset_setimo_registro()
        return self.data[offset_ini:offset_fin]

    @previsoes_com_postos_artificiais.setter
    def previsoes_com_postos_artificiais(self, prevs: List[int]):
        offset_ini = self.__offset_sexto_registro()
        offset_fin = self.__offset_setimo_registro()
        self.data = self.data[:offset_ini] + prevs + self.data[offset_fin:]

    @property
    def cenarios_calculados_com_postos_artificiais(self) -> List[int]:
        offset_ini = self.__offset_setimo_registro()
        offset_fin = self.__offset_oitavo_registro()
        return self.data[offset_ini:offset_fin]

    @cenarios_calculados_com_postos_artificiais.setter
    def cenarios_calculados_com_postos_artificiais(self, cens: List[int]):
        offset_ini = self.__offset_setimo_registro()
        offset_fin = self.__offset_oitavo_registro()
        self.data = self.data[:offset_ini] + cens + self.data[offset_fin:]

    @property
    def observacoes_mensais(self) -> List[int]:
        offset_ini = self.__offset_oitavo_registro()
        offset_fin = self.__offset_nono_registro()
        return self.data[offset_ini:offset_fin]

    @property
    def observacoes_semanais(self) -> List[int]:
        offset_ini = self.__offset_nono_registro()
        return self.data[offset_ini:]
