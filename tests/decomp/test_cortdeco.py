from idecomp.decomp.cortdeco import Cortdeco
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch
import pytest
import pandas as pd

ARQ_TESTE = "./tests/mocks/arquivos/cortdeco.rv2"

TAMANHO_CORTE = 26976
UHES_CORTE = [
    1,
    2,
    4,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    14,
    15,
    16,
    17,
    18,
    20,
    21,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    37,
    38,
    39,
    40,
    42,
    43,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    57,
    61,
    62,
    63,
    66,
    71,
    72,
    73,
    74,
    76,
    77,
    78,
    82,
    83,
    86,
    88,
    89,
    90,
    91,
    92,
    93,
    94,
    95,
    97,
    98,
    99,
    101,
    102,
    103,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    117,
    118,
    119,
    120,
    121,
    122,
    123,
    124,
    125,
    126,
    127,
    129,
    130,
    131,
    133,
    134,
    135,
    139,
    141,
    143,
    144,
    145,
    146,
    147,
    148,
    153,
    154,
    155,
    156,
    162,
    169,
    172,
    173,
    174,
    175,
    178,
    180,
    181,
    182,
    185,
    189,
    190,
    192,
    193,
    195,
    196,
    203,
    204,
    215,
    217,
    227,
    228,
    229,
    230,
    241,
    249,
    251,
    252,
    253,
    257,
    261,
    262,
    267,
    272,
    275,
    276,
    277,
    278,
    279,
    280,
    281,
    283,
    284,
    285,
    286,
    287,
    288,
    290,
    304,
    305,
    310,
    311,
    312,
    314,
    315,
]

UHES_TVIAGEM_CORTE = [156, 162]
SUBMERCADOS_CORTE = [1, 3]
REGISTRO_ULTIMO_CORTE_NO = pd.DataFrame(
    data={
        "no": [1, 2, 3, 4],
        "estagio": [1, 2, 3, 4],
        "indice_ultimo_corte": [63, 62, 61, 0],
    }
)


def test_atributos_encontrados_cortdeco():
    h = Cortdeco.read(
        ARQ_TESTE,
        tamanho_registro=TAMANHO_CORTE,
        registro_ultimo_corte_no=REGISTRO_ULTIMO_CORTE_NO,
        numero_total_cortes=21,
        numero_patamares=3,
        numero_estagios=4,
        codigos_uhes=UHES_CORTE,
        codigos_uhes_tempo_viagem=UHES_TVIAGEM_CORTE,
        codigos_submercados=SUBMERCADOS_CORTE,
        lag_maximo_tempo_viagem=3,
    )
    assert isinstance(h.cortes, pd.DataFrame)


def test_eq_cortes():
    h1 = Cortdeco.read(
        ARQ_TESTE,
        tamanho_registro=TAMANHO_CORTE,
        registro_ultimo_corte_no=REGISTRO_ULTIMO_CORTE_NO,
        numero_total_cortes=21,
        numero_patamares=3,
        numero_estagios=4,
        codigos_uhes=UHES_CORTE,
        codigos_uhes_tempo_viagem=UHES_TVIAGEM_CORTE,
        codigos_submercados=SUBMERCADOS_CORTE,
        lag_maximo_tempo_viagem=3,
    )
    h2 = Cortdeco.read(
        ARQ_TESTE,
        tamanho_registro=TAMANHO_CORTE,
        registro_ultimo_corte_no=REGISTRO_ULTIMO_CORTE_NO,
        numero_total_cortes=21,
        numero_patamares=3,
        numero_estagios=4,
        codigos_uhes=UHES_CORTE,
        codigos_uhes_tempo_viagem=UHES_TVIAGEM_CORTE,
        codigos_submercados=SUBMERCADOS_CORTE,
        lag_maximo_tempo_viagem=3,
    )

    assert h1 == h2
    assert h1.cortes.equals(h2.cortes)


def test_neq_cortes():
    h1 = Cortdeco.read(
        ARQ_TESTE,
        tamanho_registro=TAMANHO_CORTE,
        registro_ultimo_corte_no=REGISTRO_ULTIMO_CORTE_NO,
        numero_total_cortes=21,
        numero_patamares=3,
        numero_estagios=4,
        codigos_uhes=UHES_CORTE,
        codigos_uhes_tempo_viagem=UHES_TVIAGEM_CORTE,
        codigos_submercados=SUBMERCADOS_CORTE,
        lag_maximo_tempo_viagem=3,
    )
    h2 = Cortdeco.read(
        ARQ_TESTE,
        tamanho_registro=TAMANHO_CORTE,
        registro_ultimo_corte_no=REGISTRO_ULTIMO_CORTE_NO,
        numero_total_cortes=21,
        numero_patamares=3,
        numero_estagios=4,
        codigos_uhes=UHES_CORTE,
        codigos_uhes_tempo_viagem=UHES_TVIAGEM_CORTE,
        codigos_submercados=SUBMERCADOS_CORTE,
        lag_maximo_tempo_viagem=3,
    )
    df = h2.cortes
    df.at[0, "rhs"] = -1.0
    h2.cortes = df
    assert h1 != h2


