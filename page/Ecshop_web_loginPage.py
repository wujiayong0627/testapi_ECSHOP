"""
@Name: Ecshop_web_loginPage.py
@Auth: wujiayong
@Date: 2022/8/26-9:38
@Desc: 
@Ver : 0.0.0
"""
from util.yamlUtil import Yaml


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def input_username(self, username):
        self.driver.send_keys(Yaml().read_loader('login_username'), username)

    def input_password(self, password):
        self.driver.send_keys(Yaml().read_loader('login_password'), password)

    def click_submit(self):
        self.driver.click(Yaml().read_loader("login_button"))
