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
