from unittest.mock import MagicMock, patch

from idecomp.decomp.avl_turb_max import AvlTurbMax
from tests.mocks.arquivos.avl_turb_max import MockAvlTurbMax
from tests.mocks.mock_open import mock_open


def test_atributos_encontrados_avl_turb_max():
    m: MagicMock = mock_open(read_data="".join(MockAvlTurbMax))
    with patch("builtins.open", m):
        rel = AvlTurbMax.read("./tests/mocks/arquivos/avl_turb_max.py")
        assert rel.versao == "31.23"

        assert rel.tabela.at[0, "estagio"] == 0
        assert rel.tabela.at[0, "observacao"] == 0
        assert rel.tabela.at[0, "codigo_usina"] == 0
        assert rel.tabela.at[0, "nome_usina"] == 0
        assert rel.tabela.at[0, "volume_util_inicial_hm3"] == 0
        assert rel.tabela.at[0, "volume_util_final_hm3"] == 0
        assert rel.tabela.at[0, "vazao_turbinada"] == 0
        assert rel.tabela.at[0, "vazao_turbinada_maxima_pl"] == 0
        assert rel.tabela.at[0, "engolimento_maximo_priori"] == 0
        assert rel.tabela.at[0, "engolimento_maximo_posteriori"] == 0
        assert rel.tabela.at[0, "vazao_turbinada_maxima_gerador"] == 0
        assert rel.tabela.at[0, "altura_queda"] == 0
        assert rel.tabela.at[0, "altura_efetiva"] == 0
        assert rel.tabela.at[0, "altura_montante"] == 0
        assert rel.tabela.at[0, "altura_jusante"] == 0
        assert rel.tabela.at[0, "violacao_turbinamento"] == 0


def test_eq_avl_turb_max():
    m: MagicMock = mock_open(read_data="".join(MockAvlTurbMax))
    with patch("builtins.open", m):
        rel1 = AvlTurbMax.read("./tests/mocks/arquivos/avl_turb_max.py")
        rel2 = AvlTurbMax.read("./tests/mocks/arquivos/avl_turb_max.py")
        assert rel1 == rel2


def test_neq_avl_turb_max():
    m: MagicMock = mock_open(read_data="".join(MockAvlTurbMax))
    with patch("builtins.open", m):
        rel1 = AvlTurbMax.read("./tests/mocks/arquivos/avl_turb_max.py")
        rel2 = AvlTurbMax.read("./tests/mocks/arquivos/avl_turb_max.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
