
"""
-------------------------------------------------
   File Name：    main.py
   Description :  运行主函数
   Author :       Tc
   date：         2018/12/24
-------------------------------------------------
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from tornado.options import define, options, Error
from config import config_insert

sys.path.insert(0,'./')

from libs.utils.configinit import setup

class Server(object):

	def runserver(self):
		setup()
		from libs.core.server import Server
		Server().run()

if __name__=='__main__':
	Server().runserver()
