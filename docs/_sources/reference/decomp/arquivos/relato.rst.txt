.. _relato:

=============================================
Relato (relato.rvX)
=============================================

.. currentmodule:: idecomp.decomp.modelos.relato

Visão geral do modelo
======================

As informações de saída do DECOMP, localizadas no arquivo geralmente denominado
relato.rvX, onde X varia de 0 a 4, são armazenadas na classe:

.. autoclass:: Relato
   :members:

Modelos auxiliares
======================

Devido ao grande número de informações existentes no `relato.rvX`, foram definidos modelos
auxiliares para armazenar todas as informações disponíveis.

.. autoclass:: DadosGeraisRelato
   :members:

.. autoclass:: CMORelato
   :members:

Leitura
========
.. currentmodule:: idecomp.decomp.relato

A leitura do arquivo `relato.rvX` é feita através da classe :class:`LeituraRelato`.

.. autoclass:: LeituraRelato
   :members:
