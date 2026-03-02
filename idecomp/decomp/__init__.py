from typing import Any
import importlib

_LAZY_IMPORTS: dict[str, str] = {
    "Arquivos": ".arquivos",
    "AvlCortesFpha": ".avl_cortesfpha_dec",
    "AvlTurbMax": ".avl_turb_max",
    "Caso": ".caso",
    "Cortdeco": ".cortdeco",
    "Custos": ".custos",
    "Dadger": ".dadger",
    "Dadgnl": ".dadgnl",
    "DecAvlEvap": ".dec_avl_evap",
    "DecCortesEvap": ".dec_cortes_evap",
    "DecDesvFpha": ".dec_desvfpha",
    "DecEcoCotajus": ".dec_eco_cotajus",
    "DecEcoDiscr": ".dec_eco_discr",
    "DecEcoEvap": ".dec_eco_evap",
    "DecEcoQlat": ".dec_eco_qlat",
    "DecEstatEvap": ".dec_estatevap",
    "DecEstatFpha": ".dec_estatfpha",
    "DecFcfCortes": ".dec_fcf_cortes",
    "DecOperEvap": ".dec_oper_evap",
    "DecOperGnl": ".dec_oper_gnl",
    "DecOperInterc": ".dec_oper_interc",
    "DecOperRee": ".dec_oper_ree",
    "DecOperRheSoft": ".dec_oper_rhesoft",
    "DecOperSist": ".dec_oper_sist",
    "DecOperUsie": ".dec_oper_usie",
    "DecOperUsih": ".dec_oper_usih",
    "DecOperUsit": ".dec_oper_usit",
    "Decomptim": ".decomptim",
    "EcoFpha": ".eco_fpha",
    "Fcfnw": ".fcfnw",
    "Hidr": ".hidr",
    "InviabUnic": ".inviabunic",
    "Mapcut": ".mapcut",
    "OperDesvioFpha": ".oper_desvio_fpha",
    "OperDispUsihRee": ".oper_disp_usih_ree",
    "OperDispUsihSubm": ".oper_disp_usih_subm",
    "OperDispUsih": ".oper_disp_usih",
    "Postos": ".postos",
    "Relato": ".relato",
    "Relgnl": ".relgnl",
    "Vazoes": ".vazoes",
}

__all__ = sorted(_LAZY_IMPORTS.keys())


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        module = importlib.import_module(_LAZY_IMPORTS[name], __name__)
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return __all__
