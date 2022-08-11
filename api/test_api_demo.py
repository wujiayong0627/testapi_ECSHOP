import pytest

from util.assert_util import Assert
from util.log_utli import logger
from util.requests_util import RequestsUtil
from util.yaml_util import YamlUtil


class TestApiDemo:

    @pytest.mark.skipif(True, reason="跳过")
    @pytest.mark.parametrize('case_info', YamlUtil().read_testcase('api_login.yml'))
    def test_api_login(self, case_info):
        """
        登录api测试用例
        :param case_info:数据驱动，提供yaml文件中的数据.
        :return:
        """
        try:
            casename = case_info['name']
            eq = case_info['validate']['eq']

            logger.info('用例名称:{}'.format(casename))

            req = RequestsUtil("user_url").standard_yaml(case_info)
            # req = RequestsUtil("user_url").standard_yaml(method=method, url=url, data=data, headers=headers)
            assert eq in req.text
            logger.info("{}用例执行成功".format(casename))
            # RequestsUtil().close_session()
        except Exception as e:
            logger.error("用例失败:{}".format(e))

    # @pytest.mark.run(order=1)
    # @pytest.mark.skipif(True, reason="跳过")
    @pytest.mark.parametrize('case_info', YamlUtil().read_testcase('pinter_login.yml'))
    def test_pinter_lonin(self, case_info):
        """
        银行登录接口2（token）测试用例
        :return:
        """
        try:
            casename = case_info['name']
            eq = case_info['validate']["message"]
            logger.info("用例名称:{}".format(casename))

            req = RequestsUtil("pinter_url").standard_yaml(case_info)
            assert eq in req.text
            logger.info("用例执行:成功")
        except Exception as e:
            logger.error("用例执行:失败")
            logger.error("失败原因:".format(e))

    # @pytest.mark.run(order=2)
    @pytest.mark.parametrize('case_info', YamlUtil().read_testcase('pinter_balance_query.yml'))
    def test_balance_query(self, case_info):

        req = RequestsUtil("pinter_url").standard_yaml(case_info)
        Assert().result(case_info['validate'], req)
