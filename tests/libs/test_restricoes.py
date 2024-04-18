from datetime import datetime
from idecomp.libs.modelos.restricoes import (
    RegistroRestricaoEletricaHorizontePeriodo,
    RegistroRestricaoEletricaHorizonteData,
    RegistroRestricaoEletricaFormulaPeriodoPatamar,
    RegistroRestricaoEletricaFormulaDataPatamar,
    RegistroRestricaoEletricaFormula,
    RegistroRestricaoEletricaHabilita,
    RegistroRestricaoEletricaLimitesFormulaDataPatamar,
    RegistroRestricaoEletricaLimitesFormulaPeriodoPatamar,
    RegistroRestricaoEletricaRegraAtivacao,
    RegistroRestricaoEletricaTratamentoViolacaoPeriodo,
    RegistroRestricaoEletricaTratamentoViolacao,
    RegistroAliasEletricoValorPeriodoPatamar,
    RegistroAliasEletrico,
    RegistroReHorizPer,
    RegistroReHorizData,
    RegistroRePerPat,
    RegistroReDataPat,
    RegistroReLimFormPerPat,
    RegistroReLimFormDataPat,
    RegistroAliasEletValPerPat,
    RegistroAliasElet,
    RegistroReRegraAtiva,
    RegistroReHabilita,
    RegistroReTratViolPer,
    RegistroReTratViol,
    RegistroRe,
)

from idecomp.libs.restricoes import Restricoes

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.restricoes_libs import (
    MockRestricaoEletrica,
    MockRestricaoEletricaFormula,
    MockRestricaoEletricaFormulaDataPatamar,
    MockRestricaoEletricaFormulaPeriodoPatamar,
    MockRestricaoEletricaHabilita,
    MockRestricaoEletricaHorizonteData,
    MockRestricaoEletricaHorizontePeriodo,
    MockRestricaoEletricaLimitesFormulaDataPatamar,
    MockRestricaoEletricaLimitesFormulaPeriodoPatamar,
    MockRestricaoEletricaRegraAtivacao,
    MockRestricaoEletricaTratamentoViolacao,
    MockRestricaoEletricaTratamentoViolacaoPeriodo,
    MockAliasEletrico,
    MockAliasEletricoValorPeriodoPatamar,
    MockReHorizPer,
    MockReHorizData,
    MockRe,
    MockRePerPat,
    MockReDataPat,
    MockReLimFormPerPat,
    MockReLimFormDataPat,
    MockAliasElet,
    MockAliasEletValPerPat,
    MockReRegraAtiva,
    MockReHabilita,
    MockReTratViol,
    MockReTratViolPer,
    MockRestricoes,
)

ARQ_TESTE = "./tests/mocks/arquivos/__init__.py"


def test_registro_re_horiz_per():
    m: MagicMock = mock_open(read_data="".join(MockReHorizPer))
    r = RegistroReHorizPer()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [701, 1, 6]
    assert r.codigo_restricao == 701
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio_inicio == 1
    r.estagio_inicio = 0
    assert r.estagio_inicio == 0
    assert r.estagio_fim == 6
    r.estagio_fim = 0
    assert r.estagio_fim == 0


def test_registro_restricao_eletrica_horizonte_periodo():
    m: MagicMock = mock_open(
        read_data="".join(MockRestricaoEletricaHorizontePeriodo)
    )
    r = RegistroRestricaoEletricaHorizontePeriodo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [701, 1, 6]
    assert r.codigo_restricao == 701
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio_inicio == 1
    r.estagio_inicio = 0
    assert r.estagio_inicio == 0
    assert r.estagio_fim == 6
    r.estagio_fim = 0
    assert r.estagio_fim == 0


def test_registro_re_horiz_data():
    m: MagicMock = mock_open(read_data="".join(MockReHorizData))
    r = RegistroReHorizData()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [701, datetime(2021, 1, 1), datetime(2022, 2, 1)]
    assert r.codigo_restricao == 701
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.data_inicio == datetime(2021, 1, 1)
    r.data_inicio = 0
    assert r.data_inicio == 0
    assert r.data_fim == datetime(2022, 2, 1)
    r.data_fim = 0
    assert r.data_fim == 0


