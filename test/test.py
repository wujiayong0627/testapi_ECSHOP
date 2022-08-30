import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import pyautogui

service = Service(executable_path=ChromeDriverManager().install())

with webdriver.Chrome(service=service) as driver:
    driver.get("https://www.baidu.com")
    wait = WebDriverWait(driver, 10)
    original_window_one = driver.current_window_handle

    assert len(driver.window_handles) == 1

    driver.find_element(By.LINK_TEXT, "新闻").click()

    wait.until(expected_conditions.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
        if window_handle != original_window_one:
            driver.switch_to.window(window_handle)
            break

    wait.until(expected_conditions.title_is("百度新闻——海量中文资讯平台"))

    driver.switch_to.new_window("tab")
    driver.get("http://www.qq.com")
    original_window_two = driver.current_window_handle
    driver.switch_to.new_window("window")
    time.sleep(3)
    driver.close()
    driver.switch_to.window(original_window_one)

    driver.set_window_size(1024, 768)
    x = driver.get_window_position().get('x')
    y = driver.get_window_position().get('y')
    size = driver.get_window_size()
    width1 = size.get("width")
    height1 = size.get("height")
    time.sleep(5)

    print(width1,height1,x,y)

