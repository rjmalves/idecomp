from idecomp.decomp.mapcut import Mapcut
from idecomp.decomp.cortdeco import Cortdeco
import pandas as pd
import numpy as np

dir = "deck_teste/teste-leitura-cortes/"

mapcut = Mapcut.read(dir + "mapcut.rv2")
tamanho_registro = mapcut.tamanho_corte
estagio = 1
registro_ultimo_corte_no = mapcut.registro_ultimo_corte_no
indice_ultimo_corte = mapcut.registro_ultimo_corte_no.loc[
    mapcut.registro_ultimo_corte_no["estagio"] == estagio,
    "indice_ultimo_corte",
].iloc[0]
numero_total_cortes = mapcut.numero_iteracoes
numero_patamares = mapcut.patamares_por_estagio[estagio - 1]
numero_estagios = mapcut.numero_estagios
codigos_uhes = mapcut.codigos_uhes
codigos_uhes_tviagem = mapcut.codigos_uhes_tempo_viagem
codigos_submercados = mapcut.codigos_submercados_gnl
lag_maximo_tviagem = mapcut.maximo_lag_tempo_viagem
# print(registro_ultimo_corte_no)
# print(numero_total_cortes)
# print(numero_estagios)

# incremento_offset = registro_ultimo_corte_no.loc[
#     registro_ultimo_corte_no["estagio"]
#     != max(registro_ultimo_corte_no["estagio"])
# ].shape[0]
# print(incremento_offset)

# print("LEITURA 1")
cortdeco = Cortdeco.read(
    dir + "cortdeco.rv2",
    tamanho_registro,
    registro_ultimo_corte_no,
    numero_total_cortes,
    numero_patamares,
    numero_estagios,
    codigos_uhes,
    codigos_uhes_tviagem,
    codigos_submercados,
    lag_maximo_tviagem,
)
print(cortdeco)
print(cortdeco.cortes)
df1 = cortdeco.cortes
# print(cortdeco.cortes.loc[0, :])
# print(cortdeco.cortes.loc[0, "rhs"])
print("=--------- altera DF")
cortdeco.cortes.loc[0, "rhs"] = 100
# print(cortdeco.cortes.loc[0, "rhs"])
# print(cortdeco.cortes.loc[0, :])
print(cortdeco.cortes)
print("=--------- escrita")
cortdeco.write("cortdeco_teste.rv2", registro_ultimo_corte_no)

offset = 53952 + 4
tamanho = 10

with open("cortdeco_teste.rv2", "rb") as f:
    f.seek(offset)
    aaa = np.frombuffer(f.read(tamanho * 8), dtype=np.float64, count=tamanho)
    print(aaa)

# print("=--------- leitura 2")
# cortdeco2 = Cortdeco.read(
#     "cortdeco_teste.rv2",
#     tamanho_registro,
#     registro_ultimo_corte_no,
#     numero_total_cortes,
#     numero_patamares,
#     numero_estagios,
#     codigos_uhes,
#     codigos_uhes_tviagem,
#     codigos_submercados,
#     lag_maximo_tviagem,
# )
# print(cortdeco2.cortes)

# df1 = cortdeco.cortes
# df2 = cortdeco2.cortes
# print("compara df", df1.equals(df2))

# # # print(cortdeco == cortdeco2)
