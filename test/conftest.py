from pathlib import Path

import pytest


@pytest.fixture
def repo_root_dir() -> Path:
    return Path(__file__).parent.parent
