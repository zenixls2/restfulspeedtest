import socket
import sanic
from sanic.log import logger
from sanic.server import HttpProtocol
from multiprocessing import Process, Event
from signal import SIGTERM, SIGINT
from signal import signal as signal_func
import asyncio

# patch to allow pre-sock binding to cope with sock reuse 
# performance issue (lock) in processes
def serve_multiple(server_settings, workers, stop_event=None):
    if stop_event is None:
        stop_event = Event()
    server_settings['reuse_port'] = True
    signal_func(SIGINT, lambda s, f: stop_event.set())
    signal_func(SIGTERM, lambda s, f: stop_event.set())
    processes = []
    for _ in range(workers):
      process = Process(target=sanic.server.serve, kwargs=server_settings)
      process.daemon = True
      process.start()
      processes.append(process)

    for process in processes:
      process.join()

    # the above processes will block this until they're stopped
    for process in processes:
      process.terminate()
    server_settings.get('sock').close()

    asyncio.get_event_loop().stop()

def run(self, host="127.0.0.1", port=8000, debug=False, before_start=None,
            ssl=None, sock=None, workers=1, protocol=HttpProtocol,
            backlog=100, stop_event=None, register_sys_signals=True,
            access_log=True):
    server_settings = self._helper(
        host=host, port=port, debug=debug, ssl=ssl, sock=sock,
        workers=workers, protocol=protocol, backlog=backlog,
        register_sys_signals=register_sys_signals, access_log=access_log)

    try:
        self.is_running = True
        if workers == 1:
            sanic.server.serve(**server_settings)
        else:
            serve_multiple(server_settings, workers, stop_event)
    except:
        logger.exception(
            'Experienced exception while trying to serve')
    finally:
        self.is_running = False
    logger.info("Server Stopped")

sanic.server.serve_multiple = serve_multiple

from sanic import Sanic
from sanic.response import text

Sanic.run = run

app = Sanic(__name__, log_config=False)

@app.route("/")
async def test(request):
    return text("hello")

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
listener.bind(('0.0.0.0', 8080))
listener.listen(6)

app.run(host=None, port=None, sock=listener, debug=False, workers=6, access_log=False)
