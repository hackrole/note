docker笔记
==========

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2018-07-09 12:49:56
:tags: docker
:category: tools

docker registry nginx 403
-------------------------

使用官方教程部署nginx/registry成功,
使用host nginx失败.

原因: 本机nginx不支持加密，使用md5解决

.. code-block:: bash

    # use crypt
    sudo docker run --rm --entrypoint htpasswd registry:2 -Bbn test test > htpasswd
    # use md5
    sudo docker run --rm --entrypoint htpasswd registry:2 -mbn test test > htpasswd
    # TODO nginx logs

# TODO stackoverflow links

docker push 504 timeout
-----------------------

nginx config (proxy_read_timeout 10m) 解决

.. code-block:: nginx

    # default 60s, for bigger images may 504
    proxy_read_timeout 10m


docker pull ELK fails
---------------------

dns was pollocate, using *stubby* to fix it.

# TODO stubby links

.. code-block:: bash

    sudo stubby
    dig @127.0.0.1 facebook.com
    docker pull docker.elastic.co/logstash/logstash-oss:6.2.4


docker registry oss and distribution
------------------------------------

set oss location and key/token

https://github.com/docker/distribution
