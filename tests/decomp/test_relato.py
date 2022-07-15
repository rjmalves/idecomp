# Rotinas de testes associadas ao arquivo relato.rvx do DECOMP
from idecomp.decomp.modelos.relato import (
    BlocoConvergenciaRelato,
    BlocoRelatorioOperacaoUHERelato,
    BlocoBalancoEnergeticoRelato,
    BlocoCMORelato,
    BlocoGeracaoTermicaSubsistemaRelato,
    BlocoVolumeUtilReservatorioRelato,
    BlocoDadosTermicasRelato,
    BlocoDisponibilidadesTermicasRelato,
    BlocoDadosMercadoRelato,
    BlocoENAAcoplamentoREERelato,
    BlocoEnergiaArmazenadaREERelato,
    BlocoEnergiaArmazenadaSubsistemaRelato,
    BlocoENAPreEstudoSemanalSubsistemaRelato,
    BlocoENAPreEstudoSemanalREERelato,
    BlocoENAPreEstudoMensalSubsistemaRelato,
    BlocoENAPreEstudoMensalREERelato,
    BlocoDiasExcluidosSemanas,
)

from idecomp.decomp.relato import Relato

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.relato import (
    MockBalancoEnergetico,
    MockBlocoDiasExcluidosSemanas,
    MockCMO,
    MockConvergencia,
    MockDadosMercado,
    MockDadosTermicas,
    MockDisponibilidadesTermicas,
    MockENAAcoplamentoREE,
    MockENAPreEstudoMensalREE,
    MockENAPreEstudoMensalSubsistema,
    MockENAPreEstudoSemanalREE,
    MockENAPreEstudoSemanalSubsistema,
    MockEnergiaArmazenadaREE,
    MockEnergiaArmazenadaSubsistema,
    MockGeracaoTermicaSubsistema,
    MockRelato,
    MockRelatorioOperacaoUHE,
    MockVolumeUtilReservatorio,
)


def test_bloco_convergencia():
    m: MagicMock = mock_open(read_data="".join(MockConvergencia))
    b = BlocoConvergenciaRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 48
    assert b.data.shape[1] == 11
    assert b.data.iloc[0, 0] == 1
    assert b.data.iloc[0, 1] == 450767.9
    assert b.data.iloc[0, 2] == 1828276433.0
    assert b.data.iloc[0, 3] == 405491.5174150
    assert b.data.iloc[0, 4] == 23
    assert b.data.iloc[0, 5] == 0
    assert b.data.iloc[0, 7] == 4
    assert b.data.iloc[0, 8] == 0
    assert b.data.iloc[0, 9] == 14
    assert b.data.iloc[0, 10] == 0
    assert b.data.iloc[-1, -1] == 0.0


def test_bloco_relatorio_operacao():
    m: MagicMock = mock_open(read_data="".join(MockRelatorioOperacaoUHE))
    b = BlocoRelatorioOperacaoUHERelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 166
    assert b.data.shape[1] == 21
    assert b.data.iloc[0, 0] == 1
    assert b.data.iloc[0, 1] == "CAMARGOS"
    assert b.data.iloc[0, 2] == True
    assert b.data.iloc[0, 3] == False
    assert b.data.iloc[0, 4] == False
    assert b.data.iloc[0, 5] == False
    assert b.data.iloc[0, 6] == 25.3
    assert b.data.iloc[0, 7] == 24.9
    assert b.data.iloc[0, 8] == 55.1
    assert b.data.iloc[0, 9] == 98.0
    assert b.data.iloc[0, 10] == 39.8
    assert b.data.iloc[0, 11] == 98.0
    assert b.data.iloc[0, 12] == 102.3
    assert b.data.iloc[0, 13] == 17.8
    assert b.data.iloc[0, 14] == 17.8
    assert b.data.iloc[0, 15] == 17.8
    assert b.data.iloc[0, 16] == 17.8
    assert b.data.iloc[0, 17] == 0.0
    assert b.data.iloc[0, 18] == 0.0
    assert b.data.iloc[0, 19] == 31.5
    assert b.data.iloc[0, 20] == 0.0


