# Rotinas de testes associadas ao arquivo relato.rvx do DECOMP
from idecomp.decomp.modelos.relato import (
    BlocoREEsSubsistemas,
    BlocoUHEsREEsSubsistemas,
    BlocoConvergenciaRelato,
    BlocoRelatorioOperacaoRelato,
    BlocoRelatorioOperacaoUTERelato,
    BlocoBalancoEnergeticoRelato,
    BlocoCMORelato,
    BlocoGeracaoTermicaSubsistemaRelato,
    BlocoCustoOperacaoValorEsperadoRelato,
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
    MockREEsSubmercado,
    MockUHEsREEsSubmercado,
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
    MockCustoOperacaoValorEsperado,
    MockRelato,
    MockRelatorioOperacaoCustos,
    MockRelatorioOperacaoUHE,
    MockRelatorioOperacaoUTE,
    MockVolumeUtilReservatorio,
)


def test_bloco_rees_submercado():
    m: MagicMock = mock_open(read_data="".join(MockREEsSubmercado))
    b = BlocoREEsSubsistemas()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 12
    assert b.data.shape[1] == 5
    assert b.data.iloc[0, 0] == 1
    assert b.data.iloc[0, 1] == "SUDESTE"
    assert b.data.iloc[0, 2] == 1
    assert b.data.iloc[0, 3] == "SE"
    assert b.data.iloc[0, 4] == "SUDESTE"


def test_bloco_uhes_rees_submercado():
    m: MagicMock = mock_open(read_data="".join(MockUHEsREEsSubmercado))
    b = BlocoUHEsREEsSubsistemas()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 163
    assert b.data.shape[1] == 7
    assert b.data.iloc[0, 0] == 108
    assert b.data.iloc[0, 1] == "TRAICAO"
    assert b.data.iloc[0, 2] == 1
    assert b.data.iloc[0, 3] == "SUDESTE"
    assert b.data.iloc[0, 4] == 1
    assert b.data.iloc[0, 5] == "SE"
    assert b.data.iloc[0, 6] == "SUDESTE"


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


def test_bloco_relatorio_operacao_custos():
    m: MagicMock = mock_open(read_data="".join(MockRelatorioOperacaoCustos))
    b = BlocoRelatorioOperacaoRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data[1].shape[0] == 1
    assert b.data[1].shape[1] == 17
    assert b.data[1].iloc[0, 0] == 1
    assert b.data[1].iloc[0, 1] == 1
    assert b.data[1].iloc[0, 2] == 1.0
    assert b.data[1].iloc[0, 3] == 408096349.11
    assert b.data[1].iloc[0, 4] == 126483.42
    assert b.data[1].iloc[0, 5] == 126469.80
    assert b.data[1].iloc[0, 6] == 0.0
    assert b.data[1].iloc[0, 7] == 0.13
    assert b.data[1].iloc[0, 8] == 1.95
    assert b.data[1].iloc[0, 9] == 3.34
    assert b.data[1].iloc[0, 10] == 7.90
    assert b.data[1].iloc[0, 11] == 0.29
    assert b.data[1].iloc[0, 12] == 0.0
    assert b.data[1].iloc[0, 13] == 355.15
    assert b.data[1].iloc[0, 14] == 0.0
    assert b.data[1].iloc[0, 15] == 0.0
    assert b.data[1].iloc[0, 16] == 0.0


