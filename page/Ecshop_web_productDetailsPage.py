"""
@Name: Ecshop_web_productDetailsPage.py
@Auth: wujiayong
@Date: 2022/8/26-15:19
@Desc: 
@Ver : 0.0.0
"""

from util.yamlUtil import Yaml


class ProductDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_addCart(self):
        self.driver.mouse_single_click(Yaml().read_loader("add_cart"))
