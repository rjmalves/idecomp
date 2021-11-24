# Rotinas de testes associadas ao arquivo relato.rvx do DECOMP
from idecomp.decomp.relato import Relato


rel = Relato.le_arquivo("tests/_arquivos", "relato.rv0")


def test_leitura():
    n_semanas = rel.cmo_medio_subsistema.shape[1] - 2
    assert n_semanas == 5


def test_convergencia():
    conv = rel.convergencia
    assert conv.loc[0, "Zinf"] == 450767.9


def test_cmo():
    cmo_medio = rel.cmo_medio_subsistema
    assert cmo_medio.loc[0, "Estágio 1"] == 287.91


def test_geracao_termica_subsistema():
    gt = rel.geracao_termica_subsistema
    assert float(gt.loc[gt["Subsistema"] == "SE", "Estágio 1"]) == 5083.8


def test_volume_util_reservatorios():
    vol = rel.volume_util_reservatorios
    assert float(vol.loc[vol["Usina"] == "CAMARGOS", "Estágio 1"]) == 24.9
    assert float(vol.loc[vol["Usina"] == "BALBINA", "Estágio 5"]) == 31.8


def test_energia_armazenada_subsistema():
    earm = rel.energia_armazenada_subsistema
    assert float(earm.loc[earm["Subsistema"] == "SE", "Inicial"]) == 20.4


def test_energia_armazenada_ree():
    earm = rel.energia_armazenada_ree
    assert float(earm.loc[earm["REE"] == "SUDESTE", "Inicial"]) == 19.5


def test_ena_pre_estudo_semanal():
    earm = rel.ena_pre_estudo_semanal_subsistema
    assert len(list(earm.columns)) == 1


def test_armazenamento_maximo_subsistema():
    earm = rel.energia_armazenada_maxima_subsistema
    assert float(earm.loc[earm["Subsistema"] == "SE", "Earmax"]) == 204321.7


def test_dias_excluidos():
    assert rel.dias_excluidos_semana_inicial == 4
    assert rel.dias_excluidos_semana_final == 0


def test_balanco_energetico():
    bal = rel.balanco_energetico
    assert float(bal.loc[(bal["Estágio"] == 1) & (bal["Subsistema"] == "SE"),
                         "Mercado"]) == 37924.4


def test_relatorio_operacao_uhe():
    bal = rel.relatorio_operacao_uhe
    assert float(bal.loc[(bal["Estágio"] == 1) & (bal["Usina"] == "CAMARGOS"),
                         "Ponta"]) == 31.5


def test_eq_relato():
    rel2 = Relato.le_arquivo("tests/_arquivos", "relato.rv0")
    assert rel == rel2


def test_leitura_rv1():
    rel2 = Relato.le_arquivo("tests/_arquivos", "relato.rv1")
    assert rel2.cmo_medio_subsistema.shape[1] == 6


def test_leitura_rv2():
    rel2 = Relato.le_arquivo("tests/_arquivos", "relato.rv2")
    assert rel2.cmo_medio_subsistema.shape[1] == 5


def test_leitura_rv3():
    rel2 = Relato.le_arquivo("tests/_arquivos", "relato.rv3")
    assert rel2.cmo_medio_subsistema.shape[1] == 4


def test_leitura_rv4():
    rel2 = Relato.le_arquivo("tests/_arquivos", "relato.rv4")
    assert rel2.cmo_medio_subsistema.shape[1] == 3
