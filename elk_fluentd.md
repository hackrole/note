Title: fluentd note
Date: 2019-03-14
Category: programming
Tags: elk,fluentd
Author: hackrole
Email: hack.role@gmail.com

# structured log by fluentd

[centralize log from python with fluentd](https://docs.fluentd.org/v0.12/articles/python)

[run ELK fluentd with docker](https://docs.fluentd.org/v0.12/articles/docker-logging-efk-compose)


可以自行编译一个Dockerfile,来构建一个更方便使用的image
```Dockerfile
FROM fluent/fluentd:v0.12-debian

RUN gem install fluent-plugin-elasticsearch --no-rdoc --no-ri --version 1.9.7
ADD ./fluent.conf /fluentd/etc/
```

实例fluentd配置如下:
```config
# accept log from 24224, and forward to es
<source>
  @type forward
  port 24224
  bind 127.0.0.1
</source>
<match *.**>
  @type copy
  <store>
    @type elasticsearch
    # this is env you can pass while start docker with `-e ES_HOST=''`
    host "#{ENV['ES_HOST']}"
    port 9200
    logstash_format true
    logstash_prefix fluentd
    logstash_dateformat %Y%m%d
    include_tag_key true
    type_name access_log
    tag_key @log_name
    flush_interval 1s
  </store>
  <store>
    # for debug
    @type stdout
  </store>
</match>
```

可以通过使用docker network host来方便使用
```shell
docker rm --name fluent --network host --restart always --log-driver json-file --log-opt max-size=10m --log-opt max-file=3 -d -e ES_HOST={{ es_host }} <image_name>
```

## 使用python发送日志

[fluent python bind](https://github.com/fluent/fluent-logger-python)

[django fluentd log(not working as I try)](https://github.com/jayfk/django-fluentd)

```python
from fluent import sender
from fluent.event import Event

sender.setup("tag_name")
# this would seed event to fluend,
# if fluend stop or elasticsearch stop, this will not raise error
# so just add it.
Event("sub_tab_name", {"data": "data"})
```

# structlog package

[structlog](http://www.structlog.org/en/stable/index.html)

[structlog example](https://codywilbourn.com/2018/08/23/playing-with-python-structured-logs/)
