"""
@Name: test_web_demo.py
@Auth: wujiayong
@Date: 2022/7/26-13:48
@Desc: 
@Ver : 0.0.0
"""
import time

import pytest

from util.log_utli import logger
from util.yaml_util import YamlUtil


class TestWebDemo:

    @pytest.mark.skipif(True, reason="跳过")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('case_info', YamlUtil().read_testcase('web_login.yml'))
    def test_login(self, case_info, open_web):
        """
        登录界面测试用例
        :return:
        """
        try:
            casename = case_info['web_name']
            url = case_info['request']['url']
            data = case_info['request']['params']
            eq = case_info['validate']['eq']

            logger.info('用例名称:{}'.format(casename))
            logger.info("接口地址:{}".format(url))
            logger.info("输入数据:{}".format(data))

            open_web.get(url)
            open_web.find_element_by_name("username").send_keys(data['username'])
            open_web.find_element_by_name('password').send_keys(data['password'])
            open_web.find_element_by_name('submit').click()
            time.sleep(1)

            assert eq in open_web.page_source
            logger.info('{}用例执行成功'.format(casename))
        except Exception as e:
            logger.error("用例失败:{}".format(e))

        finally:
            open_web.close()
            logger.info("关闭浏览器")

    @pytest.mark.skipif(True, reason="跳过")
    @pytest.mark.run(order=1)
    def test_place_order(self, logon_user):
        """
        提交订单
        :param logon_user: 登录用户
        :return:
        """

        try:
            logon_user.find_element_by_xpath('//*[@id="show_best_area"]/div[5]').click()
            logon_user.find_element_by_xpath('//*[@id="ECS_FORMBUY"]/ul/li[8]/a[1]').click()
            logon_user.find_element_by_xpath('/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a').click()
            logon_user.find_element_by_xpath('//*[@id="theForm"]/div[15]/div[2]/input[1]').click()

            assert "订单已提交" in logon_user.page_source
            logger.info('提交订单用例执行成功')

        except Exception as e:
            logger.error("用例失败:{}".format(e))
        finally:
            logon_user.close()
            logger.info("关闭浏览器")
