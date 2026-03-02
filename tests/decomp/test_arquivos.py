from idecomp.decomp.arquivos import Arquivos

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.arquivos import MockArquivos


def test_atributos_encontrados_arquivos():
    m: MagicMock = mock_open(read_data="".join(MockArquivos))
    with patch("builtins.open", m):
        rel = Arquivos.read("./tests/mocks/arquivos/arquivos.py")
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
        rel1 = Arquivos.read("./tests/mocks/arquivos/arquivos.py")
        rel2 = Arquivos.read("./tests/mocks/arquivos/arquivos.py")
        assert rel1 == rel2


def test_neq_arquivos():
    m: MagicMock = mock_open(read_data="".join(MockArquivos))
    with patch("builtins.open", m):
        rel1 = Arquivos.read("./tests/mocks/arquivos/arquivos.py")
        rel2 = Arquivos.read("./tests/mocks/arquivos/arquivos.py")
        rel1.dadgnl = "teste"
        assert rel1 != rel2


def test_leitura_escrita_arquivos():
    m_leitura: MagicMock = mock_open(read_data="".join(MockArquivos))
    with patch("builtins.open", m_leitura):
        d1 = Arquivos.read("./tests/mocks/arquivos/arquivos.py")
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        d1.write("./tests/mocks/arquivos/arquivos.py")
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        d2 = Arquivos.read("./tests/mocks/arquivos/arquivos.py")
        assert d1 == d2
