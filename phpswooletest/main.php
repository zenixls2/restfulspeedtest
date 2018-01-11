<?php
$http = new swoole_http_server("127.0.0.1", 8080);
$http->set([
    'worker_num' => 6,
    'backlog' => 128,
    'open_cpu_affinity' => true,
    'open_tcp_nodelay' => true,
]);
$http->on("start", function($server) {
    echo "launched\n";
});
$http->on("request", function($request, $response) {
    $response->end("Hello World");
});
$http->start();
