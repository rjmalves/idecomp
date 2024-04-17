from idecomp.decomp.modelos.dadger import (
    EA,
    ES,
    QI,
    TE,
    SB,
    UH,
    CT,
    UE,
    DP,
    PQ,
    CD,
    RI,
    IA,
    TX,
    GP,
    NI,
    DT,
    MP,
    MT,
    FD,
    VE,
    RE,
    LU,
    FU,
    FI,
    FT,
    VI,
    PD,
    PU,
    RC,
    PE,
    TS,
    PV,
    CX,
    FA,
    VT,
    CS,
    ACJUSMED,
    ACCOTVOL,
    ACNUMJUS,
    ACVOLMIN,
    ACCOFEVA,
    ACNUMPOS,
    ACVSVERT,
    ACVMDESV,
    ACDESVIO,
    ACJUSENA,
    ACVAZMIN,
    ACNPOSNW,
    ACVERTJU,
    ACNUMCON,
    ACNUMMAQ,
    ACPOTEFE,
    FP,
    IR,
    CI,
    FC,
    TI,
    RQ,
    EZ,
    HV,
    LV,
    CV,
    HQ,
    LQ,
    CQ,
    AR,
    EV,
    HE,
    CM,
    FJ,
    VL,
    VA,
    VU,
    DA,
)

from idecomp.decomp.dadger import Dadger

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dadger import (
    MockEA,
    MockES,
    MockQI,
    MockTE,
    MockSB,
    MockUH,
    MockCT,
    MockUE,
    MockDP,
    MockPQ,
    MockCD,
    MockRI,
    MockIA,
    MockTX,
    MockGP,
    MockNI,
    MockDT,
    MockMP,
    MockMT,
    MockFD,
    MockVE,
    MockRE,
    MockLU,
    MockFU,
    MockFI,
    MockFT,
    MockVI,
    MockPD,
    MockPU,
    MockRC,
    MockPE,
    MockTS,
    MockPV,
    MockCX,
    MockFA,
    MockVT,
    MockCS,
    MockACJUSMED,
    MockACCOTVOL,
    MockACNUMJUS,
    MockACVOLMIN,
    MockACCOFEVA,
    MockACNUMPOS,
    MockACVSVERT,
    MockACVMDESV,
    MockACDESVIO,
    MockACJUSENA,
    MockACVAZMIN,
    MockACNPOSNW,
    MockACVERTJU,
    MockACNUMCON,
    MockACNUMMAQ,
    MockACPOTEFE,
    MockFP,
    MockIR,
    MockCI,
    MockFC,
    MockTI,
    MockRQ,
    MockEZ,
    MockHV,
    MockLV,
    MockCV,
    MockHQ,
    MockLQ,
    MockCQ,
    MockAR,
    MockEV,
    MockHE,
    MockCM,
    MockFJ,
    MockVL,
    MockVU,
    MockVA,
    MockDA,
    MockDadger,
)


def test_registro_te_dadger():
    m: MagicMock = mock_open(read_data="".join(MockTE))
    r = TE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        "PMO - JANEIRO/20 - FEVEREIRO/20 - REV 0 - FCF COM CVAR - 12 REE - VALOR ESP"
    ]
    assert (
        r.titulo
        == "PMO - JANEIRO/20 - FEVEREIRO/20 - REV 0 - FCF COM CVAR - 12 REE - VALOR ESP"
    )
    r.titulo = "Teste123"
    assert r.titulo == "Teste123"


def test_registro_sb_dadger():
    m: MagicMock = mock_open(read_data="".join(MockSB))
    r = SB()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, "SE"]
    assert r.codigo_submercado == 1
    r.codigo_submercado = 0
    assert r.codigo_submercado == 0
    assert r.nome_submercado == "SE"
    r.nome_submercado = "AB"
    assert r.nome_submercado == "AB"


def test_registro_uh_dadger():
    m: MagicMock = mock_open(read_data="".join(MockUH))
    r = UH()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 10, 25.29, None, 1, None, None, None, None, ""]
    assert r.codigo_usina == 1
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.codigo_ree == 10
    r.codigo_ree = 0
    assert r.codigo_ree == 0
    assert r.evaporacao == 1
    r.evaporacao = 0
    assert r.evaporacao == 0
    assert r.volume_inicial == 25.29
    r.volume_inicial = 0
    assert r.volume_inicial == 0
    assert r.configuracao_newave == ""
    r.configuracao_newave = "NW"
    assert r.configuracao_newave == "NW"


def test_registro_ct_dadger():
    m: MagicMock = mock_open(read_data="".join(MockCT))
    r = CT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        13,
        1,
        "ANGRA 2",
        1,
        1350.0,
        1350.0,
        20.12,
        1350.0,
        1350.0,
        20.12,
        1350.0,
        1350.0,
        20.12,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    assert r.codigo_usina == 13
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.codigo_submercado == 1
    r.codigo_submercado = 0
    assert r.codigo_submercado == 0
    assert r.nome_usina == "ANGRA 2"
    r.nome_usina = "A"
    assert r.nome_usina == "A"
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.inflexibilidade == [1350.0, 1350.0, 1350.0]
    r.inflexibilidade = [999.0]
    assert r.inflexibilidade == [999.0]
    assert r.cvu == [20.12, 20.12, 20.12]
    r.cvu = [999.0, 999.0, 999.0]
    assert r.cvu == [999.0, 999.0, 999.0]
    assert r.disponibilidade == [1350.0, 1350.0, 1350.0]
    r.disponibilidade = [999.0, 999.0, 999.0, 999.0]
    assert r.disponibilidade == [999.0, 999.0, 999.0, 999.0]


