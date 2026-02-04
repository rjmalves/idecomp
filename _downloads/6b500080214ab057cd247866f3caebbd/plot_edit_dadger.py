"""
========================================
Edição do dadger.rv0
========================================

"""

# %%
# O primeiro passo para realizar o processamento do arquivo, assim como os
# demais arquivos de saída, é a leitura.
from idecomp.decomp import Dadger

arq = Dadger.read("./decomp/dadger.rv0")


# %%
# Atualmente existe suporte para criação e edição de todos os registros
# utilizados oficialmente nos decks de DECOMP. Por exemplo, pode ser desejado
# alterar os valores de alguns registros ou substituir todo um bloco de
# registros existentes.
#
# Isto pode ser feito, por exemplo, para o bloco de geração
# das usinas não simuladas. É possível visualizar os registros existentes no formato
# de um `DataFrame`, porém isto é somente para leitura na versão atual do `idecomp`.
df_pq = arq.pq(df=True)
print(df_pq)


# %%
# Para realizar a edição ou criação de novos registros é necessário acessar os
# objetos que modelam cada registro, e isto é feito ao não forçar o argumento opcional
# `df=True`. Assim como para outros registros, é possível filtrar arbitrariamente pelos
# registros que são desejados passando as propriedades destes como argumentos opcionais
print(arq.pq(codigo_submercado=1))


# %%
# Para realizar a edição dos valores dos registros é possível acessar os objetos realizando
# os filtros adequados e alterar os valores das suas propriedades. Por exemplo, como só
# existe um registro `PQ` por submercado e estágio, os valores das suas gerações podem ser
# modificados diretamente:
reg_pq = arq.pq(codigo_submercado=1, estagio=1)
reg_pq.geracao = [10.0, 10.0, 10.0]
print(arq.pq(codigo_submercado=1, estagio=1).geracao)

# %%
# Caso seja desejado refazer completamente o bloco dos registros PQ, também é permitido
# deletar todos os registros que formam o bloco e criar um novo conjunto de registros do zero.
# Esta também é a abordagem que seria utilizada ao se construir um arquivo `dadger.rvX` a partir
# de valores de bancos de dados, por exemplo. Para isto, é necessário também importar a classe
# do registro a ser criado, no caso, o PQ:
from idecomp.decomp.dadger import PQ

registros_atuais = arq.pq()
# É interessante guardar uma referência para o registro anterior
# ao bloco PQ, para que os novos registros sejam adicionados na mesma posição.
registro_base = registros_atuais[0].previous
for r in registros_atuais:
    arq.data.remove(r)


# %%
# Supondo que foram aquisitados valores de um banco de dados, ou feito algum processamento
# e foi obtido um `DataFrame` com o conteúdo desejado para se criar o novo bloco PQ. Desta forma,
# é possível criar os registros iterativamente:
import pandas as pd

df = pd.DataFrame(
    data={
        "estagio": [1, 6, 1, 6, 1, 6, 1, 6],
        "nome": [
            "SUDESTE",
            "SUDESTE",
            "SUL",
            "SUL",
            "NORDESTE",
            "NORDESTE",
            "NORTE",
            "NORTE",
        ],
        "submercado": [1, 1, 2, 2, 3, 3, 4, 4],
        "geracao_pat1": [10.0, 10.0, 20.0, 20.0, 30.0, 30.0, 40.0, 40.0],
        "geracao_pat2": [11.0, 11.0, 21.0, 21.0, 31.0, 31.0, 41.0, 41.0],
        "geracao_pat3": [12.0, 12.0, 22.0, 22.0, 32.0, 32.0, 42.0, 42.0],
    }
)

for _, linha in df.iterrows():
    r = PQ()
    r.estagio = linha["estagio"]
    r.nome = linha["nome"]
    r.codigo_submercado = linha["submercado"]
    r.geracao = linha[
        ["geracao_pat1", "geracao_pat2", "geracao_pat3"]
    ].tolist()
    arq.data.add_after(registro_base, r)
    registro_base = r

print(arq.pq(df=True))

# %%
# Para exportar o arquivo modificado, basta utilizar o método `write` a partir do objeto que foi
# alterado. Todavia, não é obrigatório fornecer um caminho para um arquivo no disco. A exportação
# também pode ser feita para um buffer em memória, se o objetivo
# for enviar o conteúdo do arquivo através de uma requisição HTTP, por exemplo, ou armazenar em um
# banco de dados para documentos:
from io import StringIO

conteudo_dadger = StringIO()
arq.write(conteudo_dadger)
print(conteudo_dadger.getvalue())
