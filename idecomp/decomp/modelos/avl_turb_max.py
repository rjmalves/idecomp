# Imports de módulos externos
from cfinterface.components.floatfield import FloatField
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField

from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaAvlTurbMax(TabelaCSV):
    """
    Bloco com avaliação do turbinamento máximo das usinas hidrelétricas.
    """

    __slots__ = []

    BEGIN_PATTERN = "------------;------------;------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=12),
            LiteralField(size=12),
            IntegerField(size=12),
            LiteralField(size=14),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "observacao",
        "codigo_usina",
        "nome_usina",
        "volume_util_inicial_hm3",
        "volume_util_final_hm3",
        "vazao_turbinada_m3s",
        "vazao_turbinada_maxima_pl_m3s",
        "engolimento_maximo_priori_m3s",
        "engolimento_maximo_posteriori_m3s",
        "vazao_turbinada_maxima_gerador_m3s",
        "altura_queda",
        "altura_efetiva",
        "altura_montante",
        "altura_jusante",
        "violacao_turbinamento_m3s",
    ]
    END_PATTERN = ""