def test_registro_ue_dadger():
    m: MagicMock = mock_open(read_data="".join(MockUE))
    r = UE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        1,
        "Sta Cecilia",
        181,
        125,
        0.0,
        160.0,
        0.2,
    ]
    assert r.codigo_usina == 1
    assert r.codigo_submercado == 1
    assert r.nome_usina == "Sta Cecilia"
    assert r.codigo_usina_montante == 181
    assert r.codigo_usina_jusante == 125
    assert r.vazao_minima_bombeavel == 0.0
    assert r.vazao_maxima_bombeavel == 160.0
    assert r.taxa_consumo == 0.2


def test_registro_dp_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDP))
    r = DP()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        1,
        3,
        45078.0,
        32.0,
        41680.0,
        41.0,
        33894.0,
        95.0,
        None,
        None,
        None,
        None,
    ]
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.codigo_submercado == 1
    r.codigo_submercado = 0
    assert r.codigo_submercado == 0
    assert r.numero_patamares == 3
    r.numero_patamares = 0
    assert r.numero_patamares == 0
    assert r.carga == [45078.0, 41680.0, 33894.0]
    r.carga = [0]
    assert r.carga == [0]
    assert r.duracao == [32.0, 41.0, 95.0]
    r.duracao = [0, 0, 0, 0]
    assert r.duracao == [0, 0, 0, 0]


def test_registro_pq_dadger():
    m: MagicMock = mock_open(read_data="".join(MockPQ))
    r = PQ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == ["SECO_PCH", 1, 1, 2527, 2553, 2503, None, None]
    assert r.nome == "SECO_PCH"
    r.nome = "TESTE"
    assert r.nome == "TESTE"
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.codigo_submercado == 1
    r.codigo_submercado = 0
    assert r.codigo_submercado == 0
    assert r.geracao == [2527.0, 2553.0, 2503.0]
    r.geracao = [0]
    assert r.geracao == [0]


def test_registro_cd_dadger():
    m: MagicMock = mock_open(read_data="".join(MockCD))
    r = CD()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        1,
        "1PDEF",
        1,
        100,
        5249.34,
        100,
        5249.34,
        100,
        5249.34,
        None,
        None,
        None,
        None,
    ]
    assert r.codigo_curva == 1
    r.codigo_curva = 0
    assert r.codigo_curva == 0
    assert r.codigo_submercado == 1
    r.codigo_submercado = 0
    assert r.codigo_submercado == 0
    assert r.nome_curva == "1PDEF"
    r.nome_curva = "ABCD"
    assert r.nome_curva == "ABCD"
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.limite_superior == [100, 100, 100]
    r.limite_superior = [0]
    assert r.limite_superior == [0]
    assert r.custo == [5249.34, 5249.34, 5249.34]
    r.custo = [0, 0, 0, 0]
    assert r.custo == [0, 0, 0, 0]


def test_registro_ri_dadger():
    m: MagicMock = mock_open(read_data="".join(MockRI))
    r = RI()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        66,
        1,
        1,
        1680,
        7000,
        5079,
        7000,
        3179,
        1680,
        7000,
        4418,
        7000,
        2518,
        1680,
        7000,
        3474,
        7000,
        1574,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]


def test_registro_ia_dadger():
    m: MagicMock = mock_open(read_data="".join(MockIA))
    r = IA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        1,
        "NE",
        "FC",
        None,
        4200,
        5500,
        4200,
        5500,
        4200,
        5500,
        None,
        None,
        None,
        None,
    ]


def test_registro_tx_dadger():
    m: MagicMock = mock_open(read_data="".join(MockTX))
    r = TX()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [12.0]
    assert r.taxa == 12.0
    r.taxa = 0
    assert r.taxa == 0


def test_registro_gp_dadger():
    m: MagicMock = mock_open(read_data="".join(MockGP))
    r = GP()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [0.001]
    assert r.gap == 0.001
    r.gap = 0
    assert r.gap == 0


def test_registro_ni_dadger():
    m: MagicMock = mock_open(read_data="".join(MockNI))
    r = NI()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [200, None]
    assert r.iteracoes == 200
    r.iteracoes = 0
    assert r.iteracoes == 0
    assert r.tipo_limite == None
    r.tipo_limite = 1
    assert r.tipo_limite == 1


def test_registro_dt_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDT))
    r = DT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [28, 12, 2019]
    assert r.dia == 28
    r.dia = 0
    assert r.dia == 0
    assert r.mes == 12
    r.mes = 0
    assert r.mes == 0
    assert r.ano == 2019
    r.ano = 0
    assert r.ano == 0


def test_registro_mp_dadger():
    m: MagicMock = mock_open(read_data="".join(MockMP))
    r = MP()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        119,
        None,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    assert r.codigo_usina == 119
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.frequencia is None
    r.frequencia = 50
    assert r.frequencia == 50
    assert r.manutencao == [
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
    ]
    r.manutencao = [1.0, 1.0]
    assert r.manutencao == [1.0, 1.0]


def test_registro_mt_dadger():
    m: MagicMock = mock_open(read_data="".join(MockMT))
    r = MT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        4,
        1,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]

    assert r.codigo_usina == 4
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.codigo_submercado == 1
    r.codigo_submercado = 2
    assert r.codigo_submercado == 2
    assert r.manutencao == [
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
    ]
    r.manutencao = [1.0, 1.0]
    assert r.manutencao == [1.0, 1.0]


