from idecomp.decomp.dec_oper_usie import DecOperUsie

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_oper_usie import MockDecOperUsie


def test_atributos_encontrados_dec_oper_usie():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsie))
    with patch("builtins.open", m):
        rel = DecOperUsie.le_arquivo("")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "periodo"] == 1
        assert rel.tabela.at[0, "no"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "duracao"] == 40.00
        assert rel.tabela.at[0, "indiceUsina"] == 1
        assert rel.tabela.at[0, "nomeUsina"] == "STA CECILIA"
        assert rel.tabela.at[0, "indiceSubmercado"] == 1
        assert rel.tabela.at[0, "nomeSubmercado"] == "SE"
        assert rel.tabela.at[0, "indiceUsinaJusante"] == 125
        assert rel.tabela.at[0, "indiceUsinaMontante"] == 181
        assert rel.tabela.at[0, "vazaoBombeadaM3S"] == 61.21
        assert rel.tabela.at[0, "energiaBombeamentoMW"] == 12.24
        assert rel.tabela.at[0, "vazaoBombeadaMinimaM3S"] == 0.00
        assert rel.tabela.at[0, "vazaoBombeadaMaximaM3S"] == 160.00


def test_eq_dec_oper_usie():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsie))
    with patch("builtins.open", m):
        rel1 = DecOperUsie.le_arquivo("")
        rel2 = DecOperUsie.le_arquivo("")
        assert rel1 == rel2


def test_neq_dec_oper_usie():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsie))
    with patch("builtins.open", m):
        rel1 = DecOperUsie.le_arquivo("")
        rel2 = DecOperUsie.le_arquivo("")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
