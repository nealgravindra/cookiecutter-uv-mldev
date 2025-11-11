import json
import os
import subprocess
import sys
from loguru import logger
import pytest
from pathlib import Path

from importlib import resources


# @pytest.mark.gpu
def test_elasticnet():
    with resources.path("{{cookiecutter.package_name}}", "configs/test_elasticnet.yaml") as CONFIG:
        subprocess.check_call(
            [
                sys.executable,
                "-m",
                "{{cookiecutter.package_name}}.train",
                "--config",
                str(CONFIG),
            ]
        )
    with open("artifacts/metrics.json") as f:
        m = json.load(f)
        logger.info(f"Metrics: {m}")
    assert isinstance(m["final_loss"], float)
