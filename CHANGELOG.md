# v1.7.2

- Atualiza registro AC COTARE do `dadger.rvX` para utilizar notação científica com formatador 'D'

# v1.7.1

- Atualiza requisitos mínimos de dependências: `numpy` reduzida para `>=2.0`

# v1.7.0

- Gestão do projeto através de arquivo `pyproject.toml` em substituição ao par `setup.py` + `requirements.txt`.
- Correção no processamento do registro de alteração cadastral de potência efetiva (AC POTEFE) do arquivo `dadger.rvX`.
- Correção na expansão para DataFrame dos registros de duração dos patamares (DP) do arquivo `dadger.rvX`.
- Correção na leitura da versão do DECOMP nos arquivos de saída.
- Correção na leitura das probabilidades em casos deterministicos.
- Atualizado o suporte ao registro de intercâmbio (IA) do arquivo `dadger.rvX`.
- Suporte à leitura do arquivo de saída `dec_eco_evap.csv`, `dec_eco_qlat.csv`, `dec_estatevap.csv`, `dec_estatfpha.rvX`, `dec_oper_evap.csv`, `dec_oper_rhesoft.csv`, `eco_fpha_.rvX`.
- Dependência da cfinterface atualizada para v1.8.0.
- Descontinuado o uso do `pylama` como linter para garantir padrões PEP de código devido à falta de suporte em Python >= 3.12. Adoção do [ruff](https://github.com/astral-sh/ruff) em substituição.

# v1.6.0

- Suporte à leitura do arquivo de saída `avl_turb_max.csv`.
- Suporte à leitura dos arquivos de saída `oper_disp_usih.csv`, `oper_disp_usih_ree.csv` e`oper_disp_subm.csv`.

# v1.5.0

- Dependência da cfinterface atualizada para v1.7.1.
- Suporte à leitura do arquivo de saída `mapcut.rvX` [#35](https://github.com/rjmalves/idecomp/issues/35).
- Suporte à leitura e escrita do arquivo de saída `cortdeco.rvX`[#35](https://github.com/rjmalves/idecomp/issues/35).
- Simplifica a estrutura de armazenamento dos dados do arquivo `vazoes.rvX` permitindo alterações no número de cenários [#33](https://github.com/rjmalves/idecomp/issues/33).

# v1.4.0

- Dependência da cfinterface atualizada para v1.7.0.
- Uso de slots nas definições de componentes..=
- Novos dados em formatos das LIBS: restrições elétricas especiais.
- Adicionado suporte ao registro DA (desvios de água) do arquivo dadger.

# v1.3.0

- Suporte à leitura do arquivo de saída `avl_cortesfpha_dec`.
- Padronização da nomenclatura da unidade de decisão do modelo como "estágio".
- Atualizado o número máximo de cenários lidos no arquivo relato para o máximo suportado pelo modelo.

# v1.2.0

- Suporte à leitura do arquivo de saída `dec_fcf_cortes_00N.rvX`.
- Suporte à leitura do arquivo de saída `oper_desvio_fpha.csv`.

# v1.1.1

- Fix na leitura do arquivo `vazoes.rvX` quando gerado por versões antigas do GEVAZP, onde o número de postos não fazia parte dos dados do arquivo.

# v1.1.0

- Atualizada a modelagem dos registros do dadger sensíveis ao número de estágios para o máximo suportado pelo modelo (TI, VE).
- Atualizada a modelagem com propriedades para registros do dadger de manutenção e disponibilidade (MP, MT, FD).
- Atualizada na classe `Dadger` as propriedades para acesso aos registros atualizados (MP, MT, FD).

# v1.0.1

- Fix nas colunas o DataFrame de Volume Útil de Reservatórios do arquivo Relato

# v1.0.0

- Primeira major release
- Suporte à leitura e escrita todos os arquivos de entrada utilizados oficialmente no modelo DECOMP
- Suporte aos registros utilizados pelo polinômio de jusante em LIBS
- Adicionados registros VL, VA e VU ao dadger
- Registros do dadger com número de campos variáveis por patamar agora suportam o máximo do modelo DECOMP (5)
- Métodos le_arquivo e escreve_arquivo deprecados
