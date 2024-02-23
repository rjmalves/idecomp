from idecomp.decomp.dec_avl_evap import DecAvlEvap

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_avl_evap import MockDecAvlEvap


def test_atributos_encontrados_dec_avl_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecAvlEvap))
    with patch("builtins.open", m):
        rel = DecAvlEvap.read("./tests/mocks/arquivos/dec_avl_evap.py")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "codigo_usina"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert rel.tabela.at[0, "codigo_submercado"] == 1
        assert rel.tabela.at[0, "codigo_ree"] == 10
        assert rel.tabela.at[0, "volume_armazenado_hm3"] == 120.0
        assert rel.tabela.at[0, "evaporacao_calculada_hm3"] == 0.0
        assert rel.tabela.at[0, "evaporacao_modelo_hm3"] == 0.0
        assert rel.tabela.at[0, "desvio_absoluto_hm3"] == 0.0
        assert rel.tabela.at[0, "desvio_percentual"] == 0.0


def test_eq_dec_avl_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecAvlEvap))
    with patch("builtins.open", m):
        rel1 = DecAvlEvap.read("./tests/mocks/arquivos/dec_avl_evap.py")
        rel2 = DecAvlEvap.read("./tests/mocks/arquivos/dec_avl_evap.py")
        assert rel1 == rel2


def test_neq_dec_avl_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecAvlEvap))
    with patch("builtins.open", m):
        rel1 = DecAvlEvap.read("./tests/mocks/arquivos/dec_avl_evap.py")
        rel2 = DecAvlEvap.read("./tests/mocks/arquivos/dec_avl_evap.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
