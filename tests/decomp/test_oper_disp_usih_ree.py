from idecomp.decomp.oper_disp_usih_ree import OperDispUsihRee

import numpy as np  # type: ignore
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.oper_disp_usih_ree import MockOperDispUsihRee


def test_atributos_encontrados_oper_disp_usih_ree():
    m: MagicMock = mock_open(read_data="".join(MockOperDispUsihRee))
    with patch("builtins.open", m):
        rel = OperDispUsihRee.read(
            "./tests/mocks/arquivos/oper_disp_usih_ree.py"
        )
        assert rel.versao == "31.27"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "codigo_ree"] == 1
        assert rel.tabela.at[0, "nome_ree"] == "SUDESTE"
        assert rel.tabela.at[0, "geracao_hidraulica_maxima_pl"] == 7701.30


def test_atributos_nao_encontrados_oper_disp_usih_ree():
    m: MagicMock = mock_open(read_data="".join(""))
    with patch("builtins.open", m):
        d = OperDispUsihRee.read(
            "./tests/mocks/arquivos/oper_disp_usih_ree.py"
        )
        assert d.tabela is None
        assert d.versao is None


def test_eq_oper_disp_usih_ree():
    m: MagicMock = mock_open(read_data="".join(MockOperDispUsihRee))
    with patch("builtins.open", m):
        rel1 = OperDispUsihRee.read(
            "./tests/mocks/arquivos/oper_disp_usih_ree.py"
        )
        rel2 = OperDispUsihRee.read(
            "./tests/mocks/arquivos/oper_disp_usih_ree.py"
        )
        assert rel1 == rel2


def test_neq_oper_disp_usih_ree():
    m: MagicMock = mock_open(read_data="".join(MockOperDispUsihRee))
    with patch("builtins.open", m):
        rel1 = OperDispUsihRee.read(
            "./tests/mocks/arquivos/oper_disp_usih_ree.py"
        )
        rel2 = OperDispUsihRee.read(
            "./tests/mocks/arquivos/oper_disp_usih_ree.py"
        )
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
