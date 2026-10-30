Perguntas Frequentes (FAQ)
==========================

Esta página reúne as dúvidas mais comuns sobre o uso do *idecomp*. As respostas estão
organizadas por tema para facilitar a navegação.

Instalacao
----------

Como instalo o idecomp?
^^^^^^^^^^^^^^^^^^^^^^^

O *idecomp* está disponível no PyPI e pode ser instalado com o ``pip``:

.. code-block:: bash

    pip install idecomp

Para instalar uma versão específica:

.. code-block:: bash

    pip install idecomp==1.8.2

Recomenda-se utilizar um ambiente virtual (``venv`` ou ``conda``) para evitar conflitos
de dependências.

Qual versão do Python é compatível com o idecomp?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

O *idecomp* requer **Python 3.11 ou superior**. As versões 3.11, 3.12, 3.13 e 3.14 são
testadas no CI e recomendadas para uso em produção.

Estou com problemas de conflito de versão com o cfinterface. O que fazer?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

O *idecomp* depende da biblioteca `cfinterface <https://github.com/rjmalves/cfinterface>`_,
que é responsável pelo mecanismo de parse dos arquivos. A versão compatível é
``>=1.9.0``. Caso você tenha uma versão incompatível instalada, force a reinstalação com
a restrição correta:

.. code-block:: bash

    pip install "cfinterface>=1.9.0" --force-reinstall

Se o conflito persistir, crie um ambiente virtual limpo e instale o *idecomp* a partir
do zero:

.. code-block:: bash

    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    # .venv\Scripts\activate   # Windows
    pip install idecomp

Leitura de Arquivos
-------------------

Como leio um arquivo do DECOMP com o idecomp?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Utilize o método de classe ``read`` da classe correspondente ao arquivo desejado,
passando o caminho para o arquivo no disco:

.. code-block:: python

    from idecomp.decomp import Dadger

    arq = Dadger.read("./dadger.rv0")
    print(arq)

O mesmo padrão se aplica a todos os arquivos suportados. Por exemplo, para ler o
arquivo de relato:

.. code-block:: python

    from idecomp.decomp import Relato

    arq = Relato.read("./relato.rv0")

Quais arquivos do DECOMP são suportados?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

O *idecomp* suporta **41 arquivos** do modelo DECOMP. Todos estão disponíveis no
módulo ``idecomp.decomp``. Os mais utilizados são:

- ``Dadger`` — arquivo principal de dados gerais do estudo (``dadger.rvX``)
- ``Relato`` — arquivo de relatório de resultados (``relato.rvX``)
- ``Vazoes`` — arquivo de vazões previstas e geradas (``vazoes.rvX``)
- ``Hidr`` — cadastro de usinas hidrelétricas (``hidr.dat``)
- ``Caso`` — arquivo de identificação do caso (``caso.dat``)
- ``DecOperSist`` — operação por submercado em formato CSV (``dec_oper_sist.csv``)
- ``DecOperUsih`` — operação por usina hidrelétrica (``dec_oper_usih.csv``)
- ``DecOperRee`` — operação por reservatório equivalente (``dec_oper_ree.csv``)

Para ver a lista completa, inspecione o módulo:

.. code-block:: python

    import idecomp.decomp as decomp
    print(dir(decomp))

O arquivo não foi encontrado. Como tratar o erro?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quando o caminho fornecido não existe, o Python levanta ``FileNotFoundError``. Trate
o erro explicitamente para fornecer mensagens mais informativas ao usuário:

.. code-block:: python

    from idecomp.decomp import Relato

    caminho = "./relato.rv0"
    try:
        arq = Relato.read(caminho)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
        print("Verifique se o caminho está correto e se o DECOMP foi executado.")

Como o idecomp lida com a codificação dos arquivos?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

O *idecomp* utiliza codificação **UTF-8** por padrão para leitura e escrita. Arquivos
gerados por versões antigas do DECOMP podem estar em Latin-1 (ISO-8859-1). Nesse caso,
pode ocorrer ``UnicodeDecodeError`` durante a leitura.

Se encontrar esse erro, converta o arquivo para UTF-8 antes de processá-lo:

.. code-block:: python

    # Converte de Latin-1 para UTF-8
    with open("relato.rv0", "r", encoding="latin-1") as f:
        conteudo = f.read()

    with open("relato_utf8.rv0", "w", encoding="utf-8") as f:
        f.write(conteudo)

    from idecomp.decomp import Relato
    arq = Relato.read("./relato_utf8.rv0")

Escrita de Arquivos
-------------------

Como escrevo um arquivo de entrada modificado?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para arquivos de entrada (como ``Dadger``, ``Vazoes``, ``Hidr``), utilize o método
``write`` na instância do objeto após realizar as modificações desejadas:

