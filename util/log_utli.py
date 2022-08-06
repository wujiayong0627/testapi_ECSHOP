"""
@Name: log_utli.py
@Auth: wujiayong
@Date: 2022/8/5-21:29
@Desc: 
@Ver : 0.0.0
"""
import logging
import os
import time

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
log_path = os.path.join(root_path, 'log')


class Logger:

    def __init__(self):
        # 定义日志位置和文件名
        self.logname = os.path.join(log_path, '{}.log'.format(time.strftime("%Y-%m-%d")))
        # 定义一个日志容器
        self.logger = logging.getLogger('log')
        # 设置日志打印级别
        self.logger.setLevel(logging.DEBUG)
        # 创建日志输入格式
        self.formater = logging.Formatter(
            # [2022-08-06 23:20:02,975][log_utli.py 51][ERROR]: 我打印error日志
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s'
        )
        # 创建日志处理器，用来存放日志文件
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding='utf-8')
        # 文件日志存放级别
        self.filelogger.setLevel(logging.DEBUG)
        # 文件存放日志格式
        self.filelogger.setFormatter(self.formater)

        # 创建日志处理器，在控制台打印
        self.console = logging.StreamHandler()
        # 设置在控制台打印日志的界别
        self.console.setLevel(logging.DEBUG)
        # 控制台打印日志格式
        self.console.setFormatter(self.formater)

        # 将日志输出渠道添加到日志收集器中
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == '__main__':
    logger = Logger().logger
    logger.debug('我打印debug日志')
    logger.info('我打印info日志')
    logger.warning('我打印warning日志')
    logger.error('我打印error日志')
