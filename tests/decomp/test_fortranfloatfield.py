import pytest

from idecomp.decomp.modelos.campos.fortranfloatfield import FortranFloatField


def _le(texto: str, implied_decimals: int) -> float | None:
    campo = FortranFloatField(
        len(texto), 0, 2, implied_decimals=implied_decimals
    )
    return campo.read(texto)


def _escreve(
    valor: float | None, size: int, decimal_digits: int, implied_decimals: int
) -> str:
    campo = FortranFloatField(
        size, 0, decimal_digits, implied_decimals=implied_decimals, value=valor
    )
    return campo.write("")


def test_leitura_sem_ponto_usa_decimais_implicitos():
    # Em F10.2, "299" é lido pelo DECOMP como 2.99.
    for texto, valor in [
        ("       299", 2.99),
        ("      -299", -2.99),
        ("      +299", 2.99),
        ("      29 9", 2.99),
        ("   2 9  9 ", 2.99),
        ("         0", 0.0),
        ("    159300", 1593.0),
    ]:
        assert _le(texto, 2) == valor, texto


def test_leitura_com_ponto_le_como_escrito():
    for texto, valor in [
        ("    296.52", 296.52),
        ("      299.", 299.0),
        ("     1593.", 1593.0),
        ("      -.25", -0.25),
        ("     -2.99", -2.99),
    ]:
        assert _le(texto, 2) == valor, texto


def test_leitura_expoente_sem_ponto_usa_decimais_implicitos():
    for texto, valor in [
        ("     299E1", 29.9),
        ("     299e1", 29.9),
        ("     299D1", 29.9),
        ("     299d1", 29.9),
        ("    299E+1", 29.9),
        ("     299+1", 29.9),
        ("    299E-1", 0.299),
        ("     299-1", 0.299),
    ]:
        assert _le(texto, 2) == valor, texto


def test_leitura_expoente_com_ponto_le_como_escrito():
    for texto, valor in [
        ("    2.99E1", 29.9),
        ("     1.E-7", 1e-7),
        ("    1.0D-3", 1e-3),
        ("     1.0-3", 1e-3),
        ("  3.211416D+06", 3211416.0),
    ]:
        assert _le(texto, 2) == valor, texto


def test_leitura_tolerancia_f17_15():
    assert _le("                1", 15) == 1e-15
    assert _le("            1.E-7", 15) == 1e-7
    assert _le("0.000000000010000", 15) == 1e-11


def test_leitura_sem_decimais_implicitos_le_como_escrito():
    assert _le("       299", 0) == 299.0
    assert _le("     299E1", 0) == 2990.0


def test_leitura_campo_vazio_ou_invalido_retorna_none():
    for texto in [
        "          ",
        "         -",
        "         .",
        "       abc",
        "    1.2.3",
    ]:
        assert _le(texto, 2) is None, texto


def test_escrita_sempre_tem_ponto_decimal():
    assert _escreve(2.99, 10, 2, 2) == "      2.99"
    assert _escreve(299.0, 10, 2, 2) == "    299.00"
    assert _escreve(1e-15, 17, 15, 15) == "0.000000000000001"


def test_escrita_com_precisao_reduzida_mantem_ponto_decimal():
    # "123456789.00" não cabe em 10 colunas e a precisão cai para zero.
    escrito = _escreve(123456789.0, 10, 2, 2)
    assert escrito == "123456789."
    assert _le(escrito, 2) == 123456789.0


def test_escrita_sem_espaco_para_o_ponto_falha():
    with pytest.raises(ValueError, match="ponto decimal"):
        _escreve(1234567890.0, 10, 2, 2)


def test_escrita_sem_decimais_implicitos_nao_altera_o_campo():
    assert _escreve(123456789.0, 10, 2, 0) == " 123456789"


def test_escrita_de_valor_nulo_fica_em_branco():
    assert _escreve(None, 10, 2, 2) == " " * 10


def test_escrita_e_releitura_preservam_o_valor():
    for valor in [2.99, -2.99, 0.0, 296.52, 1593.0, 99999.99, 12345678.9]:
        escrito = _escreve(valor, 10, 2, 2)
        assert "." in escrito, valor
        assert _le(escrito, 2) == valor, valor
