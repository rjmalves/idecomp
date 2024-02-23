Tutorial
============

O *idecomp* provê uma interface semelhante para todos os arquivos do modelo DECOMP. Para os arquivos de entrada, são implementadas as capacidades
de leitura e escrita, permitindo uma geração automática de arquivos. Para os arquivos de saída, é implementada
somente a capacidade de leitura, de modo a permitir análise facilitada de resultados.

A leitura dos arquivos é sempre implementada a partir do método `read` da respectiva classe, enquanto que a escrita
dos arquivos é implementada pelo método `write` da instância em questão, quando for suportada.

Um exemplo é o processamento do arquivo de vazões previstas e geradas :ref:`vazoes.rvX <vazoes>`. Sendo um arquivo de entrada,
é permitido realizar a leitura e a escrita deste arquivo, modificando alguma informação de entrada caso
seja desejado pelo usuário. Por exemplo, pode-se fazer uma sensibilidade de elevar em 10% todos os valores
de vazões previstas:


.. code-block:: python

    from idecomp.decomp import Vazoes
    arq_vazoes = Vazoes.read("./vazoes.rv0")
    arq_vazoes.previsoes

       estagio      1    2    3    4    5      6      7  ...  313  314  315  316  317  318  319  320
    0        1   70.4  0.0  0.0  0.0  0.0  382.8   68.2  ...  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
    1        2  101.2  0.0  0.0  0.0  0.0  573.1   97.9  ...  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
    2        3  113.3  0.0  0.0  0.0  0.0  590.7  107.8  ...  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
    3        4  146.3  0.0  0.0  0.0  0.0  755.7  128.7  ...  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
    4        5  170.5  0.0  0.0  0.0  0.0  630.3  129.8  ...  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0

    [5 rows x 321 columns]

    df = arq_vazoes.previsoes
    df.iloc[:, 1:] *= 1.1
    arq_vazoes.previsoes = df
    arq_vazoes.previsoes

       estagio      1    2    3    4    5      6      7  ...  313  314  315  316  317  318  319  320
    0        1   70.4  0.0  0.0  0.0  0.0  382.8   68.2  ...  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
    1        2  101.2  0.0  0.0  0.0  0.0  573.1   97.9  ...  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
    2        3  113.3  0.0  0.0  0.0  0.0  590.7  107.8  ...  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
    3        4  146.3  0.0  0.0  0.0  0.0  755.7  128.7  ...  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
    4        5  170.5  0.0  0.0  0.0  0.0  630.3  129.8  ...  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0

    [5 rows x 321 columns]

    arq_vazoes.write("./vazoes.rv0")


Se tratando dos arquivos de saída, não existe implementação para o método `write`, mas é possível realizar
a leitura normalmente, e acessar todas as propriedades encontradas. Para o :ref:`relato.rvX <relato>`, por exemplo:

.. code-block:: python

    from idecomp.decomp import Relato
    arq_relato = Relato.read("./relato.rv0")
    arq_relato.convergencia.head(10)

        Iteração        Zinf  ...  Tot. Inviab (m3/s)  Tot. Inviab (Hm3)
    0          1    450767.9  ...                14.0                0.0
    1          2    450767.9  ...               481.0                0.0
    2          3    450767.9  ...               188.0                0.0
    3          4  41454619.2  ...                 0.0                0.0
    4          5  85359403.8  ...                 0.0                0.0
    5          6  85359508.8  ...                10.0                0.0
    6          7  85360125.8  ...                 0.0                0.0
    7          8  85361257.2  ...                 0.0                0.0
    8          9  85366484.0  ...                 0.0                0.0
    9         10  85366570.3  ...                 0.0                0.0
    10        11  85366634.8  ...                 0.0                0.0

    [48 rows x 11 columns]



Alguns arquivos do modelo DECOMP podem sofrer alterações de sintaxe conforme são feitas atualizações no modelo.
Desta forma, poderia ser necessário criar mais de uma classe para dar suporte ao mesmo arquivo. Todavia, o framework
`cfinterface <https://github.com/rjmalves/cfi>`_ possui uma modelagem para dar suporte a mais de uma
versão do mesmo arquivo fazendo uso do método `set_version` de cada uma das classes.
Entretanto, até o momento o uso deste método não foi necessário para nenhum arquivo do modelo DECOMP, visto
que as implementações feitas pelo desenvolvedor tendem a ser retrocompatíveis.
