# 一、yaml数据驱动封装
#
# @pytest.mark.parametrize(argnames ,argvalues)
# argnames:参数名
# argvalues:参数值（list[]、元组()、字典{}、字典值）
# 用多少个值，就会运行多少次用例
用法一(基础用法)：
class TestApi:

    @pytest.mark.parametrize('name', ['张三', '李四', '王五'])
    def test_print_name(self, name):
        print(name)

if __name__ == '__main__':
    pytest.main(["TestApi"])
用法二（解包）：
@pytest.mark.parametrize('name,age', [['张三', '12'], ['李四', '15'], ['王五', '19']])
def test_print_name2(self, name, age):
    print(name, age)

# 二、YAML语法详解（一种数据文件，支持注释、换行、裸字符串）
# 1、配置文件（配置环境、数据库相关配置、账号信息、日志格式、报告名称）
# 2、用于多接口串联（保存鉴权码、状态等）
# 3、测试用例

# 语法规则：
# 1、区分大小写
# 2、用缩进表示层级关系，不能使用tab键缩进
# 3、和缩进多少层无关，只和左边对齐有关
# 4、#表示注释
# 5、键与值之间需要用空格分开

#

# 数据组成：
# 1、map对象：键值对（键可为空）
# 2、数组*（列表）：用-开头


# 三 统一接口请求封装
# 原因：需要对所有的请求做分析处理，日志监控。
# 

# 三、拓展
# 1、requests二次封装
# 2、断言多种多样
# 3、进行多接口场景串联
# 4、日志监控（日志文件生成、控制台调试日志、邮件日志）











