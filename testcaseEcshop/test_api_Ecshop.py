import pytest

from util.assertUtil import Assert
from util.requestsUtil import Requests
from util.yamlUtil import Yaml


class TestApiEcshop:

    @pytest.mark.skipif(True, "跳过")
    @pytest.mark.api_Ecshop
    @pytest.mark.parametrize('case_info', Yaml().read_testcase('test_Ecshop_api_login.yml'))
    def test_Ecshop_api_login(self, case_info):
        """
        登录Ecshop测试用例
        :param case_info:数据驱动，提供yaml文件中的数据.
        :return:
        """
        req = Requests("user_url").standard_yaml(case_info)
        Assert().reqAssert(case_info['validate'], req)

    @pytest.mark.api_Ecshop
    @pytest.mark.parametrize("case_info", Yaml().read_testcase("test_Ecshop_api_userComments.yml"))
    def test_Ecshop_api_userComments(self, api_login_user, case_info):
        """
        测试我的留言功能
        :param api_login_user:前置条件用户已经登录
        :param case_info:
        :return:
        """
        req = api_login_user.standard_yaml(case_info)
        Assert().reqAssert(case_info['validate'], req)
