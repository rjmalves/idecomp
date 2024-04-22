# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperIntercv31(TabelaCSV):
    """
    Bloco com a operação das usinas térmicas de despacho antecipado.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;------;-----;---------;----------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=6),
            IntegerField(size=5),
            IntegerField(size=9),
            LiteralField(size=16),
            IntegerField(size=9),
            LiteralField(size=16),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=10, decimal_digits=4),
            FloatField(size=12, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "cenario",
        "patamar",
        "codigo_submercado_de",
        "nome_submercado_de",
        "codigo_submercado_para",
        "nome_submercado_para",
        "intercambio_origem_MW",
        "intercambio_destino_MW",
        "perdas_MW",
        "fator_perdas",
        "capacidade_MW",
    ]
    END_PATTERN = ""


class TabelaOperInterc(TabelaCSV):
    """
    Bloco com a operação das usinas térmicas de despacho antecipado.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;------;------;-----;---------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=6),
            IntegerField(size=6),
            IntegerField(size=5),
            IntegerField(size=9),
            LiteralField(size=16),
            IntegerField(size=9),
            LiteralField(size=16),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=10, decimal_digits=4),
            FloatField(size=12, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "no",
        "cenario",
        "patamar",
        "codigo_submercado_de",
        "nome_submercado_de",
        "codigo_submercado_para",
        "nome_submercado_para",
        "intercambio_origem_MW",
        "intercambio_destino_MW",
        "perdas_MW",
        "fator_perdas",
        "capacidade_MW",
    ]
    END_PATTERN = ""
