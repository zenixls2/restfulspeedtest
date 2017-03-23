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

### Supported Frameworks / Languages
 * Dart 1.22.1 - isolate + Stream
 * Golang 1.8 - fasthttp + fasthttprouter
 * Nodejs 7.6.0 - cluster + http core
 * Python 2.17.13 - gevent.WSGIServer + multiprocess
 * Python 3.6.0 - sanic (httptools + uvloop + asyncio)
 * Pypy 5.7.0 - gevent.WSGIServer + multiprocess
 * Scala - Akka
 * Rust 1.15.1 - mioco
 * Rust 1.15.1 - Iron
 * C - lwan
