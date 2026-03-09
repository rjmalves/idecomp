Guia de Desempenho
==================

Este guia apresenta as características de desempenho do *idecomp* e estratégias
práticas para otimizar fluxos de trabalho que processam grandes volumes de arquivos
do DECOMP. As recomendações aqui descritas são especialmente relevantes para análises
em lote, como a consolidação de resultados de múltiplos cenários ou revisões.

Importacao
----------

Ao executar ``import idecomp`` ou ``from idecomp.decomp import AlgumaClasse``, o
interpretador Python carrega o módulo ``idecomp/__init__.py``, que importa
imediatamente o subpacote ``idecomp.decomp``. O ``__init__.py`` desse subpacote,
por sua vez, importa todas as **41 classes de arquivo** do DECOMP de uma vez. Esse
comportamento de importação antecipada (*eager import*) garante que a interface
pública do pacote esteja sempre disponível de forma consistente, mas implica um
custo de inicialização proporcional ao número de módulos carregados.

Para a maioria dos scripts interativos e notebooks, esse custo é imperceptível.
Entretanto, em aplicações que chamam scripts Python repetidamente — por exemplo,
pipelines de automação que invocam o interpretador a cada execução — o tempo de
inicialização do processo pode ser relevante. Nesses casos, é possível reduzir o
escopo da importação apontando diretamente para o módulo do arquivo desejado, em
vez de importar pelo namespace agregado do subpacote.

.. code-block:: python

    # Importa pelo namespace agregado: carrega todos os 41 modulos
    from idecomp.decomp import Dadger

    # Importa diretamente do modulo: carrega apenas o modulo necessario
    from idecomp.decomp.dadger import Dadger

A segunda forma acessa ``idecomp/decomp/dadger.py`` diretamente, sem acionar a
importação em cadeia de todos os demais módulos do subpacote. O resultado funcional
é idêntico — a classe ``Dadger`` obtida é a mesma — mas o tempo de importação é
menor quando apenas um ou poucos arquivos precisam ser processados.

Para medir o impacto no seu ambiente, utilize o módulo ``time`` do Python antes de
decidir qual estratégia adotar:

.. code-block:: python

    import time

    inicio = time.perf_counter()
    from idecomp.decomp.dadger import Dadger
    fim = time.perf_counter()

    print(f"Tempo de importacao: {(fim - inicio) * 1000:.2f} ms")

Leitura e Escrita de Arquivos
------------------------------

O padrão básico de leitura de um arquivo é sempre o mesmo: instanciar a classe
correspondente chamando o método de classe ``read`` com o caminho do arquivo no
disco. O objeto retornado mantém todos os dados do arquivo em memória e expõe as
informações por meio de propriedades que retornam ``pd.DataFrame`` ou valores
escalares tipados.

.. code-block:: python

    from idecomp.decomp import DecOperSist

    # Leitura de um unico arquivo
    arq = DecOperSist.read("./resultados/dec_oper_sist.csv")
    df = arq.tabela
    print(df.shape)

Em análises de resultados do DECOMP, é comum processar o mesmo arquivo de saída
proveniente de múltiplos cenários ou revisões armazenados em diretórios separados.
O padrão recomendado para esse caso é iterar sobre os caminhos, ler cada arquivo,
extrair o DataFrame desejado e acumulá-los em uma lista para concatenação ao final:

.. code-block:: python

    from pathlib import Path
    import pandas as pd
    from idecomp.decomp.dec_oper_sist import DecOperSist

    dfs = []
    for caminho in Path("./resultados").glob("*/dec_oper_sist.csv"):
        arq = DecOperSist.read(str(caminho))
        dfs.append(arq.tabela)

    df_total = pd.concat(dfs, ignore_index=True)
    print(f"Total de linhas consolidadas: {len(df_total)}")

Concatenar ao final, em vez de concatenar incrementalmente dentro do loop, evita a
criação de cópias intermediárias do DataFrame a cada iteração — um padrão de
desempenho amplamente recomendado pelo próprio pandas. Quando o número de arquivos
for muito grande, considere adicionar ao DataFrame uma coluna de identificação
(nome do diretório ou do cenário) antes de acrescentá-lo à lista, para facilitar
a rastreabilidade dos dados na análise subsequente.

Para medir o tempo total de um processamento em lote, envolva o loop com o módulo
``time``:

.. code-block:: python

    import time
    from pathlib import Path
    import pandas as pd
    from idecomp.decomp.dec_oper_sist import DecOperSist

    caminhos = list(Path("./resultados").glob("*/dec_oper_sist.csv"))
    inicio = time.perf_counter()

    dfs = []
    for caminho in caminhos:
        arq = DecOperSist.read(str(caminho))
        dfs.append(arq.tabela)

    df_total = pd.concat(dfs, ignore_index=True)
    fim = time.perf_counter()

    print(f"{len(caminhos)} arquivos processados em {fim - inicio:.2f}s")

Uso de Memoria
--------------

