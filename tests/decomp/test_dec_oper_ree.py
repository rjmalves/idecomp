from idecomp.decomp.dec_oper_ree import DecOperRee

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_oper_ree import MockDecOperRee


def test_atributos_encontrados_dec_oper_ree():
    m: MagicMock = mock_open(read_data="".join(MockDecOperRee))
    with patch("builtins.open", m):
        rel = DecOperRee.le_arquivo("")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "periodo"] == 1
        assert rel.tabela.at[0, "no"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "indiceRee"] == 1
        assert rel.tabela.at[0, "nomeRee"] == "SUDESTE"
        assert rel.tabela.at[0, "indiceSubmercado"] == 1
        assert rel.tabela.at[0, "enaMWmes"] == 1667.5
        assert rel.tabela.at[0, "earmInicialMWmes"] == 10387.50
        assert rel.tabela.at[0, "earmInicialPercentual"] == 20.65
        assert rel.tabela.at[0, "earmFinalMWmes"] == 10956.67
        assert rel.tabela.at[0, "earmFinalPercentual"] == 21.78
        assert rel.tabela.at[0, "earmMaximoMWmes"] == 50314.5


def test_eq_dec_oper_ree():
    m: MagicMock = mock_open(read_data="".join(MockDecOperRee))
    with patch("builtins.open", m):
        rel1 = DecOperRee.le_arquivo("")
        rel2 = DecOperRee.le_arquivo("")
        assert rel1 == rel2


def test_neq_dec_oper_ree():
    m: MagicMock = mock_open(read_data="".join(MockDecOperRee))
    with patch("builtins.open", m):
        rel1 = DecOperRee.le_arquivo("")
        rel2 = DecOperRee.le_arquivo("")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
