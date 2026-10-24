# Changelog

Todas as mudancas relevantes deste projeto serao documentadas neste arquivo.

O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

## [Nao Publicado]

### Adicionado

- Registros `PEEGeracaoPeriodoPatamar` e `PEEGeracaoPeriodoPatamarComPeriodoFinal` e método `pee_ger_per_pat` da classe `Renovaveis`, para o card `PEE-GER-PER-PAT` do arquivo de renováveis, com a geração determinística dos parques eólicos equivalentes, sem a dimensão de cenários do `PEE-GER-PER-PAT-CEN`. Os layouts de período único e de intervalo de períodos são lidos, e `df=True` combina os dois [#96](https://github.com/rjmalves/idecomp/pull/96) (@jhuliamacedo).

### Corrigido

- Valores com mais de 8 caracteres eram cortados na leitura da geração do card `PEE-GER-PER-PAT-CEN` e da potência do `PEE-POT-INST-PER`, no arquivo de renováveis, e do nível de montante do `HIDRELETRICA-CURVAJUSANTE`, na classe `UsinasHidreletricas` (`17699.689` era lido como `17699.68`). A geração do `PEE-GER-PER-PAT-CEN` também passa a ser escrita com 6 casas decimais, em vez de 4 [#96](https://github.com/rjmalves/idecomp/pull/96) (@jhuliamacedo).
- Os campos `Fw.d` e `Ew.d` com `d > 0` no manual do DECOMP passam a ser lidos com o ponto decimal implícito do Fortran, como o DECOMP os lê: em `F10.2`, `299` é lido como `2.99`, e não `299.0`, enquanto `299.` e `296.52` continuam lidos como escritos. São os custos dos registros `CT`, `CD`, `CI` e `CE` do `dadger` e `TG` do `dadgnl`, as tolerâncias do `TS` e os coeficientes do `AC` `COTVOL`, `COTARE` e `COTVAZ`, que passam a ser sempre escritos com ponto decimal (um valor que não caiba no campo com o ponto gera erro).
- O campo 5 do registro `TS` era lido nas colunas da tolerância secundária, e a escrita do registro sobrescrevia essa tolerância e descartava o campo 5.
- Os coeficientes do `AC` `COTVOL` e `COTVAZ` eram escritos com 3 casas decimais, o que zerava os coeficientes pequenos (`-1.234567E-06` era escrito como `-0.000`). Passam a ser escritos em notação científica, como os do `COTARE`.

## [1.15.1] - 2026-10-22

### Corrigido

- Em decks com mais de um estágio estocástico, como os mensais, a leitura do `vazoes.rvX` dimensionava errado os registros de cenários gerados, e os registros seguintes eram lidos deslocados ou a leitura falhava. A tabela `probabilidades` da classe `Vazoes` também supunha que apenas o último estágio era estocástico e passa a atribuir o `estagio` de cada nó pelas aberturas de cada estágio [#95](https://github.com/rjmalves/idecomp/pull/95) (@renanmaciel-84).

## [1.15.0] - 2026-10-19

### Adicionado

- Método `ez` na classe `Dadger` para o registro `EZ`, o percentual do volume útil de cada usina de um subsistema acoplado hidraulicamente considerado na energia armazenada do subsistema de jusante, com filtros por `codigo_usina` e `volume` e suporte a `df=True`.

### Corrigido

- A documentação do registro `EZ` descrevia o campo `volume` como percentual do volume máximo, e não do volume útil, como no manual do DECOMP. O nome da propriedade foi mantido.

## [1.14.2] - 2026-08-11

### Corrigido

- O card `PEE-GER-PER-PAT-CEN` do `renovaveis.csv` tem dois layouts, de período único (5 campos) e de intervalo de períodos (6 campos, com `PerFin`), e a correção da 1.14.1 deixou de ler o segundo. Os dois passam a ser lidos, pelos registros `PEEGeracaoPeriodoPatamarCenario` e `PEEGeracaoPeriodoPatamarCenarioComPeriodoFinal`, e o método `pee_ger_per_pat_cen` da classe `Renovaveis` os combina, com a coluna `estagio_final` quando há o layout de intervalo.

## [1.14.1] - 2026-08-11

### Corrigido

- O registro `PEE-GER-PER-PAT-CEN` (`PEEGeracaoPeriodoPatamarCenario`) era declarado com um campo `estagio_final` que o card não tem, e a geração era lida na coluna `cenario`, com `geracao` sempre `None`. O registro passa a ter 5 campos, e o método `pee_ger_per_pat_cen` da classe `Renovaveis` perde o parâmetro `estagio_final` e tem `estagio_inicial` renomeado para `estagio`.

## [1.14.0] - 2026-08-10

### Adicionado

- Cards `EXPRESSAO-ELETRICA`, `RESTRICAO-ELETRICA-INEQUACAO` e `RESTRICAO-ELETRICA-INEQUACAO-PERIODO-PATAMAR` da funcionalidade `RESTRICAO-ELETRICA-ESPECIAL` das LIBS, com os registros `RegistroExpressaoEletrica`, `RegistroRestricaoEletricaInequacao` e `RegistroRestricaoEletricaInequacaoPeriodoPatamar` e os métodos `expressao_eletrica`, `restricao_eletrica_inequacao` e `restricao_eletrica_inequacao_periodo_patamar` da classe `Restricoes`, com filtros e suporte a `df=True`. As fórmulas são retornadas como texto, sem interpretação.

### Corrigido

- O método `re_trat_viol_per` da classe `Restricoes` retornava registros `RegistroReTratViol` em vez de `RegistroReTratViolPer` e ignorava os filtros `estagio_inicio` e `estagio_fim`.

## [1.13.0] - 2026-07-31

### Adicionado

- Propriedades nomeadas para os registros `CI` e `CE` do `dadger`, como no registro `CT` (`numero_contrato`, `codigo_submercado`, `nome_contrato`, `estagio`, `limite_inferior`, `limite_superior`, `custo` e `fator_perdas`), e métodos `ci` e `ce` na classe `Dadger`, com filtros e suporte a `df=True`. O último campo do registro, antes sem nome, é o fator de perdas.

## [1.12.0] - 2026-07-24

### Adicionado

- Leitor do arquivo `mlt.dat` (classe `Mlt`), com as médias de longo termo (MLT) de cada posto por mês, em m³/s, na propriedade `valores`.
- Leitor do arquivo `renovaveis.csv` (classe `Renovaveis`), com os registros dos parques eólicos equivalentes (`PEECadastro`, `PEESubmercado`, `PEEConfiguracaoPeriodo`, `PEEPotenciaInstaladaPeriodo` e `PEEGeracaoPeriodoPatamarCenario`).

### Alterado

- Versão mínima de `cfinterface` elevada para `1.10.1`.

### Corrigido

- O registro `IA` do `dadger` não expunha os limites de intercâmbio por patamar, que `ia(df=True)` omitia. Adicionadas as propriedades `limite_de_para` e `limite_para_de`.
- O método `ue` do `Dadger` retornava os dados do registro `UH` em vez do registro `UE`.
- Os limites de intercâmbio do registro `IA` eram escritos sem casas decimais, o que arredondava valores fracionários. Passam a ser escritos com 2 casas decimais.

## [1.11.0] - 2026-06-09

### Adicionado

- Suporte ao formato do `hidr.dat` com os coeficientes dos polinômios cota-volume e cota-área em precisão dupla (registros de 832 bytes), pelo registro `RegistroUHEHidrF64`. A classe `Hidr` detecta o formato pelo tamanho do arquivo, e ele pode ser forçado com `version="f32"` ou `version="f64"`.
- Propriedade `tamanho_registro` e método `converte_tamanho_registro` na classe `Hidr`, para consultar e converter o formato.

## [1.10.0] - 2026-04-13

### Corrigido

- Precisão decimal insuficiente na escrita de campos de registros do `dadger`, que corrompia valores numa leitura seguida de escrita:
  - `PQ` (geração): de 0 para 4 casas decimais, no modo compacto; valores pequenos como `0.0563` eram escritos como `0`.
  - `LU` (limites): de 1 para 2 casas decimais (`860.55` era escrito como `860.5`).
  - `TX`, `VI`, `CI`, `CE`, `FP` e `AR`: de 0 para 3 casas decimais, como nos registros `FD` e `MP`.

### Modificado

- Versão mínima de `cfinterface` elevada para `1.10.0`, que traz o modo `compact` do `FloatField` (sem o zero à esquerda para `|valor| < 1`) e corrige a duplicação de registros no fallback de codificação da leitura.

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

[Nao Publicado]: https://github.com/rjmalves/idecomp/compare/v1.15.1...HEAD
[1.15.1]: https://github.com/rjmalves/idecomp/compare/v1.15.0...v1.15.1
[1.15.0]: https://github.com/rjmalves/idecomp/compare/v1.14.2...v1.15.0
[1.14.2]: https://github.com/rjmalves/idecomp/compare/v1.14.1...v1.14.2
[1.14.1]: https://github.com/rjmalves/idecomp/compare/v1.14.0...v1.14.1
[1.14.0]: https://github.com/rjmalves/idecomp/compare/v1.13.0...v1.14.0
[1.13.0]: https://github.com/rjmalves/idecomp/compare/v1.12.0...v1.13.0
[1.12.0]: https://github.com/rjmalves/idecomp/compare/v1.11.0...v1.12.0
[1.11.0]: https://github.com/rjmalves/idecomp/compare/v1.10.0...v1.11.0
[1.10.0]: https://github.com/rjmalves/idecomp/compare/v1.9.0...v1.10.0
[1.9.0]: https://github.com/rjmalves/idecomp/compare/v1.8.2...v1.9.0
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