def test_registro_fd_dadger():
    m: MagicMock = mock_open(read_data="".join(MockFD))
    r = FD()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        66,
        50,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.947,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    assert r.codigo_usina == 66
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.frequencia == 50
    r.frequencia = 60
    assert r.frequencia == 60
    assert r.fator == [
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.947,
    ]
    r.fator = [1.0, 1.0]
    assert r.fator == [1.0, 1.0]


def test_registro_ve_dadger():
    m: MagicMock = mock_open(read_data="".join(MockVE))
    r = VE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        24,
        95.41,
        97.01,
        97.01,
        97.01,
        97.83,
        99.18,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    assert r.codigo_usina == 24
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.volume == [
        95.41,
        97.01,
        97.01,
        97.01,
        97.83,
        99.18,
    ]
    r.volume = [0]
    assert r.volume == [
        0,
    ]


def test_registro_re_dadger():
    m: MagicMock = mock_open(read_data="".join(MockRE))
    r = RE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [5, 1, 6]
    assert r.codigo_restricao == 5
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio_inicial == 1
    r.estagio_inicial = 0
    assert r.estagio_inicial == 0
    assert r.estagio_final == 6
    r.estagio_final = 0
    assert r.estagio_final == 0


def test_registro_lu_dadger():
    m: MagicMock = mock_open(read_data="".join(MockLU))
    r = LU()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [21, 1, 50, 212, 50, 212, 50, 212, None, None, None, None]
    assert r.codigo_restricao == 21
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.limite_inferior == [50, 50, 50, None, None]
    r.limite_inferior = [0, 0]
    assert r.limite_inferior == [0, 0, None, None, None]
    assert r.limite_superior == [212, 212, 212, None, None]
    r.limite_superior = [0, 0, 0, 0]
    assert r.limite_superior == [0, 0, 0, 0, None]


def test_registro_fu_dadger():
    m: MagicMock = mock_open(read_data="".join(MockFU))
    r = FU()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [43, 1, 47, 1, None]
    assert r.codigo_restricao == 43
    assert r.estagio == 1
    assert r.codigo_usina == 47
    assert r.coeficiente == 1
    assert r.frequencia == None


def test_registro_fi_dadger():
    m: MagicMock = mock_open(read_data="".join(MockFI))
    r = FI()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [417, 1, "NE", "SE", 1]
    assert r.codigo_restricao == 417
    assert r.estagio == 1
    assert r.codigo_submercado_de == "NE"
    assert r.codigo_submercado_para == "SE"
    assert r.coeficiente == 1


def test_registro_ft_dadger():
    m: MagicMock = mock_open(read_data="".join(MockFT))
    r = FT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [449, 1, 310, 4, 1]
    assert r.codigo_restricao == 449
    assert r.estagio == 1
    assert r.codigo_usina == 310
    assert r.codigo_submercado == 4
    assert r.coeficiente == 1


def test_registro_vi_dadger():
    m: MagicMock = mock_open(read_data="".join(MockVI))
    r = VI()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        156,
        360,
        296,
        296,
        293,
        328,
        455,
        None,
        None,
        None,
        None,
    ]
    assert r.codigo_usina == 156
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.duracao == 360
    r.duracao = 0
    assert r.duracao == 0
    assert r.vazao == [
        296,
        296,
        293,
        328,
        455,
    ]
    r.vazao = [0]
    assert r.vazao == [0]


def test_registro_acjusmed_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACJUSMED))
    r = ACJUSMED()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        285,
        73.47,
        "JAN",
        1,
        2020,
    ]
    assert r.codigo_usina == 285
    r.codigo_usina = 20
    assert r.codigo_usina == 20
    assert r.cota == 73.47
    r.cota = 55.0
    assert r.cota == 55.0
    assert r.mes == "JAN"
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana == 1
    r.semana = 5
    assert r.semana == 5
    assert r.ano == 2020
    r.ano = 2022
    assert r.ano == 2022


