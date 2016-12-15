import socket
from sanic import Sanic
from sanic.response import text
app = Sanic(__name__)

@app.route("/")
async def test(request):
    return text("hello")

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
listener.bind(('0.0.0.0', 8080))
listener.listen(4)

app.run(host=None, port=None, sock=listener, debug=False, workers=4)
