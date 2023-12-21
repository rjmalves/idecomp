# Rotinas de testes associadas ao arquivo decomp.tim do DECOMP
from idecomp.decomp.modelos.decomptim import (
    BlocoTemposEtapas,
)

from idecomp.decomp.decomptim import Decomptim

from datetime import timedelta
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.decomptim import MockBlocoTemposEtapas, MockDecompTim


def test_bloco_tempos_etapas():
    m: MagicMock = mock_open(read_data="".join(MockBlocoTemposEtapas))
    b = BlocoTemposEtapas()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 4
    assert b.data.shape[1] == 2
    assert b.data.iloc[0, 0] == "Leitura de Dados"
    assert b.data.iloc[0, 1] == timedelta(seconds=13)


def test_atributos_encontrados_decomptim():
    m: MagicMock = mock_open(read_data="".join(MockDecompTim))
    with patch("builtins.open", m):
        dt = Decomptim.read("./tests/mocks/arquivos/decomptim.py")
        assert dt.tempos_etapas is not None


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
