# pytest

### 一、运行方式
#### 1、主函数运行（命令行） pytest.mian
#####   参数：
     -s：         表示输出调试信息，用于显示测试函数中print()打印的信息
     -v：         未加前只打印模块名，加v后打印类名、模块名、方法名，显示更详细的信息
     -q：         表示只显示整体测试结果
     -m：
     -vs：        这两个参数可以一起使用
     -n：         支持多线程或者分布式运行测试用例（需安装：pytest-xdist插件）
     –reruns：    失败用例重跑，跑几次
     -x：         表示只要有一个测试用例报错，则执行停止
     –maxfail=2： 表示出现2个用例报错，则执行停止
     -k：         模糊匹配，测试用例的部分字符串，指定执行测试用例
     -html        在当前路径下生成html格式的测试报告

#### 2、使用pytest.ini 的配置文件来配置运行。
    [pytest]
    命令行参数，用空格进行分隔
    addopts = -vs (和第一种方式参数使用方法相同)
    
    注册 mark 标记,将用例进行分组利用@pytest.mark.markname,进行调用
    markers =
        demo : marks tests as demo
        smoke: marks tests as smoke
        uat : marks tests as uat
        test : marks tests as test
    
    指定最低pytest版本
    minversion = 5.0
    
    测试用例的路径，可自己配置
    testpaths =./testcase
    1 ../pytestproject为上一层的pytestproject文件夹
    2 ./testcase为pytest.ini当前目录下的同级文件夹
    
    模块名的规则，配置测试搜索的模块文件名称
    python_files = test*.py

    类名的规则，配置测试搜索的测试类名
    python_classes = Test*
    
    方法名的规则，配置测试搜索的测试函数名
    python_functions = test

### 二、前后置
#### 1、通过编写指定函数进行前后置
    
##### 方法名称
    setup()           在每个用例(方法)之前执行一次
    teardown()        在每个用例(方法)之后执行一次
    setup_class()     在每个类之前执行一次
    teardown_class()  在每个类之后执行一次
##### 实例
     def setup_class(self):
        print("开始执行TestDemo用例")

    def teardown_class(self):
        print("用例TestDemo执行结束")

    def setup(self):
        print("开始执行用例")

    def teardown(self):
        print("用例执行结束")
###  三、修饰器
#### 1、Fixture参数详解及使用（实现部分的用例的前后置）
###### Fixture修饰器来标记固定的工厂函数,在其他函数，模块，类或整个工程调用它时会被激活并优先执行,通常会被用于完成预置处理和重复操作。
##### Fixture的调用方式：

    @pytest.fixture(scope="", params="", autouse=True, ids="", name="")  
##### 参数：
    scope     作用域  函数/类/模块/包/session(会话)
    params    数据驱动
    autouse   自动执行
    ids       自定义参数名
    inameds   重命名

###### 作用域 scope（控制范围）
    function    函数级 每一个函数或方法都会调用。
    class	    模块级 每一个.py文件调用一次。
    module	    块级(包) 每一个.py文件调用一次。
    session	    会话级 每次会话只需要运行一次，会话内所有方法及类，模块都共享这个方法.
###### params（可选形参列表--数据驱动）：(list类型)提供参数数据，供调用标记方法的函数使用，可与参数ids一起使用，作为每个参数的标识，被Fixture装饰的函数要调用是采用：Request.param
###### ids：用例标识ID，自定义参数名
###### autouse：默认False，若为True，刚每个测试函数都会自动调用该fixture,无需传入fixture函数名。
    autouse=True自动调用，无需传仍何参数，作用范围跟着scope走（谨慎使用）
###### inameds：通常来说使用 fixture 的测试函数会将 fixture 的函数名作为参数传递，但是 pytest 也允许将fixture重命名。如果使用了name,那只能将name传如，函数名不再生效。

#### conftest.py:@pytest.fixture()一般情况下与conftest.py一起使用。
    1.conftest.py单独存放@pytest.fixture()的方法.用处是可以存放多个py文件之间的共享前置. 
    2.conftest.py里面的方法在调用时,不需要导入,可以直接使用 
    3.conftest.py可以有多个,也可以有多个不同的层级

#### 2、设置用例执行顺序
##### @pytest.mark.run(order=)
    order：整型，设置执行顺序

#### 3、指定某个或者某组用例执行（在运行参数上进行设置，‘-m’,'分组名称'）
##### @pytest.mark.xxxx
    xxx：指分组名称。利用pytest.mark.xxxx对用例进行标识分组。

#### 4、指定跳过测试用例（根据特定的条件，不执行标识的测试函数.）
##### @pytest.mark.skipif(condition, reason="xxx")
###### 参数：
     condition：跳过的条件，必传参数
     reason：标注原因，必传参数
###### 使用方法：
    import pytest
    class Test_ABC:

        def test_a(self):
            print("------->test_a")
            assert 1
        @pytest.mark.skipif(condition=2>1,reason = "跳过该函数") # 跳过测试函数test_b
        def test_b(self):
            print("------->test_b")
                assert 0
    执行结果：
       ------->test_a #只执行了函数test_a

#### 5、函数数据参数化（方便测试函数对测试属于的获取，数据驱动）
#####   @pytest.mark.parametrize(argnames, argvalues, indirect=False, ids=None, scope=None)
##### 参数：
    argnames: 参数名
    argvalues:参数值（list[]、元组()、字典{}、字典值）
##### 用法：   
###### 用法一(基础用法)：
        @pytest.mark.parametrize('name', ['张三', '李四', '王五'])
        def test_print_name(self, name):
            print(name)

###### 用法二（解包）：
    @pytest.mark.parametrize('name,age', [['张三', '12'], ['李四', '15'], ['王五', '19']])
    def test_print_name2(self, name, age):
        print(name, age)

#### 6、标记为预期失败函数
#####  @pytest.mark.xfail(condition=None, reason=None, raises=None, run=True, strict=False)
##### 参数：
    condition：预期失败的条件，必传参数
    reason：   失败的原因，必传参数
















# 四、接口自动化测试框架封装(接口关联的封装)
#  一般情况下，通过一个关联的yaml文件来实现(yaml_util.py)

# 五、pytest接口测试的断言
# assert关键字

# 六、pytest结合allur-pytest生成allure测试报告
# 1、生成临时的json文件报告（直接在pytest.ini 中添加参数 --alluredir ./temp）
# 2、通过临时的json文件生成allure报告（os.system(allure generate temp -o temp/reports --clean)）
# 3、allure报告的定制
