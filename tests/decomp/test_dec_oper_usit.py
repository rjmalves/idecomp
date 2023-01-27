from idecomp.decomp.dec_oper_usit import DecOperUsit

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_oper_usit import MockDecOperUsit


def test_atributos_encontrados_dec_oper_usit():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsit))
    with patch("builtins.open", m):
        rel = DecOperUsit.le_arquivo("")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "periodo"] == 1
        assert rel.tabela.at[0, "no"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "duracao"] == 40.00
        assert rel.tabela.at[0, "indiceUsina"] == 86
        assert rel.tabela.at[0, "nomeUsina"] == "SANTA CRUZ"
        assert rel.tabela.at[0, "indiceSubmercado"] == 1
        assert rel.tabela.at[0, "nomeSubmercado"] == "SE"
        assert rel.tabela.at[0, "custoIncremental"] == 116.57
        assert rel.tabela.at[0, "geracaoMinimaMW"] == 0.0
        assert rel.tabela.at[0, "geracaoMW"] == 350.00
        assert rel.tabela.at[0, "fatorManutencao"] == 1.0
        assert rel.tabela.at[0, "geracaoMaximaMW"] == 350.00
        assert rel.tabela.at[0, "custoGeracao"] == 1631.98


def test_eq_dec_oper_usit():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsit))
    with patch("builtins.open", m):
        rel1 = DecOperUsit.le_arquivo("")
        rel2 = DecOperUsit.le_arquivo("")
        assert rel1 == rel2


def test_neq_dec_oper_usit():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsit))
    with patch("builtins.open", m):
        rel1 = DecOperUsit.le_arquivo("")
        rel2 = DecOperUsit.le_arquivo("")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
