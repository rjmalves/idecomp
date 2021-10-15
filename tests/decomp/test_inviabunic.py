# Rotinas de testes associadas ao arquivo relato.rvx do DECOMP
from idecomp.decomp.inviabunic import InviabUnic


inv = InviabUnic.le_arquivo("tests/_arquivos",
                            "inviab_unic.rv0")


def test_leitura():
    n_invs = inv.inviabilidades_iteracoes.shape[0]
    assert n_invs == 1667


def test_inviabilidades_iteracoes():
    invs = inv.inviabilidades_iteracoes
    assert invs.loc[1, "Violação"] == 15.76605418


def test_inviabilidades_simulacao_final():
    invs = inv.inviabilidades_simulacao_final
    assert invs.empty
