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
 * Golang 1.8 - fasthttp + fasthttprouter
 * Nodejs 7.6.0 - cluster + http core
 * Python 2.17.13 - gevent.WSGIServer + multiprocess
 * Python 3.6.0 - sanic (httptools + uvloop + asyncio)
 * Pypy 5.7.0 - gevent.WSGIServer + multiprocess
 * Scala 2.12.2 - Akka
 * Rust 1.15.1 - mioco
 * Rust 1.15.1 - Iron
 * C - lwan
 * Groovy (Java) - Spring Boot 1.5.3

### Test Comparison
 * darttest:                32682.07
 * gotest:                71763.95
 * groovyspringboosttest:                27803.93
 * h2otest:                53921.95
 * nodetest:                45577.53
 * pypytest:                15204.38
 * python3test:                38492.04
 * pythontest:                10025.78
 * rustmiocotest:                72021.24
 * rusttest:                45998.79
 * scalatest:                52146.17
