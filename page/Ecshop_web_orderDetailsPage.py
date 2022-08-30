"""
@Name: Ecshop_web_orderDetailsPage.py
@Auth: wujiayong
@Date: 2022/8/26-15:38
@Desc: 
@Ver : 0.0.0
"""


from util.yamlUtil import Yaml


class OrderDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    def cikck_paymentMethod(self):
        self.driver.click(Yaml().read_loader("paymentMethod"))

    def click_placeOrder(self):
        self.driver.mouse_single_click(Yaml().read_loader("placeorder_button"))
