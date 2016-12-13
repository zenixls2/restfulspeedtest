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
        print(env['PATH_INFO'])

def serve_forever(listener):
    WSGIServer(listener, application, spawn=Pool(), log=None).serve_forever()
def main():
    number_of_processes = 6
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(('0.0.0.0', 8080))
    listener.listen(4)
    for i in xrange(number_of_processes):
        Process(target=serve_forever, args=(listener,)).start()

    while True:
        time.sleep(5)

main()
