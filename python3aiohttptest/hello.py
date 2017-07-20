import asyncio
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
import socket
from aiohttp import web
from signal import SIGTERM, SIGINT
from signal import signal as signal_func
from multiprocessing import Process, Event

WORKERS=4
async def handle(request):
    return web.Response(text="hello")

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
listener.bind(('0.0.0.0', 8080))
listener.listen(6)


def main():
    loop = asyncio.new_event_loop()
    app = web.Application()
    app.router.add_get('/', handle)
    web.run_app(app, sock=listener, loop=loop)
    #web.run_app(app, sock=listener)

processes = []
for _ in range(WORKERS):
    process = Process(target=main)
    process.daemon = True
    process.start()
    processes.append(process)

for process in processes:
    process.join()

for process in processes:
    process.terminate()
listener.close()
#for l in loops:
#    l.stop()
#    l.close()
