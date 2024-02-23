from idecomp.decomp.dec_oper_usit import DecOperUsit

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_oper_usit import (
    MockDecOperUsit,
    MockDecOperUsitv31,
)


def test_atributos_encontrados_dec_oper_usit():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsit))
    with patch("builtins.open", m):
        rel = DecOperUsit.read("./tests/mocks/arquivos/dec_oper_usit.py")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "no"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "duracao"] == 40.00
        assert rel.tabela.at[0, "codigo_usina"] == 86
        assert rel.tabela.at[0, "nome_usina"] == "SANTA CRUZ"
        assert rel.tabela.at[0, "codigo_submercado"] == 1
        assert rel.tabela.at[0, "nome_submercado"] == "SE"
        assert rel.tabela.at[0, "custo_incremental"] == 116.57
        assert rel.tabela.at[0, "geracao_minima_MW"] == 0.0
        assert rel.tabela.at[0, "geracao_MW"] == 350.00
        assert rel.tabela.at[0, "fator_manutencao"] == 1.0
        assert rel.tabela.at[0, "geracao_maxima_MW"] == 350.00
        assert rel.tabela.at[0, "custo_geracao"] == 1631.98


def test_eq_dec_oper_usit():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsit))
    with patch("builtins.open", m):
        rel1 = DecOperUsit.read("./tests/mocks/arquivos/dec_oper_usit.py")
        rel2 = DecOperUsit.read("./tests/mocks/arquivos/dec_oper_usit.py")
        assert rel1 == rel2


def test_neq_dec_oper_usit():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsit))
    with patch("builtins.open", m):
        rel1 = DecOperUsit.read("./tests/mocks/arquivos/dec_oper_usit.py")
        rel2 = DecOperUsit.read("./tests/mocks/arquivos/dec_oper_usit.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2


def test_atributos_encontrados_dec_oper_usit_v31():
    m: MagicMock = mock_open(read_data="".join(MockDecOperUsitv31))
    with patch("builtins.open", m):
        DecOperUsit.set_version("31.0.2")
        rel = DecOperUsit.read("./tests/mocks/arquivos/dec_oper_usit.py")
        assert rel.versao == "31.0.2"
        assert rel.tabela.at[0, "estagio"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "duracao"] == 36.0
        assert rel.tabela.at[0, "codigo_usina"] == 86
        assert rel.tabela.at[0, "nome_usina"] == "SANTA CRUZ"
        assert rel.tabela.at[0, "codigo_submercado"] == 1
        assert rel.tabela.at[0, "nome_submercado"] == "SE"
        assert rel.tabela.at[0, "custo_incremental"] == 155.86
        assert rel.tabela.at[0, "geracao_minima_MW"] == 0.0
        assert rel.tabela.at[0, "geracao_MW"] == 0.0
        assert rel.tabela.at[0, "fator_manutencao"] == 1.0
        assert rel.tabela.at[0, "geracao_maxima_MW"] == 500.0
        assert rel.tabela.at[0, "custo_geracao"] == 0.0
