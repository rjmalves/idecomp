# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaEcoDiscr(TabelaCSV):
    """
    Bloco com a discretização temporal dos estágios e patamares.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;-----;--------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            FloatField(size=8, decimal_digits=2),
            IntegerField(size=4),
            IntegerField(size=5),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "patamar",
        "duracao",
        "numero_patamares",
        "numero_aberturas",
    ]
    END_PATTERN = ""
