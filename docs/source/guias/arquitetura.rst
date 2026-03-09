Arquitetura do idecomp
======================

Visao Geral
-----------

O *idecomp* é um pacote Python que oferece uma interface de alto nível para leitura e
escrita dos arquivos do modelo `DECOMP <http://www.cepel.br/>`_, desenvolvido pelo CEPEL e
utilizado para o planejamento da operação de curto prazo do Sistema Interligado Nacional (SIN).
Cada arquivo suportado pelo pacote é representado por uma classe Python dedicada, que encapsula
a lógica de leitura, escrita e acesso aos dados.

A base do idecomp é o framework `cfinterface <https://github.com/rjmalves/cfinterface>`_,
que fornece as classes-base responsáveis pelo mecanismo de parse de arquivos de texto estruturado.
O idecomp atua como uma camada de domínio sobre esse framework: as classes de arquivo do idecomp
herdam de classes-base do cfinterface e definem quais modelos de registros ou blocos compõem
cada arquivo do DECOMP.

Dessa forma, o desenvolvedor que utiliza o idecomp não precisa conhecer os detalhes do protocolo
de parse — basta instanciar a classe do arquivo desejado, chamar o método ``read`` para carregar
os dados do disco e acessar as propriedades que retornam os dados em estruturas Python convenientes,
como ``pd.DataFrame`` do `pandas <https://pandas.pydata.org/>`_.

Estrutura de Pacotes
--------------------

O idecomp organiza seu código em dois subpacotes principais:

``idecomp/decomp/``
    Contém as 41 classes de arquivo do DECOMP, uma por arquivo suportado. Exemplos:
    ``Dadger``, ``Relato``, ``Vazoes``, ``DecOperSist``, ``Hidr``, entre outros.
    Todas as classes são expostas diretamente em ``idecomp.decomp`` via importação no
    ``__init__.py`` do subpacote.

``idecomp/decomp/modelos/``
    Contém os modelos de registros e blocos utilizados pelas classes de arquivo acima.
    São 45 módulos de modelos, organizados em subdiretórios:

    ``idecomp/decomp/modelos/blocos/``
        Definições de blocos reutilizáveis entre diferentes arquivos, como
        ``VersaoModelo``, que identifica a versão do DECOMP a partir de um cabeçalho.

    ``idecomp/decomp/modelos/arquivoscsv/``
        Adaptador para arquivos de saída no formato CSV, base para arquivos como
        ``DecOperSist``, ``DecOperUsih``, ``DecOperRee``, entre outros.

``idecomp/libs/``
    Contém 2 módulos auxiliares para arquivos do tipo LIBS utilizados em conjunto
    com o DECOMP: ``UsinasHidreletricas`` (``usinas_hidreletricas.py``) e
    ``Restricoes`` (``restricoes.py``), com seus respectivos modelos em
    ``idecomp/libs/modelos/``.

Framework cfinterface
---------------------

O cfinterface define três classes-base para arquivos de texto estruturado. O idecomp
utiliza todas as três, dependendo do formato do arquivo DECOMP em questão:

:class:`cfinterface.files.registerfile.RegisterFile`
    Base para arquivos orientados a registros, em que cada linha do arquivo corresponde
    a um registro identificado por uma palavra-chave no início da linha. O arquivo
    ``dadger.rvX`` é o principal exemplo: cada seção de dados (usinas, restrições,
    configurações de estudo) é representada por um tipo de registro próprio.

    .. code-block:: python

        from idecomp.decomp import Dadger

        arq = Dadger.read("./dadger.rv0")

        # Acessa o registro TE (título do estudo)
        titulo = arq.te
        print(titulo)

        # Acessa a tabela de usinas hidrelétricas como DataFrame
        df_usinas = arq.uh
        print(df_usinas.head())

        # Modifica um dado e salva o arquivo de entrada atualizado
        arq.te = "Novo titulo do estudo"
        arq.write("./dadger.rv0")

:class:`cfinterface.files.blockfile.BlockFile`
    Base para arquivos orientados a blocos, em que o conteúdo é dividido em seções
    delimitadas por cabeçalhos textuais. O arquivo ``relato.rvX`` é o principal
    exemplo: cada bloco de resultados (convergência, balanço energético, CMO) é
    identificado por um padrão textual de abertura e fechamento.

    .. code-block:: python

        from idecomp.decomp import Relato

        arq = Relato.read("./relato.rv0")

        # Acessa o bloco de convergência como DataFrame
        df_conv = arq.convergencia
        print(df_conv.head(10))

