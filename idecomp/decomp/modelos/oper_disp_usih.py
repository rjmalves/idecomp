# Imports de módulos externos
from cfinterface.components.floatfield import FloatField
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField

from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSVLibs


class TabelaOperDispUsih(TabelaCSVLibs):
    """
    Bloco com a disponibilidade das usinas hidrelétricas.
    """

    __slots__ = []

    BEGIN_PATTERN = "&IIIIIII;IIIIIII;IIIIII;IIIIIII;SSSSSSSSSSSSSSSSSSSS"
    LINE_MODEL = Line(
        [
            IntegerField(size=8),
            IntegerField(size=7),
            IntegerField(size=6),
            IntegerField(size=7),
            LiteralField(size=20),
            IntegerField(size=8),
            LiteralField(size=20),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "cenario",
        "patamar",
        "codigo_usina",
        "nome_usina",
        "codigo_submercado",
        "nome_submercado",
        "volume_inicial_hm3",
        "volume_final_hm3",
        "vazao_vertida_m3s",
        "vazao_turbinada_m3s",
        "vazao_turbinada_maxima_m3s",
        "geracao_hidraulica",
        "geracao_hidraulica_maxima",
        "geracao_hidraulica_maxima_pl",
    ]
    END_PATTERN = ""
