"""
@Name: conftest.py.py
@Auth: wujiayong
@Date: 2022/8/3-22:12
@Desc: 
@Ver : 0.0.0
"""

import pytest

from util.driver_util import browser
from util.log_utli import logger
from util.yaml_util import YamlUtil


@pytest.fixture(scope="function", params=YamlUtil().read_users())
def logon_user(request):
    driver = browser().web_driver()
    url = request.param['url']
    username = request.param['username']
    password = request.param['password']

    logger.info("登录地址:{}".format(url))
    logger.info("登录用户:{}".format(username))
    logger.info("登录密码:{}".format(password))

    logger.info("浏览器打开成功")

    driver.get(url)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('submit').click()
    driver.find_element_by_class_name("cur").click()
    logger.info("用户登录成功")
    yield driver


@pytest.fixture(scope='function')
def open_web():
    logger.info("浏览器打开成功")
    yield browser().web_driver()
