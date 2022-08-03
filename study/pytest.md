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
    模块级别:    setup_module、teardown_module
    函数级别:    setup_function、teardown_function，不在类中的方法
    类级别 :     setup_class、teardown_class
    方法级别:    setup_method、teardown_method
    方法细化级别: setup、teardown


###  三、修饰器
#### 1、Fixture参数详解及使用（实现部分的用例的前后置）
###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fixture修饰器来标记固定的工厂函数,在其他函数，模块，类或整个工程调用它时会被激活并优先执行,通常会被用于完成预置处理和重复操作。
##### 1.Fixture的使用方式：
    @pytest.fixture(scope="", params="", autouse=True, ids="", name="")  

##### 2.参数：
    scope     作用域  函数/类/模块/包/session(会话)
    params    数据驱动
    autouse   自动执行
    ids       自定义参数名
    inameds   重命名

###### 2.1 &nbsp;作用域 scope（控制范围）
    function    函数级 每一个函数或方法都会调用。
    class	    模块级 每一个.py文件调用一次。
    module	    块级(包) 每一个.py文件调用一次。
    session	    会话级 每次会话只需要运行一次，会话内所有方法及类，模块都共享这个方法.
###### 2.2 &nbsp;params（可选形参列表--数据驱动）：(list类型、元组、元组加字典、列表加字典)提供参数数据，供调用标记方法的函数使用，可与参数ids一起使用，作为每个参数的标识，被Fixture装饰的函数要调用是采用：Request.param
    @pytest.fixture(scope="function", autouse=False, params=["wjy", "lhh", "nug"])
    def test(request):
        yield request.param

###### 2.3  &nbsp;ids：用例标识ID，自定义参数名
###### 2.4  &nbsp;autouse：默认False，若为True，刚每个测试函数都会自动调用该fixture,无需传入fixture函数名。
    autouse=True自动调用，无需传仍何参数，作用范围跟着scope走（谨慎使用）
###### 2.5  &nbsp; inameds：通常来说使用 fixture 的测试函数会将 fixture 的函数名作为参数传递，但是 pytest 也允许将fixture重命名。如果使用了name,那只能将name传如，函数名不再生效。

##### 3、Fixture的调用方式：
    1、将fixture名称作为测试用例函数的输入参数
    2、测试用例加上装饰器：@pytest.mark.usefixtures(fixture_name)
    3、fixture设置autouse=True
###### &nbsp;  &nbsp; &nbsp; &nbsp; 调用注意事项点：
    1、在类声明上面加 @pytest.mark.usefixtures() ，代表这个类里面所有测试用例都会调用该fixture
    2、可以叠加多个 @pytest.mark.usefixtures() ，先执行的放底层，后执行的放上层
    3、可以传多个fixture参数，先执行的放前面，后执行的放后面
    4、如果fixture有返回值，用 @pytest.mark.usefixtures() 是无法获取到返回值的，必须用传参的方式（第一种调用方式）
##### 4、Fixture之yield实现后置
###### 4.1 &nbsp; yield注意事项：
    1、如果yield前面的代码，即setup部分已经抛出异常了，则不会执行yield后面的teardown内容
    2、如果测试用例抛出异常，yield后面的teardown内容还是会正常执行
###### 4.2 &nbsp; yield+with的结合
    # 官方例子
    @pytest.fixture(scope="module")
    def smtp_connection():
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp_connection:
            yield smtp_connection  # 提供夹具值
###### 4.3 &nbsp; addfinalizer 终结函数
    @pytest.fixture(scope="module")
    def test_addfinalizer(request):
        # 前置操作setup
        print("==再次打开浏览器==")
        test = "test_addfinalizer"
    
        def fin():
            # 后置操作teardown
            print("==再次关闭浏览器==")
    
        request.addfinalizer(fin)
        # 返回前置操作的变量
        return test
    
    
    def test_anthor(test_addfinalizer):
        print("==最新用例==", test_addfinalizer)
###### &nbsp; &nbsp; &nbsp;  addfinalizer 终结函数使用注意事项
    1、如果 request.addfinalizer()前面的代码，即setup部分已经抛出异常了，则不会执行 request.addfinalizer() 的teardown内容（和yield相似，应该是最近新版本改成一致了）
    2、可以声明多个终结函数并调用


#### 4.5 conftest.py
&nbsp;&nbsp;&nbsp; &nbsp; 可以理解成一个专门存放fixture的配置文件 ,@pytest.fixture()一般情况下与conftest.py一起使用。多个测试用例文件（test_*.py）的所有用例都需要用登录功能来作为前置操作，那就不能把登录功能写到某个用例文件中去了。

注意事项：

    1、pytest会默认读取conftest.py里面的所有fixture
    2、conftest.py 文件名称是固定的，不能改动
    3、conftest.py只对同一个package下的所有测试用例生效
    4、不同目录可以有自己的conftest.py，一个项目中可以有多个conftest.py
    5、测试用例文件中不需要手动import conftest.py，pytest会自动查找
#### 4.6 &nbsp;  fixture传参数 request的详细使用
案例一：传单个参数

    import pytest

    @pytest.fixture()
    def login(request):
        name = request.param
        print(f"== 账号是：{name} ==")
        return name

    data = ["pyy1", "polo"]
    ids = [f"login_test_name is:{name}" for name in data]

    @pytest.mark.parametrize("login", data, ids=ids, indirect=True)
    def test_name(login):
        print(f" 测试用例的登录账号是：{login} ")
结果：

    collecting ... collected 2 items
    
    10fixture_request.py::test_name[login_test_name is:pyy1] == 账号是：pyy1 ==
    PASSED          [ 50%] 测试用例的登录账号是：pyy1 
    
    10fixture_request.py::test_name[login_test_name is:polo] == 账号是：polo ==
    PASSED          [100%] 测试用例的登录账号是：polo 
知识点:

    1、添加  indirect=True  参数是为了把 login 当成一个函数去执行，
       而不是一个参数，并且将data当做参数传入函数。
    2、def test_name(login) ，这里的login是获取fixture返回的值
案例二：多个参数

    @pytest.fixture()
    def logins(request):
        param = request.param
        print(f"账号是：{param['username']}，密码是：{param['pwd']}")
        return param

    data = [
        {"username": "name1", "pwd": "pwd1"},
        {"username": "name2", "pwd": "pwd2"},
    ]

    @pytest.mark.parametrize("logins", data, indirect=True)
    def test_name_pwd(logins):
        print(f"账号是：{logins['username']}，密码是：{logins['pwd']}")
结果：

    10fixture_request.py::test_name_pwd[logins0] 账号是：name1，密码是：pwd1
    PASSED                      [ 50%]账号是：name1，密码是：pwd1
    
    10fixture_request.py::test_name_pwd[logins1] 账号是：name2，密码是：pwd2
    PASSED                      [100%]账号是：name2，密码是：pwd2
知识点：

    如果需要传多个参数，需要通过字典去传。

案例三：多个fixture（只加一个装饰器）
    
    # 多个fixture
    @pytest.fixture(scope="module")
    def input_user(request):
        user = request.param
        print("登录账户：%s" % user)
        return user
    
    @pytest.fixture(scope="module")
    def input_psw(request):
        psw = request.param
        print("登录密码：%s" % psw)
        return psw

    data = [
        ("name1", "pwd1"),
        ("name2", "pwd2")
    ]
    
    @pytest.mark.parametrize("input_user,input_psw", data, indirect=True)
    def test_more_fixture(input_user, input_psw):
        print("fixture返回的内容:", input_user, input_psw)

执行结果

    10fixture_request.py::test_more_fixture[name1-pwd1] 登录账户：name1
    登录密码：pwd1
    PASSED               [ 50%]fixture返回的内容: name1 pwd1
    
    10fixture_request.py::test_more_fixture[name2-pwd2] 登录账户：name2
    登录密码：pwd2
    PASSED               [100%]fixture返回的内容: name2 pwd2
     

案例四：多个fixture（叠加装饰器）
  
    @pytest.fixture(scope="function")
    def input_user(request):
        user = request.param
        print("登录账户：%s" % user)
        return user

    @pytest.fixture(scope="function")
    def input_psw(request):
        psw = request.param
        print("登录密码：%s" % psw)
        return psw
    
    name = ["name1", "name2"]
    pwd = ["pwd1", "pwd2"]
    
    @pytest.mark.parametrize("input_user", name, indirect=True)
    @pytest.mark.parametrize("input_psw", pwd, indirect=True)
    def test_more_fixture(input_user, input_psw):
        print("fixture返回的内容:", input_user, input_psw)

执行结果

    10fixture_request.py::test_more_fixture[pwd1-name1] 登录账户：name1
    登录密码：pwd1
    PASSED               [ 25%]fixture返回的内容: name1 pwd1
    
    10fixture_request.py::test_more_fixture[pwd1-name2] 登录账户：name2
    登录密码：pwd1
    PASSED               [ 50%]fixture返回的内容: name2 pwd1
    
    10fixture_request.py::test_more_fixture[pwd2-name1] 登录账户：name1
    登录密码：pwd2
    PASSED               [ 75%]fixture返回的内容: name1 pwd2
    
    10fixture_request.py::test_more_fixture[pwd2-name2] 登录账户：name2
    登录密码：pwd2
    PASSED               [100%]fixture返回的内容: name2 pwd2

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
###### 用法一&nbsp;(基础用法)：
        @pytest.mark.parametrize('name', ['张三', '李四', '王五'])
        def test_print_name(self, name):
            print(name)

###### 用法二&nbsp;（解包）：
    @pytest.mark.parametrize('name,age', [['张三', '12'], ['李四', '15'], ['王五', '19']])
    def test_print_name2(self, name, age):
        print(name, age)

#### 6、标记为预期失败函数
#####  @pytest.mark.xfail(condition=None, reason=None, raises=None, run=True, strict=False)
##### 参数：
    condition：预期失败的条件，必传参数
    reason：   失败的原因，必传参数

###  四、断言
#### 1、常用断言
######  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pytest 里面断言实际上就是 python 里面的 assert 断言方法，常用的有以下几种：
    assert xx ：判断 xx 为真
    assert not xx ：判断 xx 不为真
    assert a in b ：判断 b 包含 a 
    assert a == b ：判断 a 等于 b
    assert a != b ：判断 a 不等于 b
 #### 1、异常断言



###  五、pytest-rerunfailures（失败用例重跑插件）







[//]: # ()
[//]: # (# 四、接口自动化测试框架封装&#40;接口关联的封装&#41;)

[//]: # (#  一般情况下，通过一个关联的yaml文件来实现&#40;yaml_util.py&#41;)

[//]: # ()
[//]: # (# 五、pytest接口测试的断言)

[//]: # (# assert关键字)

[//]: # ()
[//]: # (# 六、pytest结合allur-pytest生成allure测试报告)

[//]: # (# 1、生成临时的json文件报告（直接在pytest.ini 中添加参数 --alluredir ./temp）)

[//]: # (# 2、通过临时的json文件生成allure报告（os.system&#40;allure generate temp -o temp/reports --clean&#41;）)

[//]: # (# 3、allure报告的定制)
