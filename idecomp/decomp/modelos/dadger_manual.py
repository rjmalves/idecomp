"""
Leiaute dos registros do arquivo dadger segundo o Manual do Usuário do
DECOMP, versão 31 (outubro de 2021), e comparação de linhas do dadger como
o DECOMP as lê.

O DECOMP lê o dadger com o READ formatado do Fortran, em colunas fixas. Nos
campos numéricos os brancos são ignorados e, em um campo com casas decimais
implícitas escrito sem ponto, os últimos dígitos são a parte fracionária.
As colunas do manual são a referência para a leitura; as casas decimais de
formatos como F10.0 não limitam o que o deck pode conter.

As páginas citadas são as do PDF do manual.
"""

from typing import Literal, NamedTuple

from idecomp.decomp.modelos.campos.fortranfloatfield import FortranFloatField
from idecomp.decomp.modelos.campos.fortranintegerfield import (
    FortranIntegerField,
)


class CampoManual(NamedTuple):
    """
    Campo de um registro do dadger, nas colunas do manual do DECOMP.

    O ``tipo`` é "I" (inteiro), "F" (real) ou "A" (texto). As colunas
    ``coluna_inicial`` e ``coluna_final`` começam em 1 e incluem as
    extremidades. Em um campo real escrito sem ponto, os
    ``decimais_implicitos`` últimos dígitos são a parte fracionária.
    """

    tipo: Literal["I", "F", "A"]
    coluna_inicial: int
    coluna_final: int
    decimais_implicitos: int = 0

    def le(self, linha: str) -> int | float | str | None:
        """
        Lê o campo de uma linha do dadger como o DECOMP.

        Um campo numérico em branco ou inválido é lido como None. Em um
        campo de texto, os brancos à direita são descartados e os à
        esquerda são mantidos, como na comparação de textos do Fortran.

        :param linha: A linha do dadger.
        :type linha: str
        :return: O valor lido.
        :rtype: int | float | str | None
        """
        inicio = self.coluna_inicial - 1
        tamanho = self.coluna_final - inicio
        if self.tipo == "A":
            return linha[inicio : self.coluna_final].rstrip()
        if self.tipo == "I":
            return FortranIntegerField(tamanho, inicio).read(linha)
        return FortranFloatField(
            tamanho, inicio, implied_decimals=self.decimais_implicitos
        ).read(linha)


class DiferencaLeitura(NamedTuple):
    """
    Trecho de uma linha do dadger que o DECOMP lê de forma diferente em
    dois arquivos.

    O trecho do ``registro`` vai da ``coluna_inicial`` à
    ``coluna_final``, com o ``texto_original`` e o
    ``texto_modificado``. Em um campo, ``valor_original`` e
    ``valor_modificado`` são os valores lidos; em colunas fora dos campos
    ou em uma linha comparada como texto, são None.
    """

    registro: str
    coluna_inicial: int
    coluna_final: int
    texto_original: str
    texto_modificado: str
    valor_original: int | float | str | None
    valor_modificado: int | float | str | None


def _inteiro(inicio: int, fim: int) -> CampoManual:
    return CampoManual("I", inicio, fim)


def _real(inicio: int, fim: int, decimais: int = 0) -> CampoManual:
    return CampoManual("F", inicio, fim, decimais)


def _texto(inicio: int, fim: int) -> CampoManual:
    return CampoManual("A", inicio, fim)


def _repete(
    inicio: int, largura: int, quantidade: int, decimais: int = 0
) -> list[CampoManual]:
    return [
        _real(inicio + largura * k, inicio + largura * (k + 1) - 1, decimais)
        for k in range(quantidade)
    ]


def _patamares() -> list[CampoManual]:
    # Dois valores F5.0 e um custo F10.2 por patamar, em 20 colunas a partir
    # da coluna 30, para 5 patamares.
    campos = []
    for inicio in range(30, 130, 20):
        campos += [
            _real(inicio, inicio + 4),
            _real(inicio + 5, inicio + 9),
            _real(inicio + 10, inicio + 19, 2),
        ]
    return campos


def _contrato() -> list[CampoManual]:
    # O fator de perdas fica após o último patamar: nas colunas 130-134 com
    # 5 patamares e, com menos patamares, nas colunas do primeiro valor do
    # patamar seguinte, também F5.0.
    return (
        [_inteiro(5, 7), _inteiro(9, 10), _texto(12, 21), _inteiro(25, 26)]
        + _patamares()
        + [_real(130, 134)]
    )


