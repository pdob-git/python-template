# simple_python

A simple Python package template with testing, linting, and type checking.

## Installation

```bash
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
