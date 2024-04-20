# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperGnlv31(TabelaCSV):
    """
    Bloco com a operação das usinas térmicas de despacho antecipado.
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
            IntegerField(size=5),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
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
        "lag",
        "custo_incremental",
        "beneficio_gnl",
        "geracao_minima_MW",
        "geracao_comandada_MW",
        "geracao_sinalizada_MW",
        "geracao_MW",
        "geracao_maxima_MW",
        "fator_manutencao",
        "custo_geracao",
    ]
    END_PATTERN = ""


class TabelaOperGnl(TabelaCSV):
    """
    Bloco com a operação das usinas térmicas de despacho antecipado.
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
            IntegerField(size=5),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
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
        "lag",
        "custo_incremental",
        "beneficio_gnl",
        "geracao_minima_MW",
        "geracao_comandada_MW",
        "geracao_sinalizada_MW",
        "geracao_MW",
        "geracao_maxima_MW",
        "fator_manutencao",
        "custo_geracao",
    ]
    END_PATTERN = ""
