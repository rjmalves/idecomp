from idecomp.decomp.dec_eco_evap import DecEcoEvap

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_eco_evap import MockDecEcoEvap


def test_atributos_encontrados_dec_eco_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecEcoEvap))
    with patch("builtins.open", m):
        rel = DecEcoEvap.read("./tests/mocks/arquivos/dec_eco_evap.py")
        assert rel.versao == "32.1"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "codigo_usina"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert rel.tabela.at[0, "nome_submercado"] == "SE"
        assert rel.tabela.at[0, "codigo_ree"] == 10
        assert rel.tabela.at[0, "volume_referencia_hm3"] == 521.72
        assert rel.tabela.at[0, "evaporacao_referencia_hm3"] == 0.0
        assert rel.tabela.at[0, "coeficiente_evaporacao_mensal"] == 0
        assert rel.tabela.at[0, "considera_evaporacao"] == 1
        assert rel.tabela.at[0, "considera_evaporacao_linear"] == 1
        assert rel.tabela.at[0, "flag_tipo_volume_referencia"] == 0


def test_eq_dec_eco_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecEcoEvap))
    with patch("builtins.open", m):
        rel1 = DecEcoEvap.read("./tests/mocks/arquivos/dec_eco_evap.py")
        rel2 = DecEcoEvap.read("./tests/mocks/arquivos/dec_eco_evap.py")
        assert rel1 == rel2


def test_neq_dec_eco_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecEcoEvap))
    with patch("builtins.open", m):
        rel1 = DecEcoEvap.read("./tests/mocks/arquivos/dec_eco_evap.py")
        rel2 = DecEcoEvap.read("./tests/mocks/arquivos/dec_eco_evap.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
