# requests：
### 返回对象： Response<Response>
### 内置函数：
    request(method, url, args)： 向指定的url发送指定的请求方法

    delete(url, args)：          发送 DELETE请求
    get(url, params, args)：     发送 GET请求
    post(url, data, json, args)：发送 POST请求
    put(url, data, args)：       发送 PUT请求
    
    head(url, args)：            发送 HEAD请求
    patch(url, data, args)：     发送 PATCH请求

    
#### 参数类型：
    method	各种方法，比如get、options、head、post、put、patch、delete，当然也支持自定义扩展
    url	请求的url
    params	请求携带的params
    data	请求body中的data
    json	请求body中的json格式的data
    headers	请求携带的headers
    cookies	请求携带的cookies
    files	上传文件时使用
    auth	身份认证时使用
    timeout	设置请求的超时时间，可以设置连接超时和读取超时
    proxies	设置请求的代理，支持http代理以及socks代理（需要安装第三方库"pip install requests[socks]"）
    verify	用于https请求时的ssl证书验证，默认是开启的，如果不需要则设置为False即可
    stream	是否立即下载响应内容，默认是False，即立即下载响应内容
    cert	用于指定本地文件用作客户端证书
    allow_redirects：是否允许重定向，默认True，即允许重定向

### session() 会话控制,自动处理cookies，做状态保持。
    session = requests.session()

####  response类故名思议，它包含了服务器对http请求的响应。每次调用requests去请求之后，均会返回一个response对象，通过调用该对象，可以查看具体的响应信息。 示例如下：
    import requests

    r = requests.get('https://api.github.com/events', verify=False)
    print(r.status_code)
    print(r.content)
##### 属性或属性方法	解释
    r.status_code	响应的http状态码，比如404和200
    r.headers	响应头，可单独取出某个字段的值，比如(r.headers)['content-type']
    r.raw	        原始响应，表示urllib3.response.HTTPResponse对象。使用raw时，要求在请求时设置“stream=True”
    r.url	        请求的最终地址
    r.encoding	要解码的r.text的编码方式
    r.history	请求的历史记录，可以用于查看重定向信息，以列表形式展示，排序方式是从最旧到最新的请求
    r.reason	响应状态的描述，比如 "Not Found" or "OK"
    r.cookies	服务器发回的cookies，RequestsCookieJar类型
    r.elapsed	从发送请求到响应到达之间经过的时间量，可以用于测试响应速度。比如r.elapsed.microseconds表示响应到达需要多少微秒
    r.request	PreparedRequest对象，可以用于查看发送请求时的信息，比如r.request.headers查看请求头
    r.ok	        检查”status_code“的值，如果小于400，则返回True，如果不小于400，则返回False
    r.next	        返回重定向链中下一个请求的PreparedRequest对象
    r.content	响应的内容，byte类型
    r.text	        响应的内容，unicode类型
    r.links	        响应的解析头链接
    r.is_redirect	判断是否重定向，返回True or False
    r.is_permanent_redirect	判断是否永久重定向，返回True or False
    r.apparent_encoding	用chardet库判断出的编码方式
    r.content	返回响应的内容，以字节为单位
    r.json()	返回结果的 JSON 对象 (结果需要以 JSON 格式编写的，否则会引发错误)
    r.headers	返回响应头，字典格式
    r.close()	关闭与服务器的连接
    r.elapsed	返回一个 timedelta 对象，包含了从发送请求到响应到达之间经过的时间量，可以用于测试响应速度。比如 r.elapsed.microseconds 表示响应到达需要多少微秒。
    r.history	返回包含请求历史的响应对象列表（url）
    r.is_permanent_redirect	如果响应是永久重定向的 url，则返回 True，否则返回 False
    r.is_redirect	如果响应被重定向，则返回 True，否则返回 False
    r.iter_content()迭代响应
    r.iter_lines()	迭代响应的行
    r.links	        返回响应的解析头链接
    r.raise_for_status()	如果发生错误，方法返回一个 HTTPError 对象
    r.reason	响应状态的描述，比如 "Not Found" 或 "OK"
    

