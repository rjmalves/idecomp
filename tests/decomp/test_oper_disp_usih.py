from idecomp.decomp.oper_disp_usih import OperDispUsih

import numpy as np  # type: ignore
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.oper_disp_usih import MockOperDispUsih


def test_atributos_encontrados_oper_disp_usih():
    m: MagicMock = mock_open(read_data="".join(MockOperDispUsih))
    with patch("builtins.open", m):
        rel = OperDispUsih.read("./tests/mocks/arquivos/oper_disp_usih.py")
        assert rel.versao == "31.27"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "codigo_usina"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert rel.tabela.at[0, "codigo_submercado"] == 1
        assert rel.tabela.at[0, "nome_submercado"] == "SE"
        assert rel.tabela.at[0, "volume_inicial_hm3"] == 782.05
        assert rel.tabela.at[0, "volume_final_hm3"] == 792.00
        assert rel.tabela.at[0, "vazao_vertida_m3s"] == 0.00
        assert rel.tabela.at[0, "vazao_turbinada_m3s"] == 81.62
        assert rel.tabela.at[0, "vazao_turbinada_maxima_m3s"] == 217.53
        assert rel.tabela.at[0, "geracao_hidraulica"] == 19.39
        assert rel.tabela.at[0, "geracao_hidraulica_maxima"] == 46.00
        assert rel.tabela.at[0, "geracao_hidraulica_maxima_pl"] == 45.93


def test_atributos_nao_encontrados_oper_disp_usih():
    m: MagicMock = mock_open(read_data="".join(""))
    with patch("builtins.open", m):
        d = OperDispUsih.read("./tests/mocks/arquivos/oper_disp_usih.py")
        assert d.tabela is None
        assert d.versao is None


def test_eq_oper_disp_usih():
    m: MagicMock = mock_open(read_data="".join(MockOperDispUsih))
    with patch("builtins.open", m):
        rel1 = OperDispUsih.read("./tests/mocks/arquivos/oper_disp_usih.py")
        rel2 = OperDispUsih.read("./tests/mocks/arquivos/oper_disp_usih.py")
        assert rel1 == rel2


def test_neq_oper_disp_usih():
    m: MagicMock = mock_open(read_data="".join(MockOperDispUsih))
    with patch("builtins.open", m):
        rel1 = OperDispUsih.read("./tests/mocks/arquivos/oper_disp_usih.py")
        rel2 = OperDispUsih.read("./tests/mocks/arquivos/oper_disp_usih.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
