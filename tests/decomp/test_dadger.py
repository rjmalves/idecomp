# Rotinas de testes associadas ao arquivo dadger.rvx do DECOMP
from idecomp.decomp.dadger import Dadger


dadger = Dadger.le_arquivo("tests/_arquivos", "dadger.rv0")
dadger_he = Dadger.le_arquivo("tests/_arquivos", "dadgerhe.rv0")


def test_leitura_escrita():
    dadger.escreve_arquivo("tests/_saidas", "dadger.rv0")
    dadger2 = Dadger.le_arquivo("tests/_saidas", "dadger.rv0")
    assert dadger == dadger2


def test_te():
    te = dadger.te
    assert "PMO - JUNHO/21 - JULHO/21" in te.titulo


def test_rt():
    rt = dadger.rt("CRISTA")
    rt2 = dadger.rt("DESVIO")
    assert rt.restricao == "CRISTA"
    assert rt2.restricao == "DESVIO"


def test_sb():
    sb = dadger.sb(1)
    assert sb.codigo == 1
    assert sb.nome == "SE"


def test_uh():
    uh = dadger.uh(1)
    assert uh.codigo == 1
    assert uh.ree == 10
    assert uh.volume_inicial == 71.96
    assert uh.evaporacao


def test_ct():
    ct = dadger.ct(1, 1)
    assert ct.codigo == 1
    assert ct.nome == "ANGRA 1"
    assert ct.estagio == 1
    assert ct.subsistema == 1
    assert ct.inflexibilidades == [640, 640, 640]
    assert ct.disponibilidades == [640, 640, 640]
    assert ct.cvus == [31.17, 31.17, 31.17]


def test_dp():
    dp = dadger.dp(1, 1)
    assert dp.cargas == [44182.0, 40421.0, 33226.0]
    assert dp.duracoes == [48.0, 32.0, 88.0]


def test_gp():
    gp = dadger.gp
    assert gp.gap == 0.001


def test_ni():
    ni = dadger.ni
    assert ni.iteracoes == 500


def test_dt():
    dt = dadger.dt
    assert dt.dia == 29
    assert dt.mes == 5
    assert dt.ano == 2021


def test_re():
    re = dadger.re(1)
    assert re.codigo == 1
    assert re.estagio_inicial == 1
    assert re.estagio_final == 6


def test_lu():
    lu = dadger.lu(1, 1)
    assert lu.codigo == 1
    assert lu.estagio == 1
    assert lu.limites_inferiores == [126, 126, 126]


def test_vi():
    vi = dadger.vi(156)
    assert vi.duracao == 360
    assert vi.vazoes == [404, 402, 398, 396, 354]


def test_ir():
    ir = dadger.ir("ARQFPHA")
    assert ir.tipo == "ARQFPHA"


def test_fc():
    fc = dadger.fc("NEWV21")
    assert fc.tipo == "NEWV21"
    assert fc.caminho == "CORTESH.P06"


def test_ti():
    ti = dadger.ti(1)
    assert ti.codigo == 1
    assert ti.taxas == [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]


def test_hv():
    hv = dadger.hv(3)
    assert hv.codigo == 3
    assert hv.estagio_inicial == 1
    assert hv.estagio_final == 6


def test_lv():
    lv = dadger.lv(3, 1)
    assert lv.codigo == 3
    assert lv.estagio == 1
    assert lv.limite_inferior == 622.8


def test_hq():
    hq = dadger.hq(5)
    assert hq.codigo == 5
    assert hq.estagio_inicial == 1
    assert hq.estagio_final == 6


def test_lq():
    lq = dadger.lq(5, 1)
    assert lq.codigo == 5
    assert lq.estagio == 1
    assert lq.limites_inferiores == [256.25, 256.25, 256.25]


def test_he():
    he = dadger_he.he(1, 1)
    assert he.codigo == 1
    assert he.estagio == 1
    assert he.limite == 20.0
    assert he.tipo_limite == 2
    assert he.penalidade == 1864.73
    assert he.tipo_penalidade == 0


def test_eq_dadger():
    dadger2 = Dadger.le_arquivo("tests/_arquivos", "dadger.rv0")
    assert dadger == dadger2


def test_neq_dadger():
    dadger2 = Dadger.le_arquivo("tests/_arquivos", "dadger.rv0")
    dadger2.te.titulo = "TESTE"
    assert dadger != dadger2


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
