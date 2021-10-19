# Rotinas de testes associadas ao arquivo relato.rvx do DECOMP
from idecomp.decomp.relgnl import RelGNL


rel = RelGNL.le_arquivo("tests/_arquivos", "relgnl.rv0")


def test_usinas_termicas():
    usinas = rel.usinas_termicas
    assert float(usinas.loc[(usinas["Código"] == 86) &
                            (usinas["Estágio"] == 1),
                            "Custo GT Pat 1"]) == 133.15


def test_comandos_registros_tg():
    com = rel.comandos_usinas_registros_tg
    assert float(com.loc[(com["Código"] == 86) &
                         (com["Semana"] == "28/12/2019"),
                         "Pat 1"]) == 350.00


def test_comandos_restricoes_eletricas():
    com = rel.comandos_usinas_restricoes_eletricas
    assert float(com.loc[(com["Código"] == 86) &
                         (com["Período"] == 1),
                         "Pat 1"]) == 350.00


def test_relatorio_operacao():
    ope = rel.relatorio_operacao_termica
    assert float(ope.loc[(ope["Usina"] == "SANTA CRUZ") &
                         (ope["Estágio"] == "MENSAL"),
                         "Custo"]) == 33373.8
