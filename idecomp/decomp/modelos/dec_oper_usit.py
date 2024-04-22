# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperUsitv31(TabelaCSV):
    """
    Bloco com a operação por usina termoelétrica.
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
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
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
        "custo_incremental",
        "geracao_minima_MW",
        "geracao_MW",
        "fator_manutencao",
        "geracao_maxima_MW",
        "custo_geracao",
    ]
    END_PATTERN = ""


class TabelaOperUsit(TabelaCSV):
    """
    Bloco com a operação por usina termoelétrica.
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
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=14, decimal_digits=2),
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
        "custo_incremental",
        "geracao_minima_MW",
        "geracao_MW",
        "fator_manutencao",
        "geracao_maxima_MW",
        "custo_geracao",
    ]
    END_PATTERN = ""
