from idecomp.decomp.modelos.dadgnl import TG, GL, GS, NL

from idecomp.decomp.dadgnl import Dadgnl

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
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    assert r.codigo_usina == 86
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.codigo_submercado == 1
    r.codigo_submercado = 0
    assert r.codigo_submercado == 0
    assert r.nome == "SANTA CRUZ"
    r.nome = "A"
    assert r.nome == "A"
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.inflexibilidade == [0.0, 0.0, 0.0]
    r.inflexibilidade = [999.0]
    assert r.inflexibilidade == [999.0]
    assert r.cvu == [204.96, 204.96, 204.96]
    r.cvu = [999.0, 999.0, 999.0]
    assert r.cvu == [999.0, 999.0, 999.0]
    assert r.disponibilidade == [350.0, 350.0, 350.0]
    r.disponibilidade = [0.0, 0.0, 0.0]
    assert r.disponibilidade == [0.0, 0.0, 0.0]


def test_registro_tg_dadgnl_custo_sem_ponto_decimal():
    # O custo é F10.2 no manual: escrito sem ponto decimal, "299" vale 2.99
    # para o DECOMP. As capacidades são F5.0 e são lidas como escritas.
    for linha, dados in [
        (
            "TG   86   1   ST.CRUZ NO 1       0  500    296.52    0  500    296.52    0  500    296.52",
            [0.0, 500.0, 296.52, 0.0, 500.0, 296.52, 0.0, 500.0, 296.52],
        ),
        (
            "TG  224   3   P. SERGIPE 1       01593.       299    01593.       299    01593.       299",
            [0.0, 1593.0, 2.99, 0.0, 1593.0, 2.99, 0.0, 1593.0, 2.99],
        ),
    ]:
        m: MagicMock = mock_open(read_data=linha)
        r = TG()
        with patch("builtins.open", m):
            with open("", "") as fp:
                r.read(fp)
        assert r.data[4:13] == dados
        m2: MagicMock = mock_open(read_data="")
        with patch("builtins.open", m2):
            with open("", "w") as fp:
                r.write(fp)
            escrita = "".join(c.args[0] for c in m2().write.call_args_list)
        for inicio in [39, 59, 79]:
            assert "." in escrita[inicio : inicio + 10]
        m3: MagicMock = mock_open(read_data=escrita)
        r2 = TG()
        with patch("builtins.open", m3):
            with open("", "") as fp:
                r2.read(fp)
        assert r2.data == r.data


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
    assert r.codigo_usina == 86
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.codigo_submercado == 1
    r.codigo_submercado = 0
    assert r.codigo_submercado == 0
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
    assert r.codigo_usina == 86
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.codigo_submercado == 1
    r.codigo_submercado = 0
    assert r.codigo_submercado == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.geracao == [0.0, 0.0, 0.0]
    r.geracao = [1.0, 1.0, 1.0]
    assert r.geracao == [1.0, 1.0, 1.0]
    assert r.duracao == [48, 32, 88]
    r.duracao = [0, 0, 0]
    assert r.duracao == [0, 0, 0]
    assert r.data_inicio == "29052021"
    r.data_inicio = ""
    assert r.data_inicio == ""


def test_campos_nao_encontrados_dadgnl():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        d = Dadgnl.read("./tests/mocks/arquivos/dadgnl.py")
    assert d.tg(0, 0) is None
    assert d.gs(0) is None
    assert d.nl(0) is None
    assert d.gl(0, 0) is None


def test_campos_encontrados_dadgnl():
    m: MagicMock = mock_open(read_data="".join(MockDadGNL))
    with patch("builtins.open", m):
        d = Dadgnl.read("./tests/mocks/arquivos/dadgnl.py")
    assert d.tg(86, 1) is not None
    assert d.gs(1) is not None
    assert d.nl(86) is not None
    assert d.gl(86, 1) is not None
    assert len(d.gl(df=True).columns) == 10


def test_eq_dadgnl():
    m: MagicMock = mock_open(read_data="".join(MockDadGNL))
    with patch("builtins.open", m):
        d1 = Dadgnl.read("./tests/mocks/arquivos/dadgnl.py")
        d2 = Dadgnl.read("./tests/mocks/arquivos/dadgnl.py")
        assert d1 == d2


def test_neq_dadgnl():
    m: MagicMock = mock_open(read_data="".join(MockDadGNL))
    with patch("builtins.open", m):
        d1 = Dadgnl.read("./tests/mocks/arquivos/dadgnl.py")
        d2 = Dadgnl.read("./tests/mocks/arquivos/dadgnl.py")
        d2.gs(1).semanas = 0
        assert d1 != d2


def test_leitura_escrita_dadgnl():
    m_leitura: MagicMock = mock_open(read_data="".join(MockDadGNL))
    with patch("builtins.open", m_leitura):
        d1 = Dadgnl.read("./tests/mocks/arquivos/dadgnl.py")
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        d1.write("./tests/mocks/arquivos/dadgnl.py")
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(2, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        d2 = Dadgnl.read("./tests/mocks/arquivos/dadgnl.py")
        assert d1 == d2
