# Rotinas de testes associadas ao arquivo relato.rvx do DECOMP
from idecomp.decomp.sumario import Sumario


sum = Sumario.le_arquivo("tests/_arquivos", "sumario.rv0")


def test_leitura():
    n_semanas = sum.cmo_medio_subsistema.shape[1] - 2
    assert n_semanas == 6


def test_cmo():
    cmo_medio = sum.cmo_medio_subsistema
    assert cmo_medio.loc[0, "Estágio 1"] == 117.59


def test_geracao_termica_subsistema():
    gt = sum.geracao_termica_subsistema
    assert float(gt.loc[gt["Subsistema"] == "SE", "Estágio 1"]) == 3213.8


def test_energia_armazenada_subsistema():
    earm = sum.energia_armazenada_subsistema
    assert float(earm.loc[earm["Subsistema"] == "SE", "Inicial"]) == 17.0


def test_energia_armazenada_ree():
    earm = sum.energia_armazenada_ree
    assert float(earm.loc[earm["REE"] == "SUDESTE", "Inicial"]) == 25.4


def test_eq_sumario():
    sum2 = Sumario.le_arquivo("tests/_arquivos", "sumario.rv0")
    assert sum == sum2
