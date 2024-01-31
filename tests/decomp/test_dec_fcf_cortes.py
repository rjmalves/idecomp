from idecomp.decomp.dec_fcf_cortes import DecFcfCortes
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_fcf_cortes import MockDecFcfCortes


def test_atributos_encontrados_dec_fcf_cortes():
    m: MagicMock = mock_open(read_data="".join(MockDecFcfCortes))
    with patch("builtins.open", m):
        rel = DecFcfCortes.read("./tests/mocks/arquivos/dec_fcf_cortes.py")
        assert rel.versao == "31.23"
        assert rel.tabela.at[0, "indice_iteracao"] == 1
        assert rel.tabela.at[0, "tipo_entidade"] == "RHS"
        assert rel.tabela.at[0, "indice_entidade"] == 0
        assert rel.tabela.at[0, "nome_entidade"] == "-"
        assert rel.tabela.at[0, "tipo_coeficiente"] == "RHS"
        assert rel.tabela.at[0, "indice_lag"] == 0
        assert rel.tabela.at[0, "indice_patamar"] == 0
        assert rel.tabela.at[0, "valor_coeficiente"] == -684638434.4554014
        assert rel.tabela.at[0, "unidade_coeficiente"] == "1000$"
        assert rel.tabela.at[0, "ponto_consultado"] == -338992.7207533
        assert rel.tabela.at[0, "unidade_ponto_consultado"] == "1000$"

        assert rel.tabela.at[1, "indice_iteracao"] == 1
        assert rel.tabela.at[1, "tipo_entidade"] == "USIH"
        assert rel.tabela.at[1, "indice_entidade"] == 1
        assert rel.tabela.at[1, "nome_entidade"] == "CAMARGOS"
        assert rel.tabela.at[1, "tipo_coeficiente"] == "VARM"
        assert rel.tabela.at[1, "indice_lag"] == 0
        assert rel.tabela.at[1, "indice_patamar"] == 0
        assert rel.tabela.at[1, "valor_coeficiente"] == 0.0002938
        assert rel.tabela.at[1, "unidade_coeficiente"] == "(1000$/hm3)"
        assert rel.tabela.at[1, "ponto_consultado"] == 493.2607041
        assert rel.tabela.at[1, "unidade_ponto_consultado"] == "hm3"


def test_eq_dec_fcf_cortes():
    m: MagicMock = mock_open(read_data="".join(MockDecFcfCortes))
    with patch("builtins.open", m):
        rel1 = DecFcfCortes.read("./tests/mocks/arquivos/dec_fcf_cortes.py")
        rel2 = DecFcfCortes.read("./tests/mocks/arquivos/dec_fcf_cortes.py")
        assert rel1 == rel2


def test_neq_dec_cortes_evap():
    m: MagicMock = mock_open(read_data="".join(MockDecFcfCortes))
    with patch("builtins.open", m):
        rel1 = DecFcfCortes.read("./tests/mocks/arquivos/dec_fcf_cortes.py")
        rel2 = DecFcfCortes.read("./tests/mocks/arquivos/dec_fcf_cortes.py")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
