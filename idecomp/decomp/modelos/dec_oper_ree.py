# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperReev31(TabelaCSV):
    """
    Bloco com a operação por REE.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;------;-----;--------------;----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=6),
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=4),
            LiteralField(size=15),
            FloatField(size=10, decimal_digits=1),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=16, decimal_digits=1),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "cenario",
        "codigo_ree",
        "nome_ree",
        "codigo_submercado",
        "nome_submercado",
        "ena_MWmes",
        "earm_inicial_MWmes",
        "earm_inicial_percentual",
        "earm_final_MWmes",
        "earm_final_percentual",
        "earm_maximo_MWmes",
    ]
    END_PATTERN = ""


class TabelaOperRee(TabelaCSV):
    """
    Bloco com a operação por REE.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;------;------;-----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=6),
            IntegerField(size=6),
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=4),
            LiteralField(size=15),
            FloatField(size=10, decimal_digits=1),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=16, decimal_digits=1),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "no",
        "cenario",
        "codigo_ree",
        "nome_ree",
        "codigo_submercado",
        "nome_submercado",
        "ena_MWmes",
        "earm_inicial_MWmes",
        "earm_inicial_percentual",
        "earm_final_MWmes",
        "earm_final_percentual",
        "earm_maximo_MWmes",
    ]
    END_PATTERN = ""
