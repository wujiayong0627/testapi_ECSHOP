import time

import pytest

from selenium import webdriver

from util.yaml_util import YamlUtil


@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yml()
