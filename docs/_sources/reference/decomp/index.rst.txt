.. _decomp:

DECOMP
=======


A estrutura do *idecomp* padroniza os objetos de interface existentes para cada um dos módulos desenvolvidos. 
A interface com o DECOMP segue o padrão de implementar modelos para armazenar cada uma das informações existentes
nos arquivos de entrada e saída, além de classes utilitárias para gerenciar com a leitura e interpretação das informações
dos arquivos, bem como na geração de novos arquivos. As classes de leitura e escrita tem seus nomes padronizados, sendo estes
``LeituraMODELO`` e ``EscritaMODELO``, onde ``MODELO`` varia conforma o arquivo do DECOMP em questão.

Classes são nomeadas em ``CamelCase``, enquanto funções, métodos e variáveis recebem seus nomes em ``snake_case``.


Básico da interface DECOMP
----------------------------

É recomendado que a importação seja feita sempre de forma a utilizar somente os objetos que serão de fato necessários para 
o estudo em questão. Desta forma, não é recomendado importar todo o módulo ``idecomp.decomp`` ou utilizar o `wildcard` ``*``.

A importação recomendada é, por exemplo::

    >>> from idecomp.decomp.relato import LeituraRelato

Em geral, os objetos de leitura são instanciados recebendo um único atributo, que é o diretório de leitura e possuem um dos dois métodos: ``le_arquivo()`` ou ``le_arquivos()``. 
Os métodos de leitura, além de retornarem os objetos arquiridos dos arquivos de entrada de texto, também armazenam os dados internamente ao objeto de leitura.

Para a leitura do arquivo `relato.rv0`::

    >>> from idecomp.decomp.relato import LeituraRelato
    >>>
    >>> diretorio = "/home/usuario/..."
    >>> leitor = LeituraRelato(diretorio)
    >>> leitor.le_arquivo()
    <idecomp.decomp.modelos.Relato object at 0x000001BC7663B340>
    >>> leitor.relato
    <idecomp.decomp.modelos.Relato object at 0x000001BC7663B340>

Arquivos
---------

.. toctree::
   :maxdepth: 2

   arquivos/relato
