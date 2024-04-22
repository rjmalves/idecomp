# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaFcfCortes(TabelaCSV):
    """
    Bloco com as informações dos cortes da FCF gerada para determinado nó.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;--------;------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            LiteralField(size=8),
            IntegerField(size=6),
            LiteralField(size=15),
            LiteralField(size=7),
            IntegerField(size=5),
            IntegerField(size=5),
            FloatField(size=34, decimal_digits=7),
            LiteralField(size=16),
            FloatField(size=34, decimal_digits=7),
            LiteralField(size=16),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "indice_iteracao",
        "tipo_entidade",
        "indice_entidade",
        "nome_entidade",
        "tipo_coeficiente",
        "indice_lag",
        "indice_patamar",
        "valor_coeficiente",
        "unidade_coeficiente",
        "ponto_consultado",
        "unidade_ponto_consultado",
    ]
    END_PATTERN = ""
