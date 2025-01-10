from idecomp.decomp.dec_oper_evap import DecOperEvap

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_oper_evap import (
    MockDecOperEvapv31,
    MockDecOperEvap,
)


def test_atributos_encontrados_dec_oper_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecOperEvap))
    with patch("builtins.open", m):
        rel = DecOperEvap.read("./tests/mocks/arquivos/dec_oper_evap.py")
        assert rel.versao == "32.1"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "no"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "codigo_usina"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert rel.tabela.at[0, "codigo_submercado"] == 1
        assert rel.tabela.at[0, "codigo_ree"] == 10
        assert rel.tabela.at[0, "volume_util_inicial_hm3"] == 401.72
        assert rel.tabela.at[0, "volume_util_inicial_percentual"] == 59.78
        assert rel.tabela.at[0, "volume_util_final_hm3"] == 457.63
        assert rel.tabela.at[0, "volume_util_final_percentual"] == 68.10
        assert rel.tabela.at[0, "evaporacao_modelo_hm3"] == 0.00
        assert rel.tabela.at[0, "evaporacao_calculada_hm3"] == 0.00
        assert rel.tabela.at[0, "desvio_absoluto_hm3"] == 0.000
        assert rel.tabela.at[0, "desvio_percentual"] == 0.000


def test_eq_dec_oper_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecOperEvap))
    with patch("builtins.open", m):
        rel1 = DecOperEvap.read("./tests/mocks/arquivos/dec_oper_evap.py")
        rel2 = DecOperEvap.read("./tests/mocks/arquivos/dec_oper_evap.py")
        assert rel1 == rel2


def test_neq_dec_oper_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecOperEvap))
    with patch("builtins.open", m):
        rel1 = DecOperEvap.read("./tests/mocks/arquivos/dec_oper_evap.py")
        rel2 = DecOperEvap.read("./tests/mocks/arquivos/dec_oper_evap.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2


def test_atributos_encontrados_dec_oper_evap_v31():
    m: MagicMock = mock_open(read_data="".join(MockDecOperEvapv31))
    with patch("builtins.open", m):
        DecOperEvap.set_version("31.0.2")
        rel = DecOperEvap.read("./tests/mocks/arquivos/dec_oper_evap.py")
        assert rel.versao == "31.0.2"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "codigo_usina"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert rel.tabela.at[0, "codigo_submercado"] == 1
        assert rel.tabela.at[0, "codigo_ree"] == 10
        assert rel.tabela.at[0, "volume_util_inicial_hm3"] == 401.72
        assert rel.tabela.at[0, "volume_util_inicial_percentual"] == 59.78
        assert rel.tabela.at[0, "volume_util_final_hm3"] == 457.63
        assert rel.tabela.at[0, "volume_util_final_percentual"] == 68.10
        assert rel.tabela.at[0, "evaporacao_modelo_hm3"] == 0.00
        assert rel.tabela.at[0, "evaporacao_calculada_hm3"] == 0.00
        assert rel.tabela.at[0, "desvio_absoluto_hm3"] == 0.000
        assert rel.tabela.at[0, "desvio_percentual"] == 0.000