def test_bloco_relatorio_operacao_uhe():
    m: MagicMock = mock_open(read_data="".join(MockRelatorioOperacaoUHE))
    b = BlocoRelatorioOperacaoRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data[1].shape[0] == 166
    assert b.data[1].shape[1] == 24
    assert b.data[1].iloc[0, 0] == 1
    assert b.data[1].iloc[0, 1] == 1
    assert b.data[1].iloc[0, 2] == 1.0
    assert b.data[1].iloc[0, 3] == 1
    assert b.data[1].iloc[0, 4] == "CAMARGOS"
    assert b.data[1].iloc[0, 5] == True
    assert b.data[1].iloc[0, 6] == False
    assert b.data[1].iloc[0, 7] == False
    assert b.data[1].iloc[0, 8] == False
    assert b.data[1].iloc[0, 9] == 25.3
    assert b.data[1].iloc[0, 10] == 24.9
    assert b.data[1].iloc[0, 11] == 55.1
    assert b.data[1].iloc[0, 12] == 98.0
    assert b.data[1].iloc[0, 13] == 39.8
    assert b.data[1].iloc[0, 14] == 98.0
    assert b.data[1].iloc[0, 15] == 102.3
    assert b.data[1].iloc[0, 16] == 17.8
    assert b.data[1].iloc[0, 17] == 17.8
    assert b.data[1].iloc[0, 18] == 17.8
    assert b.data[1].iloc[0, 19] == 17.8
    assert b.data[1].iloc[0, 20] == 0.0
    assert b.data[1].iloc[0, 21] == 0.0
    assert b.data[1].iloc[0, 22] == 31.5
    assert b.data[1].iloc[0, 23] == 0.0


def test_bloco_relatorio_operacao_ute():
    m: MagicMock = mock_open(read_data="".join(MockRelatorioOperacaoUTE))
    b = BlocoRelatorioOperacaoUTERelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)
    assert b.data.shape[0] == 29
    assert b.data.shape[1] == 10
    assert b.data.iloc[0, 0] == 1
    assert b.data.iloc[0, 1] == 1
    assert b.data.iloc[0, 2] == 1.0
    assert b.data.iloc[0, 3] == "SE"
    assert b.data.iloc[0, 4] == "SANTA CRUZ"
    assert b.data.iloc[0, 5] == None
    assert b.data.iloc[0, 6] == 350.0
    assert b.data.iloc[0, 7] == 350.0
    assert b.data.iloc[0, 8] == 350.0
    assert b.data.iloc[0, 9] == 6099.91


def test_bloco_balanco_energetico():
    m: MagicMock = mock_open(read_data="".join(MockBalancoEnergetico))
    b = BlocoBalancoEnergeticoRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 16
    assert b.data.shape[1] == 22
    assert b.data.loc[0, "estagio"] == 1
    assert b.data.loc[0, "cenario"] == 1
    assert b.data.loc[0, "probabilidade"] == 1
    assert b.data.loc[0, "patamar"] == "1"
    assert b.data.loc[0, "energia_armazenada_inicial_MWmed"] == 41766.0
    assert b.data.loc[0, "energia_armazenada_inicial_percentual"] == 20.4
    assert b.data.loc[0, "energia_natural_afluente_MWmed"] == 36314.0
    assert b.data.loc[0, "energia_natural_afluente_percentual"] == 17.8
    assert b.data.loc[0, "energia_armazenada_final_MWmed"] == 42365.0
    assert b.data.loc[0, "energia_armazenada_final_percentual"] == 20.7
    assert b.data.loc[0, "nome_submercado"] == "SE"
    assert b.data.loc[0, "mercado"] == 45078.0
    assert b.data.loc[0, "bacia"] == 3374.0
    assert b.data.loc[0, "consumo_bombeamento"] == 0.0
    assert b.data.loc[0, "geracao_hidraulica"] == 34768.3
    assert b.data.loc[0, "geracao_termica"] == 4576.3
    assert b.data.loc[0, "geracao_termica_antecipada"] == 554.0
    assert b.data.loc[0, "deficit"] == 0.0
    assert b.data.loc[0, "compra"] == 0.0
    assert b.data.loc[0, "venda"] == 0.0
    assert b.data.loc[0, "geracao_itaipu_50hz"] == 5529.8
    assert b.data.loc[0, "geracao_itaipu_60hz"] == 4800.9


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


def test_bloco_geracao_termica_submercado():
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


