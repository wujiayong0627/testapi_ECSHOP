"""
@Name: driver_util.py
@Auth: wujiayong
@Date: 2022/8/8-14:48
@Desc:
@Ver : 0.0.0
"""
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from util.logUtli import log_path, logger


class Browser:

    def firefox(self):
        service = FirefoxService(executable_path=GeckoDriverManager().install(), log_path=log_path + "\\geckodriver.log")
        options = webdriver.FirefoxOptions()
        # 设置浏览器编码格式
        # self.options.add_argument('lang=zh_CN.UTF-8')
        # 设置浏览器禁止加载图片
        options.set_preference('permissions.default.image', 2)

        # firefox无头模式
        # options.headless = True

        options.add_argument('--disable-gpu')
        options.add_argument('window-size=1200x600')
        driver = webdriver.Firefox(service=service, options=options)
        logger.info('浏览器操作:火狐浏览器启动成功')
        driver.implicitly_wait(10)
        return driver

    def chrome(self):
        service = ChromeService(executable_path=ChromeDriverManager().install(),
                                log_path=log_path + "\\chromedriver.log")
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options, service=service)
        logger.info('浏览器操作:谷歌浏览器启动成功')
        driver.implicitly_wait(10)
        return driver

    def edge(self):
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install(),
                              log_path=log_path + "\\edge.log")
        driver = webdriver.Edge(service=service)
        driver.implicitly_wait(10)
        logger.info('浏览器操作:Edge浏览器启动成功')
        return driver