def test_bloco_balanco_energetico():
    m: MagicMock = mock_open(read_data="".join(MockBalancoEnergetico))
    b = BlocoBalancoEnergeticoRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 4
    assert b.data.shape[1] == 21
    assert b.data.loc[0, "Estágio"] == 1
    assert b.data.loc[0, "Cenário"] == 1
    assert b.data.loc[0, "Probabilidade"] == 1
    assert b.data.loc[0, "Earm Inicial Absoluto"] == 41766.0
    assert b.data.loc[0, "Earm Inicial Percentual"] == 20.4
    assert b.data.loc[0, "ENA Absoluta"] == 36314.0
    assert b.data.loc[0, "ENA Percentual"] == 17.8
    assert b.data.loc[0, "Earm Final Absoluto"] == 42365.0
    assert b.data.loc[0, "Earm Final Percentual"] == 20.7
    assert b.data.loc[0, "Subsistema"] == "SE"
    assert b.data.loc[0, "Mercado"] == 37924.4
    assert b.data.loc[0, "Bacia"] == 3374.0
    assert b.data.loc[0, "Cbomba"] == 77.6
    assert b.data.loc[0, "Ghid"] == 30056.3
    assert b.data.loc[0, "Gter"] == 4529.8
    assert b.data.loc[0, "GterAT"] == 554.0
    assert b.data.loc[0, "Deficit"] == 0.0
    assert b.data.loc[0, "Compra"] == 0.0
    assert b.data.loc[0, "Venda"] == 0.0
    assert b.data.loc[0, "Itaipu50"] == 4333.5
    assert b.data.loc[0, "Itaipu60"] == 3434.1


def test_bloco_cmo():
    m: MagicMock = mock_open(read_data="".join(MockCMO))
    b = BlocoCMORelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 20
    assert b.data.shape[1] == 7
    assert b.data.iloc[0, 0] == "SE"
    assert b.data.iloc[0, 1] == "1"
    assert b.data.iloc[0, 2] == 287.91
    assert b.data.iloc[0, 3] == 291.06
    assert b.data.iloc[0, 4] == 291.99
    assert b.data.iloc[0, 5] == 289.35
    assert b.data.iloc[0, 6] == 287.67


def test_bloco_geracao_termica_subsistema():
    m: MagicMock = mock_open(read_data="".join(MockGeracaoTermicaSubsistema))
    b = BlocoGeracaoTermicaSubsistemaRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 5
    assert b.data.shape[1] == 6
    assert b.data.iloc[0, 0] == "SE"
    assert b.data.iloc[0, 1] == 5083.8
    assert b.data.iloc[0, 2] == 4804.5
    assert b.data.iloc[0, 3] == 4315.4
    assert b.data.iloc[0, 4] == 4632.2
    assert b.data.iloc[0, 5] == 4705.9


def test_bloco_volume_util_reservatorios():
    m: MagicMock = mock_open(read_data="".join(MockVolumeUtilReservatorio))
    b = BlocoVolumeUtilReservatorioRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 67
    assert b.data.shape[1] == 8
    assert b.data.iloc[0, 0] == 1
    assert b.data.iloc[0, 1] == "CAMARGOS"
    assert b.data.iloc[0, 2] == 25.3
    assert b.data.iloc[0, 3] == 24.9
    assert b.data.iloc[0, 4] == 27.5
    assert b.data.iloc[0, 5] == 30.4
    assert b.data.iloc[0, 6] == 35.1
    assert b.data.iloc[0, 7] == 39.2


def test_bloco_dados_termicas():
    m: MagicMock = mock_open(read_data="".join(MockDadosTermicas))
    b = BlocoDadosTermicasRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 648
    assert b.data.shape[1] == 13
    assert b.data.iloc[0, 0] == 65
    assert b.data.iloc[0, 1] == "ATLAN_CSA"
    assert b.data.iloc[0, 2] == "SE"
    assert b.data.iloc[0, 3] == 1
    assert b.data.iloc[0, 4] == 122.60
    assert b.data.iloc[0, 5] == 122.60
    assert b.data.iloc[0, 6] == 0.0
    assert b.data.iloc[0, 7] == 122.60
    assert b.data.iloc[0, 8] == 122.60
    assert b.data.iloc[0, 9] == 0
    assert b.data.iloc[0, 10] == 122.60
    assert b.data.iloc[0, 11] == 122.60
    assert b.data.iloc[0, 12] == 0


def test_bloco_disponibilidades_termicas():
    m: MagicMock = mock_open(read_data="".join(MockDisponibilidadesTermicas))
    b = BlocoDisponibilidadesTermicasRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 111
    assert b.data.shape[1] == 8
    assert b.data.iloc[0, 0] == 86
    assert b.data.iloc[0, 1] == "SANTA CRUZ"
    assert b.data.iloc[0, 2] == 100.0
    assert b.data.iloc[0, 3] == 100.0
    assert b.data.iloc[0, 4] == 100.0
    assert b.data.iloc[0, 5] == 100.0
    assert b.data.iloc[0, 6] == 100.0
    assert b.data.iloc[0, 7] == 100.0


