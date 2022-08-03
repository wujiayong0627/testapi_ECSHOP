"""
@Name: conftest.py.py
@Auth: wujiayong
@Date: 2022/8/3-22:12
@Desc: 
@Ver : 0.0.0
"""
import time

import pytest

from selenium import webdriver

from util.yaml_util import YamlUtil


@pytest.fixture(scope="function", params=YamlUtil().read_user_info('user_Information.yml'))
def logon_user(request):
    print("\n打开火狐浏览器")

    url = request.param['url']
    username = request.param['username']
    password = request.param['password']
    executable_path = request.param['executable_path']

    driver = webdriver.Firefox(executable_path=executable_path)
    driver.get(url)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('submit').click()
    driver.find_element_by_class_name("cur").click()
    yield driver
    print("\n关闭火狐浏览器")
    driver.close()


@pytest.fixture(scope='function')
def open_web():
    print("\n 打开火狐浏览器")
    driver = webdriver.Firefox(executable_path='C:\\Users\\22366\\firefox\\geckodriver')
    yield driver
    print("\n 关闭火狐浏览器")
    driver.close()
