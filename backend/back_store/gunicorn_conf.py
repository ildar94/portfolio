bind = '0.0.0.0:8000'
backlog = 2048
worker_class = 'sync'
loglevel = 'debug'
accesslog = '/usr/src/app/access_log_back_store'
acceslogformat ="%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
errorlog =  '/usr/src/app/error_log_back_store'