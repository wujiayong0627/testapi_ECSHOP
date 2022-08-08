import json
import time
import requests
import pytest

from util.requests_util import requesting
from util.yaml_util import yml
from util.log_utli import logger


class TestApiDemo:

    def setup_class(self):
        print("\n开始执行api用例")

    def teardown_class(self):
        print("\n用例api执行结束")

    def setup(self):
        print("\n开始执行用例")

    def teardown(self):
        print("\n用例执行结束")

    # @pytest.mark.skipif(True, reason="跳过")
    @pytest.mark.parametrize('case_info', yml.read_testcase_yml('test_login.yml'))
    def test_api_login(self, case_info):
        """
        登录api测试用例
        :param case_info:数据驱动，提供yaml文件中的数据.
        :return:
        """

        method = case_info['request']['method']
        url = case_info['request']['url']
        data = case_info['request']['params']
        param_type = case_info['request']['param_type']
        headers = case_info['request']['headers']
        eq = case_info['validate']['eq']

        logger.info("接口地址:" + url)
        logger.info("请求方法:" + method)
        logger.info("传入参数:" + str(data))

        req = requesting.send_request(method=method, url=url, data=data, param_type=param_type, headers=headers)

        try:
            assert eq in req.text
            logger.info( "{}用例执行成功".format(case_info['api_name']))
            # RequestsUtil().close_session()
        except AssertionError as e:
            logger.error(e)
