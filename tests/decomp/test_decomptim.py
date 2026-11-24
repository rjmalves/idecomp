# Rotinas de testes associadas ao arquivo decomp.tim do DECOMP
from idecomp.decomp.modelos.decomptim import (
    BlocoTemposEtapas,
)

from idecomp.decomp.decomptim import Decomptim

import re
from datetime import timedelta

import pytest

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.decomptim import (
    MockBlocoTemposEtapas,
    MockDecompTim,
    MockDecompTim3121,
    MockDecompTim3201,
    MockDecompTim32151,
    MockDecompTim32152,
)


def test_bloco_tempos_etapas():
    m: MagicMock = mock_open(read_data="".join(MockBlocoTemposEtapas))
    b = BlocoTemposEtapas()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape == (5, 2)
    assert b.data.iloc[0, 0] == "Leitura de Dados"
    assert b.data.iloc[0, 1] == timedelta(seconds=13)


def test_atributos_encontrados_decomptim():
    m: MagicMock = mock_open(read_data="".join(MockDecompTim))
    with patch("builtins.open", m):
        dt = Decomptim.read("./tests/mocks/arquivos/decomptim.py")
        assert dt.tempos_etapas is not None


def test_atributos_encontrados_decomptim_3121():
    m: MagicMock = mock_open(read_data="".join(MockDecompTim3121))
    with patch("builtins.open", m):
        dt = Decomptim.read("./tests/mocks/arquivos/decomptim.py")
        assert dt.tempos_etapas is not None


def test_atributos_encontrados_decomptim_3201():
    m: MagicMock = mock_open(read_data="".join(MockDecompTim3201))
    with patch("builtins.open", m):
        dt = Decomptim.read("./tests/mocks/arquivos/decomptim.py")
        assert dt.tempos_etapas is not None


def test_atributos_encontrados_decomptim_32151():
    m: MagicMock = mock_open(read_data="".join(MockDecompTim32151))
    with patch("builtins.open", m):
        dt = Decomptim.read("./tests/mocks/arquivos/decomptim.py")
        assert dt.tempos_etapas is not None


def test_atributos_encontrados_decomptim_32152():
    m: MagicMock = mock_open(read_data="".join(MockDecompTim32152))
    with patch("builtins.open", m):
        dt = Decomptim.read("./tests/mocks/arquivos/decomptim.py")
        assert dt.tempos_etapas is not None


ETAPAS = [
    "Leitura de Dados",
    "Convergencia",
    "Simulacao Final",
    "Impressao",
    "Tempo Total",
]

MOCKS_VERSOES = [
    pytest.param(MockDecompTim3121, [11, 495, 8, 0, 514], id="3121"),
    pytest.param(MockDecompTim3201, [19, 680, 9, 0, 708], id="3201"),
    pytest.param(MockDecompTim32151, [38, 256, 8, 229, 531], id="32151"),
    pytest.param(MockDecompTim32152, [32, 53, 13, 226, 324], id="32152"),
]


def le_decomptim(linhas: list[str]) -> Decomptim:
    m: MagicMock = mock_open(read_data="".join(linhas))
    with patch("builtins.open", m):
        return Decomptim.read("./tests/mocks/arquivos/decomptim.py")


@pytest.mark.parametrize("linhas, segundos", MOCKS_VERSOES)
def test_tempos_etapas_decomptim_versoes(linhas, segundos):
    tempos = le_decomptim(linhas).tempos_etapas
    assert tempos["Etapa"].tolist() == ETAPAS
    assert tempos["Tempo"].dt.total_seconds().tolist() == segundos


@pytest.mark.parametrize("linhas, segundos", MOCKS_VERSOES)
def test_soma_etapas_decomptim_versoes(linhas, segundos):
    tempo = le_decomptim(linhas).tempos_etapas["Tempo"]
    assert tempo.iloc[:4].sum() == tempo.iloc[4]


def indice_linha(linhas: list[str], padrao: str) -> int:
    return next(i for i, l in enumerate(linhas) if re.match(padrao, l))


TOTAIS_10_PRIMEIRAS_ITERACOES_3121 = [175, 7, 8, 9, 6, 8, 8, 7, 9, 10]


def test_tempos_etapas_decomptim_truncado_apos_iteracao():
    corte = indice_linha(MockDecompTim3121, r"^Iteracao\s+11\s")
    tempos = le_decomptim(MockDecompTim3121[:corte]).tempos_etapas
    assert tempos["Tempo"].dt.total_seconds().tolist() == [
        11,
        1 + sum(TOTAIS_10_PRIMEIRAS_ITERACOES_3121),
        0,
        0,
        0,
    ]


