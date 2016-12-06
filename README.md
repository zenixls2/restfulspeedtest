# Speed Test for Microservice Frameworks in Different Languages

### Brief Introdution
Just start the project for personal interests.
Some projects might be lack of performance tuning, so any contribution is welcomed.
This project is still in its early stages, and only one simple case is tested.

### Test Environment
All the tests are run using
```bash
wrk -c50 -d10s -t50 http://localhost:8080
```
on top of a MacBook Pro (Retina, 13-inch, Early 2015).

Due to lack of NUMA and other Linux specific libraries' support,
some frameworks or libraries such as Facebook proxygen still cannot be tested. Plan to re-run the whole project using a ubuntu Docker image in the future, or using some EC2 instances to run the test

### Supported Frameworks / Languages
Dart - isolate + Stream
Golang - fasthttp + fasthttprouter
Nodejs - cluster + http core
Python - gevent.WSGIServer + multiprocess
Scala - Akka
