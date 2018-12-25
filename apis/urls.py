

from apis.api import ApiHelpHandler,ApiGetHandler,ApiGetAllHandler,ApiDelHandler,ApiStatusHandler

urls = [
	(r"/", ApiHelpHandler),
	(r"/get", ApiGetHandler ),
	(r"/get_all", ApiGetAllHandler),
	(r"/delete", ApiDelHandler),
	(r"/get_status", ApiStatusHandler),
]
