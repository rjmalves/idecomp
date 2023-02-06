# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperInterc(TabelaCSV):
    """
    Bloco com a operação das usinas térmicas de despacho antecipado.
    """

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
        "periodo",
        "no",
        "cenario",
        "patamar",
        "indiceSubmercadoDe",
        "nomeSubmercadoDe",
        "indiceSubmercadoPara",
        "nomeSubmercadoPara",
        "intercambioOrigemMW",
        "intercambioDestinoMW",
        "perdasMW",
        "fatorPerdas",
        "capacidadeMW",
    ]
    END_PATTERN = ""