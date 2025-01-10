from idecomp.decomp.dec_estatfpha import DecEstatFpha
from idecomp.decomp.modelos.dec_estatfpha import (
    BlocoDesvios,
)

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_estatfpha import (
    MockDecEstatFpha,
    MockBlocoDesvios,
)


def test_atributos_encontrados_dec_estatfpha():
    m: MagicMock = mock_open(read_data="".join(MockDecEstatFpha))
    with patch("builtins.open", m):
        rel = DecEstatFpha.read("./tests/mocks/arquivos/dec_estatfpha.py")
        assert rel.versao == "32.1"
        assert rel.estatisticas_desvios is not None


def test_eq_dec_estatfpha():
    m: MagicMock = mock_open(read_data="".join(MockDecEstatFpha))
    with patch("builtins.open", m):
        rel1 = DecEstatFpha.read("./tests/mocks/arquivos/dec_estatfpha.py")
        rel2 = DecEstatFpha.read("./tests/mocks/arquivos/dec_estatfpha.py")
        assert rel1 == rel2


def test_eq_blocodesvios():
    m: MagicMock = mock_open(read_data="".join(MockBlocoDesvios))
    b1 = BlocoDesvios()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoDesvios()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    assert b1 == b2


def test_neq_blocodesvios():
    m: MagicMock = mock_open(read_data="".join(MockBlocoDesvios))
    b1 = BlocoDesvios()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b1.read(fp)
    b2 = BlocoDesvios()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b2.read(fp)
    b1.data.iloc[0, 0] = -1
    assert b1 != b2


def test_blocodesvios():
    m: MagicMock = mock_open(read_data="".join(MockBlocoDesvios))
    bloco = BlocoDesvios()
    with patch("builtins.open", m):
        with open("", "") as fp:
            bloco.read(fp)

        assert bloco.data.at[0, "valor"] == 2.37
        assert bloco.data.at[1, "valor"] == 0.64
        assert bloco.data.at[2, "valor"] == 1.08
        assert bloco.data.at[3, "valor"] == 1.29
        assert bloco.data.at[4, "valor"] == 0.29
        assert bloco.data.at[5, "valor"] == 0.35
        assert bloco.data.at[6, "valor"] == 1.71
        assert bloco.data.at[7, "valor"] == 0.66
        assert bloco.data.at[8, "valor"] == 0.95
        assert bloco.data.at[9, "valor"] == 0.35
        assert bloco.data.at[10, "valor"] == 77.3
        assert bloco.data.at[11, "valor"] == 3454.3
        assert bloco.data.at[12, "valor"] == 2461.2
        assert bloco.data.at[13, "valor"] == 11816.8
