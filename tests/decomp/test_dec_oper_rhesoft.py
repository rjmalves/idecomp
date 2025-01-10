from idecomp.decomp.dec_oper_rhesoft import DecOperRheSoft

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_oper_rhesoft import (
    MockDecOperRheSoft,
    MockDecOperRheSoftv31,
)


def test_atributos_encontrados_dec_oper_rhesoft():
    m: MagicMock = mock_open(read_data="".join(MockDecOperRheSoft))
    with patch("builtins.open", m):
        rel = DecOperRheSoft.read("./tests/mocks/arquivos/dec_oper_rhesoft.py")
        assert rel.versao == "32.1"
        assert rel.tabela.at[0, "estagio"] == 6
        assert rel.tabela.at[0, "no"] == 6
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "codigo_restricao"] == 101
        assert rel.tabela.at[0, "limite_MW"] == 10191.52
        assert rel.tabela.at[0, "valor_MW"] == 38573.58
        assert rel.tabela.at[0, "violacao_absoluta_MW"] == 0.00
        assert rel.tabela.at[0, "violacao_percentual"] == 0.000000


def test_eq_dec_oper_rhesoft():
    m: MagicMock = mock_open(read_data="".join(MockDecOperRheSoft))
    with patch("builtins.open", m):
        rel1 = DecOperRheSoft.read(
            "./tests/mocks/arquivos/dec_oper_rhesoft.py"
        )
        rel2 = DecOperRheSoft.read(
            "./tests/mocks/arquivos/dec_oper_rhesoft.py"
        )
        assert rel1 == rel2


def test_neq_dec_oper_rhesoft():
    m: MagicMock = mock_open(read_data="".join(MockDecOperRheSoft))
    with patch("builtins.open", m):
        rel1 = DecOperRheSoft.read(
            "./tests/mocks/arquivos/dec_oper_rhesoft.py"
        )
        rel2 = DecOperRheSoft.read(
            "./tests/mocks/arquivos/dec_oper_rhesoft.py"
        )
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2


def test_atributos_encontrados_dec_oper_rhesoft_v31():
    m: MagicMock = mock_open(read_data="".join(MockDecOperRheSoftv31))
    with patch("builtins.open", m):
        DecOperRheSoft.set_version("31.0.2")
        rel = DecOperRheSoft.read("./tests/mocks/arquivos/dec_oper_rhesoft.py")
        assert rel.versao == "31.0.2"
        assert rel.tabela.at[0, "estagio"] == 6
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "codigo_restricao"] == 101
        assert rel.tabela.at[0, "limite_MW"] == 10191.52
        assert rel.tabela.at[0, "valor_MW"] == 38573.58
        assert rel.tabela.at[0, "violacao_absoluta_MW"] == 0.00
        assert rel.tabela.at[0, "violacao_percentual"] == 0.000000
