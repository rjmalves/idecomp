# Changelog

Todas as mudancas relevantes deste projeto serao documentadas neste arquivo.

O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

## [Nao Publicado]

## [1.9.0] - 2026-03-10

### Adicionado

- Documentação de arquitetura, FAQ e guia de desempenho (pt_BR)
- Blocos autosummary na referência de API para 41 classes do DECOMP e 2 de libs
- Arquivo `CONTRIBUTING.md` com instruções de desenvolvimento
- Workflow de release com publicação automática no PyPI via tag
- Hooks de pre-commit com ruff e mypy
- Suporte a Python 3.13 e 3.14 na matriz de CI

### Modificado

- Dependência cfinterface atualizada para `>=1.9.0`
- Dependência pandas atualizada para `>=3.0.0`
- Dependência numpy atualizada para `>=2.2.1`
- Versão mínima de Python alterada de 3.10 para 3.11
- Tipagem estrita mypy em todos os 97 arquivos fonte
- Tema da documentação migrado de RTD para Furo com suporte a dark mode
- CI reestruturado em 4 jobs paralelos (lint, typecheck, test, docs)
- Deploy da documentação migrado para GitHub Pages oficial
- README expandido com badges, exemplos e seções de contribuição
- CHANGELOG reformatado para o padrão Keep a Changelog

### Removido

- Suporte a Python 3.10

## [1.8.2] - 2026-02-04

### Modificado

- Dependência cfinterface fixada em `>=1.8,<=1.8.3` para compatibilidade com a versão atual

## [1.8.1] - 2026-02-04

### Modificado

- Aumento nas capacidade máximas de estágios (25) e subsistemas (15) para processamento

## [1.8.0] - 2026-02-02

### Modificado

- Atualiza processamento do `postos.dat` para suporte a python `>=3.13` e pandas `>=3.0.0`

## [1.7.3] - 2025-12-29

### Modificado

- Atualiza registro AC COTARE do `dadger.rvX` com maior precisão de dígitos significativos

## [1.7.2] - 2025-12-29

### Modificado

- Atualiza registro AC COTARE do `dadger.rvX` para utilizar notação científica com formatador 'D'

## [1.7.1] - 2025-01-22

### Modificado

- Atualiza requisitos mínimos de dependências: `numpy` reduzida para `>=2.0`

## [1.7.0] - 2025-01-10

### Adicionado

- Suporte à leitura do arquivo de saída `dec_eco_evap.csv`, `dec_eco_qlat.csv`, `dec_estatevap.csv`, `dec_estatfpha.rvX`, `dec_oper_evap.csv`, `dec_oper_rhesoft.csv`, `eco_fpha_.rvX`.

### Corrigido

- Correção no processamento do registro de alteração cadastral de potência efetiva (AC POTEFE) do arquivo `dadger.rvX`.
- Correção na expansão para DataFrame dos registros de duração dos patamares (DP) do arquivo `dadger.rvX`.
- Correção na leitura da versão do DECOMP nos arquivos de saída.
- Correção na leitura das probabilidades em casos deterministicos.

### Modificado

