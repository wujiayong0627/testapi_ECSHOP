"""
@Name: csv_util.py
@Auth: wujiayong
@Date: 2022/8/16-17:32
@Desc: 
@Ver : 0.0.0
"""
import csv
import os

from util.logUtli import logger

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = os.path.join(root_path, 'datas')


class csvUtil:
    def __init__(self, filename):
        self.filename = filename

    def reader_list(self):
        datas = []
        with open(data_path + '\\' + self.filename, "r", encoding="utf-8") as f:
            file = csv.reader(f)
            for i in file:
                datas.append(i)
        return datas

    def reader_dict(self):

        datas = []
        with open(data_path + '\\' + self.filename, "r", encoding="utf-8") as f:
            file = csv.DictReader(f)
            for i in file:
                data_dict = {}
                for key, value in i.items():
                    data_dict[key] = value
                datas.append(data_dict)
        return datas

    def write_list(self, header: list, data: list):
        try:
            with open(data_path + "\\" + self.filename, 'a', encoding='utf-8', newline="") as f:
                file = csv.writer(f)
                if header is not None:
                    file.writerow(header)
                file.writerows(data)
        except FileExistsError as e:
            logger.error("写入文件失败:{}".format(e))

    def write_dict(self, data: dict, header: dict = None):
        try:
            with open(data_path + "\\" + self.filename, "a", encoding="utf-8", newline="") as f:
                file = csv.DictWriter(f, header)
                if header is not None:
                    file.writeheader()
                file.writerows(data)
        except FileExistsError as e:
            logger.error("写入文件失败:{}".format(e))

if __name__ == '__main__':
    a = csvUtil("login_data.csv")
    b = a.reader_list()
    print(b)