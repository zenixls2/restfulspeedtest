var http = require('http');
var cluster = require('cluster');
var numCPUs = require('os').cpus().length;
function handleRequest(request, response) {
    response.end("Hello");
}
if (cluster.isMaster) {
    for (var i = 0; i < numCPUs; i++) {
        cluster.fork();
        cluster.on('exit', (worker, code, signal) => {});
    }
} else {
    var server = http.createServer(handleRequest);
    server.listen(8080, function(){});
}
