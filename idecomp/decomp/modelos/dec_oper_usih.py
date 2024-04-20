# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperUsihv31(TabelaCSV):
    """
    Bloco com a operação por usina hidroelétrica.
    """

    __slots__ = []

    BEGIN_PATTERN = "-----;------;-----;--------;-----;--------------;"

    LINE_MODEL = Line(
        [
            IntegerField(size=5),
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
        "nome_submercado",
        "volume_util_maximo_hm3",
        "volume_util_inicial_hm3",
        "volume_util_inicial_percentual",
        "volume_util_final_hm3",
        "volume_util_final_percentual",
        "geracao_MW",
        "potencia_instalada_MW",
        "potencia_disponivel_MW",
        "vazao_natural_m3s",
        "vazao_natural_mlt",
        "vazao_incremental_m3s",
        "vazao_montante_m3s",
        "vazao_montante_tv_m3s",
        "vazao_defluente_m3s",
        "vazao_turbinada_m3s",
        "vazao_vertida_m3s",
        "vazao_desviada_m3s",
        "vazao_recebida_bombeamento_m3s",
        "vazao_retirada_bombeamento_m3s",
        "vazao_retirada_m3s",
        "vazao_retorno_m3s",
        "vazao_evaporada_m3s",
    ]
    END_PATTERN = ""


class TabelaOperUsih(TabelaCSV):
    """
    Bloco com a operação por usina hidroelétrica.
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
        "estagio",
        "no",
        "cenario",
        "patamar",
        "duracao",
        "codigo_usina",
        "nome_usina",
        "nome_submercado",
        "volume_util_maximo_hm3",
        "volume_util_inicial_hm3",
        "volume_util_inicial_percentual",
        "volume_util_final_hm3",
        "volume_util_final_percentual",
        "geracao_MW",
        "potencia_instalada_MW",
        "potencia_disponivel_MW",
        "vazao_natural_m3s",
        "vazao_natural_mlt",
        "vazao_incremental_m3s",
        "vazao_montante_m3s",
        "vazao_montante_tv_m3s",
        "vazao_afluente_m3s",
        "vazao_defluente_m3s",
        "vazao_turbinada_m3s",
        "vazao_vertida_m3s",
        "vazao_desviada_m3s",
        "vazao_recebida_bombeamento_m3s",
        "vazao_retirada_bombeamento_m3s",
        "vazao_retirada_m3s",
        "vazao_retorno_m3s",
        "vazao_evaporada_m3s",
    ]
    END_PATTERN = ""
