基于tornado的爬虫IP代理池
====

下载安装
下载源码:
git clone git@github.com:tangchen2018/proxy_pool_tornado.git

安装依赖:
pip install -r requirements.txt
配置config.py:
config.py 为项目配置文件

# 配置Redis
-------
host = localhost  # db host
port = 8888       # db port
name = proxy      # 默认配置

# 配置 ProxyGetter
-------
freeProxyFirst  = 1  # 这里是启动的抓取函数，可在ProxyGetter/getFreeProxy.py 扩展
freeProxySecond = 1
....

# 配置 HOST (api服务)
port = 9999          # 监听端口
# 上面配置启动后，代理api地址为 http://127.0.0.1:9999
启动:
# 如果你的依赖已经安全完成并且具备运行条件,可以直接在运行main.py
# 到Run目录下:
>>>python main.py

# 如果运行成功你应该看到有4个main.py进程

Api
api	method	Description	arg
/	GET	api介绍	None
/get	GET	随机获取一个代理	None
/get_all	GET	获取所有代理	None
/get_status	GET	查看代理数量	None
/delete	GET	删除代理	proxy=host:ip
爬虫使用
　　如果要在爬虫代码中使用的话， 可以将此api封装成函数直接使用，例如：

import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code

def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy()
    while retry_count > 0:
        try:
            html = requests.get('https://www.example.com', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None
扩展代理
　　项目默认包含几个免费的代理获取方法，但是免费的毕竟质量不好，所以如果直接运行可能拿到的代理质量不理想。所以，提供了代理获取的扩展方法。

　　添加一个新的代理获取方法如下:

1、首先在GetFreeProxy类中添加你的获取代理的静态方法， 该方法需要以生成器(yield)形式返回host:ip格式的代理，例如:
class GetFreeProxy(object):
    # ....

    # 你自己的方法
    @staticmethod
    def freeProxyCustom():  # 命名不和已有重复即可

        # 通过某网站或者某接口或某数据库获取代理 任意你喜欢的姿势都行
        # 假设你拿到了一个代理列表
        proxies = ["139.129.166.68:3128", "139.129.166.61:3128", ...]
        for proxy in proxies:
            yield proxy
        # 确保每个proxy都是 host:ip正确的格式就行
2、添加好方法后，修改Config.ini文件中的[ProxyGetter]项：
　　在config.py的[ProxyGetter]下添加自定义的方法的名字:

[ProxyGetter]
;register the proxy getter function
freeProxyFirst  = 0  # 如果要取消某个方法，将其删除或赋为0即可
....
freeProxyCustom  = 1  # 确保名字和你添加方法名字一致
　　ProxyRefreshSchedule会每隔一段时间抓取一次代理，下次抓取时会自动识别调用你定义的方法。

问题反馈
　　任何问题欢迎在Issues 中反馈，如果没有账号可以去 我的博客中留言。

　　你的反馈会让此项目变得更加完美。
