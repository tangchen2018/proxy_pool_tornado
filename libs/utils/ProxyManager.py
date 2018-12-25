# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：	 ProxyManager.py
   Description :
   Author :	    Tc
   date：	      2018/12/14
-------------------------------------------------
"""

__author__ = 'Tc'

import random

from LogHandler import LogHandler
from utilFunction import verifyProxyFormat
from getFreeProxy import GetFreeProxy

from tornado.options import options


class ProxyManager(object):
	"""
	ProxyManager
	"""

	def __init__(self):
		from db.DbClient import DbClient
		self.db = DbClient() 
		self.raw_proxy_queue = 'raw_proxy'
		self.log = LogHandler('proxy_manager')
		self.useful_proxy_queue = 'useful_proxy'

	def refresh(self):

		self.db.changeTable(self.raw_proxy_queue)
		for proxyGetter in options.ProxyGetter_Run:
            # fetch
			try:
				self.log.info(
					"{func}: fetch proxy start".format(func=proxyGetter))
				for proxy in getattr(GetFreeProxy, proxyGetter.strip())():
                    # 直接存储代理, 不用在代码中排重, hash 结构本身具有排重功能
					proxy = proxy.strip()
					if proxy and verifyProxyFormat(proxy):
						self.log.info('{func}: fetch proxy {proxy}'.format(
							func=proxyGetter, proxy=proxy))
						self.db.put(proxy)
					else:
						self.log.error(
							'{func}: fetch proxy {proxy} error'.format(
								func=proxyGetter, proxy=proxy))
			except Exception as e:
				self.log.error(
					"{func}: fetch proxy fail".format(func=proxyGetter))
				continue

	def get(self):
		self.db.changeTable(self.useful_proxy_queue)
		item_dict = self.db.getAll()
		if item_dict:
			return random.choice(list(item_dict.keys()))
		return None

	def delete(self, proxy):
		self.db.changeTable(self.useful_proxy_queue)
		self.db.delete(proxy)

	def getAll(self):
		self.db.changeTable(self.useful_proxy_queue)
		item_dict = self.db.getAll()
		return list(item_dict.keys()) if item_dict else list()

	def getNumber(self):
		self.db.changeTable(self.raw_proxy_queue)
		total_raw_proxy = self.db.getNumber()
		self.db.changeTable(self.useful_proxy_queue)
		total_useful_queue = self.db.getNumber()
		return {
			'raw_proxy': total_raw_proxy,
			'useful_proxy': total_useful_queue
		}


if __name__ == '__main__':
	pp = ProxyManager()
	pp.refresh()
