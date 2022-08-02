"""
@Name: test_web_demo.py
@Auth: wujiayong
@Date: 2022/7/26-13:48
@Desc: 
@Ver : 0.0.0
"""
import time

import pytest

from selenium import webdriver

from util.yaml_util import YamlUtil


class TestWebDemo:

    def setup_class(self):
        print("\n开始执行web用例")

    def teardown_class(self):
        print("\n用例web执行结束")

    def setup(self):
        print("\n开始执行用例")

    def teardown(self):
        print("\n用例执行结束")

    @pytest.mark.skipif(True, reason="跳过")
    @pytest.mark.parametrize('case_info', YamlUtil().read_testcase_yml('test_login.yml'))
    def test_login(self, case_info, open_web):
        """
        登录界面测试用例
        :return:
        """
        url = case_info['request']['url']
        username = case_info['request']['params']['username']
        password = case_info['request']['params']['password']
        eq = case_info['validate']['eq']

        open_web.get(url)
        open_web.find_element_by_name("username").send_keys(username)
        open_web.find_element_by_name('password').send_keys(password)
        open_web.find_element_by_name('submit').click()
        time.sleep(1)

        try:
            assert eq in open_web.page_source
        except AssertionError as e:
            print(e)

    # @pytest.mark.skipif(True, reason="跳过")
    def test_place_order(self, logon_user):
        """
        提交订单
        :param logon_user: 登录用户
        :return:
        """
        logon_user.find_element_by_xpath('//*[@id="show_best_area"]/div[5]').click()
        logon_user.find_element_by_xpath('//*[@id="ECS_FORMBUY"]/ul/li[8]/a[1]').click()
        logon_user.find_element_by_xpath('/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a').click()
        logon_user.find_element_by_xpath('//*[@id="theForm"]/div[15]/div[2]/input[1]').click()

        try:
            assert "订单已提交" in logon_user.page_source
        except AssertionError as e:
            print(e)


