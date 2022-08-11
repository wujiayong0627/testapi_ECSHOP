"""
@Name: thermalLoading_utli.py
@Auth: wujiayong
@Date: 2022/8/10-10:21
@Desc: 
@Ver : 0.0.0
"""
from util.yaml_util import YamlUtil


class ThermalLoading:

    def get_extract_data(self, key):
        """
        获取extract.yml中的值
        :param key: 键名
        :return:
        """
        return YamlUtil().read_extract(key)