def test_bloco_custo_operacao_valor_esperado():
    m: MagicMock = mock_open(read_data="".join(MockCustoOperacaoValorEsperado))
    b = BlocoCustoOperacaoValorEsperadoRelato()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 2
    assert b.data.shape[1] == 6
    assert b.data.iloc[0, 0] == "*COP"
    assert b.data.iloc[0, 1] == 90662.8
    assert b.data.iloc[0, 2] == 79546.7
    assert b.data.iloc[0, 3] == 81339.2
    assert b.data.iloc[0, 4] == 89975.9
    assert b.data.iloc[0, 5] == 85036.6


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


def test_bloco_energia_armazenada_submercado():
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


def test_bloco_ena_pre_estudo_mensal_submercado():
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


def test_bloco_ena_pre_estudo_semanal_submercado():
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
        rel = Relato.read("./tests/mocks/arquivos/relato.py")
        assert rel.rees_submercados is not None
        assert rel.uhes_rees_submercados is not None
        assert rel.convergencia is not None
        assert rel.relatorio_operacao_custos is not None
        assert rel.relatorio_operacao_uhe is not None
        assert rel.relatorio_operacao_ute is not None
        assert rel.balanco_energetico is not None
        assert rel.cmo_medio_submercado is not None
        assert rel.geracao_termica_submercado is not None
        assert rel.volume_util_reservatorios is not None
        assert rel.dados_termicas is not None
        assert rel.disponibilidades_termicas is not None
        assert rel.dados_mercado is not None
        assert rel.ena_acoplamento_ree is not None
        assert rel.energia_armazenada_ree is not None
        assert rel.energia_armazenada_submercado is not None
        assert rel.ena_pre_estudo_mensal_ree is not None
        assert rel.ena_pre_estudo_mensal_submercado is not None
        assert rel.ena_pre_estudo_semanal_ree is not None
        assert rel.ena_pre_estudo_semanal_ree is not None
        assert rel.dias_excluidos_semana_inicial is not None
        assert rel.dias_excluidos_semana_final is not None


def test_atributos_nao_encontrados_relato():
    m: MagicMock = mock_open(read_data="".join(""))
    with patch("builtins.open", m):
        rel = Relato.read("./tests/mocks/arquivos/relato.py")
        assert rel.rees_submercados is None
        assert rel.uhes_rees_submercados is None
        assert rel.convergencia is None
        assert rel.relatorio_operacao_custos is None
        assert rel.relatorio_operacao_uhe is None
        assert rel.balanco_energetico is None
        assert rel.cmo_medio_submercado is None
        assert rel.geracao_termica_submercado is None
        assert rel.volume_util_reservatorios is None
        assert rel.dados_termicas is None
        assert rel.disponibilidades_termicas is None
        assert rel.dados_mercado is None
        assert rel.ena_acoplamento_ree is None
        assert rel.energia_armazenada_ree is None
        assert rel.energia_armazenada_submercado is None
        assert rel.ena_pre_estudo_mensal_ree is None
        assert rel.ena_pre_estudo_mensal_submercado is None
        assert rel.ena_pre_estudo_semanal_ree is None
        assert rel.ena_pre_estudo_semanal_ree is None
        assert rel.dias_excluidos_semana_inicial is None
        assert rel.dias_excluidos_semana_final is None


def test_eq_relato():
    m: MagicMock = mock_open(read_data="".join(MockRelato))
    with patch("builtins.open", m):
        rel1 = Relato.read("./tests/mocks/arquivos/relato.py")
        rel2 = Relato.read("./tests/mocks/arquivos/relato.py")
        assert rel1 == rel2


def test_neq_relato():
    m: MagicMock = mock_open(read_data="".join(MockRelato))
    with patch("builtins.open", m):
        rel1 = Relato.read("./tests/mocks/arquivos/relato.py")
        rel2 = Relato.read("./tests/mocks/arquivos/relato.py")
        rel1.convergencia.iloc[0, 0] = 0
        assert rel1 != rel2
