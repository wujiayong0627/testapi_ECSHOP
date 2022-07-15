import json

import requests


class RequestsUtil:
    """
    requests类二次封装
    """

    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method, url, data, **kwargs):
        """
        发送接口请求
        :param method: get、post、delete、put请求方式
        :param url: 接口地址
        :param param_type: 数据类型：from(表单)/json
        :param data: 参数
        :param kwargs:请求头、文件等
        :return:
        """

        method = str(method).lower()

        if method == 'get':
            response = self.session.request(method=method, url=url, params=data, **kwargs)

        elif method == 'post':
            response = self.session.request(method=method, url=url, data=data, **kwargs)

        elif method == 'delete':
            response = self.session.request(method=method, url=url, data=data, **kwargs)

        elif method == 'put':
            response = self.session.request(method=method, url=url, data=data, **kwargs)

        else:
            raise ValueError

        return response

    def close_session(self):
        """
        关闭session
        :return:null
        """
        self.session.close()
