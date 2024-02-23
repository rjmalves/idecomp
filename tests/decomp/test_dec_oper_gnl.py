from idecomp.decomp.dec_oper_gnl import DecOperGnl

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_oper_gnl import MockDecOperGnl, MockDecOperGnlv31


def test_atributos_encontrados_dec_oper_gnl():
    m: MagicMock = mock_open(read_data="".join(MockDecOperGnl))
    with patch("builtins.open", m):
        rel = DecOperGnl.read("./tests/mocks/arquivos/dec_oper_gnl.py")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "no"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "duracao"] == 40.0
        assert rel.tabela.at[0, "codigo_usina"] == 86
        assert rel.tabela.at[0, "nome_usina"] == "SANTA CRUZ"
        assert rel.tabela.at[0, "codigo_submercado"] == 1
        assert rel.tabela.at[0, "nome_submercado"] == "SE"
        assert rel.tabela.at[0, "lag"] == 2
        assert rel.tabela.at[0, "custo_incremental"] == 116.57
        assert rel.tabela.at[0, "beneficio_gnl"] == 542.74
        assert rel.tabela.at[0, "geracao_minima_MW"] == 0.00
        assert rel.tabela.at[0, "geracao_comandada_MW"] == 350.00
        assert rel.tabela.at[0, "geracao_sinalizada_MW"] == 220.20
        assert rel.tabela.at[0, "geracao_MW"] == 350.0
        assert rel.tabela.at[0, "geracao_maxima_MW"] == 350.0
        assert rel.tabela.at[0, "fator_manutencao"] == 1.0
        assert rel.tabela.at[0, "custo_geracao"] == 1631.98


def test_eq_dec_oper_gnl():
    m: MagicMock = mock_open(read_data="".join(MockDecOperGnl))
    with patch("builtins.open", m):
        rel1 = DecOperGnl.read("./tests/mocks/arquivos/dec_oper_gnl.py")
        rel2 = DecOperGnl.read("./tests/mocks/arquivos/dec_oper_gnl.py")
        assert rel1 == rel2


def test_neq_dec_oper_gnl():
    m: MagicMock = mock_open(read_data="".join(MockDecOperGnl))
    with patch("builtins.open", m):
        rel1 = DecOperGnl.read("./tests/mocks/arquivos/dec_oper_gnl.py")
        rel2 = DecOperGnl.read("./tests/mocks/arquivos/dec_oper_gnl.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2


def test_atributos_encontrados_dec_oper_gnl_v31():
    m: MagicMock = mock_open(read_data="".join(MockDecOperGnlv31))
    with patch("builtins.open", m):
        DecOperGnl.set_version("31.0.2")
        rel = DecOperGnl.read("./tests/mocks/arquivos/dec_oper_gnl.py")
        assert rel.versao == "31.0.2"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "duracao"] == 36.0
        assert rel.tabela.at[0, "codigo_usina"] == 86
        assert rel.tabela.at[0, "nome_usina"] == "SANTA CRUZ"
        assert rel.tabela.at[0, "codigo_submercado"] == 1
        assert rel.tabela.at[0, "nome_submercado"] == "SE"
        assert rel.tabela.at[0, "lag"] == 2
        assert rel.tabela.at[0, "custo_incremental"] == 155.86
        assert rel.tabela.at[0, "beneficio_gnl"] == 0.0
        assert rel.tabela.at[0, "geracao_minima_MW"] == 0.0
        assert rel.tabela.at[0, "geracao_comandada_MW"] == 0.0
        assert rel.tabela.at[0, "geracao_sinalizada_MW"] == 0.0
        assert rel.tabela.at[0, "geracao_MW"] == 0.0
        assert rel.tabela.at[0, "geracao_maxima_MW"] == 500.0
        assert rel.tabela.at[0, "fator_manutencao"] == 1.0
        assert rel.tabela.at[0, "custo_geracao"] == 0.0
