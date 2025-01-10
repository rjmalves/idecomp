# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperRheSoft(TabelaCSV):
    """
    Bloco com os resultados de atendimento das restrições de energia
    armazenada mínima (RHE) modeladas com tratamento soft.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;------;------;------;"

    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=6),
            IntegerField(size=6),
            IntegerField(size=6),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=14, decimal_digits=6),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "no",
        "cenario",
        "codigo_restricao",
        "limite_MW",
        "valor_MW",
        "violacao_absoluta_MW",
        "violacao_percentual",
    ]
    END_PATTERN = ""


class TabelaOperRheSoftv31(TabelaCSV):
    """
    Bloco com os resultados de atendimento das restrições de energia
    armazenada mínima (RHE) modeladas com tratamento soft.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;------;------;"

    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=6),
            IntegerField(size=6),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
            FloatField(size=14, decimal_digits=6),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "cenario",
        "codigo_restricao",
        "limite_MW",
        "valor_MW",
        "violacao_absoluta_MW",
        "violacao_percentual",
    ]
    END_PATTERN = ""
