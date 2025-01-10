# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaEstatEvap(TabelaCSV):
    """
    Bloco com as estatísticas de desvios de modelagem da evaporação.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;----------;----------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=10),
            IntegerField(size=10),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=11, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "numero_usinas_evaporacao",
        "numero_usinas_total",
        "evaporacao_modelo_hm3",
        "evaporacao_calculada_hm3",
        "desvio_absoluto_positivo_hm3",
        "desvio_absoluto_negativo_hm3",
        "desvio_absoluto_hm3",
        "evaporacao_modelo_m3s",
        "evaporacao_calculada_m3s",
        "desvio_absoluto_positivo_m3s",
        "desvio_absoluto_negativo_m3s",
        "desvio_absoluto_m3s",
        "desvio_percentual",
    ]
    END_PATTERN = ""
