import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

options = Options()
service = Service(executable_path=GeckoDriverManager().install())
# 设置无头模式
options.headless = True
driver = webdriver.Firefox(options=options, service=service)

driver.get("https://www.baidu.com")
time.sleep(10)
driver.quit()


options = Options()
firefox_profile = FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", False)
options.profile = firefox_profile
