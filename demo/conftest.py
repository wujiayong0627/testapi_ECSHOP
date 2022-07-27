import time

import pytest

from selenium import webdriver

from util.yaml_util import YamlUtil


@pytest.fixture(scope="function", params=YamlUtil().read_user_info('user_Information.yml'))
def logon_user(request):
    print("\n打开火狐浏览器")
    username = request.param['username']
    password = request.param['password']

    driver = webdriver.Firefox(executable_path='C:\\Users\\22366\\firefox\\geckodriver')
    driver.get('http://192.168.0.158/ECShop/upload66/user.php')
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


@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yml()
