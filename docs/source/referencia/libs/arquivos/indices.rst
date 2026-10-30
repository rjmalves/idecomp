.. _indices:

========================
Índices das LIBS
========================

.. currentmodule:: idecomp.libs.indices

O arquivo de índices das LIBS (geralmente ``indices.csv``, com nome definido pelo
registro ``FA`` do ``dadger``) associa cada identificador de card das LIBS ao
arquivo que contém os seus registros. Suas informações são armazenadas na classe:

.. autoclass:: Indices
   :members:

.. currentmodule:: idecomp.libs.modelos.indices

Cada linha do arquivo é armazenada no modelo:

.. autoclass:: RegistroIndice
   :members:
