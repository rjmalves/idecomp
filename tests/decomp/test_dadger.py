from idecomp.decomp.modelos.dadger import (
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

    assert r.data == [1, 10, 25.29, 1]
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
    assert r.inflexibilidades == [999.0, None, None]
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
    assert r.cargas == [0, None, None]
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
    assert r.limites_superiores == [0, None, None]
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

    assert r.data == [200]
    assert r.iteracoes == 200
    r.iteracoes = 0
    assert r.iteracoes == 0


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
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    r.volumes = [0]
    assert r.volumes == [
        0,
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
