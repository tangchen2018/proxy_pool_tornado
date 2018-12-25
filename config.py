
#Configure the database information
#Only support redis
DB=dict(
	host = 'localhost',
	port = 6379,
	name = 'proxy',
	password = '123456',
)

#[ProxyGetter]
ProxyGetter=dict(
	Run=[
		'freeProxyFirst',
		'freeProxySecond',
		'freeProxyThird',
		'freeProxyFourth',
		'freeProxyFifth',
		'freeProxySixth',
		'freeProxySeventh',
		'freeProxyEight',
		'freeProxyNinth',
		'freeProxyTen',
		'freeProxyEleven',
		'freeProxyTwelve',

		#foreign website, outside the wall
		'freeProxyWallFirst',
		'freeProxyWallSecond',
		'freeProxyWallThird',
	]
)

#[API]
# API config http://127.0.0.1:9999
# The ip specified when starting the web API
API=dict(
	port = 9999
)

config_insert=dict(
	DB = DB,
	API = API,
	ProxyGetter = ProxyGetter
)