# pp. 54-56. Usina, mnemônico do parâmetro, mês, semana e ano.
_AC_COMUNS = [
    _inteiro(5, 7),
    _texto(10, 15),
    _texto(70, 72),
    _inteiro(75, 75),
    _inteiro(77, 80),
]

# pp. 54-55. O manual dá a coluna inicial 20 e a lista de formatos de cada
# parâmetro; as colunas seguem os formatos a partir da coluna 20. Na
# leitura, o formato E15.8 equivale ao F15.8.
_AC_PARAMETROS: dict[str, list[CampoManual]] = {
    "NUMPOS": [_inteiro(20, 24)],
    "NUMJUS": [_inteiro(20, 24)],
    "NUMCON": [_inteiro(20, 24)],
    "VERTJU": [_inteiro(20, 24)],
    "VAZMIN": [_inteiro(20, 24)],
    "NUMBAS": [_inteiro(20, 24)],
    "TIPERH": [_inteiro(20, 24)],
    "JUSENA": [_inteiro(20, 24)],
    "DESVIO": [_inteiro(20, 24), _real(25, 34)],
    "VOLMIN": [_real(20, 29)],
    "VOLMAX": [_real(20, 29)],
    "PROESP": [_real(20, 29)],
    "PERHID": [_real(20, 29)],
    "JUSMED": [_real(20, 29)],
    "VSVERT": [_real(20, 29)],
    "VMDESV": [_real(20, 29)],
    "COTVOL": [_inteiro(20, 24), _real(25, 39, 8)],
    "COTARE": [_inteiro(20, 24), _real(25, 39, 8)],
    "COFEVA": [_inteiro(20, 24), _inteiro(25, 29)],
    "NUMMAQ": [_inteiro(20, 24), _inteiro(25, 29)],
    "VAZEFE": [_inteiro(20, 24), _inteiro(25, 29)],
    "POTEFE": [_inteiro(20, 24), _real(25, 34)],
    "ALTEFE": [_inteiro(20, 24), _real(25, 34)],
    "NCHAVE": [_inteiro(20, 24), _real(25, 34)],
    "COTVAZ": [_inteiro(20, 24), _inteiro(25, 29), _real(30, 44, 8)],
    # p. 56. O manual não dá o formato do valor, que está em EXTENSOES.
    "NPOSNW": [],
}