- Gestão do projeto através de arquivo `pyproject.toml` em substituição ao par `setup.py` + `requirements.txt`.
- Atualizado o suporte ao registro de intercâmbio (IA) do arquivo `dadger.rvX`.
- Dependência da cfinterface atualizada para v1.8.0.
- Descontinuado o uso do `pylama` como linter para garantir padrões PEP de código devido à falta de suporte em Python >= 3.12. Adoção do [ruff](https://github.com/astral-sh/ruff) em substituição.

## [1.6.0] - 2024-10-04

### Adicionado

- Suporte à leitura do arquivo de saída `avl_turb_max.csv`.
- Suporte à leitura dos arquivos de saída `oper_disp_usih.csv`, `oper_disp_usih_ree.csv` e`oper_disp_subm.csv`.

## [1.5.0] - 2024-08-16

### Adicionado

- Suporte à leitura do arquivo de saída `mapcut.rvX` [#35](https://github.com/rjmalves/idecomp/issues/35).
- Suporte à leitura e escrita do arquivo de saída `cortdeco.rvX`[#35](https://github.com/rjmalves/idecomp/issues/35).

### Modificado

- Dependência da cfinterface atualizada para v1.7.1.
- Simplifica a estrutura de armazenamento dos dados do arquivo `vazoes.rvX` permitindo alterações no número de cenários [#33](https://github.com/rjmalves/idecomp/issues/33).

## [1.4.0] - 2024-04-22

### Adicionado

- Novos dados em formatos das LIBS: restrições elétricas especiais.
- Adicionado suporte ao registro DA (desvios de água) do arquivo dadger.

### Modificado

- Dependência da cfinterface atualizada para v1.7.0.
- Uso de slots nas definições de componentes.

## [1.3.0] - 2024-02-23

### Adicionado

- Suporte à leitura do arquivo de saída `avl_cortesfpha_dec`.

### Modificado

- Padronização da nomenclatura da unidade de decisão do modelo como "estágio".
- Atualizado o número máximo de cenários lidos no arquivo relato para o máximo suportado pelo modelo.

## [1.2.0] - 2024-02-05

### Adicionado

- Suporte à leitura do arquivo de saída `dec_fcf_cortes_00N.rvX`.
- Suporte à leitura do arquivo de saída `oper_desvio_fpha.csv`.

## [1.1.1] - 2024-01-04

### Corrigido

- Fix na leitura do arquivo `vazoes.rvX` quando gerado por versões antigas do GEVAZP, onde o número de postos não fazia parte dos dados do arquivo.

## [1.1.0] - 2023-12-29

### Modificado

- Atualizada a modelagem dos registros do dadger sensíveis ao número de estágios para o máximo suportado pelo modelo (TI, VE).
- Atualizada a modelagem com propriedades para registros do dadger de manutenção e disponibilidade (MP, MT, FD).
- Atualizada na classe `Dadger` as propriedades para acesso aos registros atualizados (MP, MT, FD).

## [1.0.1] - 2023-12-21

### Corrigido

- Fix nas colunas o DataFrame de Volume Útil de Reservatórios do arquivo Relato

## [1.0.0] - 2023-12-21

### Adicionado

- Primeira major release
- Suporte à leitura e escrita todos os arquivos de entrada utilizados oficialmente no modelo DECOMP
- Suporte aos registros utilizados pelo polinômio de jusante em LIBS
- Adicionados registros VL, VA e VU ao dadger
- Registros do dadger com número de campos variáveis por patamar agora suportam o máximo do modelo DECOMP (5)

### Depreciado

- Métodos le_arquivo e escreve_arquivo deprecados

[Nao Publicado]: https://github.com/rjmalves/idecomp/compare/v1.8.2...HEAD
[1.8.2]: https://github.com/rjmalves/idecomp/compare/v1.8.1...v1.8.2
[1.8.1]: https://github.com/rjmalves/idecomp/compare/v1.8.0...v1.8.1
[1.8.0]: https://github.com/rjmalves/idecomp/compare/v1.7.3...v1.8.0
[1.7.3]: https://github.com/rjmalves/idecomp/compare/v1.7.2...v1.7.3
[1.7.2]: https://github.com/rjmalves/idecomp/compare/v1.7.1...v1.7.2
[1.7.1]: https://github.com/rjmalves/idecomp/compare/v1.7.0...v1.7.1
[1.7.0]: https://github.com/rjmalves/idecomp/compare/v1.6.0...v1.7.0
[1.6.0]: https://github.com/rjmalves/idecomp/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.com/rjmalves/idecomp/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/rjmalves/idecomp/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/rjmalves/idecomp/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/rjmalves/idecomp/compare/v1.1.1...v1.2.0
[1.1.1]: https://github.com/rjmalves/idecomp/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/rjmalves/idecomp/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/rjmalves/idecomp/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/rjmalves/idecomp/releases/tag/v1.0.0