def test_registro_accotvol_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACCOTVOL))
    r = ACCOTVOL()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [
        285,
        1,
        90.0,
        "JAN",
        1,
        2020,
    ]
    assert r.codigo_usina == 285
    r.codigo_usina = 10
    assert r.codigo_usina == 10
    assert r.ordem == 1
    r.ordem = 2
    assert r.ordem == 2
    assert r.coeficiente == 90.0
    r.coeficiente = 3.14
    assert r.coeficiente == 3.14
    assert r.mes == "JAN"
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana == 1
    r.semana = 5
    assert r.semana == 5
    assert r.ano == 2020
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acvolmin_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACVOLMIN))
    r = ACVOLMIN()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [34, 15563, "", None, None]
    assert r.codigo_usina == 34
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.volume == 15563
    r.volume = 50.5
    assert r.volume == 50.5
    assert r.mes == ""
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana is None
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_accofeva_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACCOFEVA))
    r = ACCOFEVA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [95, 10, 0, "", None, None]
    assert r.codigo_usina == 95
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.mes_coeficiente == 10
    r.mes_coeficiente = 5
    assert r.mes_coeficiente == 5
    assert r.coeficiente == 0
    r.coeficiente = 5
    assert r.coeficiente == 5
    assert r.mes == ""
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana is None
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acnumpos_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACNUMPOS))
    r = ACNUMPOS()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [119, 300, "", None, None]
    assert r.codigo_usina == 119
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.codigo_posto == 300
    r.codigo_posto = 50
    assert r.codigo_posto == 50
    assert r.mes == ""
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana is None
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acvsvert_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACVSVERT))
    r = ACVSVERT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [117, 144.14, "", None, None]
    assert r.codigo_usina == 117
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.volume == 144.14
    r.volume = 50
    assert r.volume == 50
    assert r.mes == ""
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana is None
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acvmdesv_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACVMDESV))
    r = ACVMDESV()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [124, 102.0, "", None, None]
    assert r.codigo_usina == 124
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.volume == 102
    r.volume = 50
    assert r.volume == 50
    assert r.mes == ""
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana is None
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acnumjus_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACNUMJUS))
    r = ACNUMJUS()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [117, 108.0, "", None, None]
    assert r.codigo_usina == 117
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.codigo_usina_jusante == 108.0
    r.codigo_usina_jusante = 50
    assert r.codigo_usina_jusante == 50
    assert r.mes == ""
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana is None
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acdesvio_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACDESVIO))
    r = ACDESVIO()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [118, 119, 100.0, "", None, None]
    assert r.codigo_usina == 118
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.codigo_usina_jusante == 119
    r.codigo_usina_jusante = 50
    assert r.codigo_usina_jusante == 50
    assert r.limite_vazao == 100.0
    r.limite_vazao = 50.0
    assert r.limite_vazao == 50.0
    assert r.mes == ""
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana is None
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acjusena_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACJUSENA))
    r = ACJUSENA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [172, 176, "", None, None]
    assert r.codigo_usina == 172
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.codigo_usina_jusante == 176
    r.codigo_usina_jusante = 50
    assert r.codigo_usina_jusante == 50
    assert r.mes == ""
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana is None
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acvazmin_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACVAZMIN))
    r = ACVAZMIN()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [4, 0, "", None, None]
    assert r.codigo_usina == 4
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.vazao == 0
    r.vazao = 50
    assert r.vazao == 50
    assert r.mes == ""
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana is None
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acnposnw_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACNPOSNW))
    r = ACNPOSNW()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [43, 43, "", None, None]
    assert r.codigo_usina == 43
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.codigo_posto == 43
    r.codigo_posto = 50
    assert r.codigo_posto == 50
    assert r.mes == ""
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana is None
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acvertju_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACVERTJU))
    r = ACVERTJU()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [103, 1, "", None, None]
    assert r.codigo_usina == 103
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.considera_influencia == 1
    r.considera_influencia = 0
    assert r.considera_influencia == 0
    assert r.mes == ""
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana is None
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acnumcon_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACNUMCON))
    r = ACNUMCON()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [275, 2, "JAN", 1, None]
    assert r.codigo_usina == 275
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.numero_conjuntos == 2
    r.numero_conjuntos = 0
    assert r.numero_conjuntos == 0
    assert r.mes == "JAN"
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana == 1
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acnummaq_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACNUMMAQ))
    r = ACNUMMAQ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [275, 1, 2, "JAN", 1, None]
    assert r.codigo_usina == 275
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.indice_conjunto == 1
    r.indice_conjunto = 0
    assert r.indice_conjunto == 0
    assert r.numero_maquinas == 2
    r.numero_maquinas = 0
    assert r.numero_maquinas == 0
    assert r.mes == "JAN"
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana == 1
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_acpotefe_dadger():
    m: MagicMock = mock_open(read_data="".join(MockACPOTEFE))
    r = ACPOTEFE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [275, 1, 22.5, "JAN", 1, None]
    assert r.codigo_usina == 275
    r.codigo_usina = 40
    assert r.codigo_usina == 40
    assert r.indice_conjunto == 1
    r.indice_conjunto = 0
    assert r.indice_conjunto == 0
    assert r.potencia == 22.5
    r.potencia = 0
    assert r.potencia == 0
    assert r.mes == "JAN"
    r.mes = "DEZ"
    assert r.mes == "DEZ"
    assert r.semana == 1
    r.semana = 5
    assert r.semana == 5
    assert r.ano is None
    r.ano = 2022
    assert r.ano == 2022


def test_registro_fp_dadger():
    m: MagicMock = mock_open(read_data="".join(MockFP))
    r = FP()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [999, 1, 0, 5, 0, 100, 0, 5, 20, 20, None, None, 0]
    assert r.codigo_usina == 999
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.tipo_entrada_janela_turbinamento == 0
    r.tipo_entrada_janela_turbinamento = 1
    assert r.tipo_entrada_janela_turbinamento == 1
    assert r.numero_pontos_turbinamento == 5
    r.numero_pontos_turbinamento = 1
    assert r.numero_pontos_turbinamento == 1
    assert r.limite_inferior_janela_turbinamento == 0
    r.limite_inferior_janela_turbinamento = 1
    assert r.limite_inferior_janela_turbinamento == 1
    assert r.limite_superior_janela_turbinamento == 100
    r.limite_superior_janela_turbinamento = 0
    assert r.limite_superior_janela_turbinamento == 0
    assert r.tipo_entrada_janela_volume == 0
    r.tipo_entrada_janela_volume = 1
    assert r.tipo_entrada_janela_volume == 1
    assert r.numero_pontos_volume == 5
    r.numero_pontos_volume = 0
    assert r.numero_pontos_volume == 0
    assert r.limite_inferior_janela_volume == 20
    r.limite_inferior_janela_volume = 1
    assert r.limite_inferior_janela_volume == 1
    assert r.limite_superior_janela_volume == 20
    r.limite_superior_janela_volume = 0
    assert r.limite_superior_janela_volume == 0