def test_registro_restricao_eletrica_horizente_data():
    m: MagicMock = mock_open(
        read_data="".join(MockRestricaoEletricaHorizonteData)
    )
    r = RegistroRestricaoEletricaHorizonteData()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [701, datetime(2021, 1, 1), datetime(2022, 2, 1)]
    assert r.codigo_restricao == 701
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.data_inicio == datetime(2021, 1, 1)
    r.data_inicio = 0
    assert r.data_inicio == 0
    assert r.data_fim == datetime(2022, 2, 1)
    r.data_fim = 0
    assert r.data_fim == 0


def test_registro_re():
    m: MagicMock = mock_open(read_data="".join(MockRe))
    r = RegistroRe()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [702, "re(405) + constante_aditiva"]
    assert r.codigo_restricao == 702
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.formula == "re(405) + constante_aditiva"
    r.formula = "teste"
    assert r.formula == "teste"


def test_registro_restricao_eletrica_formula():
    m: MagicMock = mock_open(read_data="".join(MockRestricaoEletricaFormula))
    r = RegistroRestricaoEletricaFormula()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [702, "re(405) + constante_aditiva"]
    assert r.codigo_restricao == 702
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.formula == "re(405) + constante_aditiva"
    r.formula = "teste"
    assert r.formula == "teste"


def test_registro_re_per_pat():
    m: MagicMock = mock_open(read_data="".join(MockRePerPat))
    r = RegistroRePerPat()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [702, 1, None, None, "re(405) + constante_aditiva"]
    assert r.codigo_restricao == 702
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio_inicio == 1
    r.estagio_inicio = 0
    assert r.estagio_inicio == 0
    assert r.estagio_fim is None
    r.estagio_fim = 0
    assert r.estagio_fim == 0
    assert r.patamar is None
    r.patamar = 0
    assert r.patamar == 0
    assert r.formula == "re(405) + constante_aditiva"
    r.formula = "teste"
    assert r.formula == "teste"


def test_registro_restricao_eletrica_formula_periodo_patamar():
    m: MagicMock = mock_open(
        read_data="".join(MockRestricaoEletricaFormulaPeriodoPatamar)
    )
    r = RegistroRestricaoEletricaFormulaPeriodoPatamar()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [702, 1, None, None, "re(405) + constante_aditiva"]
    assert r.codigo_restricao == 702
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio_inicio == 1
    r.estagio_inicio = 0
    assert r.estagio_inicio == 0
    assert r.estagio_fim is None
    r.estagio_fim = 0
    assert r.estagio_fim == 0
    assert r.patamar is None
    r.patamar = 0
    assert r.patamar == 0
    assert r.formula == "re(405) + constante_aditiva"
    r.formula = "teste"
    assert r.formula == "teste"


def test_registro_re_data_pat():
    m: MagicMock = mock_open(read_data="".join(MockReDataPat))
    r = RegistroReDataPat()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        702,
        datetime(2021, 1, 1),
        None,
        None,
        "re(405) + constante_aditiva",
    ]
    assert r.codigo_restricao == 702
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.data_inicio == datetime(2021, 1, 1)
    r.data_inicio = 0
    assert r.data_inicio == 0
    assert r.data_fim is None
    r.data_fim = 0
    assert r.data_fim == 0
    assert r.patamar is None
    r.patamar = 0
    assert r.patamar == 0
    assert r.formula == "re(405) + constante_aditiva"
    r.formula = "teste"
    assert r.formula == "teste"


def test_registro_restricao_eletrica_formula_data_patamar():
    m: MagicMock = mock_open(
        read_data="".join(MockRestricaoEletricaFormulaDataPatamar)
    )
    r = RegistroRestricaoEletricaFormulaDataPatamar()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        702,
        datetime(2021, 1, 1),
        None,
        None,
        "re(405) + constante_aditiva",
    ]
    assert r.codigo_restricao == 702
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.data_inicio == datetime(2021, 1, 1)
    r.data_inicio = 0
    assert r.data_inicio == 0
    assert r.data_fim is None
    r.data_fim = 0
    assert r.data_fim == 0
    assert r.patamar is None
    r.patamar = 0
    assert r.patamar == 0
    assert r.formula == "re(405) + constante_aditiva"
    r.formula = "teste"
    assert r.formula == "teste"


