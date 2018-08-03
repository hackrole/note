minikube tips
=============

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2018-08-03 10:23:01
:status: publish
:tags: minikube,k8s,tips


minikube搭建issuses
-------------------

1) 启动失败

最新的28.2版本有bug,使用25.2版本

同时25.2版本应该使用kvm,kvm2启动会失败

注意要`rm -rf ~/.minikube`删除旧文件

国内须开启代理,代理不能使用127.0.0.1,
不然docker pull会失败.
须设置no_proxy=192.168.99.0/24

.. code-block:: bash

    https_proxy=192.168.88.242:8118 minikube start --docker-env https_proxy=192.168.88.242:8118 --docker-env http_proxy=192.168.88.242:8118 --docker-env no_proxy=192.168.99.0/24 --vm-driver kvm


启动后验证是否成功:

.. code-block:: bash

    minikube status
    kubectl cluster-info
    kubectl get pod --all-namespaces=true
    minikube dashboard
