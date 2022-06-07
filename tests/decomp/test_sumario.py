from idecomp.decomp.sumario import Sumario

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.sumario import MockSumario


def test_atributos_encontrados_sumario():
    m: MagicMock = mock_open(read_data="".join(MockSumario))
    with patch("builtins.open", m):
        rel = Sumario.le_arquivo("")
        assert rel.cmo_medio_subsistema is not None
        assert rel.geracao_termica_subsistema is not None
        assert rel.energia_armazenada_ree is not None
        assert rel.energia_armazenada_subsistema is not None


def test_atributos_nao_encontrados_sumario():
    m: MagicMock = mock_open(read_data="".join(""))
    with patch("builtins.open", m):
        rel = Sumario.le_arquivo("")
        assert rel.cmo_medio_subsistema is None
        assert rel.geracao_termica_subsistema is None
        assert rel.energia_armazenada_ree is None
        assert rel.energia_armazenada_subsistema is None


def test_eq_sumario():
    m: MagicMock = mock_open(read_data="".join(MockSumario))
    with patch("builtins.open", m):
        rel1 = Sumario.le_arquivo("")
        rel2 = Sumario.le_arquivo("")
        assert rel1 == rel2


def test_neq_sumario():
    m: MagicMock = mock_open(read_data="".join(MockSumario))
    with patch("builtins.open", m):
        rel1 = Sumario.le_arquivo("")
        rel2 = Sumario.le_arquivo("")
        rel1.cmo_medio_subsistema.iloc[0, 0] = 0
        assert rel1 != rel2