``ArquivoCSV`` (``idecomp.decomp.modelos.arquivoscsv.arquivocsv``)
    Adaptador interno do idecomp construído sobre o cfinterface para arquivos de saída
    no formato CSV gerados pelo DECOMP. Classes como ``DecOperSist``, ``DecOperUsih``
    e ``DecOperRee`` herdam de ``ArquivoCSV`` e implementam apenas a especificação
    das colunas e versões suportadas.

    .. code-block:: python

        from idecomp.decomp import DecOperSist

        arq = DecOperSist.read("./dec_oper_sist.csv")

        # Acessa a tabela de operação por submercado
        df = arq.tabela
        print(df.head())

Fluxo de Dados
--------------

O fluxo de dados no idecomp segue sempre o mesmo padrão, independentemente do tipo
de arquivo (registro, bloco ou CSV):

1. **Leitura do arquivo bruto**: o método de classe ``ClassName.read(caminho)`` abre o
   arquivo no disco e aciona o mecanismo de parse do cfinterface.
2. **Construção do objeto Python**: o cfinterface percorre o arquivo linha a linha,
   identificando registros ou blocos e instanciando os modelos correspondentes.
3. **Acesso via propriedades**: o objeto retornado expõe os dados através de propriedades
   Python, que retornam ``pd.DataFrame`` para dados tabulares ou valores escalares
   tipados para configurações simples.
4. **Escrita opcional**: para arquivos de entrada, o método ``instancia.write(caminho)``
   serializa o estado atual do objeto de volta para o formato de texto do DECOMP.

.. code-block:: python

    from idecomp.decomp import Vazoes

    # 1. Leitura: arquivo bruto -> objeto Python
    arq_vazoes = Vazoes.read("./vazoes.rv0")

    # 2. Acesso: propriedade retorna pd.DataFrame
    df = arq_vazoes.previsoes
    print(df.shape)

    # 3. Modificação e escrita (somente para arquivos de entrada)
    df.iloc[:, 1:] *= 1.1
    arq_vazoes.previsoes = df
    arq_vazoes.write("./vazoes.rv0")

Arquivos de saída do DECOMP (como ``relato.rvX``, ``dec_oper_sist.csv``) não
implementam o método ``write``, pois são gerados exclusivamente pelo próprio modelo.
Tentativas de chamar ``write`` em instâncias desses arquivos resultam em erro.

Modelos e Registros
-------------------

Cada classe de arquivo em ``idecomp/decomp/`` delega o parse dos dados para classes
de modelo definidas em ``idecomp/decomp/modelos/``. Essa separação mantém as classes
de arquivo focadas na interface pública (propriedades e métodos) enquanto os modelos
cuidam dos detalhes de formatação e posicionamento de campos.

Para arquivos baseados em ``RegisterFile`` (como ``Dadger``), os modelos são
subclasses de ``Register`` do cfinterface. Cada subclasse de ``Register`` define:

- O código (palavra-chave) que identifica a linha no arquivo.
- Os campos (posição, tipo e nome) que compõem o registro.

Para arquivos baseados em ``BlockFile`` (como ``Relato``), os modelos são subclasses
de ``Block`` do cfinterface. Cada subclasse de ``Block`` define:

- O padrão textual que delimita o início do bloco.
- A lógica de leitura das linhas internas ao bloco.

Os modelos em ``idecomp/decomp/modelos/blocos/`` são blocos reutilizáveis compartilhados
entre múltiplos arquivos. Por exemplo, o bloco ``VersaoModelo`` aparece em todos os
arquivos CSV do DECOMP e é responsável por identificar a versão do modelo a partir
do cabeçalho, permitindo que o idecomp selecione a estrutura de colunas correta para
cada versão do DECOMP.

Para aprofundamento nos mecanismos internos de ``Register``, ``Block`` e ``RegisterFile``,
consulte a `documentação do cfinterface <https://rjmalves.github.io/cfinterface/>`_.
