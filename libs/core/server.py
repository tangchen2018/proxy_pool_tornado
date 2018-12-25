import socket

import tornado.web
import tornado.httpserver
import tornado.ioloop

from tornado.options import define, options
from apis.urls import urls as apis_urls

class TApplication(tornado.web.Application):
	def __init__(self,*args,**kwargs):
		configs = {
			'gzip' : 'on',
			'debug' : True
		}
		super(TApplication, self).__init__(apis_urls,**configs)

class Server(object):
	
	def __init__(self,*args,**kwargs):
		pass

		#self.redis_db=redis_handler(options.DB_name,options.DB_host,options.DB_port,options.DB_password)
		#self.taskhandler=TaskHandler(time=self.time,redis_db=self.redis_db,mysql_db=self.mysql_db)

	def start(self):
	
		try:
			http_server = tornado.httpserver.HTTPServer(TApplication())
			http_server.listen(options.API_port)

			tornado.ioloop.IOLoop.instance().start()

		except socket.error as e:
			print('Socket Error: %s' % str(e))
		except KeyboardInterrupt as e:
			print('Gently Quit')
		except Exception as e:
			import traceback
			print(traceback.print_exc())
			
	def run(self):
		from multiprocessing import Process
		from libs.utils.ProxyValidSchedule import run as ValidRun
		from libs.utils.ProxyRefreshSchedule import run as RefreshRun

		p_list = list()
		p_list.append(Process(target=self.start, name='ProxyApiRun'))
		p_list.append(Process(target=ValidRun, name='ValidRun'))
		p_list.append(Process(target=RefreshRun, name='RefreshRun'))

		for p in p_list:
			p.daemon = True
			p.start()
		for p in p_list:
			p.join()

if __name__ == '__main__':
	run()
