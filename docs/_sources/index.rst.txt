.. idecomp documentation master file, created by
   sphinx-quickstart on Mon Jan 18 09:33:19 2021.

Interface de Programação para o DECOMP
=======================================

**Versão:** |release|

**Data:** |today|

O *idecomp* é um pacote Python para manipulação dos arquivos
de entrada e saída do programa `DECOMP <http://www.cepel.br/pt_br/produtos/decomp-modelo-de-planejamento-da-operacao-de-sistemas-hidrotermicos-interligados-de-curto-prazo.htm>`_,
desenvolvido pelo `CEPEL <http://www.cepel.br/>`_ e utilizado para os estudos de planejamento e operação do Sistema Interligado Nacional (SIN).

O idecomp oferece:

- Meios para leitura dos arquivos de entrada e saída do DECOMP
- Armazenamento e processamento de dados otimizados com o uso de `NumPy <https://numpy.org/>`_
- Dados estruturados em modelos com o uso do paradigma de orientação a objetos (OOP)
- Utilidades de escritas dos arquivos de entrada do DECOMP para elaboração automatizada de estudos

Com *idecomp* é possível ler os arquivos de texto, característicos do DECOMP, e salvar as informações em `pickle <https://docs.python.org/3/library/pickle.html>`_, 
para poupar processamento futuro e reduzir o tempo de execução.


Documentação
=============

.. toctree::
   :maxdepth: 3

   ./install.rst
   ./tutorial.rst
   ./reference.rst


Índices e Tabelas
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
