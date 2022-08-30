import json
import re

import jsonpath
import requests
from requests import HTTPError

from util.logUtli import logger
from util.thermalLoadingUtli import ThermalLoading
from util.yamlUtil import Yaml


class Requests:
    """
    requests类二次封装
    """

    def __init__(self, key):
        """

        :param key: 传入config.yml文件里面的key
        """
        self.obj = ThermalLoading()
        self.session = requests.Session()
        self.head_url = Yaml().read_config(key)

    # 替换值的方法
    # #(替换url，params,data,json,headers)
    # #(string，int,float,list,dict)
    def replace_value(self, data):
        # 保存数据类型
        data_type = type(data)
        # 判断数据类型转换成str
        if isinstance(data, dict) or isinstance(data, list):
            str_data = json.dumps(data)
        else:
            str_data = str(data)

        for cs in range(1, str_data.count('${') + 1):

            # 替换
            if "${" in str_data and "}" in str_data:
                start_index = str_data.index("${")
                end_index = str_data.index("}", start_index)
                old_value = str_data[start_index:end_index + 1]

                func_name = old_value[2:old_value.index("(")]
                args_value_one = old_value[old_value.index("(") + 1:old_value.index(")")]

                if args_value_one != '':
                    args_value_two = args_value_one.split(',')
                    new_value = getattr(self.obj, func_name)(*args_value_two)
                else:
                    new_value = getattr(self.obj, func_name)()
                logger.info('{}:{}'.format(args_value_one, new_value))
                str_data = str_data.replace(old_value, str(new_value))

        # 还原数据类型
        if isinstance(data, dict) or isinstance(data, list):
            data = json.loads(str_data)
        else:
            data = data_type(str_data)

        return data

    # 规范yaml测试用例
    def standard_yaml(self, caseinfo):
        caseinfo_keys = caseinfo.keys()
        # 判断一级关键字是否包含：name，request，validate
        if "name" in caseinfo_keys and "request" in caseinfo_keys and "validate" in caseinfo_keys:
            casename = caseinfo['name']
            logger.info("用例名称:{}".format(casename))
            # 判断request下面是否包含：method、url
            request_keys = caseinfo["request"].keys()
            if "method" in request_keys and "url" in request_keys:

                method = caseinfo['request'].pop("method")  # pop() 函数用于移除列表中的一个元素，并且返回该元素的值。
                url = caseinfo['request'].pop("url")

                req = self.send_request(method, url, **caseinfo['request'])  # caseinfo需要解包加**

                # 提取值并写入extract.yaml文件
                if "extract" in caseinfo.keys() and caseinfo["extract"] is not None:
                    for key, value in caseinfo["extract"].items():
                        if value is None:
                            pass
                        elif "(.*?)" in value or "(.+?)" in value:  # 正则表达式
                            zz_value = re.search(value, req.text)
                            extract_value = {key: zz_value.group(1)}
                            Yaml().write_extract(extract_value)
                        else:  # jsonpath
                            js_value = jsonpath.jsonpath(req.json(), value)
                            if js_value:
                                extract_value = {key: js_value[0]}
                                Yaml().write_extract(extract_value)

                return req

            else:
                logger.error('yml文件在request下必须包含method,url')
        else:
            logger.error('yml文件一级关键字必须包含name,request,validate')

    def send_request(self, method, url, **kwargs):
        try:
            method = str(method).lower()  # 转换小写
            # 基础路径的拼接和替换
            url = self.head_url + self.replace_value(url)

            logger.info("接口地址:{}".format(url))
            logger.info("请求方法:{}".format(method))

            # 参数替换
            for key, value in kwargs.items():
                if key in ['params', 'data', 'json', 'headers'] and value:
                    logger.info((str(key) + ':' + str(value)))
                    kwargs[key] = self.replace_value(value)
                elif key == "files" and value:
                    for file_key, file_path in value.items():
                        if "\\" in file_path:
                            value[file_key] = open(file_path, 'rb')
                    logger.info((str(key) + ':' + str(value)))

            with self.session.request(method, url, **kwargs) as req:
                return req

        except HTTPError as e:
            logger.error("请求异常:{}".format(e))

    def close_session(self):
        """
        关闭session
        :return:null
        """
        self.session.close()
