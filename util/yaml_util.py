import yaml


class YamlUtil:
    # 读取yml文件
    def read_extract(self, key):
        with open("./datas/extract.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    # 写入yml文件
    def write_extract(self, data):
        with open("./datas/extract.yml", mode='a', encoding='utf-8') as f:
            value = yaml.dump(data=data, stream=f, allow_unicode=True)
            return value

    # 清除yml文件
    def clear_extract(self):
        with open("./datas/extract.yml", mode='w', encoding='utf-8') as f:
            f.truncate()

    # 读取测试用例的yml文件
    def read_testcase(self, yml_name):
        with open("./testcase/" + yml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    # 读取用户的基本信息的yml文件
    def read_users(self):
        with open("./datas/users.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    # 读取公用信息
    def read_config(self, key):
        with open("./datas/config.yaml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]
