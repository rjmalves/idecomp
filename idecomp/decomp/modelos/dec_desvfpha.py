# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaDesvFpha(TabelaCSV):
    """
    Bloco com os desvios da função de produção hidráulica.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;-----;------;-----;--------------;----------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            IntegerField(size=6),
            IntegerField(size=5),
            LiteralField(size=14),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=9, decimal_digits=2),
            FloatField(size=12, decimal_digits=8),
            FloatField(size=12, decimal_digits=6),
            IntegerField(size=4),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            IntegerField(size=6),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "codigo_usina",
        "estagio",
        "no",
        "patamar",
        "nome_usina",
        "volume_total_hm3",
        "volume_util_percentual",
        "vazao_turbinada_m3s",
        "vazao_vertida_m3s",
        "vazao_jusante_m3s",
        "vazao_lateral_usina_m3s",
        "vazao_lateral_posto_m3s",
        "altura_jusante",
        "altura_montante",
        "produtibilidade_especifica",
        "perdas_hidraulicas",
        "afogamento",
        "geracao_hidraulica_fph",
        "geracao_hidraulica_fpha",
        "desvio_absoluto_MW",
        "desvio_percentual",
        "influencia_vertimento_canal_fuga",
    ]
    END_PATTERN = ""
