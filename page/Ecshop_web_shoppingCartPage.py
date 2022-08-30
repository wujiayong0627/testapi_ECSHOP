"""
@Name: Ecshop_web_shoppingCartPage.py
@Auth: wujiayong
@Date: 2022/8/26-15:27
@Desc: 
@Ver : 0.0.0
"""



from util.yamlUtil import Yaml


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_settlementCenter(self):
        self.driver.mouse_single_click(Yaml().read_loader("settlement_center_button"))