CAMPOS: dict[str, list[CampoManual]] = {
    # p. 26
    "TE": [_texto(5, 84)],
    # p. 27
    "TX": [_real(5, 9)],
    # p. 27
    "FA": [_texto(5, 54)],
    # p. 27
    "CS": [_inteiro(5, 5)],
    # p. 28
    "DT": [_inteiro(5, 6), _inteiro(10, 11), _inteiro(15, 18)],
    # p. 30. Com NEWCUT o nome é A60 (colunas 15-74); com os demais
    # mnemônicos, A200 (colunas 15-214). Fica o maior.
    "FC": [_texto(5, 10), _texto(15, 214)],
    # p. 31 (11F10.0, colunas 10-119)
    "EA": [_inteiro(5, 6)] + _repete(10, 10, 11),
    # pp. 31-32 (5F10.0, colunas 15-64)
    "ES": [_inteiro(5, 6), _inteiro(10, 10)] + _repete(15, 10, 5),
    # p. 33
    "AR": [_inteiro(6, 8), _real(12, 16), _real(18, 22)],
    # pp. 34-35. O código tem FORMATO I2, mas COLUNAS 5-7.
    "HE": [
        _inteiro(5, 7),
        _inteiro(10, 10),
        _real(15, 24),
        _inteiro(26, 27),
        _real(29, 38),
        _inteiro(40, 40),
        _inteiro(42, 42),
        _inteiro(44, 44),
        _texto(46, 105),
        _inteiro(107, 107),
    ],
    # pp. 35-36. O código tem FORMATO I2, mas COLUNAS 5-7.
    "CM": [_inteiro(5, 7), _inteiro(10, 12), _real(15, 24)],
    # p. 37
    "SB": [_inteiro(5, 6), _texto(10, 11)],
    # pp. 37-38 (5 patamares, com I->J e J->I em cada um)
    "IA": [_inteiro(5, 6), _texto(10, 11), _texto(15, 16), _inteiro(18, 18)]
    + _repete(20, 10, 10),
    # pp. 40-41 (5 patamares com 5 valores F7.0, colunas 17-191)
    "RI": [_inteiro(5, 7), _inteiro(9, 11), _inteiro(13, 15)]
    + _repete(17, 7, 25),
    # pp. 41-42 (5 patamares com carga e duração, colunas 20-119)
    "DP": [_inteiro(5, 6), _inteiro(10, 11)] + _repete(20, 10, 10),
    # pp. 42-43 (5 patamares)
    "CD": [
        _inteiro(5, 6),
        _inteiro(10, 11),
        _texto(15, 24),
        _inteiro(25, 26),
        _real(30, 34),
        _real(35, 44, 2),
        _real(45, 49),
        _real(50, 59, 2),
        _real(60, 64),
        _real(65, 74, 2),
        _real(75, 79),
        _real(80, 89, 2),
        _real(90, 94),
        _real(95, 104, 2),
    ],
    # pp. 44-46 (5 patamares, como no exemplo das pp. 45-46)
    "CI": _contrato(),
    # pp. 44-46 (mesma tabela do CI)
    "CE": _contrato(),
    # p. 46
    "RE": [_inteiro(5, 8), _inteiro(10, 11), _inteiro(15, 16)],
    # pp. 46-47 (5 patamares)
    "LU": [_inteiro(5, 8), _inteiro(10, 11)] + _repete(15, 10, 10),
    # p. 48
    "FU": [
        _inteiro(5, 8),
        _inteiro(10, 11),
        _inteiro(15, 17),
        _real(20, 29),
        _inteiro(31, 32),
    ],
    # pp. 48-49
    "FT": [
        _inteiro(5, 8),
        _inteiro(10, 11),
        _inteiro(15, 17),
        _inteiro(20, 21),
        _real(25, 34),
    ],
    # p. 49
    "FI": [
        _inteiro(5, 8),
        _inteiro(10, 11),
        _texto(15, 16),
        _texto(20, 21),
        _real(25, 34),
    ],
    # pp. 49-50
    "FE": [
        _inteiro(5, 8),
        _inteiro(10, 11),
        _inteiro(15, 17),
        _inteiro(20, 21),
        _real(25, 34),
    ],
    # pp. 50-51 (5 patamares e o fator de perdas). O exemplo do manual
    # com 5 patamares dá as colunas 55-59 e 60-64 aos dois últimos campos,
    # deixando 45-54 vazias; a regra da p. 51 e os exemplos com 1 e 3
    # patamares dão campos F5.0 contíguos, como aqui.
    "PQ": [_texto(5, 14), _inteiro(15, 16), _inteiro(20, 21)]
    + _repete(25, 5, 6),
    # p. 53
    "UH": [
        _inteiro(5, 7),
        _inteiro(10, 11),
        _real(15, 24),
        _real(25, 34),
        _inteiro(40, 40),
        _inteiro(45, 46),
        _real(50, 59),
        _real(60, 69),
        _inteiro(70, 70),
    ],
    # pp. 56-57
    "UE": [
        _inteiro(5, 7),
        _inteiro(10, 11),
        _texto(15, 26),
        _inteiro(30, 32),
        _inteiro(35, 37),
        _real(40, 49),
        _real(50, 59),
        _real(60, 69),
    ],
    # pp. 57-58
    "FP": [
        _inteiro(5, 7),
        _inteiro(10, 12),
        _inteiro(15, 15),
        _inteiro(17, 20),
        _real(22, 26),
        _real(28, 32),
        _inteiro(35, 35),
        _inteiro(37, 40),
        _real(42, 46),
        _real(48, 52),
        _real(55, 59),
        _real(61, 65),
        _real(67, 69),
    ],
    # pp. 58-59
    "FJ": [_texto(5, 16)],
    # p. 60
    "VL": [_inteiro(5, 8)]
    + [
        _real(11, 25),
        _real(27, 41),
        _real(43, 57),
        _real(59, 73),
        _real(75, 89),
        _real(91, 105),
    ],
    # pp. 60-61
    "VU": [_inteiro(5, 8), _inteiro(11, 14), _real(17, 31)],
    # p. 61
    "VA": [_inteiro(5, 8), _inteiro(11, 14), _real(17, 31)],
    # pp. 61-62
    "VI": [_inteiro(5, 7), _inteiro(10, 12)] + _repete(15, 5, 5),
    # p. 62
    "QI": [_inteiro(5, 7)] + _repete(10, 5, 5),
    # pp. 62-63
    "EV": [_inteiro(5, 5), _texto(10, 12)],
    # p. 63. O FORMATO é 24F5.0; as COLUNAS 10-94 dariam 17 valores.
    "TI": [_inteiro(5, 7)] + _repete(10, 5, 24),
    # p. 64
    "DA": [
        _inteiro(5, 7),
        _inteiro(10, 12),
        _inteiro(14, 15),
        _real(17, 22),
        _real(25, 28),
        _real(35, 44),
    ],
    # p. 65. O FORMATO é 24(F5.0); as COLUNAS 10-94 dariam 17 valores.
    "MP": [_inteiro(5, 7), _inteiro(8, 9)] + _repete(10, 5, 24),
    # p. 66. O FORMATO é 24(F5.0); as COLUNAS 10-94 dariam 17 valores.
    "FD": [_inteiro(5, 7), _inteiro(8, 9)] + _repete(10, 5, 24),
    # pp. 66-67. O FORMATO é 24F5.0; as COLUNAS 10-94 dariam 17 valores.
    "RQ": [_inteiro(5, 6)] + _repete(10, 5, 24),
    # p. 67. O FORMATO é 24(F5.0); as COLUNAS 10-94 dariam 17 valores.
    "VE": [_inteiro(5, 7)] + _repete(10, 5, 24),
    # p. 68
    "HA": [_inteiro(5, 7), _inteiro(10, 11), _inteiro(15, 16)],
    # p. 68
    "LA": [_inteiro(5, 7), _inteiro(10, 11), _real(15, 24), _real(25, 34)],
    # pp. 68-69
    "CA": [_inteiro(5, 7), _inteiro(10, 11), _inteiro(15, 17)],
    # p. 69
    "HQ": [_inteiro(5, 7), _inteiro(10, 11), _inteiro(15, 16)],
    # pp. 69-70 (5 patamares)
    "LQ": [_inteiro(5, 7), _inteiro(10, 11)] + _repete(15, 10, 10),
    # p. 70
    "CQ": [
        _inteiro(5, 7),
        _inteiro(10, 11),
        _inteiro(15, 17),
        _real(20, 29),
        _texto(35, 38),
    ],
    # p. 71
    "HV": [_inteiro(5, 7), _inteiro(10, 11), _inteiro(15, 16)],
    # pp. 71-72
    "LV": [_inteiro(5, 7), _inteiro(10, 11), _real(15, 24), _real(25, 34)],
    # p. 72
    "CV": [
        _inteiro(5, 7),
        _inteiro(10, 11),
        _inteiro(15, 17),
        _real(20, 29),
        _texto(35, 38),
    ],
    # p. 73
    "EZ": [_inteiro(5, 7), _real(10, 14)],
    # p. 74 (5 patamares)
    "CT": [_inteiro(5, 7), _inteiro(10, 11), _texto(15, 24), _inteiro(25, 26)]
    + _patamares(),
    # p. 75. O FORMATO é 24(F5.0); as COLUNAS 15-99 dariam 17 valores.
    "MT": [_inteiro(5, 7), _inteiro(10, 11)] + _repete(15, 5, 24),
    # pp. 75-76
    "GP": [_real(5, 14)],
    # p. 76
    "NI": [_inteiro(5, 7), _inteiro(9, 9)],
    # p. 76
    "PD": [_texto(5, 10)],
    # pp. 76-77
    "RT": [_texto(5, 10)],
    # p. 77. O campo tem COLUNAS 5 e FORMATO A6, mas é um flag inteiro.
    "PU": [_inteiro(5, 5)],
    # pp. 77-78. O campo 5 tem COLUNAS 25-30, mas FORMATO I5.
    "IR": [_texto(5, 11), _inteiro(15, 16), _inteiro(20, 21), _inteiro(25, 30)],
    # p. 79
    "RC": [_texto(5, 10)],
    # pp. 79-80
    "PE": [_inteiro(5, 6), _inteiro(8, 8), _real(10, 19)],
    # p. 82
    "TS": [_real(5, 21, 15), _real(23, 39, 15)],
    # pp. 82-83
    "PV": [_real(5, 24), _real(28, 47)],
    **{
        "AC" + parametro: _AC_COMUNS + campos
        for parametro, campos in _AC_PARAMETROS.items()
    },
}
"""
Campos de cada registro do dadger no manual do DECOMP. A chave é o
mnemônico do registro ou, nos registros AC, "AC" seguido do mnemônico do
parâmetro, como em "ACPOTEFE". O mnemônico das colunas 1-2 não é um campo.
"""