.. code-block:: python

    from idecomp.decomp import Vazoes

    arq = Vazoes.read("./vazoes.rv0")

    # Eleva todas as previsões em 10%
    df = arq.previsoes
    df.iloc[:, 1:] *= 1.1
    arq.previsoes = df

    # Salva o arquivo modificado
    arq.write("./vazoes_modificado.rv0")

Por que não consigo chamar ``write`` em arquivos de saída?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Arquivos de saída do DECOMP — como ``Relato``, ``DecOperSist``, ``DecOperUsih`` e
outros arquivos no formato CSV — são gerados exclusivamente pelo próprio modelo e
**não implementam o método ``write``**. Esses arquivos são somente leitura no contexto
do *idecomp*.

Tentar chamar ``write`` em uma instância de arquivo de saída levanta ``AttributeError``:

.. code-block:: python

    from idecomp.decomp import Relato

    arq = Relato.read("./relato.rv0")
    # Isso levanta AttributeError: 'Relato' object has no attribute 'write'
    # arq.write("./relato.rv0")

Para modificar resultados, trabalhe diretamente com os DataFrames retornados pelas
propriedades e salve-os em outros formatos (CSV, Parquet, Excel, etc.):

.. code-block:: python

    from idecomp.decomp import DecOperSist

    arq = DecOperSist.read("./dec_oper_sist.csv")
    df = arq.tabela
    df.to_csv("./resultado_filtrado.csv", index=False)

Como lidar com erros de permissão ao escrever?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Se o diretório de destino não existir ou não tiver permissão de escrita, o Python
levantará ``FileNotFoundError`` ou ``PermissionError``. Garanta que o diretório
existe antes de escrever:

.. code-block:: python

    import os
    from idecomp.decomp import Dadger

    arq = Dadger.read("./dadger.rv0")

    diretorio_saida = "./saida/estudo_modificado"
    os.makedirs(diretorio_saida, exist_ok=True)

    arq.write(os.path.join(diretorio_saida, "dadger.rv0"))

DataFrames e Dados
------------------

Como acesso os dados de um arquivo como DataFrame?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As propriedades das classes do *idecomp* retornam dados tabulares diretamente como
``pd.DataFrame`` do `pandas <https://pandas.pydata.org/>`_. Basta acessar a propriedade
correspondente ao dado desejado:

.. code-block:: python

    from idecomp.decomp import Relato

    arq = Relato.read("./relato.rv0")

    # Retorna pd.DataFrame com as iterações de convergência
    df_convergencia = arq.convergencia
    print(df_convergencia.dtypes)
    print(df_convergencia.head(5))

Para descobrir quais propriedades estão disponíveis em uma classe, use ``help()`` ou
inspecione os atributos do objeto:

.. code-block:: python

    from idecomp.decomp import DecOperSist

    arq = DecOperSist.read("./dec_oper_sist.csv")
    # Lista propriedades e métodos públicos
    props = [attr for attr in dir(arq) if not attr.startswith("_")]
    print(props)

Como filtro e modifico um DataFrame retornado por uma propriedade?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use as operações padrão do pandas sobre o DataFrame retornado. Para modificar os
dados e persistir a alteração no objeto, atribua o DataFrame modificado de volta
à mesma propriedade:

.. code-block:: python

    from idecomp.decomp import Vazoes

    arq = Vazoes.read("./vazoes.rv0")

    # Acessa o DataFrame de previsões
    df = arq.previsoes

    # Filtra apenas os primeiros 5 estágios
    df_filtrado = df[df["estagio"] <= 5].copy()
    print(df_filtrado)

    # Modifica todos os valores e atualiza o objeto
    df.iloc[:, 1:] *= 1.1
    arq.previsoes = df
    arq.write("./vazoes_modificado.rv0")

Como as propriedades se relacionam com os blocos e registros internos do DECOMP?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cada propriedade de uma classe de arquivo corresponde a um **registro** (em arquivos
baseados em ``RegisterFile``) ou a um **bloco** (em arquivos baseados em
``BlockFile``). Os modelos internos ficam em ``idecomp/decomp/modelos/``.

Por exemplo, no ``Dadger`` (``RegisterFile``), o método ``uh`` corresponde ao
registro ``UH`` do ``dadger.rvX``, que define as usinas hidrelétricas do estudo:

.. code-block:: python

    from idecomp.decomp import Dadger

    arq = Dadger.read("./dadger.rv0")

    # O método 'uh' mapeia para o registro UH do dadger.rvX
    df_usinas = arq.uh(df=True)
    print(df_usinas.columns.tolist())

