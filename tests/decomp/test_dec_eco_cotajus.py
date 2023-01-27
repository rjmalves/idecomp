from idecomp.decomp.dec_eco_cotajus import DecEcoCotajus

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_eco_cotajus import MockDecEcoCotajus


def test_atributos_encontrados_dec_eco_cotajus():
    m: MagicMock = mock_open(read_data="".join(MockDecEcoCotajus))
    with patch("builtins.open", m):
        rel = DecEcoCotajus.le_arquivo("")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "indiceUsina"] == 1
        assert rel.tabela.at[0, "nomeUsina"] == "CAMARGOS"
        assert rel.tabela.at[0, "indiceCurvaJusante"] == 1
        assert rel.tabela.at[0, "alturaReferenciaUsinaJusante"] == 885.64
        assert rel.tabela.at[0, "indicePolinomio"] == 1
        assert rel.tabela.at[0, "vazaoMinima"] == 0.0
        assert rel.tabela.at[0, "vazaoMaxima"] == 395.10
        assert rel.tabela.at[0, "a0"] == 885.6394760382399908849038184
        assert rel.tabela.at[0, "a1"] == -0.0000000000000000038297685
        assert rel.tabela.at[0, "a2"] == 0.000012196974728550999254
        assert rel.tabela.at[0, "a3"] == -0.0000000097634321335944003
        assert rel.tabela.at[0, "a4"] == 0.0000000000000000000000000


def test_eq_dec_eco_cotajus():
    m: MagicMock = mock_open(read_data="".join(MockDecEcoCotajus))
    with patch("builtins.open", m):
        rel1 = DecEcoCotajus.le_arquivo("")
        rel2 = DecEcoCotajus.le_arquivo("")
        assert rel1 == rel2


def test_neq_dec_eco_cotajus():
    m: MagicMock = mock_open(read_data="".join(MockDecEcoCotajus))
    with patch("builtins.open", m):
        rel1 = DecEcoCotajus.le_arquivo("")
        rel2 = DecEcoCotajus.le_arquivo("")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
