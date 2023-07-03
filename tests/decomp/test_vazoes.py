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
