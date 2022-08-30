"""
@Name: Ecshop_web_homePage.py
@Auth: wujiayong
@Date: 2022/8/26-14:27
@Desc: 
@Ver : 0.0.0
"""
from util.yamlUtil import Yaml


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_longin(self):
        self.driver.mouse_single_click(Yaml().read_loader("home_login_button"))

    def click_register(self):
        self.driver.mouse_single_click(Yaml().read_loader("home_register_button"))

    def click_commodity(self):
        self.driver.click(Yaml().read_loader("home_commodity"))
