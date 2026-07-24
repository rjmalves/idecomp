from idecomp.decomp.modelos.mlt import SecaoMlt
from idecomp.decomp.mlt import Mlt

from os.path import join
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch


ARQ_TEST = "./tests/mocks/arquivos/mlt.dat"


def test_secao_mlt():
    r = SecaoMlt()
    with open(join(ARQ_TEST), "rb") as fp:
        r.read(fp, storage="BINARY")

    assert len(r.data) == SecaoMlt.NUMERO_MESES * SecaoMlt.NUMERO_POSTOS
    assert r.data[0] == 242
    assert r.data[65] == 14678


def test_atributos_encontrados_mlt():
    h = Mlt.read(ARQ_TEST)
    assert h.valores is not None


def test_valores_mlt():
    h = Mlt.read(ARQ_TEST)
    df = h.valores
    assert df["mes"].tolist() == list(range(1, 13))
    assert df.at[0, "1"] == 242
    assert df.at[11, "1"] == 174
    assert df.at[0, "66"] == 14678


def test_eq_mlt():
    h1 = Mlt.read(ARQ_TEST)
    h2 = Mlt.read(ARQ_TEST)
    assert h1 == h2


def test_neq_mlt():
    h1 = Mlt.read(ARQ_TEST)
    h2 = Mlt.read(ARQ_TEST)
    df = h2.valores
    df["1"] = -1
    h2.valores = df
    assert h1 != h2


def test_leitura_escrita_mlt():
    h1 = Mlt.read(ARQ_TEST)
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
        h2 = Mlt.read(ARQ_TEST)
        assert h1 == h2
