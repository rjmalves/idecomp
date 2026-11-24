import math

from cfinterface.components.literalfield import LiteralField
from cfinterface.components.register import Register

from idecomp.decomp.dadger import Dadger
from idecomp.decomp.modelos.campos.fortranfloatfield import FortranFloatField
from idecomp.decomp.modelos.campos.fortranintegerfield import (
    FortranIntegerField,
)
from idecomp.decomp.modelos.dadger_manual import (
    CAMPOS,
    EXTENSOES,
    CampoManual,
    DiferencaLeitura,
    compara_linhas,
)

from tests.mocks.arquivos.dadger import MockCT, MockUH


def _leiaute_idecomp(classe: type[Register]) -> list[CampoManual]:
    campos = []
    for campo in classe.LINE.fields:
        inicio = campo.starting_position + 1
        fim = campo.starting_position + campo.size
        if isinstance(campo, LiteralField):
            campos.append(CampoManual("A", inicio, fim))
        elif isinstance(campo, FortranIntegerField):
            campos.append(CampoManual("I", inicio, fim))
        else:
            assert isinstance(campo, FortranFloatField)
            # Um "1" sem ponto no fim do campo é lido como 10 ** -d.
            decimais = round(-math.log10(campo.read("1".rjust(fim))))
            campos.append(CampoManual("F", inicio, fim, decimais))
    return sorted(campos, key=lambda c: c.coluna_inicial)


def _leiaute_manual(classe: type[Register]) -> list[CampoManual]:
    nome = classe.__name__
    campos = CAMPOS[nome] + EXTENSOES.get(nome, [])
    if nome.startswith("AC"):
        # O mnemônico do parâmetro faz parte do identificador do registro,
        # e a semana é escrita nas colunas 74-75, onde o manual tem I1 na
        # coluna 75.
        campos = [c for c in campos if c != CampoManual("A", 10, 15)]
        campos = [
            CampoManual("I", 74, 75) if c == CampoManual("I", 75, 75) else c
            for c in campos
        ]
    if nome == "IR":
        # O campo 5 tem COLUNAS 25-30 e FORMATO I5 no manual.
        campos = [
            CampoManual("I", 25, 29) if c == CampoManual("I", 25, 30) else c
            for c in campos
        ]
    return sorted(campos, key=lambda c: c.coluna_inicial)


def test_leiaute_dos_registros_dadger_segue_o_manual():
    # CX e VT não estão no manual.
    nomes = [c.__name__ for c in Dadger.REGISTERS]
    assert [n for n in nomes if n not in CAMPOS] == ["CX", "VT"]
    for classe in Dadger.REGISTERS:
        if classe.__name__ in CAMPOS:
            assert _leiaute_idecomp(classe) == _leiaute_manual(classe), (
                classe.__name__
            )


def test_campo_inteiro_le_como_o_fortran():
    campo = CampoManual("I", 5, 8)
    assert campo.le("RE  1 2 ") == 12
    assert campo.le("RE   401") == 401
    assert campo.le("RE      ") is None
    assert campo.le("RE") is None
    assert campo.le("RE  1-2 ") is None


def test_campo_real_le_com_decimais_implicitos():
    linha = " " * 39 + "      1550"
    assert CampoManual("F", 40, 49, 2).le(linha) == 15.5
    assert CampoManual("F", 40, 49).le(linha) == 1550.0
    assert CampoManual("F", 40, 49, 2).le(" " * 39 + "     15.50") == 15.5


def test_campo_de_texto_mantem_brancos_a_esquerda():
    campo = CampoManual("A", 5, 14)
    assert campo.le("CT    ANGRA 1   ") == "  ANGRA 1"
    assert campo.le("CT  ANGRA 1") == "ANGRA 1"
    assert campo.le("CT") == ""


def test_compara_linhas_iguais():
    assert compara_linhas(MockUH, MockUH) == []
    assert compara_linhas(MockCT, MockCT + "   ") == []


def test_compara_linhas_com_mesmo_valor_em_textos_diferentes():
    # "100.0" e "  100" são lidos como 100 em um campo F5.0.
    original = "PQ  SECO_PCH   1    1   100.0"
    modificada = "PQ  SECO_PCH   1    1     100"
    assert compara_linhas(original, modificada) == []


def test_compara_linhas_potefe_fora_das_colunas_do_manual():
    # A potência escrita nas colunas 25-35 é lida pelo DECOMP nas colunas
    # 25-34, sem o último dígito.
    original = "AC  288  POTEFE        1   611.111"
    modificada = "AC  288  POTEFE        1    611.111"
    assert compara_linhas(original, modificada) == [
        DiferencaLeitura(
            "ACPOTEFE", 25, 34, "   611.111", "    611.11", 611.111, 611.11
        ),
        DiferencaLeitura(
            "ACPOTEFE", 35, 69, " " * 35, "1" + " " * 34, None, None
        ),
    ]


def test_compara_linhas_com_numero_invalido():
    assert compara_linhas("RE  1-2", "RE  1-3") == [
        DiferencaLeitura("RE", 5, 8, "1-2 ", "1-3 ", None, None)
    ]
    assert compara_linhas("RE  1-2", "RE") == [
        DiferencaLeitura("RE", 5, 8, "1-2 ", "    ", None, None)
    ]


def test_compara_linhas_texto_com_brancos_a_esquerda():
    original = "PQ    SECO     1    1    2527"
    assert compara_linhas(original, "PQ    SECO     1    1    2527   ") == []
    assert compara_linhas(original, "PQ  SECO       1    1    2527") == [
        DiferencaLeitura(
            "PQ", 5, 14, "  SECO    ", "SECO      ", "  SECO", "SECO"
        )
    ]


def test_compara_linhas_de_comentario():
    assert compara_linhas("& UHE ANGRA", "& UHE ANGRA 1") == []
    assert compara_linhas("& UHE", "UH    1") == [
        DiferencaLeitura("& ", 1, 7, "& UHE", "UH    1", None, None)
    ]


def test_compara_linhas_de_registro_fora_do_manual():
    assert compara_linhas("CX     1    2", "CX     1    2  ") == []
    assert compara_linhas("CX     1    2", "CX  0001    2") == [
        DiferencaLeitura(
            "CX", 1, 13, "CX     1    2", "CX  0001    2", None, None
        )
    ]


def test_compara_linhas_de_registros_diferentes():
    assert compara_linhas("RE  449", "LU  449") == [
        DiferencaLeitura("RE", 1, 7, "RE  449", "LU  449", None, None)
    ]
