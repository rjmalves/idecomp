# idecomp

[![tests](https://github.com/rjmalves/idecomp/actions/workflows/main.yml/badge.svg)](https://github.com/rjmalves/idecomp/actions/workflows/main.yml)  
[![codecov](https://codecov.io/gh/rjmalves/idecomp/branch/main/graph/badge.svg?token=ZSJBGO81JP)](https://codecov.io/gh/rjmalves/idecomp)

O *idecomp* é um pacote Python para manipulação dos arquivos
de entrada e saída do programa [DECOMP](http://www.cepel.br/pt_br/produtos/decomp-modelo-de-planejamento-da-operacao-de-sistemas-hidrotermicos-interligados-de-curto-prazo.htm),
desenvolvido pelo [CEPEL](http://www.cepel.br/) e utilizado para os estudos de planejamento e operação do Sistema Interligado Nacional (SIN).

O idecomp oferece:

- Meios para leitura dos arquivos de entrada e saída do DECOMP
- Armazenamento e processamento de dados otimizados com o uso de [NumPy](https://numpy.org/)
- Dados estruturados em modelos com o uso do paradigma de orientação a objetos (OOP)
- Utilidades de escritas dos arquivos de entrada do DECOMP para elaboração automatizada de estudos

Com *idecomp* é possível ler os arquivos de texto, característicos do DECOMP, e salvar as informações em [pickle](https://docs.python.org/3/library/pickle.html>), 
para poupar processamento futuro e reduzir o tempo de execução.

## Instalação

O idecomp é compatível com versões de Python >= 3.5. A única dependência formal é o módulo NumPy, que deve sempre ser mantido na versão mais atualizada para a distribuição de Python instalada.

Em posse de uma instalação local de Python, é recomendado que se use um ambiente virtual para instalação de módulos de terceiros, sendo que o idecomp não é uma exceção. Para mais detalhes sobre o uso de ambientes virtuais, recomenda-se a leitura do recurso oficial de Python para ambientes virtuais: [venv](https://docs.python.org/3/library/venv.html).

```
python -m pip install idecomp
```

## Documentação

Guias, tutoriais e as referências podem ser encontrados no site oficial do pacote: https://rjmalves.github.io/idecomp
