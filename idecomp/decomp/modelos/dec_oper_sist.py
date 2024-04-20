# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperSistv31(TabelaCSV):
    """
    Bloco com a operação por submercados.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;------;-----;--------;----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
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
        "estagio",
        "cenario",
        "patamar",
        "duracao",
        "codigo_submercado",
        "nome_submercado",
        "demanda_MW",
        "geracao_pequenas_usinas_MW",
        "geracao_termica_MW",
        "geracao_termica_antecipada_MW",
        "geracao_hidroeletrica_MW",
        "energia_bombeamento_MW",
        "energia_importada_MW",
        "energia_exportada_MW",
        "intercambio_liquido_MW",
        "itaipu_50MW",
        "itaipu_60MW",
        "deficit_MW",
        "ena_MWmes",
        "earm_inicial_MWmes",
        "earm_inicial_percentual",
        "earm_final_MWmes",
        "earm_final_percentual",
        "cmo",
    ]
    END_PATTERN = ""


class TabelaOperSist(TabelaCSV):
    """
    Bloco com a operação por submercados.
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
        "estagio",
        "no",
        "cenario",
        "patamar",
        "duracao",
        "codigo_submercado",
        "nome_submercado",
        "demanda_MW",
        "geracao_pequenas_usinas_MW",
        "geracao_termica_MW",
        "geracao_termica_antecipada_MW",
        "geracao_hidroeletrica_MW",
        "geracao_eolica_MW",
        "energia_bombeamento_MW",
        "energia_importada_MW",
        "energia_exportada_MW",
        "intercambio_liquido_MW",
        "itaipu_50MW",
        "itaipu_60MW",
        "deficit_MW",
        "ena_MWmes",
        "earm_inicial_MWmes",
        "earm_inicial_percentual",
        "earm_final_MWmes",
        "earm_final_percentual",
        "cmo",
    ]
    END_PATTERN = ""
