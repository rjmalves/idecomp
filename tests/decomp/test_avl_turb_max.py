from unittest.mock import MagicMock, patch

from idecomp.decomp.avl_turb_max import AvlTurbMax
from tests.mocks.arquivos.avl_turb_max import MockAvlTurbMax
from tests.mocks.mock_open import mock_open
import numpy as np  # type: ignore


def test_atributos_encontrados_avl_turb_max():
    m: MagicMock = mock_open(read_data="".join(MockAvlTurbMax))
    with patch("builtins.open", m):
        rel = AvlTurbMax.read("./tests/mocks/arquivos/avl_turb_max.py")

        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "observacao"] == ""
        assert rel.tabela.at[0, "codigo_usina"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert rel.tabela.at[0, "volume_util_inicial_hm3"] == 782.05
        assert rel.tabela.at[0, "volume_util_final_hm3"] == 792.00
        assert rel.tabela.at[0, "vazao_turbinada_m3s"] == 41.94
        assert rel.tabela.at[0, "vazao_turbinada_maxima_pl_m3s"] == 217.53
        assert rel.tabela.at[0, "engolimento_maximo_priori_m3s"] == 217.53
        assert rel.tabela.at[0, "engolimento_maximo_posteriori_m3s"] == 218.26
        assert rel.tabela.at[0, "vazao_turbinada_maxima_gerador_m3s"] == 244.72
        assert rel.tabela.at[0, "altura_queda"] == 27.15
        assert rel.tabela.at[0, "altura_efetiva"] == 24.60
        assert rel.tabela.at[0, "altura_montante"] == 912.94
        assert rel.tabela.at[0, "altura_jusante"] == 885.70
        assert np.isnan(rel.tabela.at[0, "violacao_turbinamento_m3s"])


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
