from idecomp.decomp.inviabunic import InviabUnic

from tests.mocks.arquivos.inviab_unic import MockInviabUnic

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch


def test_bloco_inviabilidades_iteracao():
    m: MagicMock = mock_open(read_data="".join(MockInviabUnic))
    with patch("builtins.open", m):
        inv = InviabUnic.le_arquivo("").inviabilidades_iteracoes
        assert inv.iloc[0, 0] == 1
        assert inv.iloc[0, 4] == "IRRIGACAO, USINA BARRA GRANDE"
        assert inv.iloc[0, 5] == 0.6
        assert inv.iloc[0, 6] == "m3/s"
        assert inv.iloc[-1, 0] == 105


# def test_atributos_encontrados_inviabunic():
#     m: MagicMock = mock_open(read_data="".join(MockInviabUnic))
#     with patch("builtins.open", m):
#         inv = InviabUnic.le_arquivo("")
#         assert inv.inviabilidades_iteracoes is not None
#         assert inv.inviabilidades_simulacao_final is not None


# def test_atributos_nao_encontrados_inviabunic():
#     m: MagicMock = mock_open(read_data="")
#     with patch("builtins.open", m):
#         inv = InviabUnic.le_arquivo("")
#         assert inv.inviabilidades_iteracoes is None
#         assert inv.inviabilidades_simulacao_final is None


# def test_eq_inviabunic():
#     m: MagicMock = mock_open(read_data="".join(MockInviabUnic))
#     with patch("builtins.open", m):
#         inv1 = InviabUnic.le_arquivo("")
#         inv2 = InviabUnic.le_arquivo("")
#         assert inv1 == inv2


# def test_neq_inviabunic():
#     m: MagicMock = mock_open(read_data="".join(MockInviabUnic))
#     with patch("builtins.open", m):
#         inv1 = InviabUnic.le_arquivo("")
#         inv2 = InviabUnic.le_arquivo("")
#         inv2.inviabilidades_iteracoes.loc[0, 0] = 50
#         assert inv1 != inv2
