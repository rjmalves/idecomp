# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaEcoEvap(TabelaCSV):
    """
    Bloco com as informações de eco dos dados
    para a evaporação das usinas hidrelétricas.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;-----;--------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            LiteralField(size=14),
            LiteralField(size=15),
            IntegerField(size=5),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            IntegerField(size=8),
            IntegerField(size=11),
            IntegerField(size=12),
            IntegerField(size=15),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "codigo_usina",
        "nome_usina",
        "nome_submercado",
        "codigo_ree",
        "volume_referencia_hm3",
        "evaporacao_referencia_hm3",
        "coeficiente_evaporacao_mensal",
        "considera_evaporacao",
        "considera_evaporacao_linear",
        "flag_tipo_volume_referencia",
    ]
    END_PATTERN = ""
