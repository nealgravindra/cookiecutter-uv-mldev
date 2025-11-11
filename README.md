<p align="center">
  <img width="600" src="https://raw.githubusercontent.com/fpgmaas/cookiecutter-uv/main/docs/static/cookiecutter.svg">
</p style = "margin-bottom: 2rem;">

---

[![Build status](https://img.shields.io/github/actions/workflow/status/fpgmaas/cookiecutter-uv/main.yml?branch=main)](https://github.com/fpgmaas/cookiecutter-uv/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11_%7C_3.12_%7C_3.13-blue?labelColor=grey&color=blue)](https://github.com/fpgmaas/cookiecutter-uv/blob/main/pyproject.toml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://fpgmaas.github.io/cookiecutter-uv/)
[![License](https://img.shields.io/github/license/fpgmaas/cookiecutter-uv)](https://img.shields.io/github/license/fpgmaas/cookiecutter-uv)

This is a modern Cookiecutter template that can be used to initiate a Python project with all the necessary tools for development, testing, and deployment. It supports the following features:

- [uv](https://docs.astral.sh/uv/) for dependency management
- Supports both [src and flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://github.com/charliermarsh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/)/[ty](https://docs.astral.sh/ty/) and [deptry](https://github.com/fpgmaas/deptry/).
- Publishing to [PyPI](https://pypi.org) by creating a new release on GitHub
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Compatibility testing for multiple versions of Python with [tox-uv](https://github.com/tox-dev/tox-uv)
- Containerization with [Docker](https://www.docker.com/) or [Podman](https://podman.io/)
- Development environment with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)

---

<p align="center">
  <a href="https://fpgmaas.github.io/cookiecutter-uv/">Documentation</a> - <a href="https://github.com/fpgmaas/cookiecutter-uv-example">Example</a>
</p>

---

## Quickstart

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/fpgmaas/cookiecutter-uv.git
```

or if you don't have `uv` installed yet:

```bash
pip install cookiecutter
cookiecutter https://github.com/fpgmaas/cookiecutter-uv.git
```

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created. Then navigate into your newly created project directory and follow the instructions in the `README.md` to complete the setup of your project.



## Every day commands

```bash
# one-time setup
uv sync
uv lock --check # verify pyproject vs lock consistency

# run training (Hydra config)
uv run python -m <pkg>.train --config configs/MY_CONFIG.yaml

# quick smoke tests
uv run pytest -q
uv run pytest -q -m gpu # skips if no GPU

# style checks
uv run ruff check .
uv run mypy

# add / remove deps
uv add polars
uv add --dev pytest-benchmark # dev-only dep
uv remove pandas

# strict CI-style execution
uv sync --locked
uv run --locked pytest -q

# build & (optionally) publish a package
uvx --from build pyproject-build --installer uv
uvx twine upload dist/* # add PYPI token

# docs
uv run mkdocs serve
```

## Acknowledgements

This project is based on [Florian Maas\'s](https://github.com/fpgmaas) [cookiecutter-uv package](https://github.com/fpgmaas/cookiecutter-uv), which is in turn partially based on [Audrey
Feldroy\'s](https://github.com/audreyfeldroy)\'s great
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
repository.
