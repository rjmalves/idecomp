def formata_numero(num: float,
                   casas: int,
                   digitos: int) -> str:
    s = f"{round(num, casas)}"
    if len(s) > 5:
        s = s.rstrip("0")
    return s.rjust(digitos)
