from gevent.wsgi import WSGIServer
from gevent.pool import Pool
from gevent.monkey import patch_all; patch_all()
import socket
from multiprocessing import Process
import time
def application(env, start_response):
    if env['PATH_INFO'] == '/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b"Hello"]
    else:
        print env['PATH_INFO']
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('', 8080))
listener.listen(8)
def serve_forever(listener):
    WSGIServer(listener, application, spawn=Pool(), log=None).serve_forever()
number_of_processes = 8
for i in range(number_of_processes):
    Process(target=serve_forever, args=(listener,)).start()

while True:
    time.sleep(5)
