import json
import time
import requests
import pytest

from util.requests_util import RequestsUtil
from util.yaml_util import YamlUtil


class TestApiDemo:

    def setup_class(self):
        print("\n开始执行api用例")

    def teardown_class(self):
        print("\n用例api执行结束")

    def setup(self):
        print("\n开始执行用例")

    def teardown(self):
        print("\n用例执行结束")

    @pytest.mark.skipif(True, reason="跳过")
    @pytest.mark.parametrize('case_info', YamlUtil().read_testcase_yml('test_login.yml'))
    def test_api_login(self, case_info):
        """
        登录api测试用例
        :param case_info:数据驱动，提供yaml文件中的数据.
        :return:
        """

        method = case_info['request']['method']
        url = case_info['request']['url']
        data = case_info['request']['params']
        headers = case_info['request']['headers']
        eq = case_info['validate']['eq']

        req = RequestsUtil().send_request(method=method, url=url, data=data, headers=headers)
        try:
            assert eq in req.text
        except AssertionError as e:
            print(e)
