from idecomp.libs.renovaveis import Renovaveis
from idecomp.libs.modelos.renovaveis import (
    PEECadastro,
    PEESubmercado,
    PEEConfiguracaoPeriodo,
    PEEPotenciaInstaladaPeriodo,
    PEEGeracaoPeriodoPatamarCenario,
    PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal,
    PEEGeracaoPeriodoPatamar,
    PEEGeracaoPeriodoPatamarComPeriodoFinal,
)
import inspect

from cfinterface.components.register import Register

import idecomp.libs.modelos.renovaveis as modelos_renovaveis
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.renovaveis import (
    MockRenovaveis,
    MockRenovaveisPeriodoFinal,
    MockPEECadastro,
    MockPEESubmercado,
    MockPEEConfiguracaoPeriodo,
    MockPEEPotenciaInstaladaPeriodo,
    MockPEEPotenciaInstaladaPeriodoValorLongo,
    MockPEEGeracaoPeriodoPatamarCenario,
    MockPEEGeracaoPeriodoPatamarCenarioComPeriodoFinal,
    MockPEEGeracaoPeriodoPatamarCenarioValorLongo,
    MockPEEGeracaoPeriodoPatamarCenarioComPeriodoFinalValorLongo,
    MockPEEGeracaoPeriodoPatamar,
    MockPEEGeracaoPeriodoPatamarComPeriodoFinal,
    MockRenovaveisDeterministico,
    MockRenovaveisLayoutsGeracao,
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


def test_registro_renovaveis_pee_pot_inst_per_valor_longo():
    # A potência deve ser lida inteira, sem cortar no 8º caractere.
    m: MagicMock = mock_open(
        read_data="".join(MockPEEPotenciaInstaladaPeriodoValorLongo)
    )
    r = PEEPotenciaInstaladaPeriodo()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 3, 12345.678]


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


def test_registro_renovaveis_pee_ger_per_pat_cen_valor_longo():
    # A geração deve ser lida inteira, sem cortar no 8º caractere.
    m: MagicMock = mock_open(
        read_data="".join(MockPEEGeracaoPeriodoPatamarCenarioValorLongo)
    )
    r = PEEGeracaoPeriodoPatamarCenario()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [3, 2, 3, 1, 17699.689]
    assert r.geracao == 17699.689


def test_registro_renovaveis_pee_ger_per_pat_cen_com_periodo_final_valor_longo():
    m: MagicMock = mock_open(
        read_data="".join(
            MockPEEGeracaoPeriodoPatamarCenarioComPeriodoFinalValorLongo
        )
    )
    r = PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [11, 3, 3, 3, 1, 14587.9881]
    assert r.geracao == 14587.9881


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


def test_registro_renovaveis_pee_ger_per_pat():
    m: MagicMock = mock_open(read_data="".join(MockPEEGeracaoPeriodoPatamar))
    r = PEEGeracaoPeriodoPatamar()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 2, 1465.012485]
    assert r.codigo_pee == 1
    r.codigo_pee = 0
    assert r.codigo_pee == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.patamar == 2
    r.patamar = 0
    assert r.patamar == 0
    assert r.geracao == 1465.012485
    r.geracao = 0.0
    assert r.geracao == 0.0


def test_registro_renovaveis_pee_ger_per_pat_com_periodo_final():
    m: MagicMock = mock_open(
        read_data="".join(MockPEEGeracaoPeriodoPatamarComPeriodoFinal)
    )
    r = PEEGeracaoPeriodoPatamarComPeriodoFinal()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 7, 2, 1401.719926]
    assert r.codigo_pee == 1
    r.codigo_pee = 0
    assert r.codigo_pee == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.estagio_final == 7
    r.estagio_final = 0
    assert r.estagio_final == 0
    assert r.patamar == 2
    r.patamar = 0
    assert r.patamar == 0
    assert r.geracao == 1401.719926
    r.geracao = 0.0
    assert r.geracao == 0.0


def test_df_renovaveis_deterministico():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveisDeterministico))
    with patch("builtins.open", m):
        renovaveis = Renovaveis.read(ARQ_TESTE)
        df = renovaveis.pee_ger_per_pat(df=True)
        assert len(df) == 4
        assert df["geracao"].notna().all()
        assert df.at[0, "codigo_pee"] == 1
        assert df.at[0, "estagio"] == 1
        assert df.at[0, "estagio_final"] == 1
        assert df.at[0, "patamar"] == 1
        assert df.at[0, "geracao"] == 1465.012485
        assert df.at[3, "codigo_pee"] == 3
        assert df.at[3, "estagio"] == 2
        assert df.at[3, "estagio_final"] == 7
        assert df.at[3, "patamar"] == 1
        # Valores com mais de 8 caracteres não podem ser truncados.
        assert df.at[3, "geracao"] == 13219.0328
        # O card com cenários não existe neste formato.
        assert renovaveis.pee_ger_per_pat_cen() is None
        assert renovaveis.pee_ger_per_pat_cen(df=True).empty


