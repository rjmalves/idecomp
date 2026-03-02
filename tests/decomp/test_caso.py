from idecomp.decomp.caso import Caso

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.caso import MockCaso


def test_atributos_encontrados_caso():
    m: MagicMock = mock_open(read_data="".join(MockCaso))
    with patch("builtins.open", m):
        rel = Caso.read("./tests/mocks/arquivos/caso.py")
        assert rel.arquivos is not None


def test_eq_caso():
    m: MagicMock = mock_open(read_data="".join(MockCaso))
    with patch("builtins.open", m):
        rel1 = Caso.read("./tests/mocks/arquivos/caso.py")
        rel2 = Caso.read("./tests/mocks/arquivos/caso.py")
        assert rel1 == rel2


def test_neq_caso():
    m: MagicMock = mock_open(read_data="".join(MockCaso))
    with patch("builtins.open", m):
        rel1 = Caso.read("./tests/mocks/arquivos/caso.py")
        rel2 = Caso.read("./tests/mocks/arquivos/caso.py")
        rel1.arquivos = "teste"
        assert rel1 != rel2


def test_leitura_escrita_caso():
    m_leitura: MagicMock = mock_open(read_data="".join(MockCaso))
    with patch("builtins.open", m_leitura):
        d1 = Caso.read("./tests/mocks/arquivos/caso.py")
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        d1.write("./tests/mocks/arquivos/caso.py")
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        d2 = Caso.read("./tests/mocks/arquivos/caso.py")
        assert d1 == d2
