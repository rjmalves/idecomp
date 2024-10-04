# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSVLibs


class TabelaOperDesvioFpha(TabelaCSVLibs):
    """
    Bloco com os desvios da função de produção hidráulica.
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
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=12),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
            FloatField(size=75, decimal_digits=2),
            FloatField(size=15, decimal_digits=2),
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
        "vazao_turbinada_m3s",
        "vazao_vertida_m3s",
        "volume_inicial_hm3",
        "volume_final_hm3",
        "volume_medio_hm3",
        "altura_montante",
        "vazao_lateral_usina_m3s",
        "vazao_lateral_posto_m3s",
        "vazao_jusante_m3s",
        "altura_jusante",
        "altura_liquida",
        "perdas_hidraulicas",
        "produtibilidade_especifica",
        "geracao_hidraulica_pl",
        "geracao_hidraulica_fpha",
        "geracao_hidraulica_fph",
        "desvio_absoluto_pl_fph",
        "desvio_percentual_pl_fph",
        "desvio_absoluto_pl_fpha",
        "desvio_percentual_pl_fpha",
    ]
    END_PATTERN = ""
