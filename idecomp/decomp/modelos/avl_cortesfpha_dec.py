# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaCortesFpha(TabelaCSV):
    """
    Bloco com as informações dos cortes da função de produção hidráulica.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;-----;--------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=7),
            FloatField(size=10, decimal_digits=6),
            FloatField(size=16, decimal_digits=8),
            FloatField(size=16, decimal_digits=8),
            FloatField(size=16, decimal_digits=8),
            FloatField(size=16, decimal_digits=8),
            FloatField(size=16, decimal_digits=8),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "codigo_usina",
        "estagio",
        "nome_usina",
        "segmento_fpha",
        "fator_correcao",
        "rhs",
        "coeficiente_volume_util",
        "coeficiente_vazao_turbinada",
        "coeficiente_vazao_vertida",
        "coeficiente_vazao_lateral",
    ]
    END_PATTERN = ""
