

from tornado.web import RequestHandler

class HomeHandler(RequestHandler):

	def __init__(self,*args,**kwargv):
		super(HomeHandler, self).__init__(*args, **kwargv)	

	@property
	def redis_db(self):
		return self.application.redis_db
