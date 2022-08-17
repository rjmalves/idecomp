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
    assert r.codigo == 1
    r.codigo = 0
    assert r.codigo == 0
    assert r.nome == "SE"
    r.nome = "AB"
    assert r.nome == "AB"


def test_registro_uh_dadger():

    m: MagicMock = mock_open(read_data="".join(MockUH))
    r = UH()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 10, 25.29, None, 1, None, None, None, None]
    assert r.codigo == 1
    r.codigo = 0
    assert r.codigo == 0
    assert r.ree == 10
    r.ree = 0
    assert r.ree == 0
    assert r.evaporacao == 1
    r.evaporacao = 0
    assert r.evaporacao == 0
    assert r.volume_inicial == 25.29
    r.volume_inicial = 0
    assert r.volume_inicial == 0


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
    ]
    assert r.codigo == 13
    r.codigo = 0
    assert r.codigo == 0
    assert r.subsistema == 1
    r.subsistema = 0
    assert r.subsistema == 0
    assert r.nome == "ANGRA 2"
    r.nome = "A"
    assert r.nome == "A"
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.inflexibilidades == [1350.0, 1350.0, 1350.0]
    r.inflexibilidades = [999.0]
    assert r.inflexibilidades == [999.0]
    assert r.cvus == [20.12, 20.12, 20.12]
    r.cvus = [999.0, 999.0, 999.0]
    assert r.cvus == [999.0, 999.0, 999.0]
    assert r.disponibilidades == [1350.0, 1350.0, 1350.0]
    r.disponibilidades = [999.0, 999.0, 999.0, 999.0]
    assert r.disponibilidades == [999.0, 999.0, 999.0, 999.0]


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
    assert r.codigo == 1
    assert r.subsistema == 1
    assert r.nome == "Sta Cecilia"
    assert r.uhe_montante == 181
    assert r.uhe_jusante == 125
    assert r.vazao_minima_bombeavel == 0.0
    assert r.vazao_maxima_bombeavel == 160.0
    assert r.taxa_consumo == 0.2


def test_registro_dp_dadger():

    m: MagicMock = mock_open(read_data="".join(MockDP))
    r = DP()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, 1, 3, 45078.0, 32.0, 41680.0, 41.0, 33894.0, 95.0]
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.subsistema == 1
    r.subsistema = 0
    assert r.subsistema == 0
    assert r.num_patamares == 3
    r.num_patamares = 0
    assert r.num_patamares == 0
    assert r.cargas == [45078.0, 41680.0, 33894.0]
    r.cargas = [0]
    assert r.cargas == [0]
    assert r.duracoes == [32.0, 41.0, 95.0]
    r.duracoes = [0, 0, 0, 0]
    assert r.duracoes == [0, 0, 0, 0]


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
    ]
    assert r.numero_curva == 1
    r.numero_curva = 0
    assert r.numero_curva == 0
    assert r.subsistema == 1
    r.subsistema = 0
    assert r.subsistema == 0
    assert r.nome_curva == "1PDEF"
    r.nome_curva = "ABCD"
    assert r.nome_curva == "ABCD"
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.limites_superiores == [100, 100, 100]
    r.limites_superiores = [0]
    assert r.limites_superiores == [0]
    assert r.custos == [5249.34, 5249.34, 5249.34]
    r.custos = [0, 0, 0, 0]
    assert r.custos == [0, 0, 0, 0]


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
    ]


def test_registro_ia_dadger():

    m: MagicMock = mock_open(read_data="".join(MockIA))
    r = IA()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [1, "NE", "FC", None, 4200, 5500, 4200, 5500, 4200, 5500]


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
    ]


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
    ]


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
    ]


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
    ]
    assert r.codigo == 24
    r.codigo = 0
    assert r.codigo == 0
    assert r.volumes == [
        95.41,
        97.01,
        97.01,
        97.01,
        97.83,
        99.18,
    ]
    r.volumes = [0]
    assert r.volumes == [
        0,
    ]


def test_registro_re_dadger():

    m: MagicMock = mock_open(read_data="".join(MockRE))
    r = RE()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [5, 1, 6]
    assert r.codigo == 5
    r.codigo = 0
    assert r.codigo == 0
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

    assert r.data == [21, 1, 50, 212, 50, 212, 50, 212]
    assert r.codigo == 21
    r.codigo = 0
    assert r.codigo == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.limites_inferiores == [50, 50, 50]
    r.limites_inferiores = [0, 0]
    assert r.limites_inferiores == [0, 0, None]
    assert r.limites_superiores == [212, 212, 212]
    r.limites_superiores = [0, 0, 0, 0]
    assert r.limites_superiores == [0, 0, 0, 0]


def test_registro_fu_dadger():

    m: MagicMock = mock_open(read_data="".join(MockFU))
    r = FU()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [43, 1, 47, 1, None]
    assert r.restricao == 43
    assert r.estagio == 1
    assert r.uhe == 47
    assert r.coeficiente == 1
    assert r.frequencia == None


