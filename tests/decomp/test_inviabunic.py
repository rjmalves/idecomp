from idecomp.decomp.inviabunic import InviabUnic

from tests.mocks.arquivos.inviab_unic import MockInviabUnic

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch


def test_bloco_inviabilidades_iteracao():
    m: MagicMock = mock_open(read_data="".join(MockInviabUnic))
    with patch("builtins.open", m):
        inv = InviabUnic.read(
            "./tests/mocks/arquivos/inviab_unic.py"
        ).inviabilidades_iteracoes
        assert inv.iloc[0, 0] == 1
        assert inv.iloc[0, 4] == "IRRIGACAO, USINA BARRA GRANDE"
        assert inv.iloc[0, 5] == 0.6
        assert inv.iloc[0, 6] == "m3/s"
        assert inv.iloc[-1, 0] == 105
