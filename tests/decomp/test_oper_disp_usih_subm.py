from idecomp.decomp.oper_disp_usih_subm import OperDispUsihSubm

import numpy as np  # type: ignore
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.oper_disp_usih_subm import MockOperDispUsihSubm


def test_atributos_encontrados_oper_disp_usih_subm():
    m: MagicMock = mock_open(read_data="".join(MockOperDispUsihSubm))
    with patch("builtins.open", m):
        rel = OperDispUsihSubm.read(
            "./tests/mocks/arquivos/oper_disp_usih_subm.py"
        )
        assert rel.versao == "31.27"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "codigo_submercado"] == 1
        assert rel.tabela.at[0, "nome_submercado"] == "SE"
        assert rel.tabela.at[0, "geracao_hidraulica_maxima_pl"] == 55786.19


def test_atributos_nao_encontrados_oper_disp_usih_subm():
    m: MagicMock = mock_open(read_data="".join(""))
    with patch("builtins.open", m):
        d = OperDispUsihSubm.read(
            "./tests/mocks/arquivos/oper_disp_usih_subm.py"
        )
        assert d.tabela is None
        assert d.versao is None


def test_eq_oper_disp_usih_subm():
    m: MagicMock = mock_open(read_data="".join(MockOperDispUsihSubm))
    with patch("builtins.open", m):
        rel1 = OperDispUsihSubm.read(
            "./tests/mocks/arquivos/oper_disp_usih_subm.py"
        )
        rel2 = OperDispUsihSubm.read(
            "./tests/mocks/arquivos/oper_disp_usih_subm.py"
        )
        assert rel1 == rel2


def test_neq_oper_disp_usih_subm():
    m: MagicMock = mock_open(read_data="".join(MockOperDispUsihSubm))
    with patch("builtins.open", m):
        rel1 = OperDispUsihSubm.read(
            "./tests/mocks/arquivos/oper_disp_usih_subm.py"
        )
        rel2 = OperDispUsihSubm.read(
            "./tests/mocks/arquivos/oper_disp_usih_subm.py"
        )
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