def test_registro_fi_dadger():

    m: MagicMock = mock_open(read_data="".join(MockFI))
    r = FI()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [417, 1, "NE", "SE", 1]
    assert r.restricao == 417
    assert r.estagio == 1
    assert r.de == "NE"
    assert r.coeficiente == 1


def test_registro_ft_dadger():

    m: MagicMock = mock_open(read_data="".join(MockFT))
    r = FT()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)

    assert r.data == [449, 1, 310, 4, 1]
    assert r.restricao == 449
    assert r.estagio == 1
    assert r.ute == 310
    assert r.subsistema == 4
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
    assert r.uhe == 156
    r.uhe = 0
    assert r.uhe == 0
    assert r.duracao == 360
    r.duracao = 0
    assert r.duracao == 0
    assert r.vazoes == [
        296,
        296,
        293,
        328,
        455,
    ]
    r.vazoes = [0]
    assert r.vazoes == [0]


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
    assert r.uhe == 285
    r.uhe = 20
    assert r.uhe == 20
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
    assert r.uhe == 285
    r.uhe = 10
    assert r.uhe == 10
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
    assert r.uhe == 34
    r.uhe = 40
    assert r.uhe == 40
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
    assert r.uhe == 95
    r.uhe = 40
    assert r.uhe == 40
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
    assert r.uhe == 119
    r.uhe = 40
    assert r.uhe == 40
    assert r.posto == 300
    r.posto = 50
    assert r.posto == 50
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
    assert r.uhe == 117
    r.uhe = 40
    assert r.uhe == 40
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
    assert r.uhe == 124
    r.uhe = 40
    assert r.uhe == 40
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
    assert r.uhe == 117
    r.uhe = 40
    assert r.uhe == 40
    assert r.jusante == 108.0
    r.jusante = 50
    assert r.jusante == 50
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
    assert r.uhe == 118
    r.uhe = 40
    assert r.uhe == 40
    assert r.jusante == 119
    r.jusante = 50
    assert r.jusante == 50
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
    assert r.uhe == 172
    r.uhe = 40
    assert r.uhe == 40
    assert r.aproveitamento == 176
    r.aproveitamento = 50
    assert r.aproveitamento == 50
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
    assert r.uhe == 4
    r.uhe = 40
    assert r.uhe == 40
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
    assert r.uhe == 43
    r.uhe = 40
    assert r.uhe == 40
    assert r.posto == 43
    r.posto = 50
    assert r.posto == 50
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
    assert r.uhe == 103
    r.uhe = 40
    assert r.uhe == 40
    assert r.influi == 1
    r.influi = 0
    assert r.influi == 0
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
    assert r.uhe == 275
    r.uhe = 40
    assert r.uhe == 40
    assert r.conjunto == 2
    r.conjunto = 0
    assert r.conjunto == 0
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
    assert r.uhe == 275
    r.uhe = 40
    assert r.uhe == 40
    assert r.conjunto == 1
    r.conjunto = 0
    assert r.conjunto == 0
    assert r.maquinas == 2
    r.maquinas = 0
    assert r.maquinas == 0
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
    assert r.uhe == 275
    r.uhe = 40
    assert r.uhe == 40
    assert r.conjunto == 1
    r.conjunto = 0
    assert r.conjunto == 0
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
    assert r.codigo == 999
    r.codigo = 0
    assert r.codigo == 0
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
    assert r.ree == 1
    r.ree = 2
    assert r.ree == 2
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
    assert r.ree == 1
    r.ree = 2
    assert r.ree == 2
    assert r.numero_semanas == 5
    r.numero_semanas = 4
    assert r.numero_semanas == 4
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
    assert r.uhe == 156
    r.uhe = 2
    assert r.uhe == 2
    assert r.vazoes == [136, 168, 174, 152, 128]
    r.vazoes = [1, 2, 3]
    assert r.vazoes == [1, 2, 3]


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
    ]
    assert r.codigo == 107
    r.codigo = 0
    assert r.codigo == 0
    assert r.taxas == [-24.6, -24.6, -24.6, -24.6, -24.6, -24.6]


def test_registro_rq_dadger():

    m: MagicMock = mock_open(read_data="".join(MockRQ))
    r = RQ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [1, 100, 100, 100, 100, 100, 0, None, None]
    assert r.ree == 1
    r.ree = 0
    assert r.ree == 0
    assert r.vazoes == [100, 100, 100, 100, 100, 0]
    r.vazoes = [100, 100, 100]
    assert r.vazoes == [100, 100, 100]


