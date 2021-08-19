# Rotinas de testes associadas ao arquivo dadger.rvx do DECOMP
from idecomp.decomp.dadgnl import DadGNL


dadgnl = DadGNL.le_arquivo("tests/_arquivos", "dadgnl.rv0")


def test_leitura_escrita():
    dadgnl.escreve_arquivo("tests/_saidas", "dadgnl.rv0")
    dadgnl2 = DadGNL.le_arquivo("tests/_saidas", "dadgnl.rv0")
    assert dadgnl == dadgnl2


def test_tg():
    tg = dadgnl.tg(86, 1)
    assert tg.codigo == 86
    assert tg.subsistema == 1
    assert tg.nome == "SANTA CRUZ"
    assert tg.estagio == 1
    assert tg.inflexibilidades == [0.0, 0.0, 0.0]
    assert tg.disponibilidades == [350.0, 350.0, 350.0]
    assert tg.cvus == [204.96, 204.96, 204.96]


def test_gs():
    gs = dadgnl.gs(1)
    assert gs.mes == 1
    assert gs.semanas == 5


def test_nl():
    nl = dadgnl.nl(86)
    assert nl.codigo == 86
    assert nl.subsistema == 1
    assert nl.lag == 2


def test_gl():
    gl = dadgnl.gl(86, 1)
    assert gl.codigo == 86
    assert gl.subsistema == 1
    assert gl.estagio == 1
    assert gl.geracoes == [0.0, 0.0, 0.0]
    assert gl.duracoes == [48.0, 32.0, 88.0]


def test_eq_dadgnl():
    dadgnl2 = DadGNL.le_arquivo("tests/_arquivos", "dadgnl.rv0")
    assert dadgnl == dadgnl2


def test_neq_dadgnl():
    dadgnl2 = DadGNL.le_arquivo("tests/_arquivos", "dadgnl.rv0")
    dadgnl2.nl(86).lag = 3
    assert dadgnl != dadgnl2


# def test_leitura_rv1():
#     rv = Dadger.le_arquivo("tests/_arquivos", "dadger.rv1")
#     assert "" in rv.te.titulo


# def test_leitura_rv2():
#     rv = Dadger.le_arquivo("tests/_arquivos", "dadger.rv2")
#     assert "" in rv.te.titulo


# def test_leitura_rv3():
#     rv = Dadger.le_arquivo("tests/_arquivos", "dadger.rv3")
#     assert "" in rv.te.titulo


# def test_leitura_rv4():
#     rv = Dadger.le_arquivo("tests/_arquivos", "dadger.rv4")
#     assert "" in rv.te.titulo
