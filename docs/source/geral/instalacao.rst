Instalação
============

O *idecomp* é compatível com versões de Python >= 3.8. 

Em posse de uma instalação local de Python, é recomendado que se use um ambiente virtual para instalação de módulos de terceiros, sendo que o *idecomp* não é uma exceção.
Para mais detalhes sobre o uso de ambientes virtuais, recomenda-se a leitura do recurso oficial de Python para ambientes virtuais: `venv <https://docs.python.org/3/library/venv.html>`_.

Antes de prosseguir, é necessário verificar se está instalada a última versão do ``pip``, o gerenciador de pacotes de Python. Isso pode ser feito com, por exemplo::

    $ python -m pip install ---upgrade pip


Instalando a versão distribuída oficialmente
---------------------------------------------

É possível instalar a versão distribuída oficialmente com ``pip``::

    $ pip install idecomp

Para atualizar para uma versão mais recente, basta adicionar a flag ``--upgrade``::

    $ pip install --upgrade idecomp

Para instalar uma versão específica::

    $ pip install --upgrade idecomp==x.y.z

Instalando a versão de desenvolvimento
---------------------------------------

É possível realizar a instalação desta versão fazendo o uso do `Git <https://git-scm.com/>`_. Para instalar a versão de desenvolvimento, é necessário
primeiramente desinstalar a versão instalada (se houver), com::

    $ pip uninstall idecomp

Em seguida, basta fazer::

    $ pip install git+https://github.com/rjmalves/idecomp

Também é possível selecionar um branch ou release específicos::

    $ pip install git+https://github.com/rjmalves/idecomp@v1.0.0
