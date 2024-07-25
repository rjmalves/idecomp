from idecomp.decomp.modelos.mapcut import SecaoDadosMapcut
from idecomp.decomp.mapcut import Mapcut
from os.path import join


ARQ_TEST = "./tests/mocks/arquivos/mapcut.rv2"


def test_secao_dados_mapcut():
    r = SecaoDadosMapcut()
    with open(join(ARQ_TEST), "rb") as fp:
        r.read(fp, storage="BINARY")

    assert r.numero_iteracoes == 21
    assert r.numero_cortes == 21 * 3
    assert r.numero_submercados == 5
    assert r.numero_uhes == 165
    assert r.numero_cenarios == 356
    assert r.tamanho_corte == 26976
    assert len(r.codigos_uhes) == 165
    assert len(r.codigos_uhes_jusante) == 165
    assert len(r.indice_no_arvore) == 356
    assert r.numero_estagios == 4
    assert r.numero_semanas == 3
    assert r.numero_uhes_tempo_viagem == 2
    assert r.maximo_lag_tempo_viagem == 3
    assert len(r.indice_primeiro_no_estagio) == 4
    assert r.patamares_por_estagio == [3] * 4


def test_atributos_encontrados_mapcut():
    m = Mapcut.read(ARQ_TEST)

    assert m.numero_iteracoes is not None
    assert m.numero_cortes is not None
    assert m.numero_submercados is not None
    assert m.numero_uhes is not None
    assert m.numero_cenarios is not None
    assert m.tamanho_corte is not None
    assert m.codigos_uhes is not None
    assert m.codigos_uhes_jusante is not None
    assert m.indice_no_arvore is not None
    assert m.numero_estagios is not None
    assert m.numero_semanas is not None
    assert m.numero_uhes_tempo_viagem is not None
    assert m.maximo_lag_tempo_viagem is not None
    assert m.indice_primeiro_no_estagio is not None
    assert m.patamares_por_estagio is not None


def test_eq_mapcut():
    h1 = Mapcut.read(ARQ_TEST)
    h2 = Mapcut.read(ARQ_TEST)
    assert h1 == h2
