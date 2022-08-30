import pytest

from util.yamlUtil import Yaml


@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    """
    进行extract.yml清理工作
    :return:
    """
    Yaml().clear_extract()


