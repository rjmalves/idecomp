from idecomp.decomp.dec_oper_usih import DecOperUsih

import numpy as np  # type: ignore
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_oper_usih import MockDecOperUsih


def test_atributos_encontrados_dec_oper_usih():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsih))
    with patch("builtins.open", m):
        rel = DecOperUsih.le_arquivo("")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "periodo"] == 1
        assert rel.tabela.at[0, "no"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "duracao"] == 40.00
        assert rel.tabela.at[0, "indice_usina"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert rel.tabela.at[0, "nome_submercado"] == "SE"
        assert rel.tabela.at[0, "volume_util_maximo_hm3"] == 672.00
        assert rel.tabela.at[0, "volume_util_inicial_hm3"] == 31.58
        assert rel.tabela.at[0, "volume_util_inicial_percentual"] == 4.70
        assert rel.tabela.at[0, "volume_util_final_hm3"] == 1.17
        assert rel.tabela.at[0, "volume_util_final_percentual"] == 0.17
        assert rel.tabela.at[0, "geracao_MW"] == 22.12
        assert rel.tabela.at[0, "potencia_instalada_MW"] == 46.00
        assert rel.tabela.at[0, "potencia_disponivel_MW"] == 46.00
        assert np.isnan(rel.tabela.at[0, "vazao_natural_m3s"])
        assert np.isnan(rel.tabela.at[0, "vazao_natural_mlt"])
        assert np.isnan(rel.tabela.at[0, "vazao_incremental_m3s"])
        assert np.isnan(rel.tabela.at[0, "vazao_montante_m3s"])
        assert np.isnan(rel.tabela.at[0, "vazao_montante_tv_m3s"])
        assert np.isnan(rel.tabela.at[0, "vazao_afluente_m3s"])
        assert rel.tabela.at[0, "vazao_defluente_m3s"] == 196.61
        assert rel.tabela.at[0, "vazao_turbinada_m3s"] == 196.61
        assert rel.tabela.at[0, "vazao_vertida_m3s"] == 0.0
        assert rel.tabela.at[0, "vazao_desviada_m3s"] == 0.0
        assert rel.tabela.at[0, "vazao_recebida_bombeamento_m3s"] == 0.0
        assert rel.tabela.at[0, "vazao_retirada_bombeamento_m3s"] == 0.0
        assert rel.tabela.at[0, "vazao_retirada_m3s"] == 0.20
        assert rel.tabela.at[0, "vazao_retorno_m3s"] == 0.0
        assert rel.tabela.at[0, "vazao_evaporada_m3s"] == 0.0


def test_eq_dec_oper_usih():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsih))
    with patch("builtins.open", m):
        rel1 = DecOperUsih.le_arquivo("")
        rel2 = DecOperUsih.le_arquivo("")
        assert rel1 == rel2


def test_neq_dec_oper_usih():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsih))
    with patch("builtins.open", m):
        rel1 = DecOperUsih.le_arquivo("")
        rel2 = DecOperUsih.le_arquivo("")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
