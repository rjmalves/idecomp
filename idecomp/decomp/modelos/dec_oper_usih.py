# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperUsih(TabelaCSV):
    """
    Bloco com a operação por usina hidroelétrica.
    """

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
            LiteralField(size=15),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "periodo",
        "no",
        "cenario",
        "patamar",
        "duracao",
        "indiceUsina",
        "nomeUsina",
        "nomeSubmercado",
        "volumeUtilMaximoHm3",
        "volumeUtilInicialHm3",
        "volumeUtilInicialPercentual",
        "volumeUtilFinalHm3",
        "volumeUtilFinalPercentual",
        "geracaoMW",
        "potenciaInstaladaMW",
        "potenciaDisponivelMW",
        "vazaoNaturalM3S",
        "vazaoNaturalMLT",
        "vazaoIncrementalM3S",
        "vazaoMontanteM3S",
        "vazaoMontanteTVM3S",
        "vazaoAfluenteM3S",
        "vazaoDefluenteM3S",
        "vazaoTurbinadaM3S",
        "vazaoVertidaM3S",
        "vazaoDesviadaM3S",
        "vazaoRecebidaBombeamentoM3S",
        "vazaoRetiradaBombeamentoM3S",
        "vazaoRetiradaM3S",
        "vazaoRetornoM3S",
        "vazaoEvaporadaM3S",
    ]
    END_PATTERN = ""
