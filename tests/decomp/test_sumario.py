from idecomp.decomp.relato import Relato

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.sumario import MockSumario


def test_atributos_encontrados_sumario():
    m: MagicMock = mock_open(read_data="".join(MockSumario))
    with patch("builtins.open", m):
        rel = Relato.read("./tests/mocks/arquivos/sumario.py")
        assert rel.cmo_medio_submercado is not None
        assert rel.geracao_termica_submercado is not None
        assert rel.energia_armazenada_ree is not None
        assert rel.energia_armazenada_submercado is not None


def test_atributos_nao_encontrados_sumario():
    m: MagicMock = mock_open(read_data="".join(""))
    with patch("builtins.open", m):
        rel = Relato.read("./tests/mocks/arquivos/sumario.py")
        assert rel.cmo_medio_submercado is None
        assert rel.geracao_termica_submercado is None
        assert rel.energia_armazenada_ree is None
        assert rel.energia_armazenada_submercado is None


def test_eq_sumario():
    m: MagicMock = mock_open(read_data="".join(MockSumario))
    with patch("builtins.open", m):
        rel1 = Relato.read("./tests/mocks/arquivos/sumario.py")
        rel2 = Relato.read("./tests/mocks/arquivos/sumario.py")
        assert rel1 == rel2


def test_neq_sumario():
    m: MagicMock = mock_open(read_data="".join(MockSumario))
    with patch("builtins.open", m):
        rel1 = Relato.read("./tests/mocks/arquivos/sumario.py")
        rel2 = Relato.read("./tests/mocks/arquivos/sumario.py")
        rel1.cmo_medio_submercado.iloc[0, 0] = 0
        assert rel1 != rel2
