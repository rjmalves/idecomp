from idecomp.decomp.modelos.postos import RegistroPostos
from idecomp.decomp.postos import Postos

from os.path import join
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch


ARQ_TEST = "./tests/mocks/arquivos/postos.dat"


def test_registro_postos_postos():
    r = RegistroPostos()
    with open(join(ARQ_TEST), "rb") as fp:
        r.read(fp, storage="BINARY")

    assert len(r.data) == 3
    assert r.data[0] == "CAMARGOS"
    assert r.data[1] == 1931
    assert r.data[2] == 2019


def test_atributos_encontrados_postos():
    h = Postos.read(ARQ_TEST)
    assert h.postos is not None


def test_atributos_nao_encontrados_postos():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        ad = Postos.read(ARQ_TEST)
        assert ad.postos is None


def test_eq_postos():
    h1 = Postos.read(ARQ_TEST)
    h2 = Postos.read(ARQ_TEST)
    assert h1 == h2


def test_neq_postos():
    h1 = Postos.read(ARQ_TEST)
    h2 = Postos.read(ARQ_TEST)
    h2.postos.iloc[0, 0] = "TESTE"
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        h2.write(ARQ_TEST)
        assert h1 != h2


def test_leitura_escrita_postos():
    h1 = Postos.read(ARQ_TEST)
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        h1.write("./tests/mocks/arquivos/postos.dat")
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data=b"".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        h2 = Postos.read(ARQ_TEST)
        assert h1 == h2


def test_leitura_escrita_editando_postos():
    h1 = Postos.read(ARQ_TEST)
    vaz = h1.postos
    num_postos_original = vaz.shape[0]
    h1.postos.loc[vaz.shape[0]] = ["TESTE", 0, 0]
    m_escrita: MagicMock = mock_open(read_data="")
    # Testa aumentando a quantidade de postos
    with patch("builtins.open", m_escrita):
        h1.write(ARQ_TEST)
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
        assert len(linhas_escritas) == num_postos_original
    # Testa reduzindo a quantidade de postos
    num_postos_reduzidos = 10
    h1.postos.drop(
        index=list(range(num_postos_reduzidos, num_postos_original + 1)),
        inplace=True,
    )
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        h1.write(ARQ_TEST)
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
        assert len(linhas_escritas) == num_postos_reduzidos
