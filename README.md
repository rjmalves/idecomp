# idecomp

[![tests](https://github.com/rjmalves/idecomp/actions/workflows/main.yml/badge.svg)](https://github.com/rjmalves/idecomp/actions/workflows/main.yml) [![codecov](https://codecov.io/gh/rjmalves/idecomp/branch/main/graph/badge.svg?token=ZSJBGO81JP)](https://codecov.io/gh/rjmalves/idecomp) [![PyPI](https://img.shields.io/pypi/v/idecomp)](https://pypi.org/project/idecomp/) [![Python](https://img.shields.io/pypi/pyversions/idecomp)](https://pypi.org/project/idecomp/) [![Licenca](https://img.shields.io/pypi/l/idecomp)](https://github.com/rjmalves/idecomp/blob/main/LICENSE.md) [![docs](https://img.shields.io/badge/docs-online-blue)](https://rjmalves.github.io/idecomp/)

O `idecomp` é um pacote Python para manipulação dos arquivos
de entrada e saída do programa [DECOMP](http://www.cepel.br/pt_br/produtos/decomp-modelo-de-planejamento-da-operacao-de-sistemas-hidrotermicos-interligados-de-curto-prazo.htm). O DECOMP é desenvolvido pelo [CEPEL](http://www.cepel.br/) e utilizado para os estudos de planejamento e operação do Sistema Interligado Nacional (SIN).

O idecomp oferece:

- Leitura e escrita de arquivos de entrada e saída do DECOMP
- Dados tabulares com pandas DataFrame para análise e pós-processamento
- Mapeamento classe-por-arquivo, com uma classe dedicada para cada arquivo do DECOMP
- Base sólida no framework [cfinterface](https://github.com/rjmalves/cfinterface) para leitura de formatos de colunas fixas
- Tipagem estática completa, compatível com mypy e verificadores de tipo
- Suporte a Python >= 3.10 com API moderna orientada a objetos

## Exemplo Rápido

```python
from idecomp.decomp import Dadger

# Leitura do arquivo dadger.rv0
dadger = Dadger.read("dadger.rv0")

# Acesso aos registros de usinas termelétricas no estágio 1
termicas = dadger.ct(estagio=1)
print(f"Usinas termelétricas no estágio 1: {len(termicas)}")
```

## Instalação

O idecomp é compatível com versões de Python >= 3.10.

Instalação com pip (recomendado):

```
pip install idecomp
```

Instalação alternativa com uv:

```
uv add idecomp
```

## Documentação

Guias, tutoriais e referências de API estão disponíveis no site oficial do pacote:
https://rjmalves.github.io/idecomp/

## Projetos Relacionados

- [inewave](https://github.com/rjmalves/inewave) — pacote equivalente para manipulação dos arquivos do NEWAVE
- [cfinterface](https://github.com/rjmalves/cfinterface) — framework base para leitura e escrita de formatos de colunas fixas

## Contribuindo

Contribuições são bem-vindas! Consulte o [CONTRIBUTING.md](CONTRIBUTING.md) para instruções sobre como configurar o ambiente de desenvolvimento e enviar contribuições.

## Licenca

Distribuído sob a licença MIT. Consulte o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.
