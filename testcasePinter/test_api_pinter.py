"""
@Name: test_api_pinter.py
@Auth: wujiayong
@Date: 2022/8/24-17:10
@Desc: 
@Ver : 0.0.0
"""
import pytest

from util.assertUtil import Assert
from util.requestsUtil import Requests
from util.yamlUtil import Yaml


class TestApiPinter:

    @pytest.mark.api_pinter
    @pytest.mark.parametrize('case_info', Yaml().read_testcase('test_pinter_api_login.yml'))
    def test_pinter_api_login(self, case_info):
        """
        银行登录接口2（token）测试用例
        :return:
        """
        req = Requests("pinter_url").standard_yaml(case_info)
        Assert().reqAssert(case_info['validate'], req)

    @pytest.mark.api_pinter
    @pytest.mark.parametrize('case_info', Yaml().read_testcase('test_pinter_api_balanceQuery.yml'))
    def test_pinter_api_balanceQuery(self, case_info):
        """
        余额查询
        :param case_info:
        :return:
        """
        req = Requests("pinter_url").standard_yaml(case_info)
        Assert().reqAssert(case_info['validate'], req)
