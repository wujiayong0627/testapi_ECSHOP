"""
@Name: Ecshop_web_loginUser.py
@Auth: wujiayong
@Date: 2022/8/26-16:42
@Desc: 
@Ver : 0.0.0
"""
from page.Ecshop_web_homePage import HomePage
from page.Ecshop_web_loginPage import LoginPage
from util.driverUtil import driver
from util.yamlUtil import Yaml
from util.logUtli import logger


class LoginUser:
    def __init__(self, case_info):
        self.browser = driver()
        self._logger(case_info)

    def login_user_case(self):
        HomePage(self.browser).click_longin()
        LoginPage(self.browser).input_username(self.username)
        LoginPage(self.browser).input_password(self.password)
        LoginPage(self.browser).click_submit()

        return self.browser.driver

    def login_user(self, browser):
        HomePage(browser).click_longin()
        LoginPage(browser).input_username(self.username)
        LoginPage(browser).input_password(self.password)
        LoginPage(browser).click_submit()

    def _logger(self, case_info):
        self.name = case_info['name']
        self.username = case_info['username']
        self.password = case_info['password']
        logger.info('用例名称:{}'.format(self.name))
        logger.info("用户名:{}".format(self.username))
        logger.info("密码:{}".format(self.password))
