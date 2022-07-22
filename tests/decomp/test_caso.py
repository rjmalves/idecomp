from idecomp.decomp.caso import Caso

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.caso import MockCaso


def test_atributos_encontrados_caso():
    m: MagicMock = mock_open(read_data="".join(MockCaso))
    with patch("builtins.open", m):
        rel = Caso.le_arquivo("")
        assert rel.arquivos is not None

def test_eq_caso():
    m: MagicMock = mock_open(read_data="".join(MockCaso))
    with patch("builtins.open", m):
        rel1 = Caso.le_arquivo("")
        rel2 = Caso.le_arquivo("")
        assert rel1 == rel2


def test_neq_caso():
    m: MagicMock = mock_open(read_data="".join(MockCaso))
    with patch("builtins.open", m):
        rel1 = Caso.le_arquivo("")
        rel2 = Caso.le_arquivo("")
        rel1.arquivos = "teste"
        assert rel1 != rel2
