import pytest

from util.requestsUtil import Requests
from util.yamlUtil import Yaml


@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    """
    进行extract.yml清理工作
    :return:
    """
    Yaml().clear_extract()


@pytest.fixture(scope="function", params=Yaml().read_users())
def api_login_user(request):
    """
    api登录用户
    :param request:数据驱动，提供yaml文件中的数据.
    :return:
    """
    req = Requests("user_url")
    req.standard_yaml(request.param)
    yield req






