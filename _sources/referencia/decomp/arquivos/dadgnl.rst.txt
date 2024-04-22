.. _dadgnl:

=============================================
Dados de Térmicas GNL (dadgnl.rvX)
=============================================

.. currentmodule:: idecomp.decomp.dadgnl

As informações de entrada das térmicas de despacho antecipado (GNL) do DECOMP, localizadas no arquivo geralmente denominado
dadgnl.rvX, onde X varia de 0 a 4, são armazenadas na classe:

.. autoclass:: DadGNL
   :members:


.. currentmodule:: idecomp.decomp.modelos.dadgnl


As informações existentes em cada um dos registros são armazenadas em modelos próprios
para cada um. Os registros suportados até o momento são os utilizados nos estudos oficiais
de operação:

.. autoclass:: TG
   :members:

.. autoclass:: GS
   :members:

.. autoclass:: NL
   :members:

.. autoclass:: GL
   :members:
