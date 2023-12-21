# Rotinas de testes associadas ao arquivo relgnl.rvx do DECOMP
from idecomp.decomp.modelos.relgnl import (
    BlocoDadosUsinasRelgnl,
    BlocoComandosUsinasAjustesTGRelgnl,
    BlocoComandosUsinasAjustesRERelgnl,
    BlocoRelatorioOperacaoRelgnl,
)

from idecomp.decomp.relgnl import Relgnl

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.relgnl import (
    MockDadosTermicasGNL,
    MockPossiveisAjustesRelGNL,
    MockPossiveisAjustesRERelGNL,
    MockRelatorioOperacao,
    MockRelGNL,
)


def test_bloco_dados_termicas_relgnl():
    m: MagicMock = mock_open(read_data="".join(MockDadosTermicasGNL))
    b = BlocoDadosUsinasRelgnl()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 24
    assert b.data.shape[1] == 13
    assert b.data.iloc[0, 0] == 86
    assert b.data.iloc[0, 1] == "SANTA CRUZ"
    assert b.data.iloc[0, 2] == "SE"
    assert b.data.iloc[0, 3] == 1
    assert b.data.iloc[0, 4] == 0.00
    assert b.data.iloc[0, 5] == 350.00
    assert b.data.iloc[0, 6] == 133.15
    assert b.data.iloc[0, 7] == 0.00
    assert b.data.iloc[0, 8] == 350.00
    assert b.data.iloc[0, 9] == 133.15
    assert b.data.iloc[0, 10] == 0.00
    assert b.data.iloc[0, 11] == 350.00
    assert b.data.iloc[0, 12] == 133.15


def test_bloco_possiveis_ajustes_relgnl():
    m: MagicMock = mock_open(read_data="".join(MockPossiveisAjustesRelGNL))
    b = BlocoComandosUsinasAjustesTGRelgnl()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)
    assert b.data.shape[0] == 27
    assert b.data.shape[1] == 8
    assert b.data.iloc[0, 0] == 86
    assert b.data.iloc[0, 1] == "SANTA CRUZ"
    assert b.data.iloc[0, 2] == 2
    assert b.data.iloc[0, 3] == "SE"
    assert b.data.iloc[0, 4] == "28/12/2019"
    assert b.data.iloc[0, 5] == 350.00
    assert b.data.iloc[0, 6] == 350.00
    assert b.data.iloc[0, 7] == 350.00


def test_bloco_possiveis_ajustes_re_relgnl():
    m: MagicMock = mock_open(read_data="".join(MockPossiveisAjustesRERelGNL))
    b = BlocoComandosUsinasAjustesRERelgnl()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)
    assert b.data.shape[0] == 18
    assert b.data.shape[1] == 8
    assert b.data.iloc[0, 0] == 86
    assert b.data.iloc[0, 1] == "SANTA CRUZ"
    assert b.data.iloc[0, 2] == 2
    assert b.data.iloc[0, 3] == "SE"
    assert b.data.iloc[0, 4] == 1
    assert b.data.iloc[0, 5] == 350.00
    assert b.data.iloc[0, 6] == 350.00
    assert b.data.iloc[0, 7] == 350.00


def test_bloco_relatorio_operacao_relgnl():
    m: MagicMock = mock_open(read_data="".join(MockRelatorioOperacao))
    b = BlocoRelatorioOperacaoRelgnl()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 18
    assert b.data.shape[1] == 15
    assert b.data.iloc[0, 0] == 1
    assert b.data.iloc[0, 1] == 1
    assert b.data.iloc[0, 2] == 1.0
    assert b.data.iloc[0, 3] == "SE"
    assert b.data.iloc[0, 4] == "SANTA CRUZ"
    assert b.data.iloc[0, 5] == 2
    assert b.data.iloc[0, 6] == "Sem 10"
    assert b.data.iloc[0, 7] == "29/02/2020"
    assert b.data.iloc[0, 8] == 350.0
    assert b.data.iloc[0, 9] == 34.57
    assert b.data.iloc[0, 10] == 350.0
    assert b.data.iloc[0, 11] == 39.86
    assert b.data.iloc[0, 12] == 350.0
    assert b.data.iloc[0, 13] == 71.68
    assert b.data.iloc[0, 14] == 6674.8


def test_atributos_encontrados_relgnl():
    m: MagicMock = mock_open(read_data="".join(MockRelGNL))
    with patch("builtins.open", m):
        rel = Relgnl.read("./tests/mocks/arquivos/relgnl.py")
        assert rel.usinas_termicas is not None
        assert rel.comandos_usinas_registros_tg is not None
        assert rel.comandos_usinas_restricoes_eletricas is not None
        assert rel.relatorio_operacao_termica is not None


def test_atributos_nao_encontrados_relgnl():
    m: MagicMock = mock_open(read_data="".join(""))
    with patch("builtins.open", m):
        rel = Relgnl.read("./tests/mocks/arquivos/relgnl.py")
        assert rel.usinas_termicas is None
        assert rel.comandos_usinas_registros_tg is None
        assert rel.comandos_usinas_restricoes_eletricas is None
        assert rel.relatorio_operacao_termica is None