def test_registro_ir_dadger():
    m: MagicMock = mock_open(read_data="".join(MockIR))
    r = IR()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == ["NORMAL", 17, 61, None]
    assert r.tipo == "NORMAL"
    r.tipo = "ABC"
    assert r.tipo == "ABC"


def test_registro_ci_dadger():
    m: MagicMock = mock_open(read_data="".join(MockCI))
    r = CI()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [0, 2, "", 1, 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0.0, None]


def test_registro_fc_dadger():
    m: MagicMock = mock_open(read_data="".join(MockFC))
    r = FC()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == ["NEWV21", "../../cortesh.dat"]
    assert r.caminho == "../../cortesh.dat"
    r.caminho = "."
    assert r.caminho == "."


def test_registro_ea_dadger():
    m: MagicMock = mock_open(read_data="".join(MockEA))
    r = EA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [
        1,
        1917.35,
        1405.37,
        1633.83,
        1622.15,
        2694.79,
        2352.88,
        2843.12,
        5599.16,
        6315.02,
        10150.71,
        3773.21,
    ]
    assert r.codigo_ree == 1
    r.codigo_ree = 2
    assert r.codigo_ree == 2
    assert r.ena == [
        1917.35,
        1405.37,
        1633.83,
        1622.15,
        2694.79,
        2352.88,
        2843.12,
        5599.16,
        6315.02,
        10150.71,
        3773.21,
    ]
    r.ena = [1, 2, 3]
    assert r.ena == [1, 2, 3]


def test_registro_es_dadger():
    m: MagicMock = mock_open(read_data="".join(MockES))
    r = ES()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [
        1,
        5,
        1917.35,
        1405.37,
        1633.83,
        1622.15,
        2694.79,
    ]
    assert r.codigo_ree == 1
    r.codigo_ree = 2
    assert r.codigo_ree == 2
    assert r.numero_semanas_mes_anterior == 5
    r.numero_semanas_mes_anterior = 4
    assert r.numero_semanas_mes_anterior == 4
    assert r.ena == [
        1917.35,
        1405.37,
        1633.83,
        1622.15,
        2694.79,
    ]
    r.ena = [1, 2, 3]
    assert r.ena == [1, 2, 3]


def test_registro_qi_dadger():
    m: MagicMock = mock_open(read_data="".join(MockQI))
    r = QI()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [156, 136, 168, 174, 152, 128]
    assert r.codigo_usina == 156
    r.codigo_usina = 2
    assert r.codigo_usina == 2
    assert r.vazao == [136, 168, 174, 152, 128]
    r.vazao = [1, 2, 3]
    assert r.vazao == [1, 2, 3]