EXTENSOES: dict[str, list[CampoManual]] = {
    # Número de patamares.
    "DP": [_inteiro(15, 15)],
    # Configuração do NEWAVE.
    "UH": [_texto(72, 73)],
    # Tempos de viagem para mais 4 estágios.
    "VI": _repete(40, 5, 4),
    # Flag para zerar coeficientes e tolerância do teste de otimalidade.
    "TS": [_inteiro(43, 43), _real(47, 63, 15)],
    # Parâmetros de atualização das variáveis de folga.
    "PV": [_inteiro(51, 53), _real(57, 59), _real(63, 82), _real(86, 105)],
    # Código do posto.
    "ACNPOSNW": [_inteiro(20, 24)],
}
"""
Campos que a idecomp lê e o manual do DECOMP não documenta, com as mesmas
chaves de :data:`CAMPOS`.
"""


def _registro(linha: str) -> str:
    mnemonico = linha[:2]
    if mnemonico == "AC":
        return mnemonico + linha[9:15].strip()
    return mnemonico


def _invalido(campo: CampoManual, texto: str, valor: object) -> bool:
    return campo.tipo != "A" and valor is None and texto.strip() != ""


def _compara_texto(
    registro: str, original: str, modificada: str
) -> list[DiferencaLeitura]:
    original = original.rstrip()
    modificada = modificada.rstrip()
    if original == modificada:
        return []
    fim = max(len(original), len(modificada))
    return [
        DiferencaLeitura(registro, 1, fim, original, modificada, None, None)
    ]


