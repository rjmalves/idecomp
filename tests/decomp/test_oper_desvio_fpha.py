from idecomp.decomp.oper_desvio_fpha import OperDesvioFpha

import numpy as np  # type: ignore
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.oper_desvio_fpha import MockOperDesvioFpha


def test_atributos_encontrados_oper_desvio_fpha():
    m: MagicMock = mock_open(read_data="".join(MockOperDesvioFpha))
    with patch("builtins.open", m):
        rel = OperDesvioFpha.read("./tests/mocks/arquivos/oper_desvio_fpha.py")
        assert rel.versao == "31.23"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "codigo_usina"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert rel.tabela.at[0, "vazao_turbinada_m3s"] == 142.12
        assert rel.tabela.at[0, "vazao_vertida_m3s"] == 0.00
        assert rel.tabela.at[0, "volume_inicial_hm3"] == 563.79
        assert rel.tabela.at[0, "volume_final_hm3"] == 565.33
        assert rel.tabela.at[0, "volume_medio_hm3"] == 564.56
        assert rel.tabela.at[0, "altura_montante"] == 909.63
        assert rel.tabela.at[0, "vazao_lateral_usina_m3s"] == 0
        assert rel.tabela.at[0, "vazao_lateral_posto_m3s"] == 0
        assert rel.tabela.at[0, "vazao_jusante_m3s"] == 142.12
        assert rel.tabela.at[0, "altura_jusante"] == 885.85
        assert rel.tabela.at[0, "altura_liquida"] == 23.68
        assert rel.tabela.at[0, "perdas_hidraulicas"] == 0.10
        assert rel.tabela.at[0, "produtibilidade_especifica"] == 0.008767000000
        assert rel.tabela.at[0, "geracao_hidraulica_pl"] == 30.33
        assert rel.tabela.at[0, "geracao_hidraulica_fpha"] == 30.33
        assert rel.tabela.at[0, "geracao_hidraulica_fph"] == 29.51
        assert rel.tabela.at[0, "desvio_absoluto_pl_fph"] == 0.82
        assert rel.tabela.at[0, "desvio_percentual_pl_fph"] == 2.78
        assert rel.tabela.at[0, "desvio_absoluto_pl_fpha"] == 0
        assert rel.tabela.at[0, "desvio_percentual_pl_fpha"] == 0


def test_atributos_nao_encontrados_oper_media_fpha():
    m: MagicMock = mock_open(read_data="".join(""))
    with patch("builtins.open", m):
        d = OperDesvioFpha.read("./tests/mocks/arquivos/oper_desvio_fpha.py")
        assert d.tabela is None
        assert d.versao is None


def test_eq_oper_desvio_fpha():
    m: MagicMock = mock_open(read_data="".join(MockOperDesvioFpha))
    with patch("builtins.open", m):
        rel1 = OperDesvioFpha.read(
            "./tests/mocks/arquivos/oper_desvio_fpha.py"
        )
        rel2 = OperDesvioFpha.read(
            "./tests/mocks/arquivos/oper_desvio_fpha.py"
        )
        assert rel1 == rel2


def test_neq_oper_desvio_fpha():
    m: MagicMock = mock_open(read_data="".join(MockOperDesvioFpha))
    with patch("builtins.open", m):
        rel1 = OperDesvioFpha.read(
            "./tests/mocks/arquivos/oper_desvio_fpha.py"
        )
        rel2 = OperDesvioFpha.read(
            "./tests/mocks/arquivos/oper_desvio_fpha.py"
        )
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
