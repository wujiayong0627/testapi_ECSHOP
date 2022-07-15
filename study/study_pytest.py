import pytest

# 运行方式
# 1、主函数运行（命令行） pytest.mian
#   参数：
#     -s：表示输出调试信息，用于显示测试函数中print()打印的信息
#     -v：未加前只打印模块名，加v后打印类名、模块名、方法名，显示更详细的信息
#     -q：表示只显示整体测试结果
#     -vs：这两个参数可以一起使用
#     -n：支持多线程或者分布式运行测试用例（需安装：pytest-xdist插件）
#     –reruns：失败用例重跑，跑几次
#     -x：表示只要有一个测试用例报错，则执行停止
#     –maxfail=2：表示出现2个用例报错，则执行停止
#     -k：模糊匹配，测试用例的部分字符串，指定执行测试用例
#     -html 在当前路径下生成html格式的测试报告

# 2、使用朋友test.ini 的配置文件来配置运行。
# [pytest]
# 命令行参数，用空格进行分隔
# addopts = -vs (和第一种方式参数使用方法相同)
#
# 注册 mark 标记,将用例进行分组利用@pytest.mark.markname,进行调用
# markers =
#     demo : marks tests as demo
#     smoke: marks tests as smoke
#     uat : marks tests as uat
#     test : marks tests as test

# 指定最低pytest版本
# minversion = 5.0
#
# 测试用例的路径，可自己配置
# testpaths =./testcase
# 1 ../pytestproject为上一层的pytestproject文件夹
# 2 ./testcase为pytest.ini当前目录下的同级文件夹
#
# 模块名的规则，配置测试搜索的模块文件名称
# python_files = test*.py
#
# 类名的规则，配置测试搜索的测试类名
# python_classes = Test*
#
# 方法名的规则，配置测试搜索的测试函数名
# python_functions = test
#
# 前后置 夹具
# setup/teardown 在每个用例之前和之后执行一次
#
# setup_class/teardown_class  在每个类之前和之后执行一次
#
# @pytest.fixture(scope="", params="", autouse=True, ids="", name="")   实现部分的用例的前后置
# scope 作用域  函数/类/模块/包/session(会话)
# params 数据驱动
# autouse 自动执行
# ids  自定义参数名
# inameds 重命名

# @pytest.fixture()一般情况下与conftest.py一起使用.

# conftest.py 固定名称
# 1.conftest.py单独存放@pytest.fixture()的方法.用处是可以存放多个py文件之间的共享前置.
# 2.conftest.py里面的方法在调用时,不需要导入,可以直接使用
# 3.conftest.py可以有多个,也可以有多个不同的层级


# 四、接口自动化测试框架封装(接口关联的封装)
#  一般情况下，通过一个关联的yaml文件来实现(yaml_util.py)

# 五、pytest接口测试的断言
# assert关键字

# 六、pytest结合allur-pytest生成allure测试报告
# 1、生成临时的json文件报告（直接在pytest.ini 中添加参数 --alluredir ./temp）
# 2、通过临时的json文件生成allure报告（os.system(allure generate temp -o temp/reports --clean)）
# 3、allure报告的定制
