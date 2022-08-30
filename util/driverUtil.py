"""
@Name: driverUtil.py
@Auth: wujiayong
@Date: 2022/8/25-17:05
@Desc: 
@Ver : 0.0.0
"""

import time

from selenium.common.exceptions import TimeoutException

from util.browserUtli import Browser
from util.logUtli import logger

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from util.yamlUtil import Yaml


class driver:

    def __init__(self, browser="chrome"):
        """
        初始化driver
        :param browser:浏览器名称
        """
        if browser == "chrome":
            self.driver = Browser().chrome()
        elif browser == "firefox":
            self.driver = Browser().firefox()
        elif browser == "ie":
            self.driver = Browser().edge()
        else:
            self.driver = None
            logger.error("浏览器选择错误：输入的浏览器名称不正确;例如:chrome,firefox,edge")

        self.open_url()

    def open_url(self):
        """
        打开网址
        :param url:
        :return:
        """
        try:
            self.driver.get(Yaml().read_config("user_url"))
            logger.info("浏览器操作:网页打开成功")
        except TimeoutException:
            logger.info("浏览器操作:网页打开超时")

    def find_element(self, locator, timeout=10):
        """
        定位单个元素,如果定位成功返回元素本身,如果失败,返回False
        :param timeout: 等待时间
        :param locator: 定位器,例如("id","id属性值")
        :return: 元素本身
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(eval(locator)))
            return element
        except TimeoutException:
            logger.error(f"显性等待:超时,无法定位{locator}元素")
            return False

    def click(self, locator):
        """
        点击元素
        :return:
        """
        element = self.find_element(locator)
        element.click()

    def mouse_single_click(self, locator):
        """
        鼠标单击元素
        :param locator:
        :return:
        """
        action = ActionChains(self.driver)
        element = self.find_element(locator)
        action.click(element).perform()

    def send_keys(self, locator, text):
        """
        元素输入
        :param locator: 定位器
        :param text: 输入内容
        :return:
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def close(self):
        """
        关闭浏览器
        :return:
        """
        logger.info("浏览器操作:关闭浏览器")
        self.driver.quit()

    def to_homePage(self):
        """
        进入首页
        :param locator:
        :return:
        """
        self.mouse_single_click(str(("xpath", "//img[@src='themes/default/images/logo.gif']")))
