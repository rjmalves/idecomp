import numpy as np

from idecomp.decomp.modelos.vazoes import SecaoVazoesPostos
from idecomp.decomp.vazoes import Vazoes

from os.path import join
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch


ARQ_TEST = "./tests/mocks/arquivos/vazoes.rv0"


def test_secao_vazoes_postos():
    r = SecaoVazoesPostos()
    with open(join(ARQ_TEST), "rb") as fp:
        r.read(fp, storage="BINARY")

    assert r.numero_postos == 320


def test_atributos_encontrados_vazoes():
    h = Vazoes.read(ARQ_TEST)
    assert h.probabilidades is not None
    assert h.previsoes is not None
    assert h.previsoes_com_postos_artificiais is not None
    assert h.cenarios_gerados is not None
    assert h.cenarios_calculados_com_postos_artificiais is not None


def test_eq_vazoes():
    h1 = Vazoes.read(ARQ_TEST)
    h2 = Vazoes.read(ARQ_TEST)
    assert h1 == h2


def test_neq_vazoes():
    h1 = Vazoes.read(ARQ_TEST)
    h2 = Vazoes.read(ARQ_TEST)
    df = h2.probabilidades
    df["probabilidade"] = -1.0
    h2.probabilidades = df
    assert h1 != h2


def test_leitura_escrita_vazoes():
    h1 = Vazoes.read(ARQ_TEST)
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        h1.write(ARQ_TEST)
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data=b"".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        h2 = Vazoes.read(ARQ_TEST)
        assert h1 == h2


def _registro(valores, dtype=np.int32) -> bytes:
    r = np.zeros(SecaoVazoesPostos.TAMANHO_REGISTRO, dtype=dtype)
    r[: len(valores)] = valores
    return r.tobytes()


def _nos_estocasticos(aberturas, numero_semanas):
    return [
        (e, k)
        for e in range(numero_semanas + 1, len(aberturas) + 1)
        for k in range(1, aberturas[e - 1] + 1)
    ]


def _arquivo_sintetico(aberturas, numero_semanas) -> bytes:
    # Cada registro recebe um marcador próprio, para que qualquer
    # desalinhamento na leitura apareça nos valores lidos.
    n = SecaoVazoesPostos.TAMANHO_REGISTRO
    nos = _nos_estocasticos(aberturas, numero_semanas)
    probs = [1.0 / a for a in aberturas for _ in range(a)]
    return b"".join(
        [
            _registro([3, len(aberturas), *aberturas, n]),
            _registro([1, 2, 3]),
            _registro([numero_semanas, 0, 1, 2025, n, 2]),
            _registro(probs, dtype=np.float32),
            *[_registro([100 + s] * n) for s in range(numero_semanas)],
            *[_registro([1000 * e + k] * n) for e, k in nos],
            *[_registro([200 + s] * n) for s in range(numero_semanas)],
            *[_registro([-(1000 * e + k)] * n) for e, k in nos],
            *[_registro([300 + m] * n) for m in range(11)],
            *[_registro([400 + s] * n) for s in range(2)],
        ]
    )


def _verifica_leitura_estagios_estocasticos(aberturas, numero_semanas):
    m: MagicMock = mock_open(
        read_data=_arquivo_sintetico(aberturas, numero_semanas)
    )
    with patch("builtins.open", m):
        h = Vazoes.read(ARQ_TEST)
    nos = _nos_estocasticos(aberturas, numero_semanas)
    estagios = [e for e, _ in nos]
    cenarios = [k for _, k in nos]

    df = h.cenarios_gerados
    assert df["estagio"].tolist() == estagios
    assert df["cenario"].tolist() == cenarios
    assert df["1"].tolist() == [1000 * e + k for e, k in nos]
    df = h.cenarios_calculados_com_postos_artificiais
    assert df["estagio"].tolist() == estagios
    assert df["cenario"].tolist() == cenarios
    assert df["1"].tolist() == [-(1000 * e + k) for e, k in nos]
    assert h.previsoes_com_postos_artificiais["1"].tolist() == [
        200 + s for s in range(numero_semanas)
    ]
    assert h.observacoes_mensais["1"].tolist() == list(range(300, 311))
    assert h.observacoes_semanais["1"].tolist() == [400, 401]
    df = h.probabilidades
    assert df["estagio"].tolist() == (
        list(range(1, numero_semanas + 1)) + estagios
    )
    assert df["cenario"].tolist() == [1] * numero_semanas + cenarios


def test_leitura_vazoes_estagios_mensais_sem_aberturas():
    _verifica_leitura_estagios_estocasticos([1] * 8, 6)


def test_leitura_vazoes_multiplos_estagios_com_aberturas():
    _verifica_leitura_estagios_estocasticos([1] * 6 + [3, 4], 6)
