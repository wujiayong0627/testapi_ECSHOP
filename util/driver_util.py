"""
@Name: driver_util.py
@Auth: wujiayong
@Date: 2022/8/8-14:48
@Desc: 
@Ver : 0.0.0
"""
import os

from selenium import webdriver

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
log_path = os.path.join(root_path, 'log')
firefoxDriver_path = 'C:\\Users\\22366\\Chowder\\driver\\geckodriver.exe'


class browser:

    def __init__(self):
        self.options = webdriver.FirefoxOptions()
        # 设置浏览器编码格式
        self.options.add_argument('lang=zh_CN.UTF-8')
        # 设置浏览器禁止加载图片
        self.options.set_preference('permissions.default.image', 2)

        # firefox无头模式
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('window-size=1200x600')

        self.web_driver = webdriver.Firefox(executable_path=firefoxDriver_path, options=self.options,
                                            service_log_path=log_path + "\\geckodriver.log")


driver = browser().web_driver