def test_atributos_cortes():
    h = Cortdeco.read(
        ARQ_TESTE,
        tamanho_registro=TAMANHO_CORTE,
        registro_ultimo_corte_no=REGISTRO_ULTIMO_CORTE_NO,
        numero_total_cortes=21,
        numero_patamares=3,
        numero_estagios=4,
        codigos_uhes=UHES_CORTE,
        codigos_uhes_tempo_viagem=UHES_TVIAGEM_CORTE,
        codigos_submercados=SUBMERCADOS_CORTE,
        lag_maximo_tempo_viagem=3,
    )
    # TODO - usar np.allclose
    assert h.cortes.at[0, "indice_corte"] == 1
    assert h.cortes.at[0, "no"] == 1
    assert h.cortes.at[0, "estagio"] == 1
    assert h.cortes.at[0, "rhs"] == 392918510283.4334717
    assert h.cortes.at[0, "pi_varm_uhe1"] == -108.13001990261628
    assert h.cortes.at[0, "pi_qdefp_uhe156_lag0"] == -1679.1694642265875
    assert h.cortes.at[0, "pi_gnl_sbm1_pat1_lag1"] == 59.92984473788813


def test_atributos_coeficientes():
    h = Cortdeco.read(
        ARQ_TESTE,
        tamanho_registro=TAMANHO_CORTE,
        registro_ultimo_corte_no=REGISTRO_ULTIMO_CORTE_NO,
        numero_total_cortes=21,
        numero_patamares=3,
        numero_estagios=4,
        codigos_uhes=UHES_CORTE,
        codigos_uhes_tempo_viagem=UHES_TVIAGEM_CORTE,
        codigos_submercados=SUBMERCADOS_CORTE,
        lag_maximo_tempo_viagem=3,
    )
    assert h.coeficientes_volume_armazenado.at[0, "indice_corte"] == 1
    assert h.coeficientes_volume_armazenado.at[0, "no"] == 1
    assert h.coeficientes_volume_armazenado.at[0, "estagio"] == 1
    assert h.coeficientes_volume_armazenado.at[0, "codigo_usina"] == 1
    assert (
        h.coeficientes_volume_armazenado.at[0, "valor"] == -108.13001990261628
    )
    assert h.coeficientes_defluencia_tempo_viagem.at[0, "indice_corte"] == 1
    assert h.coeficientes_defluencia_tempo_viagem.at[0, "codigo_usina"] == 156
    assert h.coeficientes_defluencia_tempo_viagem.at[0, "lag"] == 0
    assert (
        h.coeficientes_defluencia_tempo_viagem.at[0, "valor"]
        == -1679.1694642265875
    )
    assert h.coeficientes_geracao_gnl.at[0, "indice_corte"] == 1
    assert h.coeficientes_geracao_gnl.at[0, "codigo_submercado"] == 1
    assert h.coeficientes_geracao_gnl.at[0, "lag"] == 1
    assert h.coeficientes_geracao_gnl.at[0, "valor"] == 59.92984473788813


def test_leitura_escrita_cortdeco():
    h1 = Cortdeco.read(
        ARQ_TESTE,
        tamanho_registro=TAMANHO_CORTE,
        registro_ultimo_corte_no=REGISTRO_ULTIMO_CORTE_NO,
        numero_total_cortes=21,
        numero_patamares=3,
        numero_estagios=4,
        codigos_uhes=UHES_CORTE,
        codigos_uhes_tempo_viagem=UHES_TVIAGEM_CORTE,
        codigos_submercados=SUBMERCADOS_CORTE,
        lag_maximo_tempo_viagem=3,
    )
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        h1.write(
            ARQ_TESTE, df_registro_ultimo_corte_no=REGISTRO_ULTIMO_CORTE_NO
        )
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data=b"".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        h2 = Cortdeco.read(
            ARQ_TESTE,
            tamanho_registro=TAMANHO_CORTE,
            registro_ultimo_corte_no=REGISTRO_ULTIMO_CORTE_NO,
            numero_total_cortes=21,
            numero_patamares=3,
            numero_estagios=4,
            codigos_uhes=UHES_CORTE,
            codigos_uhes_tempo_viagem=UHES_TVIAGEM_CORTE,
            codigos_submercados=SUBMERCADOS_CORTE,
            lag_maximo_tempo_viagem=3,
        )
        assert h1 == h2
