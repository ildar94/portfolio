bind = '127.0.0.1:8000'
backlog = 2048
worker_class = 'sync'
loglevel = 'debug'
accesslog = '/var/log/gunicorn/access_log_back_store'
acceslogformat ="%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
errorlog =  '/var/log/gunicorn/error_log_back_store'