def test_registro_ti_dadger():
    m: MagicMock = mock_open(read_data="".join(MockTI))
    r = TI()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [
        107,
        -24.6,
        -24.6,
        -24.6,
        -24.6,
        -24.6,
        -24.6,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    assert r.codigo_usina == 107
    r.codigo_usina = 0
    assert r.codigo_usina == 0
    assert r.taxa == [-24.6, -24.6, -24.6, -24.6, -24.6, -24.6]
    r.taxa = [5.0]
    assert r.taxa == [5.0]


def test_registro_rq_dadger():
    m: MagicMock = mock_open(read_data="".join(MockRQ))
    r = RQ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [1, 100, 100, 100, 100, 100, 0, None, None]
    assert r.codigo_ree == 1
    r.codigo_ree = 0
    assert r.codigo_ree == 0
    assert r.vazao == [100, 100, 100, 100, 100, 0]
    r.vazao = [100, 100, 100]
    assert r.vazao == [100, 100, 100]


def test_registro_ez_dadger():
    m: MagicMock = mock_open(read_data="".join(MockEZ))
    r = EZ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [251, 55.0]
    assert r.codigo_usina == 251
    r.codigo_usina = 200
    assert r.codigo_usina == 200
    assert r.volume == 55.0
    r.volume = 100.0
    assert r.volume == 100.0


def test_registro_hv_dadger():
    m: MagicMock = mock_open(read_data="".join(MockHV))
    r = HV()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [3, 1, 6]
    assert r.codigo_restricao == 3
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio_inicial == 1
    r.estagio_inicial = 0
    assert r.estagio_inicial == 0
    assert r.estagio_final == 6
    r.estagio_final = 0
    assert r.estagio_final == 0


def test_registro_lv_dadger():
    m: MagicMock = mock_open(read_data="".join(MockLV))
    r = LV()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [101, 1, 3898.2, 38982.0]
    assert r.codigo_restricao == 101
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.limite_inferior == 3898.2
    r.limite_inferior = 0
    assert r.limite_inferior == 0
    assert r.limite_superior == 38982.0
    r.limite_superior = 0
    assert r.limite_superior == 0


def test_registro_cv_dadger():
    m: MagicMock = mock_open(read_data="".join(MockCV))
    r = CV()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [117, 1, 43, -1.5866762, "VARM"]
    assert r.codigo_restricao == 117
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.codigo_usina == 43
    r.codigo_usina = 10
    assert r.codigo_usina == 10
    assert r.coeficiente == -1.5866762
    r.coeficiente = 1
    assert r.coeficiente == 1
    assert r.tipo == "VARM"
    r.tipo = ""
    assert r.tipo == ""


def test_registro_hq_dadger():
    m: MagicMock = mock_open(read_data="".join(MockHQ))
    r = HQ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [5, 1, 6]
    assert r.codigo_restricao == 5
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio_inicial == 1
    r.estagio_inicial = 0
    assert r.estagio_inicial == 0
    assert r.estagio_final == 6
    r.estagio_final = 0
    assert r.estagio_final == 0


def test_registro_lq_dadger():
    m: MagicMock = mock_open(read_data="".join(MockLQ))
    r = LQ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [
        10,
        1,
        300,
        9999,
        300,
        9999,
        300,
        9999,
        None,
        None,
        None,
        None,
    ]
    assert r.codigo_restricao == 10
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.limite_inferior == [300, 300, 300, None, None]
    r.limite_inferior = [0]
    assert r.limite_inferior == [0, None, None, None, None]
    assert r.limite_superior == [9999, 9999, 9999, None, None]
    r.limite_superior = [0, 0, 0, 0]
    assert r.limite_superior == [0, 0, 0, 0, None]


def test_registro_cq_dadger():
    m: MagicMock = mock_open(read_data="".join(MockCQ))
    r = CQ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [11, 1, 27, 1, "QDEF"]
    assert r.codigo_restricao == 11
    r.codigo_restricao = 5
    assert r.codigo_restricao == 5
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.codigo_usina == 27
    r.codigo_usina = 10
    assert r.codigo_usina == 10
    assert r.coeficiente == 1
    r.coeficiente = -1
    assert r.coeficiente == -1
    assert r.tipo == "QDEF"
    r.tipo = ""
    assert r.tipo == ""


def test_registro_ar_dadger():
    m: MagicMock = mock_open(read_data="".join(MockAR))
    r = AR()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [1, None, None]
    assert r.estagio == 1
    r.estagio = 2
    assert r.estagio == 2
    assert r.alfa is None
    r.alfa = 50
    assert r.alfa == 50
    assert r.lamb is None
    r.lamb = 10
    assert r.lamb == 10


def test_registro_ev_dadger():
    m: MagicMock = mock_open(read_data="".join(MockEV))
    r = EV()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [1, "INI"]
    assert r.modelo == 1
    r.modelo = 0
    assert r.modelo == 0
    assert r.volume_referencia == "INI"
    r.volume_referencia = "FIN"
    assert r.volume_referencia == "FIN"


def test_registro_he_dadger():
    m: MagicMock = mock_open(read_data="".join(MockHE))
    r = HE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [1, 2, 60.0, 1, 1710.0, 1, 0, 0, "prodrhe.dat"]
    assert r.codigo_restricao == 1
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.tipo_limite == 2
    r.tipo_limite = 0
    assert r.tipo_limite == 0
    assert r.limite == 60.0
    r.limite = 0
    assert r.limite == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.valor_penalidade == 1710
    r.valor_penalidade = 0
    assert r.valor_penalidade == 0
    assert r.forma_calculo_produtibilidades == 1
    r.forma_calculo_produtibilidades = 0
    assert r.forma_calculo_produtibilidades == 0
    assert r.tipo_valores_produtibilidades == 0
    r.tipo_valores_produtibilidades = 0
    assert r.tipo_valores_produtibilidades == 0
    assert r.tipo_penalidade == 0
    r.tipo_penalidade = 1
    assert r.tipo_penalidade == 1
    assert r.arquivo_produtibilidades == "prodrhe.dat"
    r.arquivo_produtibilidades = "teste.dat"
    assert r.arquivo_produtibilidades == "teste.dat"


def test_registro_cm_dadger():
    m: MagicMock = mock_open(read_data="".join(MockCM))
    r = CM()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [1, 1, 1.0]
    assert r.codigo_restricao == 1
    r.codigo_restricao = 0
    assert r.codigo_restricao == 0
    assert r.codigo_ree == 1
    r.codigo_ree = 0
    assert r.codigo_ree == 0
    assert r.coeficiente == 1.0
    r.coeficiente = 0
    assert r.coeficiente == 0


def test_registro_fj_dadger():
    m: MagicMock = mock_open(read_data="".join(MockFJ))
    r = FJ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == ["polinjus.dat"]
    assert r.arquivo == "polinjus.dat"
    r.arquivo = "teste.dat"
    assert r.arquivo == "teste.dat"


def test_registro_pd_dadger():
    m: MagicMock = mock_open(read_data="".join(MockPD))
    r = PD()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == ["PRIMAL"]
    assert r.algoritmo == "PRIMAL"
    r.algoritmo = "DUAL"
    assert r.algoritmo == "DUAL"


def test_registro_pu_dadger():
    m: MagicMock = mock_open(read_data="".join(MockPU))
    r = PU()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [1]
    assert r.pl == 1
    r.pl = 0
    assert r.pl == 0


def test_registro_rc_dadger():
    m: MagicMock = mock_open(read_data="".join(MockRC))
    r = RC()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == ["ESCADA"]
    assert r.mnemonico == "ESCADA"
    r.mnemonico = ""
    assert r.mnemonico == ""


def test_registro_pe_dadger():
    m: MagicMock = mock_open(read_data="".join(MockPE))
    r = PE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [1, 0, 10000.00]
    assert r.codigo_submercado == 1
    r.codigo_submercado = 2
    assert r.codigo_submercado == 2
    assert r.tipo == 0
    r.tipo = 1
    assert r.tipo == 1
    assert r.penalidade == 10000.00
    r.penalidade = 500.00
    assert r.penalidade == 500.00


def test_registro_ts_dadger():
    m: MagicMock = mock_open(read_data="".join(MockTS))
    r = TS()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [0.00000000001, 0.000000000001, 1, 0.000000000001]
    assert r.tolerancia_primaria == 0.00000000001
    r.tolerancia_primaria = 0.00000000002
    assert r.tolerancia_primaria == 0.00000000002
    assert r.tolerancia_secundaria == 0.000000000001
    r.tolerancia_secundaria = 0.00000000002
    assert r.tolerancia_secundaria == 0.00000000002
    assert r.zera_coeficientes == 1
    r.zera_coeficientes = 0
    assert r.zera_coeficientes == 0
    assert r.tolerancia_teste_otimalidade == 0.000000000001
    r.tolerancia_teste_otimalidade = 0.00000000002
    assert r.tolerancia_teste_otimalidade == 0.00000000002


def test_registro_pv_dadger():
    m: MagicMock = mock_open(read_data="".join(MockPV))
    r = PV()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [
        10000000000000000.00,
        10000000000000000.00,
        1,
        1.2,
        10000000000000000.00,
        10000000000000000.00,
    ]
    assert r.penalidade_variaveis_folga == 10000000000000000.00
    r.penalidade_variaveis_folga = 12000000000000000.00
    assert r.penalidade_variaveis_folga == 12000000000000000.00
    assert r.tolerancia_viabilidade_restricoes == 10000000000000000.00
    r.tolerancia_viabilidade_restricoes = 12000000000000000.00
    assert r.tolerancia_viabilidade_restricoes == 12000000000000000.00
    assert r.iteracoes_atualizacao_penalidade == 1
    r.iteracoes_atualizacao_penalidade = 0
    assert r.iteracoes_atualizacao_penalidade == 0
    assert r.fator_multiplicacao_folga == 1.2
    r.fator_multiplicacao_folga = 1.5
    assert r.fator_multiplicacao_folga == 1.5
    assert r.valor_inicial_variaveis_folga == 10000000000000000.00
    r.valor_inicial_variaveis_folga = 12000000000000000.00
    assert r.valor_inicial_variaveis_folga == 12000000000000000.00
    assert r.valor_final_variaveis_folga == 10000000000000000.00
    r.valor_final_variaveis_folga = 12000000000000000.00
    assert r.valor_final_variaveis_folga == 12000000000000000.00


def test_registro_cx_dadger():
    m: MagicMock = mock_open(read_data="".join(MockCX))
    r = CX()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [101, 102]
    assert r.codigo_newave == 101
    r.codigo_newave = 105
    assert r.codigo_newave == 105
    assert r.codigo_decomp == 102
    r.codigo_decomp = 110
    assert r.codigo_decomp == 110


def test_registro_fa_dadger():
    m: MagicMock = mock_open(read_data="".join(MockFA))
    r = FA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == ["indices.csv"]
    assert r.arquivo == "indices.csv"
    r.arquivo = "indices2.csv"
    assert r.arquivo == "indices2.csv"


def test_registro_vt_dadger():
    m: MagicMock = mock_open(read_data="".join(MockVT))
    r = VT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == ["ventos.dat"]
    assert r.arquivo == "ventos.dat"
    r.arquivo = "ventos2.dat"
    assert r.arquivo == "ventos2.dat"


def test_registro_cs_dadger():
    m: MagicMock = mock_open(read_data="".join(MockCS))
    r = CS()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [1]
    assert r.consistencia == 1
    r.consistencia = 0
    assert r.consistencia == 0


def test_registro_vl_dadger():
    m: MagicMock = mock_open(read_data="".join(MockVL))
    r = VL()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [288, 1, None, None, None, None, None]
    assert r.codigo_usina_influenciada == 288
    r.codigo_usina_influenciada = 0
    assert r.codigo_usina_influenciada == 0
    assert r.fator_impacto_defluencia == 1
    r.fator_impacto_defluencia = 0
    assert r.fator_impacto_defluencia == 0
    assert r.coeficiente_a0 is None
    r.coeficiente_a0 = 0
    assert r.coeficiente_a0 == 0
    assert r.coeficiente_a1 is None
    r.coeficiente_a1 = 0
    assert r.coeficiente_a1 == 0
    assert r.coeficiente_a2 is None
    r.coeficiente_a2 = 0
    assert r.coeficiente_a2 == 0
    assert r.coeficiente_a3 is None
    r.coeficiente_a3 = 0
    assert r.coeficiente_a3 == 0
    assert r.coeficiente_a4 is None
    r.coeficiente_a4 = 0
    assert r.coeficiente_a4 == 0


def test_registro_vu_dadger():
    m: MagicMock = mock_open(read_data="".join(MockVU))
    r = VU()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [288, 314, 1]
    assert r.codigo_usina_influenciada == 288
    r.codigo_usina_influenciada = 0
    assert r.codigo_usina_influenciada == 0
    assert r.codigo_usina_influenciadora == 314
    r.codigo_usina_influenciadora = 0
    assert r.codigo_usina_influenciadora == 0
    assert r.fator_impacto_defluencia == 1
    r.fator_impacto_defluencia = 0
    assert r.fator_impacto_defluencia == 0


def test_registro_va_dadger():
    m: MagicMock = mock_open(read_data="".join(MockVA))
    r = VA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [288, 288, 0.07]
    assert r.codigo_usina_influenciada == 288
    r.codigo_usina_influenciada = 0
    assert r.codigo_usina_influenciada == 0
    assert r.codigo_posto_influenciador == 288
    r.codigo_posto_influenciador = 0
    assert r.codigo_posto_influenciador == 0
    assert r.fator_impacto_incremental == 0.07
    r.fator_impacto_incremental = 0
    assert r.fator_impacto_incremental == 0


def test_registro_da_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDA))
    r = DA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [97, 98, 1, 17, 100, 20000]
    assert r.codigo_usina_retirada == 97
    r.codigo_usina_retirada = 0
    assert r.codigo_usina_retirada == 0
    assert r.codigo_usina_retorno == 98
    r.codigo_usina_retorno = 0
    assert r.codigo_usina_retorno == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.vazao_desviada == 17
    r.vazao_desviada = 0
    assert r.vazao_desviada == 0
    assert r.retorno_percentual == 100
    r.retorno_percentual = 0
    assert r.retorno_percentual == 0
    assert r.custo == 20000
    r.custo = 0
    assert r.custo == 0


