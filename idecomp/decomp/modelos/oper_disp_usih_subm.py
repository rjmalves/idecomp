# Imports de módulos externos
from cfinterface.components.floatfield import FloatField
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField

from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSVLibs


class TabelaOperDispUsihSubm(TabelaCSVLibs):
    """
    Bloco com a disponibilidade das usinas hidrelétricas por submercado.
    """

    __slots__ = []

    BEGIN_PATTERN = "&IIIIIII;IIIIIII;IIIIII;IIIIIIII;SSSSSSSSSSSSSSSSSSSS;"
    LINE_MODEL = Line(
        [
            IntegerField(size=8),
            IntegerField(size=7),
            IntegerField(size=6),
            IntegerField(size=8),
            LiteralField(size=20),
            FloatField(size=15, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "cenario",
        "patamar",
        "codigo_submercado",
        "nome_submercado",
        "geracao_hidraulica_maxima_pl",
    ]
    END_PATTERN = ""
