from multiprocessing import cpu_count
 
# Server sockets
bind = '127.0.0.1:8001'  # See nginx vhost config.
backlog = 1024
 
workers = cpu_count() * 2 + 1
worker_class = 'gevent'
worker_connections = 1000
timeout = 30
keepalive = 2
 
# Debugging
#debug = True
debug = False
spew = False
 
# Server mechanics
daemon = False
pidfile = 'servegunicorn.pid'
umask = 0
user = None
group = None
tmp_upload_dir = None
 
# Logging
#loglevel = 'debug'
loglevel = 'error'
logfile = 'logs/gunicorn-log.log'
accesslog = 'logs/gunicorn-access.log'
errorlog = 'logs/gunicorn-error.log'
 
proc_name = None