No ``Relato`` (``BlockFile``), a propriedade ``convergencia`` mapeia para o bloco
de convergência do ``relato.rvX``, delimitado por um padrão textual específico no
arquivo de saída.

Para entender a correspondência entre propriedades e registros/blocos de um arquivo
específico, consulte a :doc:`../referencia/decomp/index` ou a documentação do cfinterface.

O que retornam os métodos de acesso a registros, como ``Dadger.uh()``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nos arquivos baseados em ``RegisterFile`` (``Dadger``, ``Dadgnl`` e os arquivos
das LIBS), cada método de acesso recebe filtros opcionais pelos campos do registro
e o argumento ``df``. O tipo do retorno depende de ``df`` e de quantos registros
atendem aos filtros:

- com ``df=False`` (padrão), o retorno é ``None`` quando nenhum registro atende aos
  filtros, **o próprio registro** quando apenas um atende e uma **lista** quando
  mais de um atende;
- com ``df=True``, os filtros são ignorados e o retorno é sempre um
  ``pd.DataFrame`` com todos os registros do tipo, vazio quando não há nenhum.

Os métodos possuem sobrecargas (``typing.overload``) sobre ``df``, de modo que
verificadores de tipo reconhecem o retorno ``pd.DataFrame`` quando ``df=True``.
Quando o código precisa de uma lista independentemente da quantidade de registros
encontrados, normalize o retorno:

.. code-block:: python

    from idecomp.decomp import Dadger

    arq = Dadger.read("./dadger.rv0")

    # Um único registro UH, ou None
    uh = arq.uh(1)

    # Um registro CT ou uma lista deles, conforme o deck
    r = arq.ct(estagio=1)
    cts = [] if r is None else r if isinstance(r, list) else [r]

    # Todos os registros CT, sempre como DataFrame
    df_ct = arq.ct(df=True)

Erros Comuns
------------

Recebi um erro de parse do cfinterface. O que significa?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Erros de parse geralmente indicam que o arquivo do DECOMP está **malformado** ou em
uma versão não reconhecida. O cfinterface tenta fazer o parse linha a linha e levanta
exceções quando encontra conteúdo inesperado.

Verifique os pontos mais comuns:

1. O arquivo está completo e não foi truncado durante a execução do DECOMP.
2. A extensão e o nome do arquivo correspondem ao tipo esperado (``dadger.rv0``,
   ``relato.rv0``, ``dec_oper_sist.csv``, etc.).
3. O arquivo não foi editado manualmente de forma incorreta.

.. code-block:: python

    from idecomp.decomp import Dadger

    # Se o arquivo estiver malformado, use try/except para capturar o erro
    try:
        arq = Dadger.read("./dadger.rv0")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {type(e).__name__}: {e}")
        print("Verifique se o arquivo dadger.rv0 está íntegro.")

Como lidar com versões diferentes do DECOMP?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alguns arquivos de saída CSV do DECOMP possuem estruturas de colunas diferentes
conforme a versão do modelo. O *idecomp* utiliza o dicionário ``VERSIONS`` do
cfinterface para lidar com isso automaticamente: ao ler o arquivo, o *idecomp*
inspeciona o cabeçalho e seleciona a estrutura de colunas correta.

Caso o arquivo tenha sido gerado por uma versão do DECOMP não reconhecida, o *idecomp*
pode não conseguir fazer o parse corretamente. Verifique a versão do DECOMP que
gerou o arquivo:

.. code-block:: python

    from idecomp.decomp import DecOperSist

    arq = DecOperSist.read("./dec_oper_sist.csv")

    # Verifica a versão detectada no cabeçalho
    if hasattr(arq, "versao"):
        print(f"Versão detectada: {arq.versao}")

Se a versão não for suportada, considere atualizar o *idecomp* para a versão mais
recente, que pode incluir suporte a versões mais novas do DECOMP.

Uma propriedade está retornando ``None``. Por que?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quando uma propriedade retorna ``None``, o registro ou bloco correspondente **não
foi encontrado no arquivo**. Isso pode ocorrer quando:

1. O arquivo não contém aquele bloco de dados (por exemplo, o estudo não modelou
   a feature correspondente).
2. O arquivo está em uma versão mais antiga do DECOMP que não gerava aquele campo.
3. O arquivo está correto, mas o dado esperado não foi gerado nesta execução.

Sempre verifique se a propriedade é ``None`` antes de operar sobre ela:

.. code-block:: python

    from idecomp.decomp import Relato

    arq = Relato.read("./relato.rv0")

    df_cmo = arq.cmo_medio_subsistema
    if df_cmo is None:
        print("Dados de CMO não encontrados no arquivo relato.rv0.")
        print("Verifique se o estudo incluiu o cálculo de CMO.")
    else:
        print(df_cmo.head())