def test_bloco_dados_mercado():
    m: MagicMock = mock_open(read_data="".join(MockDadosMercado))
    b = BlocoDadosMercadoRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 36
    assert b.data.shape[1] == 8
    assert b.data.iloc[0, 0] == 1
    assert b.data.iloc[0, 1] == "SE"
    assert b.data.iloc[0, 2] == 32.0
    assert b.data.iloc[0, 3] == 45078.0
    assert b.data.iloc[0, 4] == 41.0
    assert b.data.iloc[0, 5] == 41680.0
    assert b.data.iloc[0, 6] == 95.0
    assert b.data.iloc[0, 7] == 33894.0


def test_bloco_ena_acoplamento_ree():
    m: MagicMock = mock_open(read_data="".join(MockENAAcoplamentoREE))
    b = BlocoENAAcoplamentoREERelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 1392
    assert b.data.shape[1] == 10
    assert b.data.iloc[0, 0] == 1
    assert b.data.iloc[0, 1] == "SUDESTE"
    assert b.data.iloc[0, 2] == "SE"
    assert b.data.iloc[0, 3] == 1
    assert b.data.iloc[0, 4] == 3909.5
    assert b.data.iloc[0, 5] == 4757.4
    assert b.data.iloc[0, 6] == 5605.3
    assert b.data.iloc[0, 7] == 6609.8
    assert b.data.iloc[0, 8] == 7946.4
    assert b.data.iloc[0, 9] == 7640.1


def test_bloco_energia_armazenada_ree():
    m: MagicMock = mock_open(read_data="".join(MockEnergiaArmazenadaREE))
    b = BlocoEnergiaArmazenadaREERelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 12
    assert b.data.shape[1] == 8
    assert b.data.iloc[0, 0] == 1
    assert b.data.iloc[0, 1] == "SUDESTE"
    assert b.data.iloc[0, 2] == 19.5
    assert b.data.iloc[0, 3] == 19.4
    assert b.data.iloc[0, 4] == 19.4
    assert b.data.iloc[0, 5] == 19.7
    assert b.data.iloc[0, 6] == 20.6
    assert b.data.iloc[0, 7] == 21.8


def test_bloco_energia_armazenada_subsistema():
    m: MagicMock = mock_open(
        read_data="".join(MockEnergiaArmazenadaSubsistema)
    )
    b = BlocoEnergiaArmazenadaSubsistemaRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 4
    assert b.data.shape[1] == 7
    assert b.data.iloc[0, 0] == "SE"
    assert b.data.iloc[0, 1] == 20.4
    assert b.data.iloc[0, 2] == 20.7
    assert b.data.iloc[0, 3] == 21.1
    assert b.data.iloc[0, 4] == 21.9
    assert b.data.iloc[0, 5] == 23.3
    assert b.data.iloc[0, 6] == 25.2


def test_bloco_ena_pre_estudo_mensal_ree():
    m: MagicMock = mock_open(read_data="".join(MockENAPreEstudoMensalREE))
    b = BlocoENAPreEstudoMensalREERelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 12
    assert b.data.shape[1] == 13
    assert b.data.iloc[0, 0] == "SUDESTE"
    assert b.data.iloc[0, 1] == 50314.5
    assert b.data.iloc[0, 2] == 4371.6
    assert b.data.iloc[0, 3] == 2503.3
    assert b.data.iloc[0, 4] == 1617.3
    assert b.data.iloc[0, 5] == 1596.9
    assert b.data.iloc[0, 6] == 1706.7
    assert b.data.iloc[0, 7] == 2179.8
    assert b.data.iloc[0, 8] == 2541.1
    assert b.data.iloc[0, 9] == 3796.6
    assert b.data.iloc[0, 10] == 5973.3
    assert b.data.iloc[0, 11] == 7093.4
    assert b.data.iloc[0, 12] == 5209.3


def test_bloco_ena_pre_estudo_mensal_subsistema():
    m: MagicMock = mock_open(
        read_data="".join(MockENAPreEstudoMensalSubsistema)
    )
    b = BlocoENAPreEstudoMensalSubsistemaRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 4
    assert b.data.shape[1] == 13
    assert b.data.iloc[0, 0] == "SE"
    assert b.data.iloc[0, 1] == 204321.7
    assert b.data.iloc[0, 2] == 39005.7
    assert b.data.iloc[0, 3] == 19389.1
    assert b.data.iloc[0, 4] == 13720.1
    assert b.data.iloc[0, 5] == 13718.4
    assert b.data.iloc[0, 6] == 16329.3
    assert b.data.iloc[0, 7] == 21774.2
    assert b.data.iloc[0, 8] == 30729.5
    assert b.data.iloc[0, 9] == 38234.5
    assert b.data.iloc[0, 10] == 52288.9
    assert b.data.iloc[0, 11] == 66003.0
    assert b.data.iloc[0, 12] == 46132.5


