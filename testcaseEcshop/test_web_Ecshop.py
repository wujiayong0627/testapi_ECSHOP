"""
@Name: test_web_demo.py
@Auth: wujiayong
@Date: 2022/7/26-13:48
@Desc: 
@Ver : 0.0.0
"""
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from process.Ecshop_web_PurchaseGoods import PurchaseGoods
from process.Ecshop_web_loginUser import LoginUser

from util.logUtli import logger
from util.yamlUtil import Yaml
from util.assertUtil import Assert


class TestWebEcshop:

    # @pytest.mark.skipif(True, reason="跳过")
    @pytest.mark.web_Ecshop
    @pytest.mark.parametrize('case_info', Yaml().read_testcase('test_Ecshhop_web_userLogin.yml'))
    def test_Ecshhop_web_userLogin(self, case_info):
        """
        登录界面测试用例
        :return:
        """
        driver = LoginUser(case_info).login_user_case()
        Assert().driverAssert(case_info['validate'], driver)

    @pytest.mark.web_Ecshop
    @pytest.mark.parametrize('case_info', Yaml().read_testcase('test_Ecshhop_web_purchaseGoods.yml'))
    def test_Ecshhop_web_purchaseGoods(self,case_info):
        """
        购买商品测试用例
        :param case_info:
        :return:
        """
        driver = PurchaseGoods(case_info).login_buy_goods()
        Assert().driverAssert(case_info['validate'], driver)
