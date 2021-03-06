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
 * PHP 7.2 - swoole

### Test Comparison (Requests/sec)
 * darttest:                32682.07
 * gotest:                86434.56
 * groovyspringboosttest:                27803.93
 * h2otest:                53921.95
 * jrubytorqueboxtest:                35189.56
 * nodetest:                35412.58
 * phpswooletest:                51156.86
 * pypytest:                15204.38
 * python3aiohttptest:                 7592.93
 * python3test:                28413.94
 * pythontest:                10025.78
 * rustmiocotest:                73404.16
 * rusttest:                42359.07
 * scalatest:                52146.17

### Average Latency
 * darttest: 13.75ms
 * gotest: 1.11ms
 * groovyspringboosttest: 4.58ms
 * h2otest: 1.89ms
 * jrubytorqueboxtest: 2.73ms
 * nodetest: 5.23ms
 * phpswooletest: 17.35ms
 * pypytest: 3.04k
 * python3aiohttptest: 12.64ms
 * python3test: 5.12ms
 * pythontest: 2.48k
 * rustmiocotest: 1.30ms
 * rusttest: 725.99us
 * scalatest: 7.32ms

### Max Latency
 * darttest: 169.23ms
 * gotest: 88.88ms
 * groovyspringboosttest: 220.43ms
 * h2otest: 155.39ms
 * jrubytorqueboxtest: 29.00ms
 * nodetest: 127.98ms
 * phpswooletest: 251.90ms
 * pypytest: 7.75k
 * python3aiohttptest: 61.07ms
 * python3test: 128.05ms
 * pythontest: 9.25k
 * rustmiocotest: 3.88ms
 * rusttest: 8.96ms
 * scalatest: 498.91ms
