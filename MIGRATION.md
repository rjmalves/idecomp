# Guia de Migração: idecomp v1.8.1 -> v1.9.0

## Requisitos

- Python >= 3.10
- cfinterface >= 1.9.0
- numpy >= 2.0
- pandas >= 2.2

## Mudanças na API pública

A API pública do idecomp (classes em `idecomp.decomp` e `idecomp.libs`) é
**totalmente retrocompatível**. Nenhuma assinatura de método acessível ao
usuário foi alterada. Todas as chamadas `read()` e `write()` existentes
continuam funcionando sem modificação.

As mudanças descritas abaixo são internas aos handlers e não afetam o
código de projetos consumidores.

## Mudanças internas relevantes

### StorageType enum

Os 5 handlers binários (`Hidr`, `Postos`, `Vazoes`, `Cortdeco`, `Mapcut`)
agora utilizam `StorageType.BINARY` (enum da cfinterface v1.9.0) em vez
do literal de string `"BINARY"`. Esta mudança é transparente para
consumidores — o atributo `STORAGE` é usado internamente pelo framework
cfinterface para selecionar o modo de I/O.

### mypy strict mode

Todos os módulos de produção (`idecomp.decomp`, `idecomp.decomp.modelos`,
`idecomp.libs`, `idecomp.libs.modelos`, `idecomp.config`) passam sob
`mypy --strict` com zero erros. Anotações de tipo foram adicionadas a
todas as funções e métodos, incluindo `IO[Any]` para parâmetros de
arquivo, `Optional[Any]` para parâmetros de inicialização e `-> None`
em todos os setters de propriedade.

### PEP 562 lazy imports

O `idecomp/decomp/__init__.py` agora utiliza o padrão de importação
lazy via PEP 562 (`__getattr__` + `__dir__`). Os 41 handlers são
importados sob demanda no primeiro acesso, reduzindo o tempo de
importação inicial do pacote. Todos os padrões de importação existentes
continuam funcionando:

- `from idecomp.decomp import Dadger`
- `import idecomp.decomp; idecomp.decomp.Dadger`
- `from idecomp.decomp import *`

### Otimização de concatenação de DataFrames

Os métodos `__concatena_blocos` em `Relato`, `Custos` e `Relgnl`, além
das propriedades `dados_tempo_viagem`, `dados_gnl` e `dados_custos` em
`SecaoDadosMapcut`, foram otimizados para coletar DataFrames em uma lista
e chamar `pd.concat` uma única vez, eliminando o padrão O(n²) de
concatenação em loop.

## Novos recursos de desenvolvimento

### pytest-xdist

O pacote `pytest-xdist` foi adicionado como dependência de desenvolvimento.
Para executar os testes em paralelo:

```bash
pytest -n auto
```

A execução paralela é opt-in — o modo sequencial (`pytest`) continua
funcionando normalmente.

### Suite de benchmarks

Uma suite de benchmarks foi adicionada no diretório `benchmarks/` para
medir o desempenho de leitura dos handlers e o tempo de importação do
módulo. Para executar:

```bash
python benchmarks/run_benchmarks.py
```

Os resultados são escritos em `benchmarks/benchmark_results.md`.

## Ações necessárias para consumidores

1. Atualize a dependência cfinterface para `>= 1.9.0` no seu projeto.
2. Nenhuma alteração de código é necessária se o seu projeto utiliza
   apenas a API pública do idecomp (`read()`, `write()`, propriedades
   dos handlers).
