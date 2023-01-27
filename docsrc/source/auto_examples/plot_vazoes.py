"""
========================================
vazoes.dat
========================================
"""

#%%
# O primeiro passo para realizar o processamento do arquivo, assim como os
# demais arquivos de saída, é a leitura. A função de leitura recebe dois argumentos,
# sendo que o segundo é opcional.
from idecomp.decomp import Vazoes

arq = Vazoes.le_arquivo(".", nome_arquivo="vazoes.rv0")


#%%
# O arquivo de vazões contém informações do histórico de vazões por posto de medição, servindo
# de entrada para os modelos de planejamento.
df = arq.vazoes
print(df)


#%%
# A partir deste dataframe é possível realizar análises e produzir visualizações. Por exemplo,
# utilizando o módulo plotly. Deste ponto em diante, não é mais necessário o conhecimento
# específico do arquivo ou da idecomp.
import plotly.graph_objects as go

# sphinx_gallery_thumbnail_number = 1
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=[df["66"]], name="Vazao Posto 66"))
fig