Cada objeto de arquivo do *idecomp* mantém em memória a representação Python
completa do arquivo lido — registros, blocos ou colunas CSV, dependendo do tipo.
Para arquivos de saída CSV com muitas linhas (como ``dec_oper_sist.csv`` com colunas
de estágio, cenário e patamar), o objeto pode ocupar memória significativa quando
múltiplos arquivos são carregados simultaneamente.

O padrão recomendado para operações em lote é **ler, extrair e descartar**: após
obter o DataFrame desejado de um objeto de arquivo, remova a referência ao objeto
com ``del`` para que o coletor de lixo do Python possa liberar a memória associada.

.. code-block:: python

    from idecomp.decomp.dec_oper_sist import DecOperSist

    arq = DecOperSist.read("./dec_oper_sist.csv")
    df = arq.tabela         # extrai o DataFrame necessario
    del arq                 # libera o objeto do arquivo da memoria

    # A partir daqui, apenas df permanece em memoria
    print(df.head())

Em loops que processam dezenas ou centenas de arquivos, combine esse padrão com
uma chamada explícita ao coletor de lixo ao final de cada iteração quando o
consumo de memória for crítico:

.. code-block:: python

    import gc
    from pathlib import Path
    import pandas as pd
    from idecomp.decomp.dec_oper_sist import DecOperSist

    dfs = []
    for caminho in Path("./resultados").glob("*/dec_oper_sist.csv"):
        arq = DecOperSist.read(str(caminho))
        df_parcial = arq.tabela
        del arq        # descarta o objeto antes de passar para o proximo arquivo
        gc.collect()   # forca a coleta de lixo (recomendado para lotes muito grandes)
        dfs.append(df_parcial)

    df_total = pd.concat(dfs, ignore_index=True)

Note que ``gc.collect()`` adiciona um pequeno overhead por chamada. Avalie se o
ganho de memória justifica esse custo no seu caso de uso, medindo o consumo de
memória com ferramentas como ``tracemalloc`` (biblioteca padrão) ou ``memory_profiler``
(pacote externo).

Dicas de Otimizacao
--------------------

As dicas a seguir sintetizam as práticas mais eficientes para uso do *idecomp* em
fluxos de trabalho de maior escala.

**1. Prefira importações diretas de módulo quando o tempo de inicialização importa.**
Use ``from idecomp.decomp.nome_modulo import NomeClasse`` em vez de
``from idecomp.decomp import NomeClasse`` para evitar o carregamento antecipado de
todos os 41 módulos. Aplique essa estratégia em scripts invocados repetidamente por
pipelines de automação.

**2. Use geradores para processar arquivos em lote sem acumular todos na memória.**
Se o objetivo é calcular estatísticas ou filtrar linhas, um gerador evita carregar
todos os DataFrames simultaneamente:

.. code-block:: python

    from pathlib import Path
    import pandas as pd
    from idecomp.decomp.dec_oper_sist import DecOperSist

    def gerar_tabelas(padrao):
        for caminho in Path("./resultados").glob(padrao):
            arq = DecOperSist.read(str(caminho))
            yield arq.tabela
            del arq

    # Concatena sob demanda, sem manter todos os objetos vivos ao mesmo tempo
    df_total = pd.concat(gerar_tabelas("*/dec_oper_sist.csv"), ignore_index=True)

**3. Filtre os DataFrames imediatamente após a extração.**
Quanto antes as linhas irrelevantes forem descartadas, menor será o consumo de
memória ao longo do processamento. Aplique filtros baseados em colunas como
``estagio``, ``cenario`` ou ``patamar`` logo após acessar a propriedade do arquivo:

.. code-block:: python

    from idecomp.decomp.dec_oper_sist import DecOperSist

    arq = DecOperSist.read("./dec_oper_sist.csv")
    df = arq.tabela

    # Filtra apenas o primeiro estagio antes de qualquer outra operacao
    df_filtrado = df[df["estagio"] == 1].copy()
    del arq, df

**4. Libere objetos de arquivo com ``del`` após extrair os dados necessários.**
Objetos de arquivo do *idecomp* não são referências leves — eles armazenam a
representação estruturada completa do arquivo. Descartá-los explicitamente com
``del`` após a extração do DataFrame é especialmente importante em loops com muitas
iterações.

**5. Utilize ``gc.collect()`` em lotes muito grandes.**
Para processamentos com centenas de arquivos de grande volume, chame ``gc.collect()``
periodicamente (por exemplo, a cada 50 arquivos) para garantir que objetos
descartados sejam de fato liberados antes que o Python reutilize a memória. Avalie
o impacto com ``tracemalloc`` antes e depois de adotar essa prática:

.. code-block:: python

    import gc
    import tracemalloc
    from pathlib import Path
    import pandas as pd
    from idecomp.decomp.dec_oper_sist import DecOperSist

    tracemalloc.start()

    dfs = []
    caminhos = list(Path("./resultados").glob("*/dec_oper_sist.csv"))
    for i, caminho in enumerate(caminhos):
        arq = DecOperSist.read(str(caminho))
        dfs.append(arq.tabela)
        del arq
        if (i + 1) % 50 == 0:
            gc.collect()

    df_total = pd.concat(dfs, ignore_index=True)

    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Pico de memoria: {memoria_pico / 1024 / 1024:.1f} MB")