def test_registro_re_lim_form_per_pat():
    m: MagicMock = mock_open(read_data="".join(MockReLimFormPerPat))
    r = RegistroReLimFormPerPat()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [701, 1, 6, 1, None, 4100]
    assert r.codigo_restricao == 701
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio_inicio == 1
    r.estagio_inicio = 0
    assert r.estagio_inicio == 0
    assert r.estagio_fim == 6
    r.estagio_fim = 0
    assert r.estagio_fim == 0
    assert r.patamar == 1
    r.patamar = 0
    assert r.patamar == 0
    assert r.limite_inferior is None
    r.limite_inferior = 0
    assert r.limite_inferior == 0
    assert r.limite_superior == 4100
    r.limite_superior = 0
    assert r.limite_superior == 0


def test_registro_restricao_eletrica_limite_formula_periodo_patamar():
    m: MagicMock = mock_open(
        read_data="".join(MockRestricaoEletricaLimitesFormulaPeriodoPatamar)
    )
    r = RegistroRestricaoEletricaLimitesFormulaPeriodoPatamar()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [701, 1, 6, 1, None, 4100]
    assert r.codigo_restricao == 701
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio_inicio == 1
    r.estagio_inicio = 0
    assert r.estagio_inicio == 0
    assert r.estagio_fim == 6
    r.estagio_fim = 0
    assert r.estagio_fim == 0
    assert r.patamar == 1
    r.patamar = 0
    assert r.patamar == 0
    assert r.limite_inferior is None
    r.limite_inferior = 0
    assert r.limite_inferior == 0
    assert r.limite_superior == 4100
    r.limite_superior = 0
    assert r.limite_superior == 0


def test_registro_re_lim_form_data_pat():
    m: MagicMock = mock_open(read_data="".join(MockReLimFormDataPat))
    r = RegistroReLimFormDataPat()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [701, datetime(2021, 1, 1), None, 1, None, 4100]
    assert r.codigo_restricao == 701
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.data_inicio == datetime(2021, 1, 1)
    r.data_inicio = 0
    assert r.data_inicio == 0
    assert r.data_fim is None
    r.data_fim = 0
    assert r.data_fim == 0
    assert r.patamar == 1
    r.patamar = 0
    assert r.patamar == 0
    assert r.limite_inferior is None
    r.limite_inferior = 0
    assert r.limite_inferior == 0
    assert r.limite_superior == 4100
    r.limite_superior = 0
    assert r.limite_superior == 0


def test_registro_restricao_eletrica_limite_formula_data_patamar():
    m: MagicMock = mock_open(
        read_data="".join(MockRestricaoEletricaLimitesFormulaDataPatamar)
    )
    r = RegistroRestricaoEletricaLimitesFormulaDataPatamar()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [701, datetime(2021, 1, 1), None, 1, None, 4100]
    assert r.codigo_restricao == 701
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.data_inicio == datetime(2021, 1, 1)
    r.data_inicio = 0
    assert r.data_inicio == 0
    assert r.data_fim is None
    r.data_fim = 0
    assert r.data_fim == 0
    assert r.patamar == 1
    r.patamar = 0
    assert r.patamar == 0
    assert r.limite_inferior is None
    r.limite_inferior = 0
    assert r.limite_inferior == 0
    assert r.limite_superior == 4100
    r.limite_superior = 0
    assert r.limite_superior == 0


def test_registro_alias_elet():
    m: MagicMock = mock_open(read_data="".join(MockAliasElet))
    r = RegistroAliasElet()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, "constante_aditiva"]
    assert r.codigo_alias == 1
    r.codigo_alias = 0
    assert r.codigo_alias == 0
    assert r.identificador_alias == "constante_aditiva"
    r.identificador_alias = "teste"
    assert r.identificador_alias == "teste"


