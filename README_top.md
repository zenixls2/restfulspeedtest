# Speed Test for Microservice Frameworks in Different Languages

### Brief Introdution
Just start the project for personal interests.
Some projects might be lack of performance tuning, so any contribution is welcomed.
This project is still in its early stages, and only one simple case is tested.

### Test Environment
All the tests are run using
```bash
wrk --latency -t12 -d10s -c100 http://localhost:8080/
```
on top of a MacBook Pro (Retina, 13-inch, Early 2015).

Python3.6 introduced several improvements including some code from uvloop
merged into asyncio. However, uvloop still outperforms. See [Issue #26081](http://bugs.python.org/issue28544) and [Issue #26081](https://bugs.python.org/issue26081).

Due to lack of NUMA and other Linux specific libraries' support,
some frameworks or libraries such as Facebook proxygen still cannot be tested. Plan to re-run the whole project using a ubuntu Docker image in the future, or using some EC2 instances to run the test.

For some languages with JIT implementation, the cold-start time should be considered. We should run at least 3 times of tests beforehand to warm-up the service.

### Supported Frameworks / Languages
 * Dart 1.22.1 - isolate + Stream
 * Golang 1.9.1 - fasthttp + fasthttprouter
 * Nodejs 8.5.0 - cluster + http core
 * Python 2.17.13 - gevent.WSGIServer + multiprocess
 * Python 3.6.4 - sanic 0.7.0 (httptools + uvloop + asyncio)
 * Python 3.6.1 - aiohttp 2.2.3
 * Pypy 5.7.0 - gevent.WSGIServer + multiprocess
 * Scala 2.12.2 - Akka
 * Rust 1.19.0 - mioco 0.8.1
 * Rust 1.19.0 - Iron 0.5.1
 * C - lwan
 * Groovy (Java) - Spring Boot 1.5.3
 * JRuby - Torquebox 4.0.0 Beta3

