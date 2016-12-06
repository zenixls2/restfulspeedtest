import 'dart:io';
import 'dart:async';
import 'dart:isolate';

import 'package:isolate/isolate_runner.dart';
import "package:isolate/ports.dart";
import "package:isolate/runner.dart";

typedef Future RemoteStop();

Future<RemoteStop> runHttpServer(
    Runner runner, int port, HttpListener listener) async {
  var stopPort = await runner.run(_startHttpServer, [port, listener]);

  return () => _sendStop(stopPort);
}

Future _sendStop(SendPort stopPort) => singleResponseFuture(stopPort.send);

Future<SendPort> _startHttpServer(List args) async {
  int port = args[0];
  HttpListener listener = args[1];

  var server =
      await HttpServer.bind(InternetAddress.ANY_IP_V4, port, shared: true);
  await listener.start(server);

  return singleCallbackPort((SendPort resultPort) {
    sendFutureResult(new Future.sync(listener.stop), resultPort);
  });
}

class HttpListener {
  final SendPort _counter;
  StreamSubscription _subscription;

  HttpListener(this._counter);

  Future start(HttpServer server) async {
    _subscription = server.listen((HttpRequest request) async {
      await request.response.addStream(request);
      request.response
        ..write("Hello")
        ..close();
    });
  }

  Future stop() async {
    await _subscription.cancel();
    _subscription = null;
  }
}

Future main() async {
  var counter = new ReceivePort();
  HttpListener listener = new HttpListener(counter.sendPort);
  ServerSocket socket = await ServerSocket
      .bind(InternetAddress.LOOPBACK_IP_V4, 8080, shared: true);
  var isolates = await Future
      .wait(new Iterable.generate(5, (_) => IsolateRunner.spawn()),
          cleanUp: (isolate) {
    isolate.close();
  });
  List<RemoteStop> stoppers =
      await Future.wait(isolates.map((IsolateRunner isolate) {
    return runHttpServer(isolate, socket.port, listener);
  }), cleanUp: (server) {
    server.stop();
  });

  await socket.close();
  ProcessSignal.SIGINT.watch().listen((ProcessSignal signal) {
    for (var stopper in stoppers) {
      stopper();
    }
    counter.close();
    exit(0);
  });
}
