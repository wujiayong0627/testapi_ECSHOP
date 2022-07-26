import pytest

from selenium import webdriver

from util.yaml_util import YamlUtil


@pytest.fixture(scope="function")
def conn_database():
    print("打开火狐浏览器")
    driver = webdriver.Firefox(executable_path='C:\\Users\\22366\\firefox\\geckodriver')
    yield
    print("关闭火狐浏览器")
    driver.close()


@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yml()
