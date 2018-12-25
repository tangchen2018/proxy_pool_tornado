"""
-------------------------------------------------
   File Name：    DbClient.py
   Description :  DB工厂类
   Author :      	Tc 
   date：          2018/12/25
-------------------------------------------------
"""
__author__ = 'Tc'

from tornado.options import options

class DbClient(object):
	"""
    DbClient DB工厂类 提供get/put/pop/delete/getAll/changeTable方法

    目前存放代理的table/collection/hash有两种：
        raw_proxy： 存放原始的代理；
        useful_proxy_queue： 存放检验后的代理；

    抽象方法定义：
        get(proxy): 返回proxy的信息；
        put(proxy): 存入一个代理；
        pop(): 弹出一个代理
        exists(proxy)： 判断代理是否存在
        getNumber(raw_proxy): 返回代理总数（一个计数器）；
        update(proxy, num): 修改代理属性计数器的值;
        delete(proxy): 删除指定代理；
        getAll(): 返回所有代理；
        changeTable(name): 切换 table or collection or hash;


        所有方法需要相应类去具体实现：
            SSDB：SsdbClient.py
            REDIS:RedisClient.py  停用 统一使用SsdbClient.py

    """

	def __init__(self):
		"""
        init
        :return:
        """
		self.__initDbClient()

	def __initDbClient(self):
		from db.SsdbClient import SsdbClient
		self.client=SsdbClient(name=options.DB_name,host=options.DB_host,port=options.DB_port,password=options.DB_password)

	def get(self, key, **kwargs):
		return self.client.get(key, **kwargs)

	def put(self, key, **kwargs):
		return self.client.put(key, **kwargs)

	def update(self, key, value, **kwargs):
		return self.client.update(key, value, **kwargs)

	def delete(self, key, **kwargs):
		return self.client.delete(key, **kwargs)

	def exists(self, key, **kwargs):
		return self.client.exists(key, **kwargs)

	def pop(self, **kwargs):
		return self.client.pop(**kwargs)

	def getAll(self):
		return self.client.getAll()

	def changeTable(self, name):
		self.client.changeTable(name)

	def getNumber(self):
		return self.client.getNumber()


if __name__ == "__main__":
	import sys	
	sys.path.insert(0,'../')
	from configinit import setup
	setup()
	account = DbClient()
	account.changeTable('useful_proxy')
	print(account.getAll())
