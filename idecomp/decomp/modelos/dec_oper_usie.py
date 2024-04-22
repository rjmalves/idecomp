# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperUsiev31(TabelaCSV):
    """
    Bloco com a operação por estação elevatória.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;------;-----;--------;-----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=6),
            IntegerField(size=5),
            FloatField(size=8, decimal_digits=2),
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=4),
            LiteralField(size=15),
            IntegerField(size=7),
            IntegerField(size=7),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "cenario",
        "patamar",
        "duracao",
        "codigo_usina",
        "nome_usina",
        "codigo_submercado",
        "nome_submercado",
        "codigo_usina_jusante",
        "codigo_usina_montante",
        "vazao_bombeada_m3s",
        "energia_bombeamento_MW",
        "vazao_bombeada_minima_m3s",
        "vazao_bombeada_maxima_m3s",
    ]
    END_PATTERN = ""


class TabelaOperUsie(TabelaCSV):
    """
    Bloco com a operação por estação elevatória.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;------;------;-----;--------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=6),
            IntegerField(size=6),
            IntegerField(size=5),
            FloatField(size=8, decimal_digits=2),
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=4),
            LiteralField(size=15),
            IntegerField(size=7),
            IntegerField(size=7),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "estagio",
        "no",
        "cenario",
        "patamar",
        "duracao",
        "codigo_usina",
        "nome_usina",
        "codigo_submercado",
        "nome_submercado",
        "codigo_usina_jusante",
        "codigo_usina_montante",
        "vazao_bombeada_m3s",
        "energia_bombeamento_MW",
        "vazao_bombeada_minima_m3s",
        "vazao_bombeada_maxima_m3s",
    ]
    END_PATTERN = ""
