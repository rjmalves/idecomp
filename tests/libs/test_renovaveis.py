from idecomp.libs.renovaveis import Renovaveis
from idecomp.libs.modelos.renovaveis import (
    PEECadastro,
    PEESubmercado,
    PEEConfiguracaoPeriodo,
    PEEPotenciaInstaladaPeriodo,
    PEEGeracaoPeriodoPatamarCenario,
    PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal,
)
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.renovaveis import (
    MockRenovaveis,
    MockRenovaveisPeriodoFinal,
    MockPEECadastro,
    MockPEESubmercado,
    MockPEEConfiguracaoPeriodo,
    MockPEEPotenciaInstaladaPeriodo,
    MockPEEGeracaoPeriodoPatamarCenario,
    MockPEEGeracaoPeriodoPatamarCenarioComPeriodoFinal,
)

ARQ_TESTE = "./tests/__init__.py"


def test_atributos_encontrados_renovaveis():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m):
        renovaveis = Renovaveis.read(ARQ_TESTE)
        assert renovaveis.pee_cad() is not None
        assert renovaveis.pee_subm() is not None
        assert renovaveis.pee_config_per() is not None
        assert renovaveis.pee_pot_inst_per() is not None
        assert renovaveis.pee_ger_per_pat_cen() is not None


def test_df_renovaveis_pee_cad():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m):
        renovaveis = Renovaveis.read(ARQ_TESTE)
        df = renovaveis.pee_cad(df=True)
        assert len(df) == 8
        assert df.at[0, "codigo_pee"] == 1
        assert df.at[0, "nome_pee"] == "Eolica SECO"


def test_registro_renovaveis_pee_cad():
    m: MagicMock = mock_open(read_data="".join(MockPEECadastro))
    r = PEECadastro()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, "Eolica SECO"]
    assert r.codigo_pee == 1
    r.codigo_pee = 0
    assert r.codigo_pee == 0
    assert r.nome_pee == "Eolica SECO"
    r.nome_pee = "Eolica S"
    assert r.nome_pee == "Eolica S"


def test_df_renovaveis_pee_subm():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m):
        renovaveis = Renovaveis.read(ARQ_TESTE)
        df = renovaveis.pee_subm(df=True)
        assert len(df) == 8
        assert df.at[0, "codigo_pee"] == 1
        assert df.at[0, "codigo_submercado"] == 1


def test_registro_renovaveis_pee_subm():
    m: MagicMock = mock_open(read_data="".join(MockPEESubmercado))
    r = PEESubmercado()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1]
    assert r.codigo_pee == 1
    r.codigo_pee = 0
    assert r.codigo_pee == 0
    assert r.codigo_submercado == 1
    r.codigo_submercado = 0
    assert r.codigo_submercado == 0


def test_df_renovaveis_pee_config_per():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m):
        renovaveis = Renovaveis.read(ARQ_TESTE)
        df = renovaveis.pee_config_per(df=True)
        assert len(df) == 8
        assert df.at[0, "codigo_pee"] == 1
        assert df.at[0, "estagio_inicial"] == 1
        assert df.at[0, "estagio_final"] == 3
        assert df.at[0, "estado_operacao"] == "centralizado"


def test_registro_renovaveis_pee_config_per():
    m: MagicMock = mock_open(read_data="".join(MockPEEConfiguracaoPeriodo))
    r = PEEConfiguracaoPeriodo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 3, "centralizado"]
    assert r.codigo_pee == 1
    r.codigo_pee = 0
    assert r.codigo_pee == 0
    assert r.estagio_inicial == 1
    r.estagio_inicial = 0
    assert r.estagio_inicial == 0
    assert r.estagio_final == 3
    r.estagio_final = 0
    assert r.estagio_final == 0
    assert r.estado_operacao == "centralizado"
    r.estado_operacao = "descentralizado"
    assert r.estado_operacao == "descentralizado"


def test_df_renovaveis_pee_pot_inst_per():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m):
        renovaveis = Renovaveis.read(ARQ_TESTE)
        df = renovaveis.pee_pot_inst_per(df=True)
        assert len(df) == 8
        assert df.at[0, "codigo_pee"] == 1
        assert df.at[0, "estagio_inicial"] == 1
        assert df.at[0, "estagio_final"] == 3
        assert df.at[0, "potencia_instalada"] == 99999.0


def test_registro_renovaveis_pee_pot_inst_per():
    m: MagicMock = mock_open(read_data="".join(MockPEEPotenciaInstaladaPeriodo))
    r = PEEPotenciaInstaladaPeriodo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 3, 99999.0]
    assert r.codigo_pee == 1
    r.codigo_pee = 0
    assert r.codigo_pee == 0
    assert r.estagio_inicial == 1
    r.estagio_inicial = 0
    assert r.estagio_inicial == 0
    assert r.estagio_final == 3
    r.estagio_final = 0
    assert r.estagio_final == 0
    assert r.potencia_instalada == 99999.0
    r.potencia_instalada = 0.0
    assert r.potencia_instalada == 0.0


