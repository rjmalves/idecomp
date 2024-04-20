# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaEcoCotajus(TabelaCSV):
    """
    Bloco com o eco dos polinômios por partes das curvas de jusante.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;--------------;---------;------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=9),
            FloatField(size=12, decimal_digits=2),
            IntegerField(size=9),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=37, decimal_digits=25),
            FloatField(size=37, decimal_digits=25),
            FloatField(size=37, decimal_digits=25),
            FloatField(size=37, decimal_digits=25),
            FloatField(size=37, decimal_digits=25),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "codigo_usina",
        "nome_usina",
        "indice_curva_jusante",
        "altura_referencia_usina_jusante",
        "indice_polinomio",
        "vazao_minima",
        "vazao_maxima",
        "a0",
        "a1",
        "a2",
        "a3",
        "a4",
    ]
    END_PATTERN = ""
