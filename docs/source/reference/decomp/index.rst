.. _decomp:

DECOMP
=======


A estrutura do *idecomp* padroniza os objetos de interface existentes. 
A interface com o DECOMP segue o padrão de implementar modelos para armazenar cada uma das informações existentes
nos arquivos de entrada e saída, além de classes utilitárias para gerenciar com a leitura e interpretação das informações
dos arquivos, bem como na geração de novos arquivos.

Classes são nomeadas em ``CamelCase``, enquanto funções, métodos e variáveis recebem seus nomes em ``snake_case``.


Básico da interface DECOMP
----------------------------

É recomendado que a importação seja feita sempre de forma a utilizar somente os objetos que serão de fato necessários para 
o estudo em questão. Desta forma, não é recomendado importar todo o módulo ``idecomp.decomp`` ou utilizar o `wildcard` ``*``.

A importação recomendada é, por exemplo::

    >>> from idecomp.decomp.relato import Relato

Para a leitura do arquivo `relato.rv0`::

    >>> from idecomp.decomp.relato import Relato
    >>>
    >>> diretorio = "/home/usuario/..."
    >>> rel = Relato.le_arquivo(diretorio, "relato.rv0")
    >>> rel
    <idecomp.decomp.Relato object at 0x000001BC7663B340>

Arquivos
---------

.. toctree::
   :maxdepth: 2

   arquivos/caso
   arquivos/arquivos
   arquivos/dadger
   arquivos/dadgnl
   arquivos/hidr
   arquivos/vazoes
   arquivos/postos
   arquivos/relato
   arquivos/sumario
   arquivos/fcfnw
   arquivos/decomptim
   arquivos/relgnl
   arquivos/inviabunic
   arquivos/dec_avl_evap
   arquivos/dec_cortes_evap
   arquivos/dec_eco_cotajus
   arquivos/dec_eco_discr
   arquivos/dec_oper_gnl
   arquivos/dec_oper_interc
   arquivos/dec_oper_ree
   arquivos/dec_oper_sist
   arquivos/dec_oper_usie
   arquivos/dec_oper_usih
   arquivos/dec_oper_usit
