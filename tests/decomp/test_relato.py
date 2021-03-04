# Rotinas de testes associadas ao arquivo relato.rvx do DECOMP
from idecomp.decomp.relato import LeituraRelato


leitor = LeituraRelato("tests/_arquivos")
leitor.le_arquivo()


def test_leitura():
    n_semanas = leitor.relato.dados_gerais.numero_semanas_1_mes
    assert n_semanas == 5


def test_cmo():
    cmo_medio = leitor.relato.cmo.custo_medio_subsistema
    assert len(cmo_medio.keys()) == 5


def test_eq_relato():
    leitor2 = LeituraRelato("tests/_arquivos")
    leitor2.le_arquivo()
    assert leitor2.relato == leitor.relato
