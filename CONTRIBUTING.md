# Como Contribuir

Obrigado pelo interesse em contribuir com o _idecomp_! Este guia descreve o fluxo de trabalho recomendado para configurar o ambiente, manter a qualidade do código e enviar contribuições.

## Configuracao do Ambiente

Clone o repositório e instale as dependências de desenvolvimento com `uv`:

```bash
git clone https://github.com/rjmalves/idecomp.git
cd idecomp
uv sync --extra dev
```

Verifique se a instalação está correta executando a suíte de testes:

```bash
uv run pytest ./tests
```

## Hooks de Pre-commit

O projeto utiliza [pre-commit](https://pre-commit.com/) para garantir a qualidade do código antes de cada commit. Instale o `pre-commit` e registre os hooks no repositório:

```bash
pip install pre-commit
pre-commit install
```

Os hooks de `ruff` (lint) e `ruff-format` (formatação) são executados automaticamente em todo commit.

O hook do `mypy` está configurado com `stages: [manual]` porque os stubs de tipo do `cfinterface` estão incompletos e bloqueariam todos os commits se executados automaticamente. Para executar a verificação completa de tipos manualmente:

```bash
pre-commit run --hook-stage manual --all-files
```

Alternativamente, o `mypy` pode ser executado diretamente:

```bash
uv run mypy ./idecomp
```

## Ferramentas de Qualidade

| Ferramenta    | Propósito                       | Comando                        |
| ------------- | ------------------------------- | ------------------------------ |
| `ruff check`  | Linting (PEP8 e outras regras)  | `uv run ruff check ./idecomp`  |
| `ruff format` | Formatação automática do código | `uv run ruff format ./idecomp` |
| `mypy`        | Verificação de tipagem estática | `uv run mypy ./idecomp`        |
| `pytest`      | Execução da suíte de testes     | `uv run pytest ./tests`        |

Para verificar a formatação sem aplicar mudanças:

```bash
uv run ruff format --check ./idecomp
```

## Convencoes de Codigo

- **PEP8**: O estilo do código é verificado pelo `ruff`, seguindo as diretrizes do [PEP8](https://peps.python.org/pep-0008/).
- **Tipagem estatica obrigatoria**: Todas as variáveis e funções devem ter tipos declarados ou inferíveis. Evite tipos ambíguos ou que variam durante a execução.
- **Dados tabulares como DataFrame**: Propriedades das classes que retornam dados tabulares devem retornar `pd.DataFrame`, seguindo as formas normais de dados tabulares sempre que possível.
- **Nomenclatura em snake_case**: Propriedades das classes e colunas dos `pd.DataFrame` devem ser nomeadas em `snake_case`, evitando ambiguidades.

## Executando Testes

Para executar todos os testes:

```bash
uv run pytest ./tests
```

Para executar com relatório de cobertura:

```bash
uv run pytest --cov=idecomp ./tests
```

## Construindo a Documentacao

Instale as dependências de documentação e gere o site localmente:

```bash
uv sync --extra docs
uv run sphinx-build -M html docs/source docs/build
```

O site gerado estará disponível em `docs/build/html/index.html`.

## Fluxo de Pull Requests

1. Faça um fork do repositório e crie um branch descritivo a partir do `main`:
   ```bash
   git checkout -b minha-contribuicao
   ```
2. Implemente as mudanças, seguindo as convenções de código descritas acima.
3. Certifique-se de que os testes passam e que não há erros de lint ou tipagem:
   ```bash
   uv run pytest ./tests
   uv run ruff check ./idecomp
   uv run mypy ./idecomp
   ```
4. Faça commit das mudanças e envie o branch para o seu fork:
   ```bash
   git push origin minha-contribuicao
   ```
5. Abra um Pull Request no repositório principal. O CI executará automaticamente lint, verificação de tipos, testes e build da documentação.
