Como contribuir?
=================

.. note::

    Para instruções de configuração do ambiente de desenvolvimento, instalação de dependências
    e fluxo de Pull Requests, consulte o arquivo `CONTRIBUTING.md <https://github.com/rjmalves/idecomp/blob/main/CONTRIBUTING.md>`_
    na raiz do repositório.

O framework `cfinterface`
--------------------------

O módulo *idecomp* é desenvolvido com o framework `cfinterface <https://github.com/rjmalves/cfi>`_, que oferece três modelos de arquivo:

- :obj:`~cfinterface.files.blockfile.BlockFile` — blocos com padrão específico de início/fim
- :obj:`~cfinterface.files.sectionfile.SectionFile` — seções obrigatórias em ordem fixa
- :obj:`~cfinterface.files.registerfile.RegisterFile` — linhas com formato constante

Arquivos podem ser texto ou binário. Exemplos no *idecomp*:

- :obj:`~cfinterface.files.blockfile.BlockFile`: :ref:`relato.rvX <relato>`, :ref:`inviab_unic.rvX <inviabunic>`
- :obj:`~cfinterface.files.sectionfile.SectionFile`: :ref:`caso.dat <caso>`, :ref:`arquivos.rvX <arquivos>`
- :obj:`~cfinterface.files.registerfile.RegisterFile`: :ref:`dadger.rvX <dadger>`, :ref:`dadgnl.rvX <dadgnl>`

.. warning::

    O conteúdo da documentação não deve ser movido para o repositório. Isto é feito
    automaticamente pelos scripts de CI no caso de qualquer modificação no branch `main`.


Diretrizes de modelagem
------------------------

Cada arquivo de entrada do DECOMP é mapeado para uma classe com nome `PascalCase` (ignorando abreviações). Exemplos:

- `arquivos.rvX` → classe :ref:`Arquivos <arquivos>`
- `dadger.rvX` → classe :ref:`Dadger <dadger>`
- `relato.rvX` → classe :ref:`Relato <relato>`

**Dados tabulares**: Propriedades retornam :obj:`~pandas.DataFrame` quando possível, normalizadas para formas tabulares padrão.

**Nomenclatura**: Use `snake_case` para propriedades e colunas, evitando ambiguidades:

- Usinas: `codigo_usina`, `nome_usina`
- Submercados/subsistemas: `codigo_submercado`, `nome_submercado`
- REE: similar aos submercados


Convenções de código
---------------------

Todas as releases passam por testes e controle de qualidade. As convenções são:

1. **PEP8**: Siga as diretrizes de sintaxe usando `ruff <https://docs.astral.sh/ruff/>`_ para formatação (``ruff format``) e lint (``ruff check``).
2. **Tipagem estática**: Todas as variáveis devem ter tipos declarados ou inferíveis. Evite tipos que variam durante a execução.


Procedimentos de teste
-----------------------

Execute antes de cada ``git push``:

.. code-block:: bash

    $ uv run pytest ./tests
    $ uv run mypy ./idecomp
    $ uv run ruff check ./idecomp

Usa-se `pytest <https://pytest.org>`_ para testes, `mypy <http://mypy-lang.org/>`_ para tipagem, e `ruff <https://docs.astral.sh/ruff/>`_ para lint.
