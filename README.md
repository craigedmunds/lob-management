# Repository Organization Tool

A Python tool using Invoke for repository management tasks.

## Installation

```bash
poetry install
```

## Usage

```bash
# Validate repository
poetry run invoke validate

# Argo CMP
poetry run invoke argo-cmp

# Generate code or config
poetry run invoke generate
```

## Development

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest
```
