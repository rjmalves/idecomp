Como contribuir?
=================

O framework `cfinterface` e dependências de desenvolvimento
------------------------------------------------------------

O módulo *idecomp* é desenvolvido considerando o framework proposto no módulo `cfinterface <https://github.com/rjmalves/cfi>`_.

A abordagem proposta no framework consiste em classificar os arquivos processados com relação à sua construção. São definidas três classes de arquvos:

- :obj:`~cfinterface.files.blockfile.BlockFile`
- :obj:`~cfinterface.files.sectionfile.SectionFile`
- :obj:`~cfinterface.files.registerfile.RegisterFile`

Esta classificação independe do arquivo ser constituído de armazenamento no formato texto ou binário, sendo que
esta informação é fornecida na declaração da classe que modela o arquivo em questão. Também é possível fornecer
informações sobre a codificação padrão utilizada em casos de arquivos gerados com caracteres especiais.

A modelagem de arquivos como :obj:`~cfinterface.files.blockfile.BlockFile` se baseia na definição de blocos do arquivo que
possuem um padrão específico, binário ou textual, que indica o início de um conjunto de informações que seja
autocontido e bem definido. Opcionalmente, também pode haver um padrão de terminação, ou o bloco pode determinar
a sua terminação seguindo outros critérios. Um bloco é definido como um elemento da classe :obj:`~cfinterface.components.block.Block`.
Exemplos de arquivos do módulo *idecomp* que são implementados através deste modelo são o :ref:`relato.rvX <relato>` e :ref:`inviab_unic.rvX <inviabunic>`.

O uso dos modelos da :obj:`~cfinterface.files.sectionfile.SectionFile` se baseia na definição de seções do arquivo que
sempre aparecem em uma mesma ordem e são obrigatórias. Da mesma forma, o arquivo pode ser binário ou textual. Diferentemente da modelagem
por :obj:`~cfinterface.files.blockfile.BlockFile`, que permite que um mesmo bloco apareça diversas vezes no arquivo, a abordagem
por seções não permite flexibilidade na definição de quais conteúdos aparecem e na ordem que aparecem. Podem, cada objeto
:obj:`~cfinterface.components.section.Section` pode definir o seu critério de fim, permitindo uma certa flexibilidade dentro de cada
seção. Exemplos de arquivos do módulo *idecomp* que são implementados através deste modelo são o :ref:`caso.dat <caso>` e :ref:`arquivos.rvX <arquivos>`.

Por fim, a abordagem por :obj:`~cfinterface.files.registerfile.RegisterFile` se baseia na definição de unidades mínimas de conteúdo
que ocupam sempre uma única linha e tem formato constante, que são chamadas de registros. Da mesma forma, o arquivo pode ser binário ou textual.
Registros podem ser vistos como blocos de uma só linha mas, devido à sua simplicidade, são de mais fácil definição, através da classe
:obj:`~cfinterface.components.register.Register`. A implementação de um registro consiste apenas na sua definição, visto que
a leitura e a escrita deste são inteiramente obtidas do formato dos seus campos. No *idecomp*, os arquivos :ref:`dadger.rvX <dadger>` e :ref:`dadgnl.rvX <dadgnl>` são modelados
seguindo esta abordagem.



Para instalar as dependências de desenvolvimento, incluindo as necessárias para a geração automática do site::
    
    $ git clone https://github.com/rjmalves/idecomp.git
    $ cd idecomp
    $ pip install -r dev-requirements.txt

.. warning::

    O conteúdo da documentação não deve ser movido para o repositório. Isto é feito
    automaticamente pelos scripts de CI no caso de qualquer modificação no branch `main`.


Diretrizes de modelagem para o módulo `idecomp`
------------------------------------------------

A principal diretriz para o desenvolvimento do *idecomp* é a relação entre arquivos do modelo DECOMP e as classes
disponíveis para uso. Cada arquivo de entrada do modelo é mapeado para uma classe do módulo, que segue
o nome geralmente utilizado para o arquivo nos casos de exemplo que são fornecidos junto com o modelo pelo desenvolvedor
ou pelo ONS para publicação dos decks das revisões semanais do PMO. É utilizado sempre `PascalCase` para determinação dos nomes
das classes, sendo que abreviações que possivelmente se encontram nos nomes dos arquivos são ignoradas na mudança de caso. Por exemplo:

