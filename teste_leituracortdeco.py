from idecomp.decomp.mapcut import Mapcut
from idecomp.decomp.cortdeco import Cortdeco
import pandas as pd

dir = "deck_teste/teste-leitura-cortes/"

mapcut = Mapcut.read(dir + "mapcut.rv2")
tamanho_registro = mapcut.tamanho_corte
estagio = 1
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

print(tamanho_registro)
print(indice_ultimo_corte)
print(lag_maximo_tviagem)
print(numero_total_cortes)

cortdeco = Cortdeco.read(
    dir + "cortdeco.rv2",
    tamanho_registro,
    indice_ultimo_corte,
    numero_total_cortes,
    numero_patamares,
    numero_estagios,
    codigos_uhes,
    codigos_uhes_tviagem,
    codigos_submercados,
    lag_maximo_tviagem,
)

print(cortdeco.cortes)

# print(mapcut.dados_gnl)
# # # print(mapcut.codigos_submercados_gnl)

gnl_cols = [col for col in cortdeco.cortes.columns if "sbm" in col]
# print(cortdeco[gnl_cols])


qdefp_cols = [col for col in cortdeco.cortes.columns if "sbm" in col]
print(len(qdefp_cols))
df = cortdeco.cortes
df_melted = pd.melt(df, id_vars=["indice_corte"], value_vars=qdefp_cols)
print(df_melted)
df_melted["variable"].str.split("sbm", expand=True)
df_melted["codigo_submercado"] = (
    df_melted["variable"]
    .str.split("sbm", expand=True)[1]
    .str.split("_", expand=True)[0]
)
df_melted["lag"] = (
    df_melted["variable"]
    .str.split("pat", expand=True)[1]
    .str.split("_", expand=True)[0]
)

print(df_melted.head(25))
print(df_melted)
df_melted["codigo_usina"] = df_melted["variable"].str.split("_", expand=True)[
    0
]
df_melted["lag"] = df_melted["variable"].str.split("lag", expand=True)[1]
df_melted = df_melted.drop(["variable"], axis=1)
df_melted.rename(
    columns={
        "value": "valor",
    },
    inplace=True,
)
df_melted = df_melted[["indice_corte", "codigo_usina", "lag", "valor"]]
# print(df_melted["variable"].str.split("uhe", expand=True)[1])

# print(cortdeco.coeficientes_varm)
# print(cortdeco.coeficientes_qdefp)
print(cortdeco.coeficientes_volume_armazenado.dtypes)
print(cortdeco.coeficientes_defluencia_tempo_viagem.dtypes)
print(cortdeco.coeficientes_geracao_gnl.dtypes)
