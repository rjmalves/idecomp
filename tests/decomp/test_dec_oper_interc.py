from idecomp.decomp.dec_oper_interc import DecOperInterc

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_oper_interc import MockDecOperInterc


def test_atributos_encontrados_dec_oper_interc():
    m: MagicMock = mock_open(read_data="".join(MockDecOperInterc))
    with patch("builtins.open", m):
        rel = DecOperInterc.le_arquivo("")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "periodo"] == 1
        assert rel.tabela.at[0, "no"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "indiceSubmercadoDe"] == 4
        assert rel.tabela.at[0, "nomeSubmercadoDe"] == "N"
        assert rel.tabela.at[0, "indiceSubmercadoPara"] == 11
        assert rel.tabela.at[0, "nomeSubmercadoPara"] == "FC"
        assert rel.tabela.at[0, "intercambioOrigemMW"] == 5343.64
        assert rel.tabela.at[0, "intercambioDestinoMW"] == 5343.64
        assert rel.tabela.at[0, "perdasMW"] == 0.00
        assert rel.tabela.at[0, "fatorPerdas"] == 0.0000
        assert rel.tabela.at[0, "capacidadeMW"] == 99999.00


def test_eq_dec_oper_interc():
    m: MagicMock = mock_open(read_data="".join(MockDecOperInterc))
    with patch("builtins.open", m):
        rel1 = DecOperInterc.le_arquivo("")
        rel2 = DecOperInterc.le_arquivo("")
        assert rel1 == rel2


def test_neq_dec_oper_interc():
    m: MagicMock = mock_open(read_data="".join(MockDecOperInterc))
    with patch("builtins.open", m):
        rel1 = DecOperInterc.le_arquivo("")
        rel2 = DecOperInterc.le_arquivo("")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