def test_campos_nao_encontrados_dadger():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        d = Dadger.read(".")
    assert d.te is None
    assert d.sb(0) is None
    assert d.uh(0) is None
    assert d.ct(0, 0) is None
    assert d.dp(0, 0) is None
    assert d.ac(0, ACNUMCON, mes="", revisao=0, ano=0) is None
    assert d.cd(0, 0) is None
    assert d.tx is None
    assert d.gp is None
    assert d.ni is None
    assert d.dt is None
    assert d.re(0) is None
    assert d.lu(0, 0) is None
    assert d.vi(0) is None
    assert d.ir("") is None
    assert d.rt("") is None
    assert d.fc("") is None
    assert d.ti(0) is None
    assert d.fp(0, 0) is None
    assert d.ve(0) is None
    assert d.hv(0) is None
    assert d.lv(0, 0) is None
    assert d.hq(0) is None
    assert d.lq(0, 0) is None
    assert d.he(0, 0) is None
    assert d.cm(0) is None
    assert d.vl() is None
    assert d.va() is None
    assert d.vu() is None
    assert d.da() is None


def test_campos_encontrados_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m):
        d = Dadger.read("./tests/mocks/arquivos/dadger.py")
    assert d.te is not None
    assert d.sb(1) is not None
    assert d.uh(1) is not None
    assert d.ct(65, 1) is not None
    assert d.dp(1, 1) is not None
    assert d.ac(285, ACJUSMED) is not None
    assert d.cd(1, 1) is not None
    assert d.tx is not None
    assert d.gp is not None
    assert d.ni is not None
    assert d.dt is not None
    assert d.re(449) is not None
    assert d.lu(449, 1) is not None
    assert d.vi(156) is not None
    assert d.ir("GRAFICO") is not None
    assert d.rt("CRISTA") is not None
    assert d.fc("NEWV21") is not None
    assert d.ti(1) is not None
    assert d.mp(119) is not None
    assert d.mt(149, 2) is not None
    assert d.fd(66, 50) is not None
    assert d.fp(999, 1) is not None
    assert d.ve(1) is not None
    assert d.hv(101) is not None
    assert d.lv(101, 1) is not None
    assert d.hq(254) is not None
    assert d.lq(254, 1) is not None
    assert d.he(1, 1) is not None
    assert d.cm(1) is not None
    assert len(d.lq(df=True).columns) == 12


