from idecomp.decomp.dec_estatevap import DecEstatEvap

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_estatevap import MockDecEstatEvap


def test_atributos_encontrados_dec_estatevap():
    m: MagicMock = mock_open(read_data="".join(MockDecEstatEvap))
    with patch("builtins.open", m):
        rel = DecEstatEvap.read("./tests/mocks/arquivos/dec_estatevap.py")
        assert rel.versao == "32.1"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "numero_usinas_evaporacao"] == 167
        assert rel.tabela.at[0, "numero_usinas_total"] == 167
        assert rel.tabela.at[0, "evaporacao_modelo_hm3"] == 260.150
        assert rel.tabela.at[0, "evaporacao_calculada_hm3"] == 260.145
        assert rel.tabela.at[0, "desvio_absoluto_positivo_hm3"] == 0.003
        assert rel.tabela.at[0, "desvio_absoluto_negativo_hm3"] == 0.008
        assert rel.tabela.at[0, "desvio_absoluto_hm3"] == 0.010
        assert rel.tabela.at[0, "evaporacao_modelo_m3s"] == 430.143
        assert rel.tabela.at[0, "evaporacao_calculada_m3s"] == 430.134
        assert rel.tabela.at[0, "desvio_absoluto_positivo_m3s"] == 0.004
        assert rel.tabela.at[0, "desvio_absoluto_negativo_m3s"] == 0.013
        assert rel.tabela.at[0, "desvio_absoluto_m3s"] == 0.017
        assert rel.tabela.at[0, "desvio_percentual"] == 0.00


def test_eq_dec_estatevap():
    m: MagicMock = mock_open(read_data="".join(MockDecEstatEvap))
    with patch("builtins.open", m):
        rel1 = DecEstatEvap.read("./tests/mocks/arquivos/dec_estatevap.py")
        rel2 = DecEstatEvap.read("./tests/mocks/arquivos/dec_estatevap.py")
        assert rel1 == rel2


def test_neq_dec_estatevap():
    m: MagicMock = mock_open(read_data="".join(MockDecEstatEvap))
    with patch("builtins.open", m):
        rel1 = DecEstatEvap.read("./tests/mocks/arquivos/dec_estatevap.py")
        rel2 = DecEstatEvap.read("./tests/mocks/arquivos/dec_estatevap.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
