# Rotinas de testes associadas ao arquivo relato.rvx do DECOMP
from idecomp.decomp.relato import LeituraRelato


leitor = LeituraRelato("tests/_arquivos")
leitor.le_arquivo("relato.rv0")


def test_leitura():
    n_semanas = leitor.relato.dados_gerais.numero_semanas_1_mes
    assert n_semanas == 5


def test_cmo():
    cmo_medio = leitor.relato.cmo_medio_subsistema
    assert len(cmo_medio.keys()) == 5


def test_geracao_termica_subsistema():
    gt = leitor.relato.geracao_termica_subsistema
    assert len(gt.keys()) == 5


def test_earm_subsistema():
    earm = leitor.relato.energia_armazenada_inicial_subsistema
    assert len(earm.keys()) == 4
    earm = leitor.relato.energia_armazenada_subsistema
    assert len(earm.keys()) == 4


def test_ena_pre_estudo_semanal_subsistema():
    ena = leitor.relato.energia_afluente_pre_estudo_semanal_subsistema
    assert len(ena.keys()) == 4
    assert len(ena['SE']) == 0


def test_armazenamento_maximo_subsistema():
    earmax = leitor.relato.armazenamento_maximo_subsistema
    assert len(earmax.keys()) == 4
    assert all([e > 0 for e in earmax.values()])


def test_mercado_subsistema():
    ghid = leitor.relato.mercado_subsistema
    assert len(ghid.keys()) == 4
    assert all([len(e) == 5 for e in ghid.values()])


def test_bacia_subsistema():
    ghid = leitor.relato.bacia_subsistema
    assert len(ghid.keys()) == 4
    assert all([len(e) == 5 for e in ghid.values()])


def test_geracao_hidraulica_subsistema():
    ghid = leitor.relato.geracao_hidraulica_subsistema
    assert len(ghid.keys()) == 4
    assert all([len(e) == 5 for e in ghid.values()])


def test_geracao_termica_antecipada_subsistema():
    ghid = leitor.relato.geracao_termica_antecipada_subsistema
    assert len(ghid.keys()) == 4
    assert all([len(e) == 5 for e in ghid.values()])


def test_deficit_subsistema():
    ghid = leitor.relato.deficit_subsistema
    assert len(ghid.keys()) == 4
    assert all([len(e) == 5 for e in ghid.values()])


def test_eq_relato():
    leitor2 = LeituraRelato("tests/_arquivos")
    leitor2.le_arquivo()
    assert leitor2.relato == leitor.relato


def test_leitura_rv1():
    leitor2 = LeituraRelato("tests/_arquivos")
    leitor2.le_arquivo("relato.rv1")
    n = leitor2.relato.dados_gerais.numero_semanas_1_mes
    assert n == 4
    tabela_cmo = leitor2.relato.cmo_medio_subsistema
    assert tabela_cmo["SE"].size == 4


def test_leitura_rv2():
    leitor2 = LeituraRelato("tests/_arquivos")
    leitor2.le_arquivo("relato.rv2")
    n = leitor2.relato.dados_gerais.numero_semanas_1_mes
    assert n == 3
    tabela_cmo = leitor2.relato.cmo_medio_subsistema
    assert tabela_cmo["SE"].size == 3


def test_leitura_rv3():
    leitor2 = LeituraRelato("tests/_arquivos")
    leitor2.le_arquivo("relato.rv3")
    n = leitor2.relato.dados_gerais.numero_semanas_1_mes
    assert n == 2
    tabela_cmo = leitor2.relato.cmo_medio_subsistema
    assert tabela_cmo["SE"].size == 2


def test_leitura_rv4():
    leitor2 = LeituraRelato("tests/_arquivos")
    leitor2.le_arquivo("relato.rv4")
    n = leitor2.relato.dados_gerais.numero_semanas_1_mes
    assert n == 1
    tabela_cmo = leitor2.relato.cmo_medio_subsistema
    assert tabela_cmo["SE"].size == 1
