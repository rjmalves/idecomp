# Rotinas de testes associadas ao arquivo custos.rvx do DECOMP
from idecomp.decomp.modelos.custos import (
    BlocoRelatorioCustos,
)

from idecomp.decomp.custos import Custos

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.custos import (
    MockBlocoRelatorioCustos,
    MockCustos,
)


def test_bloco_relatorio_custos():
    m: MagicMock = mock_open(read_data="".join(MockBlocoRelatorioCustos))
    b = BlocoRelatorioCustos()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data[0].shape[0] == 162
    assert b.data[0].shape[1] == 4
    assert b.data[0].iloc[0, 0] == 1


def test_atributos_encontrados_custos():
    m: MagicMock = mock_open(read_data="".join(MockCustos))
    with patch("builtins.open", m):
        rel = Custos.read("./tests/mocks/arquivos/custos.py")
        assert rel.relatorio_variaveis_duais is not None
        assert rel.relatorio_fcf is not None


def test_atributos_nao_encontrados_relato():
    m: MagicMock = mock_open(read_data="".join(""))
    with patch("builtins.open", m):
        rel = Custos.read("./tests/mocks/arquivos/custos.py")
        assert rel.relatorio_variaveis_duais is None
        assert rel.relatorio_fcf is None


def test_eq_custos():
    m: MagicMock = mock_open(read_data="".join(MockCustos))
    with patch("builtins.open", m):
        rel1 = Custos.read("./tests/mocks/arquivos/custos.py")
        rel2 = Custos.read("./tests/mocks/arquivos/custos.py")
        assert rel1 == rel2
