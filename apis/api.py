
import json

from apis.base import ApiBase
from tornado import web,gen,curl_httpclient,httpclient

from ProxyManager import ProxyManager

class ApiHelpHandler(ApiBase):

	@web.asynchronous
	def get(self,*args,**kwargs):
		api_list = {
			'get': u'get an usable proxy',
			'get_all': u'get all proxy from proxy pool',
			'delete?proxy=127.0.0.1:8080': u'delete an unable proxy',
			'get_status': u'proxy statistics'
		}

		self.finish(json.dumps(api_list,ensure_ascii=False))

class ApiGetHandler(ApiBase):

	@web.asynchronous
	def get(self,*args,**kwargs):
		proxy = ProxyManager().get()
		self.finish(proxy if proxy else 'no proxy!')

class ApiGetAllHandler(ApiBase):
	@web.asynchronous
	def get(self,*args,**kwargs):
		self.finish(str(ProxyManager().getAll()))

class ApiDelHandler(ApiBase):
	@web.asynchronous
	def get(self,*args,**kwargs):
		for proxy in self.get_arguments('proxy'):
			ProxyManager().delete(proxy)
		self.finish("success")

class ApiStatusHandler(ApiBase):
	
	@web.asynchronous
	def get(self,*args,**kwargs):
		self.finish(ProxyManager().getNumber())

