from idecomp.decomp.dec_cortes_evap import DecCortesEvap

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_cortes_evap import MockDecCortesEvap


def test_atributos_encontrados_dec_cortes_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecCortesEvap))
    with patch("builtins.open", m):
        rel = DecCortesEvap.le_arquivo("")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "periodo"] == 1
        assert rel.tabela.at[0, "indice_usina"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert rel.tabela.at[0, "submercado"] == 1
        assert rel.tabela.at[0, "ree"] == 10
        assert rel.tabela.at[0, "derivada_cota_area"] == 3.3046855042
        assert rel.tabela.at[0, "derivada_volume_cota"] == 0.0364387763
        assert rel.tabela.at[0, "volume_referencia_hm3"] == 151.58
        assert rel.tabela.at[0, "evaporacao_referencia_hm3"] == 0.0
        assert rel.tabela.at[0, "coeficiente_volume"] == 0.0
        assert rel.tabela.at[0, "rhs_volume"] == 0.0


def test_eq_dec_cortes_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecCortesEvap))
    with patch("builtins.open", m):
        rel1 = DecCortesEvap.le_arquivo("")
        rel2 = DecCortesEvap.le_arquivo("")
        assert rel1 == rel2


def test_neq_dec_cortes_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecCortesEvap))
    with patch("builtins.open", m):
        rel1 = DecCortesEvap.le_arquivo("")
        rel2 = DecCortesEvap.le_arquivo("")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