def compara_linhas(original: str, modificada: str) -> list[DiferencaLeitura]:
    """
    Compara duas linhas do dadger como o DECOMP as lê.

    Duas linhas de comentário, iniciadas por "&", não têm diferenças. Nos
    registros de :data:`CAMPOS`, cada campo do manual e de
    :data:`EXTENSOES` é lido nas duas linhas e é diferente se os valores
    lidos forem diferentes, ou se os textos forem diferentes e um deles for
    um número inválido. As colunas fora dos campos são diferentes se os
    textos forem diferentes. Linhas de outros registros, ou de registros
    diferentes, são comparadas como texto, sem os brancos à direita.

    :param original: A linha do arquivo original.
    :type original: str
    :param modificada: A linha do arquivo modificado.
    :type modificada: str
    :return: As diferenças, em ordem de coluna.
    :rtype: list[DiferencaLeitura]
    """
    if original.startswith("&") and modificada.startswith("&"):
        return []
    registro = _registro(original)
    campos = CAMPOS.get(registro, []) + EXTENSOES.get(registro, [])
    if not campos or _registro(modificada) != registro:
        return _compara_texto(registro, original, modificada)
    largura = max(
        len(original), len(modificada), *[c.coluna_final for c in campos]
    )
    original = original.ljust(largura)
    modificada = modificada.ljust(largura)
    lidas = [True, True] + [False] * (largura - 2)
    diferencas = []
    for campo in campos:
        inicio = campo.coluna_inicial - 1
        fim = campo.coluna_final
        lidas[inicio:fim] = [True] * (fim - inicio)
        texto_original = original[inicio:fim]
        texto_modificado = modificada[inicio:fim]
        valor_original = campo.le(original)
        valor_modificado = campo.le(modificada)
        invalido = _invalido(campo, texto_original, valor_original) or (
            _invalido(campo, texto_modificado, valor_modificado)
        )
        if valor_original != valor_modificado or (
            invalido and texto_original != texto_modificado
        ):
            diferencas.append(
                DiferencaLeitura(
                    registro,
                    campo.coluna_inicial,
                    campo.coluna_final,
                    texto_original,
                    texto_modificado,
                    valor_original,
                    valor_modificado,
                )
            )
    inicio = 0
    while inicio < largura:
        if lidas[inicio]:
            inicio += 1
            continue
        fim = inicio
        while fim < largura and not lidas[fim]:
            fim += 1
        if original[inicio:fim] != modificada[inicio:fim]:
            diferencas.append(
                DiferencaLeitura(
                    registro,
                    inicio + 1,
                    fim,
                    original[inicio:fim],
                    modificada[inicio:fim],
                    None,
                    None,
                )
            )
        inicio = fim
    return sorted(diferencas, key=lambda d: d.coluna_inicial)