def test_bloco_ena_pre_estudo_semanal_ree():
    m: MagicMock = mock_open(read_data="".join(MockENAPreEstudoSemanalREE))
    b = BlocoENAPreEstudoSemanalREERelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 12
    assert b.data.shape[1] == 7
    assert b.data.iloc[0, 0] == "SUDESTE"
    assert b.data.iloc[0, 1] == 50314.5
    assert b.data.iloc[0, 2] == 10.0
    assert b.data.iloc[0, 3] == 5.0
    assert b.data.iloc[0, 4] == 3.0
    assert b.data.iloc[0, 5] == 2000.0
    assert b.data.iloc[0, 6] == 10000.0


def test_bloco_ena_pre_estudo_semanal_subsistema():
    m: MagicMock = mock_open(
        read_data="".join(MockENAPreEstudoSemanalSubsistema)
    )
    b = BlocoENAPreEstudoSemanalSubsistemaRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 4
    assert b.data.shape[1] == 7
    assert b.data.iloc[0, 0] == "SE"
    assert b.data.iloc[0, 1] == 204321.7
    assert b.data.iloc[0, 2] == 4.0
    assert b.data.iloc[0, 3] == 599.0
    assert b.data.iloc[0, 4] == 1.0
    assert b.data.iloc[0, 5] == 0.1
    assert b.data.iloc[0, 6] == 10000.0


def test_bloco_dias_excluidos_semanas():
    m: MagicMock = mock_open(read_data="".join(MockBlocoDiasExcluidosSemanas))
    b = BlocoDiasExcluidosSemanas()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data == [4, 0]


def test_atributos_encontrados_relato():
    m: MagicMock = mock_open(read_data="".join(MockRelato))
    with patch("builtins.open", m):
        rel = Relato.le_arquivo("")
        assert rel.convergencia is not None
        assert rel.relatorio_operacao_uhe is not None
        assert rel.balanco_energetico is not None
        assert rel.cmo_medio_subsistema is not None
        assert rel.geracao_termica_subsistema is not None
        assert rel.volume_util_reservatorios is not None
        assert rel.dados_termicas is not None
        assert rel.disponibilidades_termicas is not None
        assert rel.dados_mercado is not None
        assert rel.ena_acoplamento_ree is not None
        assert rel.energia_armazenada_ree is not None
        assert rel.energia_armazenada_subsistema is not None
        assert rel.ena_pre_estudo_mensal_ree is not None
        assert rel.ena_pre_estudo_mensal_subsistema is not None
        assert rel.ena_pre_estudo_semanal_ree is not None
        assert rel.ena_pre_estudo_semanal_ree is not None
        assert rel.dias_excluidos_semana_inicial is not None
        assert rel.dias_excluidos_semana_final is not None


def test_atributos_nao_encontrados_relato():
    m: MagicMock = mock_open(read_data="".join(""))
    with patch("builtins.open", m):
        rel = Relato.le_arquivo("")
        assert rel.convergencia is None
        assert rel.relatorio_operacao_uhe is None
        assert rel.balanco_energetico is None
        assert rel.cmo_medio_subsistema is None
        assert rel.geracao_termica_subsistema is None
        assert rel.volume_util_reservatorios is None
        assert rel.dados_termicas is None
        assert rel.disponibilidades_termicas is None
        assert rel.dados_mercado is None
        assert rel.ena_acoplamento_ree is None
        assert rel.energia_armazenada_ree is None
        assert rel.energia_armazenada_subsistema is None
        assert rel.ena_pre_estudo_mensal_ree is None
        assert rel.ena_pre_estudo_mensal_subsistema is None
        assert rel.ena_pre_estudo_semanal_ree is None
        assert rel.ena_pre_estudo_semanal_ree is None
        assert rel.dias_excluidos_semana_inicial is None
        assert rel.dias_excluidos_semana_final is None


def test_eq_relato():
    m: MagicMock = mock_open(read_data="".join(MockRelato))
    with patch("builtins.open", m):
        rel1 = Relato.le_arquivo("")
        rel2 = Relato.le_arquivo("")
        assert rel1 == rel2


def test_neq_relato():
    m: MagicMock = mock_open(read_data="".join(MockRelato))
    with patch("builtins.open", m):
        rel1 = Relato.le_arquivo("")
        rel2 = Relato.le_arquivo("")
        rel1.convergencia.iloc[0, 0] = 0
        assert rel1 != rel2