def test_df_renovaveis_pee_ger_per_pat_cen():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m):
        renovaveis = Renovaveis.read(ARQ_TESTE)
        df = renovaveis.pee_ger_per_pat_cen(df=True)
        assert len(df) == 6
        # A coluna de geração deve estar totalmente preenchida: guarda contra
        # a regressão em que um campo espúrio deslocava tudo e zerava geracao.
        assert df["geracao"].notna().all()
        assert df.at[0, "codigo_pee"] == 1
        assert df.at[0, "estagio"] == 1
        assert df.at[0, "patamar"] == 1
        assert df.at[0, "cenario"] == 1
        assert df.at[0, "geracao"] == 81.0966
        assert df.at[5, "codigo_pee"] == 14
        assert df.at[5, "estagio"] == 3
        assert df.at[5, "patamar"] == 3
        assert df.at[5, "cenario"] == 353
        assert df.at[5, "geracao"] == 1.611293


def test_registro_renovaveis_pee_ger_per_pat_cen():
    m: MagicMock = mock_open(
        read_data="".join(MockPEEGeracaoPeriodoPatamarCenario)
    )
    r = PEEGeracaoPeriodoPatamarCenario()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 1, 1, 81.0966]
    assert r.codigo_pee == 1
    r.codigo_pee = 0
    assert r.codigo_pee == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.patamar == 1
    r.patamar = 0
    assert r.patamar == 0
    assert r.cenario == 1
    r.cenario = 0
    assert r.cenario == 0
    assert r.geracao == 81.0966
    r.geracao = 0.0
    assert r.geracao == 0.0


def test_registro_renovaveis_pee_ger_per_pat_cen_com_periodo_final():
    m: MagicMock = mock_open(
        read_data="".join(MockPEEGeracaoPeriodoPatamarCenarioComPeriodoFinal)
    )
    r = PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 1, 1, 1, 7.7428]
    assert r.codigo_pee == 1
    r.codigo_pee = 0
    assert r.codigo_pee == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.estagio_final == 1
    r.estagio_final = 0
    assert r.estagio_final == 0
    assert r.patamar == 1
    r.patamar = 0
    assert r.patamar == 0
    assert r.cenario == 1
    r.cenario = 0
    assert r.cenario == 0
    assert r.geracao == 7.7428
    r.geracao = 0.0
    assert r.geracao == 0.0


def test_df_renovaveis_pee_ger_per_pat_cen_com_periodo_final():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveisPeriodoFinal))
    with patch("builtins.open", m):
        renovaveis = Renovaveis.read(ARQ_TESTE)
        df = renovaveis.pee_ger_per_pat_cen(df=True)
        assert len(df) == 6
        # Geração totalmente preenchida também no layout de 6 campos.
        assert df["geracao"].notna().all()
        assert df.at[0, "codigo_pee"] == 1
        assert df.at[0, "estagio"] == 1
        assert df.at[0, "estagio_final"] == 1
        assert df.at[0, "patamar"] == 1
        assert df.at[0, "cenario"] == 1
        assert df.at[0, "geracao"] == 7.7428
        assert df.at[5, "codigo_pee"] == 14
        assert df.at[5, "estagio"] == 3
        assert df.at[5, "estagio_final"] == 3
        assert df.at[5, "patamar"] == 3
        assert df.at[5, "cenario"] == 353
        assert df.at[5, "geracao"] == 1.611293


def test_dispatch_layouts_pee_ger_per_pat_cen():
    # 5 campos -> registro de período único
    m: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m):
        registros = Renovaveis.read(ARQ_TESTE).pee_ger_per_pat_cen()
        assert len(registros) == 6
        assert all(
            isinstance(r, PEEGeracaoPeriodoPatamarCenario) for r in registros
        )
    # 6 campos -> registro de intervalo de períodos (com PerFin)
    m2: MagicMock = mock_open(read_data="".join(MockRenovaveisPeriodoFinal))
    with patch("builtins.open", m2):
        registros2 = Renovaveis.read(ARQ_TESTE).pee_ger_per_pat_cen()
        assert len(registros2) == 6
        assert all(
            isinstance(r, PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal)
            for r in registros2
        )


def test_eq_renovaveis():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m):
        renovaveis1 = Renovaveis.read(ARQ_TESTE)
        renovaveis2 = Renovaveis.read(ARQ_TESTE)
        assert renovaveis1 == renovaveis2


def test_neq_renovaveis():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveis))
    with patch("builtins.open", m):
        renovaveis1 = Renovaveis.read(ARQ_TESTE)
        renovaveis2 = Renovaveis.read(ARQ_TESTE)
        renovaveis1.pee_cad()[0].codigo_pee = -1
        assert renovaveis1 != renovaveis2
