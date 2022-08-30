"""
@Name: Ecshop_web_PurchaseGoods.py
@Auth: wujiayong
@Date: 2022/8/26-16:15
@Desc: 
@Ver : 0.0.0
"""

from page.Ecshop_web_homePage import HomePage
from page.Ecshop_web_productDetailsPage import ProductDetailsPage
from page.Ecshop_web_shoppingCartPage import ShoppingCartPage
from page.Ecshop_web_orderDetailsPage import OrderDetailsPage

from process.Ecshop_web_loginUser import LoginUser

from util.driverUtil import driver


class PurchaseGoods:

    def __init__(self, case_info):
        self.browser = driver()
        self.case_info = case_info

    def login_buy_goods(self):
        LoginUser(self.case_info).login_user(self.browser)
        self.browser.to_homePage()
        HomePage(self.browser).click_commodity()
        ProductDetailsPage(self.browser).click_addCart()
        ShoppingCartPage(self.browser).click_settlementCenter()
        OrderDetailsPage(self.browser).click_placeOrder()

        return self.browser.driver
