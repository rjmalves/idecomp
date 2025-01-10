from idecomp.decomp.eco_fpha import EcoFpha

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.eco_fpha import MockEcoFpha


def test_atributos_encontrados_eco_fpha():
    m: MagicMock = mock_open(read_data="".join(MockEcoFpha))
    with patch("builtins.open", m):
        rel = EcoFpha.read("./tests/mocks/arquivos/eco_fpha.py")
        assert rel.versao == "32.1"
        assert rel.tabela.at[0, "codigo_usina"] == 1
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert rel.tabela.at[0, "tipo"] == 2
        assert rel.tabela.at[0, "conv"] == 1
        assert rel.tabela.at[0, "alfa"] == 1
        assert rel.tabela.at[0, "rems"] == 1
        assert rel.tabela.at[0, "numero_pontos_vazao_turbinada"] == 5
        assert rel.tabela.at[0, "vazao_turbinada_minima"] == 0.0
        assert rel.tabela.at[0, "vazao_turbinada_maxima"] == 210.7
        assert rel.tabela.at[0, "numero_pontos_volume_armazenado"] == 5
        assert rel.tabela.at[0, "volume_armazenado_minimo"] == 387.3
        assert rel.tabela.at[0, "volume_armazenado_maximo"] == 656.1
        assert rel.tabela.at[0, "geracao_minima"] == 0.0
        assert rel.tabela.at[0, "geracao_maxima"] == 46.0


def test_eq_eco_fpha():
    m: MagicMock = mock_open(read_data="".join(MockEcoFpha))
    with patch("builtins.open", m):
        rel1 = EcoFpha.read("./tests/mocks/arquivos/eco_fpha.py")
        rel2 = EcoFpha.read("./tests/mocks/arquivos/eco_fpha.py")
        assert rel1 == rel2


def test_neq_eco_fpha():
    m: MagicMock = mock_open(read_data="".join(MockEcoFpha))
    with patch("builtins.open", m):
        rel1 = EcoFpha.read("./tests/mocks/arquivos/eco_fpha.py")
        rel2 = EcoFpha.read("./tests/mocks/arquivos/eco_fpha.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
