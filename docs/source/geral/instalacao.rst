Instalação
============

O *idecomp* requer Python >= 3.10.

Use um ambiente virtual para instalar dependências. Veja a documentação oficial de `venv <https://docs.python.org/3/library/venv.html>`_ para detalhes.


Instalando a versão distribuída oficialmente
---------------------------------------------

É possível instalar a versão distribuída oficialmente com ``pip``:

.. code-block:: bash

    pip install idecomp

Para atualizar para uma versão mais recente, basta adicionar a flag ``--upgrade``:

.. code-block:: bash

    pip install --upgrade idecomp

Para instalar uma versão específica:

.. code-block:: bash

    pip install idecomp==x.y.z

.. tip::

    Se você utiliza o gerenciador de pacotes `uv <https://docs.astral.sh/uv/>`_, é possível adicionar o *idecomp* ao seu projeto com:

    .. code-block:: bash

        uv add idecomp


Instalando a versão de desenvolvimento
----------------------------------------

É possível realizar a instalação da versão de desenvolvimento clonando o repositório e instalando as dependências com `uv <https://docs.astral.sh/uv/>`_:

.. code-block:: bash

    git clone https://github.com/rjmalves/idecomp.git
    cd idecomp
    uv sync --extra dev

Também é possível instalar diretamente a partir do repositório remoto com ``pip``, sem necessidade de clonar:

.. code-block:: bash

    pip install git+https://github.com/rjmalves/idecomp


Verificando a instalação
--------------------------

Após a instalação, verifique se o pacote está disponível:

.. code-block:: bash

    python -c "import idecomp; print(idecomp.__version__)"
