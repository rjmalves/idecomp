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
        assert rel.tabela.at[0, "indiceUsina"] == 1
        assert rel.tabela.at[0, "nomeUsina"] == "CAMARGOS"
        assert rel.tabela.at[0, "nomeSubmercado"] == "SE"
        assert rel.tabela.at[0, "volumeUtilMaximoHm3"] == 672.00
        assert rel.tabela.at[0, "volumeUtilInicialHm3"] == 31.58
        assert rel.tabela.at[0, "volumeUtilInicialPercentual"] == 4.70
        assert rel.tabela.at[0, "volumeUtilFinalHm3"] == 1.17
        assert rel.tabela.at[0, "volumeUtilFinalPercentual"] == 0.17
        assert rel.tabela.at[0, "geracaoMW"] == 22.12
        assert rel.tabela.at[0, "potenciaInstaladaMW"] == 46.00
        assert rel.tabela.at[0, "potenciaDisponivelMW"] == 46.00
        assert np.isnan(rel.tabela.at[0, "vazaoNaturalM3S"])
        assert np.isnan(rel.tabela.at[0, "vazaoNaturalMLT"])
        assert np.isnan(rel.tabela.at[0, "vazaoIncrementalM3S"])
        assert np.isnan(rel.tabela.at[0, "vazaoMontanteM3S"])
        assert np.isnan(rel.tabela.at[0, "vazaoMontanteTVM3S"])
        assert np.isnan(rel.tabela.at[0, "vazaoAfluenteM3S"])
        assert rel.tabela.at[0, "vazaoDefluenteM3S"] == 196.61
        assert rel.tabela.at[0, "vazaoTurbinadaM3S"] == 196.61
        assert rel.tabela.at[0, "vazaoVertidaM3S"] == 0.0
        assert rel.tabela.at[0, "vazaoDesviadaM3S"] == 0.0
        assert rel.tabela.at[0, "vazaoRecebidaBombeamentoM3S"] == 0.0
        assert rel.tabela.at[0, "vazaoRetiradaBombeamentoM3S"] == 0.0
        assert rel.tabela.at[0, "vazaoRetiradaM3S"] == 0.20
        assert rel.tabela.at[0, "vazaoRetornoM3S"] == 0.0
        assert rel.tabela.at[0, "vazaoEvaporadaM3S"] == 0.0


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
