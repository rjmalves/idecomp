# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaEcoQlat(TabelaCSV):
    """
    Bloco com as informações de eco dos dados para cálculo
    da vazão de jusante das usinas hidrelétricas.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;-----;--------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            LiteralField(size=14),
            FloatField(size=9, decimal_digits=3),
            LiteralField(size=9),
            IntegerField(size=9),
            FloatField(size=9, decimal_digits=3),
            FloatField(size=9, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "codigo_usina",
        "nome_usina",
        "fator_participacao_usina",
        "tipo_entidade_jusante",
        "codigo_entidade_jusante",
        "fator_participacao_entidade",
        "vazao_incremental_media_m3s",
    ]
    END_PATTERN = ""
