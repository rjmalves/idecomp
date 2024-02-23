from idecomp.decomp.dec_desvfpha import DecDesvFpha

import numpy as np  # type: ignore
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_desvfpha import MockDecDesvFpha


def test_atributos_encontrados_dec_desvfpha():
    m: MagicMock = mock_open(read_data="".join(MockDecDesvFpha))
    with patch("builtins.open", m):
        rel = DecDesvFpha.read("./tests/mocks/arquivos/dec_desvfpha.py")
        assert rel.versao == "31.0.2"
        assert rel.tabela.at[0, "codigo_usina"] == 1
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "no"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert rel.tabela.at[0, "volume_total_hm3"] == 739.26
        assert rel.tabela.at[0, "volume_util_percentual"] == 92.15
        assert rel.tabela.at[0, "vazao_turbinada_m3s"] == 111.70
        assert rel.tabela.at[0, "vazao_vertida_m3s"] == 0.00
        assert rel.tabela.at[0, "vazao_jusante_m3s"] == 111.70
        assert rel.tabela.at[0, "vazao_lateral_usina_m3s"] == 0.00
        assert rel.tabela.at[0, "vazao_lateral_posto_m3s"] == 0.00
        assert rel.tabela.at[0, "altura_jusante"] == 885.79
        assert rel.tabela.at[0, "altura_montante"] == 912.33
        assert rel.tabela.at[0, "produtibilidade_especifica"] == 0.00876680
        assert rel.tabela.at[0, "perdas_hidraulicas"] == 0.095000
        assert rel.tabela.at[0, "afogamento"] == 0
        assert rel.tabela.at[0, "geracao_hidraulica_fph"] == 25.90
        assert rel.tabela.at[0, "geracao_hidraulica_fpha"] == 26.38
        assert rel.tabela.at[0, "desvio_absoluto_MW"] == 0.48
        assert rel.tabela.at[0, "desvio_percentual"] == 1.84
        assert rel.tabela.at[0, "influencia_vertimento_canal_fuga"] == 1


def test_eq__dec_desvfpha():
    m: MagicMock = mock_open(read_data="".join(MockDecDesvFpha))
    with patch("builtins.open", m):
        rel1 = DecDesvFpha.read("./tests/mocks/arquivos/dec_desvfpha.py")
        rel2 = DecDesvFpha.read("./tests/mocks/arquivos/dec_desvfpha.py")
        assert rel1 == rel2


def test_neq_dec_desvfpha():
    m: MagicMock = mock_open(read_data="".join(MockDecDesvFpha))
    with patch("builtins.open", m):
        rel1 = DecDesvFpha.read("./tests/mocks/arquivos/dec_desvfpha.py")
        rel2 = DecDesvFpha.read("./tests/mocks/arquivos/dec_desvfpha.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
