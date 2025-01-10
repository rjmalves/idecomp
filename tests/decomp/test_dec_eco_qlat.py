from idecomp.decomp.dec_eco_qlat import DecEcoQlat
import numpy as np  # type: ignore
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_eco_qlat import MockDecEcoQlat


def test_atributos_encontrados_dec_eco_qlat():
    m: MagicMock = mock_open(read_data="".join(MockDecEcoQlat))
    with patch("builtins.open", m):
        rel = DecEcoQlat.read("./tests/mocks/arquivos/dec_eco_qlat.py")
        assert rel.versao == "32.1"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "codigo_usina"] == 146
        assert rel.tabela.at[0, "nome_usina"] == "FONTES C"
        assert rel.tabela.at[0, "fator_participacao_usina"] == 1.000
        assert rel.tabela.at[0, "tipo_entidade_jusante"] == "USIH"
        assert rel.tabela.at[0, "codigo_entidade_jusante"] == 147
        assert rel.tabela.at[0, "fator_participacao_entidade"] == 1.000
        assert np.isnan(rel.tabela.at[0, "vazao_incremental_media_m3s"])


def test_eq_dec_eco_qlat():
    m: MagicMock = mock_open(read_data="".join(MockDecEcoQlat))
    with patch("builtins.open", m):
        rel1 = DecEcoQlat.read("./tests/mocks/arquivos/dec_eco_qlat.py")
        rel2 = DecEcoQlat.read("./tests/mocks/arquivos/dec_eco_qlat.py")
        assert rel1 == rel2


def test_neq_dec_eco_qlat():
    m: MagicMock = mock_open(read_data="".join(MockDecEcoQlat))
    with patch("builtins.open", m):
        rel1 = DecEcoQlat.read("./tests/mocks/arquivos/dec_eco_qlat.py")
        rel2 = DecEcoQlat.read("./tests/mocks/arquivos/dec_eco_qlat.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
