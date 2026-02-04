"""
========================================
Visualização de dados no dadger.rv0
========================================
"""

# %%
# O primeiro passo para realizar o processamento do arquivo, assim como os
# demais arquivos de saída, é a leitura.
from idecomp.decomp import Dadger

arq = Dadger.read("./decomp/dadger.rv0")


# %%
# O dadger, sendo um arquivo que se organiza por meio da declaração de registros, não
# possui, atualmente, uma interface que seja tabular. Desta forma, os métodos existentes
# retornam nenhum, um ou uma lista de objetos do registro específico solicitado.
termicas_semana1 = arq.ct(estagio=1)
print(len(termicas_semana1))


# %%
# Mesmo sem uma interface explícita para dados tabulares, os registros foram construídos
# com o uso de propriedades que devem facilitar o pós-processamento pelo usuário. Por exemplo,
# para gerar um gráfico comparativo de GT em relação ao CVU:
import plotly.express as px
import pandas as pd

gtmin_pat1 = [t.inflexibilidade[0] for t in termicas_semana1]
gtmax_pat1 = [t.disponibilidade[0] for t in termicas_semana1]
cvus_pat1 = [t.cvu[0] for t in termicas_semana1]
df = pd.DataFrame(data={"cvu": cvus_pat1, "gt": gtmax_pat1})
df.sort_values("cvu", inplace=True)
df["gt"] = df["gt"].cumsum()
df["gt"] += sum(gtmin_pat1)

# sphinx_gallery_thumbnail_number = 1
fig = px.line(
    df,
    x="gt",
    y="cvu",
    line_shape="hv",
)
fig
