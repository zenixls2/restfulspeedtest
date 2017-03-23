from gevent.wsgi import WSGIServer
from gevent.pool import Pool
import gevent
from gevent.monkey import patch_all; patch_all()
import socket
from multiprocessing import Process, Event
import sys
import signal

import time
def application(env, start_response):
    if env['PATH_INFO'] == '/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b"Hello"]
    else:
        print(env['PATH_INFO'])

def serve_forever(listener):
    WSGIServer(listener, application, spawn=Pool(), log=None).serve_forever()


processes = []
def killall():
    for process in processes:
        try:
            process.terminate()
        except OSError:
            pass
    sys.exit(0)

def main():
    number_of_processes = 6
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(('0.0.0.0', 8080))
    listener.listen(number_of_processes)
    sighandler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    gevent.signal(signal.SIGINT, killall)
    gevent.signal(signal.SIGTERM, killall)
    for i in xrange(number_of_processes):
        process = Process(target=serve_forever, args=(listener,))
        process.daemon = True
        process.start()
        processes.append(process)

    try:
        for process in processes:
            process.join()
    except:
        pass

    for process in processes:
        process.terminate()

    listener.close()

if __name__ == '__main__':
    main()
