# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperSist(TabelaCSV):
    """
    Bloco com a operação por submercados.
    """

    BEGIN_PATTERN = "-----;------;------;-----;--------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=6),
            IntegerField(size=6),
            IntegerField(size=5),
            FloatField(size=8, decimal_digits=2),
            IntegerField(size=4),
            LiteralField(size=15),
            FloatField(size=12, decimal_digits=1),
            FloatField(size=10, decimal_digits=1),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=12, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=1),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "periodo",
        "no",
        "cenario",
        "patamar",
        "duracao",
        "indiceSubmercado",
        "nomeSubmercado",
        "demandaMW",
        "geracaoPequenasUsinasMW",
        "geracaoTermicaMW",
        "geracaoTermicaAntecipadaMW",
        "geracaoHidroeletricaMW",
        "geracaoEolicaMW",
        "energiaBombeamentoMW",
        "energiaImportadaMW",
        "energiaExportadaMW",
        "intercambioLiquidoMW",
        "itaipu50MW",
        "itaipu60MW",
        "deficitMW",
        "enaMWmes",
        "earmInicialMWmes",
        "earmInicialPercentual",
        "earmFinalMWmes",
        "earmFinalPercentual",
        "cmo",
    ]
    END_PATTERN = ""