def test_registro_alias_eletrico():
    m: MagicMock = mock_open(read_data="".join(MockAliasEletrico))
    r = RegistroAliasEletrico()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, "constante_aditiva"]
    assert r.codigo_alias == 1
    r.codigo_alias = 0
    assert r.codigo_alias == 0
    assert r.identificador_alias == "constante_aditiva"
    r.identificador_alias = "teste"
    assert r.identificador_alias == "teste"


def test_registro_alias_elet_val_per_pat():
    m: MagicMock = mock_open(read_data="".join(MockAliasEletValPerPat))
    r = RegistroAliasEletValPerPat()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, None, 1, 1000]
    assert r.codigo_alias == 1
    r.codigo_alias = 0
    assert r.codigo_alias == 0
    assert r.estagio_inicio == 1
    r.estagio_inicio = 0
    assert r.estagio_inicio == 0
    assert r.estagio_fim is None
    r.estagio_fim = 0
    assert r.estagio_fim == 0
    assert r.patamar == 1
    r.patamar = 0
    assert r.patamar == 0
    assert r.valor == 1000
    r.valor = 0
    assert r.valor == 0


def test_registro_alias_eletrico_valor_periodo_patamar():
    m: MagicMock = mock_open(
        read_data="".join(MockAliasEletricoValorPeriodoPatamar)
    )
    r = RegistroAliasEletricoValorPeriodoPatamar()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, None, 1, 1000]
    assert r.codigo_alias == 1
    r.codigo_alias = 0
    assert r.codigo_alias == 0
    assert r.estagio_inicio == 1
    r.estagio_inicio = 0
    assert r.estagio_inicio == 0
    assert r.estagio_fim is None
    r.estagio_fim = 0
    assert r.estagio_fim == 0
    assert r.patamar == 1
    r.patamar = 0
    assert r.patamar == 0
    assert r.valor == 1000
    r.valor = 0
    assert r.valor == 0


def test_registro_re_regra_ativa():
    m: MagicMock = mock_open(read_data="".join(MockReRegraAtiva))
    r = RegistroReRegraAtiva()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [62, "53000 < demanda_sin & demanda_sin <= 63000"]
    assert r.codigo_regra_ativacao == 62
    r.codigo_regra_ativacao = 0
    assert r.codigo_regra_ativacao == 0
    assert r.regra_ativacao == "53000 < demanda_sin & demanda_sin <= 63000"
    r.regra_ativacao = "teste"
    assert r.regra_ativacao == "teste"


def test_registro_restricao_eletrica_regra_ativacao():
    m: MagicMock = mock_open(
        read_data="".join(MockRestricaoEletricaRegraAtivacao)
    )
    r = RegistroRestricaoEletricaRegraAtivacao()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [62, "53000 < demanda_sin & demanda_sin <= 63000"]
    assert r.codigo_regra_ativacao == 62
    r.codigo_regra_ativacao = 0
    assert r.codigo_regra_ativacao == 0
    assert r.regra_ativacao == "53000 < demanda_sin & demanda_sin <= 63000"
    r.regra_ativacao = "teste"
    assert r.regra_ativacao == "teste"


def test_registro_re_habilita():
    m: MagicMock = mock_open(read_data="".join(MockReHabilita))
    r = RegistroReHabilita()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [703, 61]
    assert r.codigo_restricao == 703
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.codigo_regra_ativacao == 61
    r.codigo_regra_ativacao = 0
    assert r.codigo_regra_ativacao == 0


def test_registro_restricao_eletrica_habilita():
    m: MagicMock = mock_open(read_data="".join(MockRestricaoEletricaHabilita))
    r = RegistroRestricaoEletricaHabilita()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [703, 61]
    assert r.codigo_restricao == 703
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.codigo_regra_ativacao == 61
    r.codigo_regra_ativacao = 0
    assert r.codigo_regra_ativacao == 0


def test_registro_re_trat_viol():
    m: MagicMock = mock_open(read_data="".join(MockReTratViol))
    r = RegistroReTratViol()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [701, "hard", 1]
    assert r.codigo_restricao == 701
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.tipo_violacao == "hard"
    r.tipo_violacao = "teste"
    assert r.tipo_violacao == "teste"
    assert r.custo_violacao == 1
    r.custo_violacao = 0
    assert r.custo_violacao == 0