def test_tempos_etapas_decomptim_truncado_no_meio_da_iteracao():
    corte = indice_linha(MockDecompTim3121, r"^Iteracao\s+11\s") + 3
    tempos = le_decomptim(MockDecompTim3121[:corte]).tempos_etapas
    assert tempos["Tempo"].dt.total_seconds().tolist() == [
        11,
        1 + sum(TOTAIS_10_PRIMEIRAS_ITERACOES_3121),
        0,
        0,
        0,
    ]


def test_tempos_etapas_decomptim_truncado_no_meio_da_simulacao_final():
    corte = indice_linha(MockDecompTim32152, r"^Sim\. Final\s") + 3
    tempos = le_decomptim(MockDecompTim32152[:corte]).tempos_etapas
    assert tempos["Tempo"].dt.total_seconds().tolist() == [32, 53, 0, 0, 0]


def test_bloco_tempos_etapas_linha_sem_tempo():
    m: MagicMock = mock_open(read_data="Leitura de Dados:   sem tempo\n")
    b = BlocoTemposEtapas()
    with patch("builtins.open", m):
        with open("", "") as fp:
            with pytest.raises(ValueError, match="Leitura de Dados"):
                b.read(fp)


def test_atributos_nao_encontrados_decomptim():
    m: MagicMock = mock_open(read_data="".join(""))
    with patch("builtins.open", m):
        dt = Decomptim.read("./tests/mocks/arquivos/decomptim.py")
        assert dt.tempos_etapas is None


def test_eq_decomptim():
    m: MagicMock = mock_open(read_data="".join(MockDecompTim))
    with patch("builtins.open", m):
        dt1 = Decomptim.read("./tests/mocks/arquivos/decomptim.py")
        dt2 = Decomptim.read("./tests/mocks/arquivos/decomptim.py")
        assert dt1 == dt2


def test_neq_decomptim():
    m: MagicMock = mock_open(read_data="".join(MockDecompTim))
    with patch("builtins.open", m):
        dt1 = Decomptim.read("./tests/mocks/arquivos/decomptim.py")
        dt2 = Decomptim.read("./tests/mocks/arquivos/decomptim.py")
        dt1.tempos_etapas.iloc[0, 0] = "Leitura de Algo"
        assert dt1 != dt2


COLUNAS_ITERACOES = [
    "iteracao",
    "envio_variaveis",
    "descida_1a_parte",
    "descida_2a_parte",
    "retorno",
    "total",
]

ITERACOES_VERSOES = [
    pytest.param(MockDecompTim3121, 34, [1, 1, 5, 168, 1, 175], id="3121"),
    pytest.param(MockDecompTim3201, 38, [1, 1, 6, 22, 2, 31], id="3201"),
    pytest.param(MockDecompTim32151, 21, [1, 2, 2, 35, 3, 42], id="32151"),
    pytest.param(MockDecompTim32152, 4, [1, 1, 1, 7, 1, 10], id="32152"),
]

LINHAS_VERSOES = [
    pytest.param(MockDecompTim3121, id="3121"),
    pytest.param(MockDecompTim3201, id="3201"),
    pytest.param(MockDecompTim32151, id="32151"),
    pytest.param(MockDecompTim32152, id="32152"),
]

ENVIO_INICIAL = re.compile(r"^Envio de Variaveis:\s+(\d+)h\s*(\d+)min\s*(\d+)s")
TEMPO_CONVERGENCIA = re.compile(
    r"^\s+(\d+)\s+\S+\s+\S+\s+\S+\s+(\d+):(\d\d):(\d\d)\|"
)


def envio_inicial(linhas: list[str]) -> timedelta:
    ocorrencias = [
        m for linha in linhas if (m := ENVIO_INICIAL.match(linha)) is not None
    ]
    assert len(ocorrencias) == 1
    horas, minutos, segundos = map(int, ocorrencias[0].groups())
    return timedelta(hours=horas, minutes=minutos, seconds=segundos)


def tempos_referencia(linhas: list[str]) -> dict[int, timedelta]:
    referencia: dict[int, timedelta] = {}
    for linha in linhas:
        if (m := TEMPO_CONVERGENCIA.match(linha)) is not None:
            iteracao, horas, minutos, segundos = map(int, m.groups())
            referencia[iteracao] = timedelta(
                hours=horas, minutes=minutos, seconds=segundos
            )
    return referencia


