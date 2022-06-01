from idecomp.decomp.modelos.dadgnl import TG, GL, GS, NL

from idecomp.decomp.dadgnl import DadGNL

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dadgnl import (
    MockTG,
    MockGL,
    MockGS,
    MockNL,
    MockDadGNL,
)


def test_registro_tg_dadgnl():

    m: MagicMock = mock_open(read_data="".join(MockTG))
    r = TG()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        86,
        1,
        "SANTA CRUZ",
        1,
        0.0,
        350.0,
        204.96,
        0.0,
        350.0,
        204.96,
        0.0,
        350.0,
        204.96,
    ]
    assert r.codigo == 86
    r.codigo = 0
    assert r.codigo == 0
    assert r.subsistema == 1
    r.subsistema = 0
    assert r.subsistema == 0
    assert r.nome == "SANTA CRUZ"
    r.nome = "A"
    assert r.nome == "A"
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.inflexibilidades == [0.0, 0.0, 0.0]
    r.inflexibilidades = [999.0]
    assert r.inflexibilidades == [999.0]
    assert r.cvus == [204.96, 204.96, 204.96]
    r.cvus = [999.0, 999.0, 999.0]
    assert r.cvus == [999.0, 999.0, 999.0]
    assert r.disponibilidades == [350.0, 350.0, 350.0]
    r.disponibilidades = [0.0, 0.0, 0.0]
    assert r.disponibilidades == [0.0, 0.0, 0.0]


def test_registro_gs_dadgnl():

    m: MagicMock = mock_open(read_data="".join(MockGS))
    r = GS()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        5,
    ]
    assert r.mes == 1
    r.mes = 0
    assert r.mes == 0
    assert r.semanas == 5
    r.semanas = 0
    assert r.semanas == 0


def test_registro_nl_dadgnl():

    m: MagicMock = mock_open(read_data="".join(MockNL))
    r = NL()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [86, 1, 2]
    assert r.codigo == 86
    r.codigo = 0
    assert r.codigo == 0
    assert r.subsistema == 1
    r.subsistema = 0
    assert r.subsistema == 0
    assert r.lag == 2
    r.lag = 0
    assert r.lag == 0


def test_registro_gl_dadgnl():

    m: MagicMock = mock_open(read_data="".join(MockGL))
    r = GL()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [86, 1, 1, 0.0, 48, 0.0, 32, 0.0, 88, "29052021"]
    assert r.codigo == 86
    r.codigo = 0
    assert r.codigo == 0
    assert r.subsistema == 1
    r.subsistema = 0
    assert r.subsistema == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.geracoes == [0.0, 0.0, 0.0]
    r.geracoes = [1.0, 1.0, 1.0]
    assert r.geracoes == [1.0, 1.0, 1.0]
    assert r.duracoes == [48, 32, 88]
    r.duracoes = [0, 0, 0]
    assert r.duracoes == [0, 0, 0]