def test_cria_lu_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m):
        d = Dadger.read("./tests/mocks/arquivos/dadger.py")
        lu = d.lu(1, 2)
        assert lu is not None
        assert lu.limite_inferior == d.lu(1, 1).limite_inferior
        lu.limite_inferior = [0.0]
        assert lu.limite_inferior != d.lu(1, 1).limite_inferior
        assert lu.limite_superior == d.lu(1, 1).limite_superior
        lu.limite_superior = [0.0]
        assert lu.limite_superior != d.lu(1, 1).limite_superior


def test_cria_lv_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m):
        d = Dadger.read("./tests/mocks/arquivos/dadger.py")
        lv = d.lv(3, 2)
        assert lv is not None
        assert lv.limite_inferior == d.lv(3, 1).limite_inferior
        lv.limite_inferior = 0.0
        assert lv.limite_inferior != d.lv(3, 1).limite_inferior
        assert lv.limite_superior == d.lv(3, 1).limite_superior
        lv.limite_superior = 0.0
        assert lv.limite_superior != d.lv(3, 1).limite_superior


def test_cria_lq_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m):
        d = Dadger.read("./tests/mocks/arquivos/dadger.py")
        lq = d.lq(5, 2)
        assert lq is not None
        assert lq.limite_inferior == d.lq(5, 1).limite_inferior
        lq.limite_inferior = [0.0]
        assert lq.limite_inferior != d.lq(5, 1).limite_inferior
        assert lq.limite_superior == d.lq(5, 1).limite_superior
        lq.limite_superior = [0.0]
        assert lq.limite_superior != d.lq(5, 1).limite_superior


def test_eq_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m):
        d1 = Dadger.read("./tests/mocks/arquivos/dadger.py")
        d2 = Dadger.read("./tests/mocks/arquivos/dadger.py")
        assert d1 == d2


def test_neq_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m):
        d1 = Dadger.read("./tests/mocks/arquivos/dadger.py")
        d2 = Dadger.read("./tests/mocks/arquivos/dadger.py")
        d2.te.titulo = "Teste"
        assert d1 != d2


def test_leitura_escrita_dadger():
    m_leitura: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m_leitura):
        d1 = Dadger.read("./tests/mocks/arquivos/dadger.py")
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        d1.write("./tests/mocks/arquivos/dadger.py")
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(2, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        d2 = Dadger.read("./tests/mocks/arquivos/dadger.py")
        assert d1 == d2
