from idecomp.decomp.dec_eco_discr import DecEcoDiscr

import numpy as np  # type: ignore
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_eco_discr import MockDecEcoDiscr


def test_atributos_encontrados_dec_eco_discr():
    m: MagicMock = mock_open(read_data="".join(MockDecEcoDiscr))
    with patch("builtins.open", m):
        rel = DecEcoDiscr.read("./tests/mocks/arquivos/dec_eco_discr.py")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "duracao"] == 40.0
        assert np.isnan(rel.tabela.at[0, "numero_patamares"])
        assert np.isnan(rel.tabela.at[0, "numero_aberturas"])


def test_eq_dec_eco_discr():
    m: MagicMock = mock_open(read_data="".join(MockDecEcoDiscr))
    with patch("builtins.open", m):
        rel1 = DecEcoDiscr.read("./tests/mocks/arquivos/dec_eco_discr.py")
        rel2 = DecEcoDiscr.read("./tests/mocks/arquivos/dec_eco_discr.py")
        assert rel1 == rel2


def test_neq_dec_eco_discr():
    m: MagicMock = mock_open(read_data="".join(MockDecEcoDiscr))
    with patch("builtins.open", m):
        rel1 = DecEcoDiscr.read("./tests/mocks/arquivos/dec_eco_discr.py")
        rel2 = DecEcoDiscr.read("./tests/mocks/arquivos/dec_eco_discr.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