def test_registro_restricao_eletrica_tratamento_violacao():
    m: MagicMock = mock_open(
        read_data="".join(MockRestricaoEletricaTratamentoViolacao)
    )
    r = RegistroRestricaoEletricaTratamentoViolacao()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [701, "hard", 1]
    assert r.codigo_restricao == 701
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.tipo_violacao == "hard"
    r.tipo_violacao = "teste"
    assert r.tipo_violacao == "teste"
    assert r.custo_violacao == 1
    r.custo_violacao = 0
    assert r.custo_violacao == 0


def test_registro_re_trat_viol_per():
    m: MagicMock = mock_open(read_data="".join(MockReTratViolPer))
    r = RegistroReTratViolPer()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [701, 1, 6, "hard", 1000]
    assert r.codigo_restricao == 701
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio_inicio == 1
    r.estagio_inicio = 0
    assert r.estagio_inicio == 0
    assert r.estagio_fim == 6
    r.estagio_fim = 0
    assert r.estagio_fim == 0
    assert r.tipo_violacao == "hard"
    r.tipo_violacao = "teste"
    assert r.tipo_violacao == "teste"
    assert r.custo_violacao == 1000
    r.custo_violacao = 0
    assert r.custo_violacao == 0


def test_registro_restricao_eletrica_tratamento_violacao_periodo():
    m: MagicMock = mock_open(
        read_data="".join(MockRestricaoEletricaTratamentoViolacaoPeriodo)
    )
    r = RegistroRestricaoEletricaTratamentoViolacaoPeriodo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [701, 1, 6, "hard", 1000]
    assert r.codigo_restricao == 701
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio_inicio == 1
    r.estagio_inicio = 0
    assert r.estagio_inicio == 0
    assert r.estagio_fim == 6
    r.estagio_fim = 0
    assert r.estagio_fim == 0
    assert r.tipo_violacao == "hard"
    r.tipo_violacao = "teste"
    assert r.tipo_violacao == "teste"
    assert r.custo_violacao == 1000
    r.custo_violacao = 0
    assert r.custo_violacao == 0


def test_atributos_encontrados_restricoes():
    m: MagicMock = mock_open(read_data="".join(MockRestricoes))
    with patch("builtins.open", m):
        e = Restricoes.read(ARQ_TESTE)
        assert len(e.re_horiz_per()) > 0
        assert len(e.restricao_eletrica_horizonte_periodo()) > 0
        assert len(e.alias_elet()) > 0
        assert len(e.alias_elet_val_per_pat()) > 0
        assert len(e.alias_eletrico_valor_periodo_patamar()) > 0
        assert len(e.re_per_pat()) > 0
        assert len(e.re_horiz_per()) > 0
        assert len(e.re_lim_form_per_pat()) > 0
        assert len(e.re_regra_ativa()) > 0
        assert len(e.restricao_eletrica_regra_ativacao()) > 0
        assert len(e.re_habilita()) > 0
        assert len(e.restricao_eletrica_habilita()) > 0


def test_eq_restricoes():
    m: MagicMock = mock_open(read_data="".join(MockRestricoes))
    with patch("builtins.open", m):
        cf1 = Restricoes.read(ARQ_TESTE)
        cf2 = Restricoes.read(ARQ_TESTE)
        assert cf1 == cf2


def test_neq_restricoes():
    m: MagicMock = mock_open(read_data="".join(MockRestricoes))
    with patch("builtins.open", m):
        cf1 = Restricoes.read(ARQ_TESTE)
        cf2 = Restricoes.read(ARQ_TESTE)
        cf2.data.remove(cf1.re_horiz_per()[0])
        assert cf1 != cf2


def test_leitura_escrita_restricoes():
    m_leitura: MagicMock = mock_open(read_data="".join(MockRestricoes))
    with patch("builtins.open", m_leitura):
        cf1 = Restricoes.read(ARQ_TESTE)
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        cf1.write(ARQ_TESTE)
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
        ]
        for li in linhas_escritas:
            print(li)
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        cf2 = Restricoes.read(ARQ_TESTE)
        assert cf1 == cf2
