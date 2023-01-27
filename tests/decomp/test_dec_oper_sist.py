from idecomp.decomp.dec_oper_sist import DecOperSist

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_oper_sist import MockDecOperSist


def test_atributos_encontrados_dec_oper_sist():
    m: MagicMock = mock_open(read_data="".join(MockDecOperSist))
    with patch("builtins.open", m):
        rel = DecOperSist.le_arquivo("")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "periodo"] == 1
        assert rel.tabela.at[0, "no"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "duracao"] == 40.00
        assert rel.tabela.at[0, "indiceSubmercado"] == 1
        assert rel.tabela.at[0, "nomeSubmercado"] == "SE"
        assert rel.tabela.at[0, "demandaMW"] == 48383.0
        assert rel.tabela.at[0, "geracaoPequenasUsinasMW"] == 3374.0
        assert rel.tabela.at[0, "geracaoTermicaMW"] == 6509.80
        assert rel.tabela.at[0, "geracaoTermicaAntecipadaMW"] == 548.00
        assert rel.tabela.at[0, "geracaoHidroeletricaMW"] == 33567.62
        assert rel.tabela.at[0, "geracaoEolicaMW"] == 0.00
        assert rel.tabela.at[0, "energiaBombeamentoMW"] == 13.58
        assert rel.tabela.at[0, "energiaImportadaMW"] == 0.00
        assert rel.tabela.at[0, "energiaExportadaMW"] == 0.00
        assert rel.tabela.at[0, "intercambioLiquidoMW"] == 7576.16
        assert rel.tabela.at[0, "itaipu50MW"] == 1900.00
        assert rel.tabela.at[0, "itaipu60MW"] == 5009.89
        assert rel.tabela.at[0, "deficitMW"] == 0.00
        assert rel.tabela.at[0, "enaMWmes"] == 12608.1
        assert rel.tabela.at[0, "earmInicialMWmes"] == 47877.48
        assert rel.tabela.at[0, "earmInicialPercentual"] == 23.43
        assert rel.tabela.at[0, "earmFinalMWmes"] == 52743.55
        assert rel.tabela.at[0, "earmFinalPercentual"] == 25.81
        assert rel.tabela.at[0, "cmo"] == 956.18


def test_eq_dec_oper_sist():
    m: MagicMock = mock_open(read_data="".join(MockDecOperSist))
    with patch("builtins.open", m):
        rel1 = DecOperSist.le_arquivo("")
        rel2 = DecOperSist.le_arquivo("")
        assert rel1 == rel2


def test_neq_dec_oper_sist():
    m: MagicMock = mock_open(read_data="".join(MockDecOperSist))
    with patch("builtins.open", m):
        rel1 = DecOperSist.le_arquivo("")
        rel2 = DecOperSist.le_arquivo("")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
