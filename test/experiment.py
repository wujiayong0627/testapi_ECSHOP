import pytest
import yaml

from selenium import webdriver

class YamlUtil:
    # 读取yml文件
    def read_extract_yml(self, key):
        with open("./extract.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    # 写入yml文件
    def write_extract_yml(self, data):
        with open("./extract.yml", mode='a', encoding='utf-8') as f:
            value = yaml.dump(data=data, stream=f, allow_unicode=True)
            return value

    # 清除yml文件
    def clear_extract_yml(self):
        with open("./extract.yml", mode='w', encoding='utf-8') as f:
            f.truncate()

    # 读取测试用例的yml文件
    def read_testcase_yml(self, yml_name):
        with open("./testcase/" + yml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    # 读取用户的基本信息的yml文件
    def read_user_info(self, yml_name):
        with open("./" + yml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value


@pytest.mark.parametrize("case_info", YamlUtil().read_user_info('user_Information.yml'))
@pytest.fixture(scope="function")
def logon_user(case_info):
    print("打开火狐浏览器")
    username = case_info['username']
    password = case_info['password']

    driver = webdriver.Firefox(executable_path='C:\\Users\\22366\\firefox\\geckodriver')
    driver.get('http://192.168.0.158/ECShop/upload66/user.php')
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('submit').click()
    yield driver
    print("关闭火狐浏览器")
    driver.close()

if __name__ == '__main__':
    a = YamlUtil().read_user_info("user_Information.yml")
    b = logon_user()
    print(a)