- `arquivos.rvX` é modelado na classe :ref:`Arquivos <arquivos>`
- `dadger.rvX` é modelado na classe :ref:`Dadger <dadger>`
- `relato.rvX` é modelado na classe :ref:`Relato <relato>`

É convencionado, sempre que possível, que as propriedades das classes que contém os dados processados dos arquivos
lidem com objetos do tipo :obj:`~pandas.DataFrame` para a representação de dados tabulares. Além disso, se possível,
é recomendado processar a informação contida nos arquivos para que esteja na seguindo as formas normais
para dados tabulares, mesmo quando há divergência na representação textual nos arquivos de entrada do DECOMP.

As propriedades das classes e também as colunas dos :obj:`~pandas.DataFrame` que são produzidos são convencionados de
serem nomeados em `snake_case`. Além disso, deve-se evitar ao máximo ambiguidades na escolha dos nomes das propriedades e
das colunas. Alguns pontos recorrentes onde são encontradas ambiguidades e deve-se adotar um termo único são:

- Propriedade ou :obj:`~pandas.DataFrame` que contenha informações de usinas (hidrelétricas, termelétricas, etc.) e venham e conter atributos
  como código (`int`) e nome (`str`) convenciona-se chamar de *nome_usina* e *codigo_usina*, para garantir o único sentido possível.
- Propriedade ou :obj:`~pandas.DataFrame` que contenha informações relativas aos submercados de energia, que ora são
  mencionados como subsistemas de energia, adota-se o termo único *submercado*. De modo semelhante, locais onde apareçam
  informações desta entendidade são denominados *codigo_submercado* e *nome_submercado*. O mesmo raciocínio se aplica
  ao se referir a REE.


Convenções de código
---------------------

O *idecomp* considera critérios de qualidade de código em seus scripts de Integração Contínua (CI), além de uma bateria de testes unitários.
Desta forma, não é possível realizar uma *release* de uma versão que não passe em todos os testes estabelecidos ou não
atenda aos critérios de qualidade de código impostos.

A primeira convenção é que sejam seguidas as diretrizes de sintaxe `PEP8 <https://peps.python.org/pep-0008/>`_, provenientes do guia de estilo
do autor da linguagem. Além disso, não é recomendado que existam funções muito complexas, com uma quantidade
excessiva de *branches* e *loops*, o que piora e legibilidade do código. Isto pode ser garantido através de módulos
específicos para análise de qualidade de código, como será mencionado a seguir. A única exceção é a regra `E203 <https://www.flake8rules.com/rules/E203.html>`_.

Para garantir a formatação é recomendado utilizar o módulo `black <https://github.com/psf/black>`_, que realiza formatação automática e possui
integração nativa com alguns editores de texto no formato de *plugins* ou extensões. 

A segunda convenção é que seja utilizada tipagem estática. Isto é, não deve ser uitilizada uma variável em código a qual possua
tipo de dados que possa mudar durante a execução do mesmo. Além disso, não deve ser declarada uma variável cujo tipo não é possível de
ser inferido em qualquer situação, permanencendo incerto para o leitor o tipo de dados da variável a menos que seja feita uma
execução de teste do programa.


Procedimentos de teste
-----------------------

O *idecomp* realiza testes utilizando o pacote de testes de Python `pytest <https://pytest.org>`_
e controle da qualidade de código com `pylama <https://pylama.readthedocs.io/en/latest//>`_.
A tipagem estática é garantida através do uso de `mypy <http://mypy-lang.org/>`_
, que é sempre executado nos scripts de Integração Contínua (CI).

Antes de realizar um ``git push`` é recomendado que se realize estes três procedimentos
descritos, que serão novamente executados pelo ambiente de CI::

    $ pytest ./tests
    $ mypy ./idecomp
    $ pylama ./idecomp --ignore E203
