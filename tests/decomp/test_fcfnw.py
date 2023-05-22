# Rotinas de testes associadas ao arquivo fcfnwx.rvx do DECOMP
from idecomp.decomp.modelos.fcfnw import BlocoCortesFCF

from idecomp.decomp.fcfnw import Fcfnw

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.fcfnwn import MockBlocoFCFn, MockFcfnwn
from tests.mocks.arquivos.fcfnwi import MockBlocoFCFi, MockFcfnwi


def test_bloco_fcfnwn():
    m: MagicMock = mock_open(read_data="".join(MockBlocoFCFn))
    b = BlocoCortesFCF()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 27
    assert b.data.shape[1] == 23
    assert b.data.iloc[0, 0] == 1
    assert b.data.iloc[0, 1] == 620028557.5
    assert b.data.iloc[0, 2] == 1
    assert b.data.iloc[0, 3] == 0.0
    assert b.data.iloc[0, 4] == 0.0
    assert b.data.iloc[0, 5] == 0.0
    assert b.data.iloc[0, 6] == 0.0
    assert b.data.iloc[0, 7] == 0.0
    assert b.data.iloc[0, 8] == 0.0
    assert b.data.iloc[0, 9] == 0.0
    assert b.data.iloc[0, 10] == 0.0
    assert b.data.iloc[0, 11] == 0.0
    assert b.data.iloc[0, 12] == 0.0
    assert b.data.iloc[0, 13] == 0.0
    assert b.data.iloc[0, 14] == 0.0
    assert b.data.iloc[0, 15] == 0.0
    assert b.data.iloc[0, 16] == -118.17033
    assert b.data.iloc[0, 17] == -88.93798
    assert b.data.iloc[0, 18] == -117.4438
    assert b.data.iloc[0, 19] == -88.31033
    assert b.data.iloc[0, 20] == -112.95881
    assert b.data.iloc[0, 21] == -80.82157
    assert b.data.iloc[0, 22] == 0.0


def test_bloco_fcfnwi():
    m: MagicMock = mock_open(read_data="".join(MockBlocoFCFi))
    b = BlocoCortesFCF()
    with patch("builtins.open", m):
        with open("", "") as fp:
            b.read(fp)

    assert b.data.shape[0] == 462
    assert b.data.shape[1] == 16
    assert b.data.iloc[0, 0] == 1
    assert b.data.iloc[0, 1] == 620028557.5
    assert b.data.iloc[0, 2] == 4
    assert b.data.iloc[0, 3] == -1766.04097
    assert b.data.iloc[0, 4] == -2980.23111
    assert b.data.iloc[0, 5] == -499.07998
    assert b.data.iloc[0, 6] == -498.35024
    assert b.data.iloc[0, 7] == -497.2732
    assert b.data.iloc[0, 8] == -516.88109
    assert b.data.iloc[0, 9] == -450.78657
    assert b.data.iloc[0, 10] == -435.89905
    assert b.data.iloc[0, 11] == -409.23236
    assert b.data.iloc[0, 12] == -388.78735
    assert b.data.iloc[0, 13] == -312.55757
    assert b.data.iloc[0, 14] == -229.15331
    assert b.data.iloc[0, 15] == -138.34944
