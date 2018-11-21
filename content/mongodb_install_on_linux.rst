linux(ubuntu)下安装mongodb服务器
================================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08 14:34:30
:tags: mongodb
:category: programming


概述
----

安装过程可以参考观望，文档很详细.

ubuntu官网源有提供mongodb安装，但是一般版本都比较落后，更新不及时。
所以可以采用mongodb提供的安装源，安装最新的mongodb.

mongodb只为64-bit的长期支持版本提供安装源，即ubuntu12.04/ubuntu14.04. 其他版本也许可以使用，但是不推荐。

mongodb官网有5个主要的包:
1) mongodb-dev. meta-pacage. 自动安装其他四个包.
2) mongodb-org-server. mongod-daemon以及配置文件/init脚本
3) mongodb-org-mongos. mongos-daemon.
4) mongodb-org-shell. mongo-shell
5) mongodb-org-tools. mongoimport/mongodump/bsondump/mongoexport/retore/stat/perf/oplog等工具.

安装过程
--------

具体过程如下::

    # import mongodb GPK key
    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

    # add source
    # 12.04
    echo "deb http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
    # 14.04
    echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

    sudo apt-get update
    sudo apt-get install -y mongodb-org


如果想安装特定版本mongodb::

    # 如果只mongodb-org=3.2.0，会安装最新版本mongodb. 后面的必须也制定。
    sudo apt-get install -y mongodb-org=3.2.0 mongodb-org-server=3.2.0 mongodb-org-shell=3.2.0 mongodb-org-mongos=3.2.0 mongodb-org-tools=3.2.0


如果想使用老版本mongodb，同时阻止upgrade更新::

    echo "mongodb-org hold" | sudo dpkg --set-selections
    echo "mongodb-org-server hold" | sudo dpkg --set-selections
    echo "mongodb-org-shell hold" | sudo dpkg --set-selections
    echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
    echo "mongodb-org-tools hold" | sudo dpkg --set-selections


补充:手动安装mongodb
--------------------

实例过程如下::

    # 下载可用包.
    curl -O https://fastdl.mongodb.org/linux/mongodb-linux-i686-3.2.0.tgz

    # 解压
    tar -zxvf mongodb-linux-i686-3.2.0.tgz

    # copy to right locationi. and set $PATH.
    mkdir -p mongodb
    cp -R -n mongodb-linux-i686-3.2.0/ mongodb
    export PATH=<mongodb-install-directory>/bin:$PATH

补充:源码安装
-------------

mongodb使用python pycons做自动构建。需要先安装pyconds.

**TODO**
