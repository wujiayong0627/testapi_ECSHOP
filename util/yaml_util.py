import yaml


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
        with open("./data/" + yml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value


YamlUtil = YamlUtil()
