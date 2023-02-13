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
        assert rel.tabela.at[0, "indice_usina"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "STA CECILIA"
        assert rel.tabela.at[0, "indice_submercado"] == 1
        assert rel.tabela.at[0, "nome_submercado"] == "SE"
        assert rel.tabela.at[0, "indice_usina_jusante"] == 125
        assert rel.tabela.at[0, "indice_usina_montante"] == 181
        assert rel.tabela.at[0, "vazao_bombeada_m3s"] == 61.21
        assert rel.tabela.at[0, "energia_bombeamento_MW"] == 12.24
        assert rel.tabela.at[0, "vazao_bombeada_minima_m3s"] == 0.00
        assert rel.tabela.at[0, "vazao_bombeada_maxima_m3s"] == 160.00


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
