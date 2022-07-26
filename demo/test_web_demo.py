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
        print("\n 打开火狐浏览器")
        self.driver = webdriver.Firefox(executable_path='C:\\Users\\22366\\firefox\\geckodriver')
        print("\n开始执行用例")

    def teardown(self):
        print("\n 关闭火狐浏览器")
        self.driver.close()
        print("\n用例执行结束")

    @pytest.mark.parametrize('case_info', YamlUtil().read_testcase_yml('test_login.yml'))
    def test_login(self, case_info):
        """
        登录界面测试用例
        :return:
        """
        username = case_info['request']['params']['username']
        password = case_info['request']['params']['password']
        eq = case_info['validate']['eq']

        self.driver.get('http://192.168.0.158/ECShop/upload66/user.php')
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_name('submit').click()
        time.sleep(1)
        try:
            assert eq in self.driver.page_source
        except AssertionError as e:
            print(e)
