# Python Template

A simple Python package template with testing, linting, and type checking.

## Project generation

```bash
# Clone template
git clone {template_repo}

# Create python environment
python -m venv .venv
source ./.venv/bin/activate  

# Install cookie_cutter
pip install cookiecutter

# Generate project
cookiecutter {cloned-folder}/python-template
```

## Installation

```bash
# Navigate to project
cd {project_folder}

# Install requirements
pip install -r requirements-dev.txt
pip install -e .
```

## Usage

```bash
simple_python
# Output: Hello, World!
```

## Development

### Run tests

```bash
pytest
```

### Lint and format

```bash
ruff check --fix .
ruff format .
```

### Type check

```bash
mypy src/
```

### Install pre-commit hooks

```bash
pre-commit install
```
