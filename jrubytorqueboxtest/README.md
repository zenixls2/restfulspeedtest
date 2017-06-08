#JRuby + Torquebox
------------------

### Installation
```bash
rvm install jruby
jruby -S gem install bundler
jruby -S bundle install
```

### Execution
```bash
jruby -S torquebox run -b 0.0.0.0 -e production -p 8080
```

or use script provided by me:

```bash
./run.sh
```

