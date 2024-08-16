from idecomp.decomp.modelos.mapcut import SecaoDadosMapcut
from idecomp.decomp.mapcut import Mapcut
from os.path import join
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch
import pytest

ARQ_TESTE = "./tests/mocks/arquivos/mapcut.rv2"


def test_secao_dados_mapcut():
    r = SecaoDadosMapcut()
    with open(join(ARQ_TESTE), "rb") as fp:
        r.read(fp, storage="BINARY")

    assert r.numero_iteracoes == 21
    assert r.numero_cortes == 21 * 3
    assert r.numero_submercados == 5
    assert r.numero_uhes == 165
    assert r.numero_cenarios == 356
    assert r.registro_ultimo_corte_no.shape == (356, 3)
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
    assert len(r.lag_tempo_viagem_por_uhe) == 2 * 4
    assert len(r.codigos_uhes_tempo_viagem) == 2
    assert r.dados_tempo_viagem.shape == (48, 5)
    assert len(r.codigos_submercados_gnl) == 2
    assert r.dados_gnl.shape == (4 * 2, 5)
    assert r.dados_custos.shape == (4, 7)


def test_atributos_encontrados_mapcut():
    m = Mapcut.read(ARQ_TESTE)

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


def test_atributos_nao_encontrados_mapcut():
    m: MagicMock = mock_open(read_data=b"")
    with pytest.raises(ValueError):
        with patch("builtins.open", m):
            h = Mapcut.read(ARQ_TESTE)


def test_eq_mapcut():
    h1 = Mapcut.read(ARQ_TESTE)
    h2 = Mapcut.read(ARQ_TESTE)
    assert h1 == h2


def test_secao_dados_mapcut():
    r = Mapcut.read(ARQ_TESTE)

    assert r.numero_iteracoes == 21
    assert r.numero_cortes == 21 * 3
    assert r.numero_submercados == 5
    assert r.numero_uhes == 165
    assert r.numero_cenarios == 356
    assert r.registro_ultimo_corte_no.shape == (356, 3)
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
    assert len(r.lag_tempo_viagem_por_uhe) == 2 * 4
    assert len(r.codigos_uhes_tempo_viagem) == 2
    assert r.dados_tempo_viagem.shape == (48, 5)
    assert len(r.codigos_submercados_gnl) == 2
    assert r.dados_gnl.shape == (4 * 2, 5)
    assert r.dados_custos.shape == (4, 7)
