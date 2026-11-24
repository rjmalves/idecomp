import pytest

from idecomp.decomp.modelos.campos.fortranintegerfield import (
    FortranIntegerField,
)


def _le(texto: str) -> int | None:
    campo = FortranIntegerField(len(texto), 0)
    return campo.read(texto)


def _escreve(
    valor: int | None, size: int, preferred_size: int | None = None
) -> str:
    campo = FortranIntegerField(
        size, 0, value=valor, preferred_size=preferred_size
    )
    return campo.write("")


def test_leitura_ignora_brancos():
    for texto, valor in [
        ("  12", 12),
        ("1 2 ", 12),
        ("401 ", 401),
        ("1001", 1001),
        (" -12", -12),
        ("+  5", 5),
    ]:
        assert _le(texto) == valor, texto


def test_leitura_campo_vazio_ou_invalido_retorna_none():
    for texto in ["    ", "  - ", "1-2 ", " 1.5"]:
        assert _le(texto) is None, texto


def test_escrita_alinhada_a_direita():
    assert _escreve(12, 4) == "  12"
    assert _escreve(1001, 4) == "1001"


def test_escrita_alinhada_nas_colunas_preferidas():
    assert _escreve(401, 4, 3) == "401 "
    assert _escreve(99, 4, 3) == " 99 "
    assert _escreve(1001, 4, 3) == "1001"


def test_escrita_de_valor_nulo_fica_em_branco():
    assert _escreve(None, 4, 3) == "    "


def test_escrita_que_nao_cabe_no_campo_falha():
    with pytest.raises(ValueError, match="não cabe"):
        _escreve(12345, 4)
