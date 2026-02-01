# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A Cookiecutter template for ML/AI Python projects using `uv` (Astral's package manager). It generates production-ready projects with PyTorch, Hydra config management, CI/CD, and modern Python tooling.

## Common Commands

### Template Development (this repo)
```bash
make bake                # Generate project without prompts (uses defaults)
make bake-with-inputs    # Generate with interactive prompts
make install             # Create virtual environment
make check               # Run ruff, mypy, deptry
make test                # Run pytest with coverage
```

### Generated Project Commands
```bash
make install             # Install venv + pre-commit hooks
make check               # Lint, type-check, dependency check
make test                # Run pytest
uv run python -m <pkg>.train --config configs/<config>.yaml  # Run ML training
```

## Architecture

### Template Structure
- `cookiecutter.json` - Defines template variables (project_name, layout, optional features)
- `{{cookiecutter.project_name}}/` - Template directory that becomes the generated project
- `hooks/pre_gen_project.py` - Validates project naming conventions
- `hooks/post_gen_project.py` - Removes unused files based on user choices, handles src/flat layout

### Key Template Variables
- `layout`: "src" (src/pkg/) or "flat" (pkg/ at root)
- `type_checker`: "mypy" or "ty" (Astral's new type checker)
- Optional features: `include_github_actions`, `mkdocs`, `codecov`, `dockerfile`, `devcontainer`, `publish_to_pypi`, `deptry`

### Generated Project Components
- `train.py` - PyTorch ElasticNet example with Hydra config and Click CLI
- `configs/` - YAML configs for Hydra (seed, training params, data params, device)
- `.github/workflows/` - CI for quality checks, multi-Python testing (3.9-3.13), release publishing

### Build System
- Uses Hatchling with dynamic versioning from git tags
- Dependencies managed via `uv.lock` for reproducibility
- Dev dependencies in `[dependency-groups]` (PEP 735)

## Testing

```bash
# Template generator tests
uv run pytest tests/

# Key test files:
# - tests/test_cookiecutter.py - Tests template generation with various configs
# - tests/test_elasticnet.py - Tests the generated ML training code
```

## Code Quality

Pre-commit hooks run ruff (format + lint). Ruff config: line-length=120, target Python 3.9+.
