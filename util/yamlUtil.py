import json
import os

import yaml

from util.parameterizeUtil import ddt

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
common_path = os.path.join(root_path, 'common')
casedata_path = os.path.join(root_path, 'casedata')


class Yaml:

    def read_extract(self, key):
        """
        读取extract.yml文件
        :param key:
        :return:
        """
        with open(common_path + "/extract.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    def write_extract(self, data):
        """
        写入extract.yml文件
        :param data:
        :return:
        """
        with open(common_path + "/extract.yml", mode='a', encoding='utf-8') as f:
            value = yaml.dump(data=data, stream=f, allow_unicode=True)
            return value

    def clear_extract(self):
        """
        清除extract.yml文件
        :return:
        """
        with open(common_path + "/extract.yml", mode='w', encoding='utf-8') as f:
            f.truncate()

    # 读取测试用例的yml文件
    def read_testcase(self, yml_name):
        """
        读取测试用例模板方法，若yml里面数据用例大于等于2时，直接返回caseinfo，否则调用ddt方法进行读取datas中的csv数据
        :param yml_name:
        :return:
        """
        with open(casedata_path + '/' + yml_name, mode='r', encoding='utf-8') as f:
            caseinfo = yaml.load(stream=f, Loader=yaml.FullLoader)
            if len(caseinfo) >= 2:  # 判断yaml用例文件中有几条用例，当用例大于等于2时，直接返回caseinfo
                return caseinfo
            else:  # 当等于1时，因为数据驱动后的caseinfo是字典列表我们就需要对caseinfo解包
                if "parameterize" in dict(*caseinfo).keys():
                    new_caseinfo = ddt(*caseinfo)
                    return new_caseinfo
                else:
                    return caseinfo

    def read_users(self):
        """
        读取用户信息
        :return:
        """
        with open(common_path + "/users.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    def read_config(self, key):
        """
        获取配置信息
        :param key: 键
        :return:
        """
        with open(common_path + "/config.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    def read_loader(self,key):
        """
        获取定位器信息
        :param key:
        :return:
        """
        with open(common_path + "/locator.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]


if __name__ == '__main__':
    a = Yaml().read_loader('login_username')
    print(a)