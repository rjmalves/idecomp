from idecomp.decomp.arquivos import Arquivos

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.arquivos import MockArquivos


def test_atributos_encontrados_arquivos():
    m: MagicMock = mock_open(read_data="".join(MockArquivos))
    with patch("builtins.open", m):
        rel = Arquivos.le_arquivo("")
        assert rel.arquivos is not None
        assert rel.dadger is not None
        assert rel.vazoes is not None
        assert rel.hidr is not None
        assert rel.mlt is not None
        assert rel.perdas is not None
        assert rel.dadgnl is not None
        assert rel.caminho is not None

def test_eq_arquivos():
    m: MagicMock = mock_open(read_data="".join(MockArquivos))
    with patch("builtins.open", m):
        rel1 = Arquivos.le_arquivo("")
        rel2 = Arquivos.le_arquivo("")
        assert rel1 == rel2


def test_neq_arquivos():
    m: MagicMock = mock_open(read_data="".join(MockArquivos))
    with patch("builtins.open", m):
        rel1 = Arquivos.le_arquivo("")
        rel2 = Arquivos.le_arquivo("")
        rel1.dadgnl = "teste"
        assert rel1 != rel2
