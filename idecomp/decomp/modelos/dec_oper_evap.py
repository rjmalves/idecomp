# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperEvapv31(TabelaCSV):
    """
    Bloco com as informações de operação da
    evaporação das usinas hidrelétricas.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;------;-----;--------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=6),
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=4),
            IntegerField(size=5),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=11, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "cenario",
        "codigo_usina",
        "nome_usina",
        "codigo_submercado",
        "codigo_ree",
        "volume_util_inicial_hm3",
        "volume_util_inicial_percentual",
        "volume_util_final_hm3",
        "volume_util_final_percentual",
        "evaporacao_modelo_hm3",
        "evaporacao_calculada_hm3",
        "desvio_absoluto_hm3",
        "desvio_percentual",
    ]
    END_PATTERN = ""


class TabelaOperEvap(TabelaCSV):
    """
    Bloco com as informações de operação da
    evaporação das usinas hidrelétricas.
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
            IntegerField(size=5),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=12, decimal_digits=3),
            FloatField(size=11, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "no",
        "cenario",
        "codigo_usina",
        "nome_usina",
        "codigo_submercado",
        "codigo_ree",
        "volume_util_inicial_hm3",
        "volume_util_inicial_percentual",
        "volume_util_final_hm3",
        "volume_util_final_percentual",
        "evaporacao_modelo_hm3",
        "evaporacao_calculada_hm3",
        "desvio_absoluto_hm3",
        "desvio_percentual",
    ]
    END_PATTERN = ""
