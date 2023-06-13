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
