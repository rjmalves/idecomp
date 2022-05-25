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
