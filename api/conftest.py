import time

import pytest

from util.yaml_util import yml


@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    yml.clear_extract_yml()