@pytest.mark.parametrize("linhas, n_iteracoes, primeira", ITERACOES_VERSOES)
def test_tempos_iteracoes_decomptim_versoes(linhas, n_iteracoes, primeira):
    tempos = le_decomptim(linhas).tempos_iteracoes
    assert tempos.shape == (n_iteracoes, 6)
    assert tempos.columns.tolist() == COLUNAS_ITERACOES
    assert tempos["iteracao"].dtype.kind == "i"
    assert tempos["iteracao"].tolist() == list(range(1, n_iteracoes + 1))
    fases = tempos.iloc[0]
    assert [
        fases["iteracao"],
        *(fase.total_seconds() for fase in fases.iloc[1:]),
    ] == primeira


@pytest.mark.parametrize("linhas", LINHAS_VERSOES)
def test_fases_iteracoes_somam_total_decomptim_versoes(linhas):
    tempos = le_decomptim(linhas).tempos_iteracoes
    fases = tempos[COLUNAS_ITERACOES[1:5]].sum(axis=1)
    assert (fases == tempos["total"]).all()


@pytest.mark.parametrize("linhas", LINHAS_VERSOES)
def test_cruzamento_tempos_iteracoes_com_convergencia_decomptim(linhas):
    tempos = le_decomptim(linhas).tempos_iteracoes
    referencia = tempos_referencia(linhas)
    iteracoes = tempos["iteracao"].tolist()
    assert len(referencia) > 0
    assert len(referencia) == len(tempos)
    assert sorted(referencia) == iteracoes
    acumulado = envio_inicial(linhas) + tempos["total"].cumsum()
    for iteracao, tempo in zip(iteracoes, acumulado.tolist()):
        tolerancia = timedelta(seconds=1) * iteracao
        assert abs(tempo - referencia[iteracao]) <= tolerancia


def test_tempos_iteracoes_decomptim_truncado_antes_do_ultimo_total():
    corte = indice_linha(MockDecompTim3121, r"^Iteracao\s+34\s") + 4
    tempos = le_decomptim(MockDecompTim3121[:corte]).tempos_iteracoes
    assert len(tempos) == 33
    assert tempos["iteracao"].iloc[-1] == 33


def test_tempos_iteracoes_decomptim_fase_ausente_vale_zero():
    linhas = [
        "RELATORIO DE CONVERGENCIA DO PROCESSO ITERATIVO\n",
        "Iteracao   1 - Envio de Variaveis: 000h 00min 01s\n",
        "               Descida 1a Parte:   000h 00min 05s\n",
        "               Total:              000h 00min 06s\n",
    ]
    tempos = le_decomptim(linhas).tempos_iteracoes
    assert tempos.shape == (1, 6)
    assert tempos["descida_2a_parte"].iloc[0] == timedelta(0)
    assert tempos["retorno"].iloc[0] == timedelta(0)


@pytest.mark.parametrize(
    "linha, campo",
    [
        ("Iteracao   1 - Envio de Variaveis: sem tempo\n", "Envio"),
        ("               Descida 1a Parte:   sem tempo\n", "Descida 1a"),
        ("               Descida 2a Parte:   sem tempo\n", "Descida 2a"),
        ("               Retorno:            sem tempo\n", "Retorno"),
    ],
)
def test_bloco_tempos_etapas_fase_iteracao_sem_tempo(linha, campo):
    abertura = "Iteracao   1 - Envio de Variaveis: 000h 00min 01s\n"
    dados = linha if linha.startswith("Iteracao") else abertura + linha
    m: MagicMock = mock_open(read_data=dados)
    b = BlocoTemposEtapas()
    with patch("builtins.open", m):
        with open("", "") as fp:
            with pytest.raises(ValueError, match=campo):
                b.read(fp)


def test_tempos_iteracoes_nao_encontrados_decomptim():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        dt = Decomptim.read("./tests/mocks/arquivos/decomptim.py")
        assert dt.tempos_iteracoes is None


def test_neq_decomptim_tempos_iteracoes():
    dt1 = le_decomptim(MockDecompTim3121)
    dt2 = le_decomptim(MockDecompTim3121)
    assert dt1 == dt2
    dt1.tempos_iteracoes.iloc[0, 1] = timedelta(seconds=99)
    assert dt1 != dt2