def test_demais_cards_renovaveis_deterministico():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveisDeterministico))
    with patch("builtins.open", m):
        renovaveis = Renovaveis.read(ARQ_TESTE)
        cad = renovaveis.pee_cad(df=True)
        assert cad["nome_pee"].tolist() == [
            "PQ_SECO_Red_PCH",
            "PQ_SECO_Red_EOL",
        ]
        assert len(renovaveis.pee_subm(df=True)) == 2
        assert len(renovaveis.pee_pot_inst_per(df=True)) == 2
        config = renovaveis.pee_config_per(df=True)
        assert config["estado_operacao"].tolist() == ["fixo", "centralizado"]


def test_pee_ger_per_pat_ausente_no_formato_por_cenarios():
    for mock in (MockRenovaveis, MockRenovaveisPeriodoFinal):
        m: MagicMock = mock_open(read_data="".join(mock))
        with patch("builtins.open", m):
            renovaveis = Renovaveis.read(ARQ_TESTE)
            assert renovaveis.pee_ger_per_pat() is None
            assert renovaveis.pee_ger_per_pat(df=True).empty
            assert len(renovaveis.pee_ger_per_pat_cen(df=True)) == 6


def test_dispatch_layouts_geracao():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveisLayoutsGeracao))
    with patch("builtins.open", m):
        renovaveis = Renovaveis.read(ARQ_TESTE)
        cen = renovaveis.pee_ger_per_pat_cen()
        assert [type(r) for r in cen] == [
            PEEGeracaoPeriodoPatamarCenario,
            PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal,
        ]
        det = renovaveis.pee_ger_per_pat()
        assert [type(r) for r in det] == [
            PEEGeracaoPeriodoPatamar,
            PEEGeracaoPeriodoPatamar,
            PEEGeracaoPeriodoPatamarComPeriodoFinal,
            PEEGeracaoPeriodoPatamarComPeriodoFinal,
        ]
        assert [r.codigo_pee for r in det] == [1, 2, 3, 4]
        assert det[2].geracao == 13219.0328


def test_df_pee_ger_per_pat_layouts_misturados():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveisLayoutsGeracao))
    with patch("builtins.open", m):
        df = Renovaveis.read(ARQ_TESTE).pee_ger_per_pat(df=True)
        assert len(df) == 4
        assert df["codigo_pee"].tolist() == [1, 2, 3, 4]
        assert df["estagio"].tolist() == [3, 4, 5, 6]
        # Período único não tem PerFin: estagio_final fica nulo.
        assert df["estagio_final"].isna().tolist() == [True, True, False, False]
        assert df.at[2, "estagio_final"] == 7
        assert df["patamar"].tolist() == [1, 2, 3, 1]
        assert df["geracao"].tolist() == [1465.012485, 12.5, 13219.0328, 0.0]


def test_filtro_pee_ger_per_pat():
    m: MagicMock = mock_open(read_data="".join(MockRenovaveisDeterministico))
    with patch("builtins.open", m):
        renovaveis = Renovaveis.read(ARQ_TESTE)
        registros = renovaveis.pee_ger_per_pat(codigo_pee=1, patamar=2)
        assert len(registros) == 1
        assert registros[0].geracao == 1401.719926


def test_leitura_escrita_renovaveis_deterministico():
    for mock in (MockRenovaveisDeterministico, MockRenovaveisLayoutsGeracao):
        m_leitura: MagicMock = mock_open(read_data="".join(mock))
        with patch("builtins.open", m_leitura):
            cf1 = Renovaveis.read(ARQ_TESTE)
        m_escrita: MagicMock = mock_open(read_data="")
        with patch("builtins.open", m_escrita):
            cf1.write(ARQ_TESTE)
            chamadas = m_escrita.mock_calls
            linhas_escritas = [
                chamadas[i].args[0] for i in range(1, len(chamadas) - 1)
            ]
        m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
        with patch("builtins.open", m_releitura):
            cf2 = Renovaveis.read(ARQ_TESTE)
            assert cf1 == cf2
            assert len(cf2.pee_ger_per_pat()) == len(cf1.pee_ger_per_pat())


def test_registros_modelados_renovaveis():
    # Todo registro modelado precisa estar em REGISTERS para ser lido
    registros = [
        c
        for _, c in inspect.getmembers(modelos_renovaveis, inspect.isclass)
        if issubclass(c, Register)
        and c.__module__ == modelos_renovaveis.__name__
    ]
    assert [r for r in registros if r not in Renovaveis.REGISTERS] == []