def test_registro_ez_dadger():

    m: MagicMock = mock_open(read_data="".join(MockEZ))
    r = EZ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [251, 55.0]
    assert r.uhe == 251
    r.uhe = 200
    assert r.uhe == 200
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
    assert r.codigo == 3
    r.codigo = 0
    assert r.codigo == 0
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
    assert r.codigo == 101
    r.codigo = 0
    assert r.codigo == 0
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
    assert r.restricao == 117
    r.restricao = 0
    assert r.restricao == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.uhe == 43
    r.uhe = 10
    assert r.uhe == 10
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
    assert r.codigo == 5
    r.codigo = 0
    assert r.codigo == 0
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
    assert r.data == [10, 1, 300, 9999, 300, 9999, 300, 9999]
    assert r.codigo == 10
    r.codigo = 0
    assert r.codigo == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.limites_inferiores == [300, 300, 300]
    r.limites_inferiores = [0]
    assert r.limites_inferiores == [0, None, None]
    assert r.limites_superiores == [9999, 9999, 9999]
    r.limites_superiores = [0, 0, 0, 0]
    assert r.limites_superiores == [0, 0, 0, 0]


def test_registro_cq_dadger():

    m: MagicMock = mock_open(read_data="".join(MockCQ))
    r = CQ()
    with patch("builtins.open", m):
        with open("", "") as fp:
            r.read(fp)
    assert r.data == [11, 1, 27, 1, "QDEF"]
    assert r.restricao == 11
    r.restricao = 5
    assert r.restricao == 5
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.uhe == 27
    r.uhe = 10
    assert r.uhe == 10
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
    assert r.periodo == 1
    r.periodo = 2
    assert r.periodo == 2
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
    assert r.codigo == 1
    r.codigo = 0
    assert r.codigo == 0
    assert r.tipo_limite == 2
    r.tipo_limite = 0
    assert r.tipo_limite == 0
    assert r.limite == 60.0
    r.limite = 0
    assert r.limite == 0
    assert r.estagio == 1
    r.estagio = 0
    assert r.estagio == 0
    assert r.penalidade == 1710
    r.penalidade = 0
    assert r.penalidade == 0
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
    assert r.codigo == 1
    r.codigo = 0
    assert r.codigo == 0
    assert r.ree == 1
    r.ree = 0
    assert r.ree == 0
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


def test_campos_nao_encontrados_dadger():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        d = Dadger.le_arquivo("", "")
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


def test_campos_encontrados_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m):
        d = Dadger.le_arquivo("", "")
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
    assert d.fp(999, 1) is not None
    assert d.ve(1) is not None
    assert d.hv(101) is not None
    assert d.lv(101, 1) is not None
    assert d.hq(254) is not None
    assert d.lq(254, 1) is not None
    assert d.he(1, 1) is not None
    assert d.cm(1) is not None


def test_cria_lu_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m):
        d = Dadger.le_arquivo("", "")
        lu = d.lu(1, 2)
        assert lu is not None
        assert lu.limites_inferiores == d.lu(1, 1).limites_inferiores
        lu.limites_inferiores = [0.0]
        assert lu.limites_inferiores != d.lu(1, 1).limites_inferiores
        assert lu.limites_superiores == d.lu(1, 1).limites_superiores
        lu.limites_superiores = [0.0]
        assert lu.limites_superiores != d.lu(1, 1).limites_superiores


def test_cria_lv_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m):
        d = Dadger.le_arquivo("", "")
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
        d = Dadger.le_arquivo("", "")
        lq = d.lq(5, 2)
        assert lq is not None
        assert lq.limites_inferiores == d.lq(5, 1).limites_inferiores
        lq.limites_inferiores = [0.0]
        assert lq.limites_inferiores != d.lq(5, 1).limites_inferiores
        assert lq.limites_superiores == d.lq(5, 1).limites_superiores
        lq.limites_superiores = [0.0]
        assert lq.limites_superiores != d.lq(5, 1).limites_superiores


def test_eq_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m):
        d1 = Dadger.le_arquivo("")
        d2 = Dadger.le_arquivo("")
        assert d1 == d2


def test_neq_dadger():
    m: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m):
        d1 = Dadger.le_arquivo("")
        d2 = Dadger.le_arquivo("")
        d2.te.titulo = "Teste"
        assert d1 != d2


def test_leitura_escrita_dadger():
    m_leitura: MagicMock = mock_open(read_data="".join(MockDadger))
    with patch("builtins.open", m_leitura):
        d1 = Dadger.le_arquivo("")
    m_escrita: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m_escrita):
        d1.escreve_arquivo("", "")
        # Recupera o que foi escrito
        chamadas = m_escrita.mock_calls
        linhas_escritas = [
            chamadas[i].args[0] for i in range(2, len(chamadas) - 1)
        ]
    m_releitura: MagicMock = mock_open(read_data="".join(linhas_escritas))
    with patch("builtins.open", m_releitura):
        d2 = Dadger.le_arquivo("")
        assert d1 == d2
