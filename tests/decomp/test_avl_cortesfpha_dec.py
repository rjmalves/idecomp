from idecomp.decomp.avl_cortesfpha_dec import AvlCortesFpha

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.avl_cortesfpha_dec import MockAvlCortesFpha


def test_atributos_encontrados_avl_cortesfpha_dec():
    m: MagicMock = mock_open(read_data="".join(MockAvlCortesFpha))
    with patch("builtins.open", m):
        rel = AvlCortesFpha.read(
            "./tests/mocks/arquivos/avl_cortesfpha_dec.py"
        )
        assert rel.versao == "31.23"

        assert rel.tabela.at[0, "codigo_usina"] == 1
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "nome_usina"] == "CAMARGOS"
        assert rel.tabela.at[0, "segmento_fpha"] == 1
        assert rel.tabela.at[0, "fator_correcao"] == 0.991429
        assert rel.tabela.at[0, "rhs"] == -9.42177264
        assert rel.tabela.at[0, "coeficiente_volume_util"] == 0.03350655
        assert rel.tabela.at[0, "coeficiente_vazao_turbinada"] == 0.18047226
        assert rel.tabela.at[0, "coeficiente_vazao_vertida"] == -0.00594416
        assert rel.tabela.at[0, "coeficiente_vazao_lateral"] == 0.00000000


def test_eq_avl_cortesfpha_dec():
    m: MagicMock = mock_open(read_data="".join(MockAvlCortesFpha))
    with patch("builtins.open", m):
        rel1 = AvlCortesFpha.read(
            "./tests/mocks/arquivos/avl_cortesfpha_dec.py"
        )
        rel2 = AvlCortesFpha.read(
            "./tests/mocks/arquivos/avl_cortesfpha_dec.py"
        )
        assert rel1 == rel2


def test_neq_avl_cortesfpha_dec():
    m: MagicMock = mock_open(read_data="".join(MockAvlCortesFpha))
    with patch("builtins.open", m):
        rel1 = AvlCortesFpha.read(
            "./tests/mocks/arquivos/avl_cortesfpha_dec.py"
        )
        rel2 = AvlCortesFpha.read(
            "./tests/mocks/arquivos/avl_cortesfpha_dec.py"
        )
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
