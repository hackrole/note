anisble note
==============

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2019-01-23 10:30:39
:status: published
:tags: ansible
:category: programming

playbook组织
-------------

应该按项目组织playbook, 而不是按组件.

比如一个畅通的web应用, api-server, db, 负载均衡, redis-cache, 日志收集
应该在一个playbook里写,而不是分成四个play,每个装一块.

playbook的粒度控制在项目级别.

在hosts中列出host,之后按项目分好组.设置好组变量和全局变量.一般如果需要设置太多host变量,多半都是ansible组织出现问题.
简单变量可是使用hosts来完成,配合部分group vars_files, 少使用host vars_files

需要加密的信息使用ansible-vault


playbook编写注意
----------------

尽量保证每个playbook考虑周全,不然出现第一次跑ok,第二次跑就挂的情况.

还有可以考虑实现判断某一步是否已完成,避免每次都重复在一遍,也要考虑通过命令传参来强制跳过判断重复执行.

个人更喜欢用supervisor取代systemctl/init.d, supervisor加载新配制的方式是,
使用service supervisor restart的方式有不少问题.
.. code-block:: 

    - name: reload supervisor
      cmd: supervisorctl reread && supervisorctl update
    - name: ensure programming running
      supervisorctl:
        name: program
        state: started

supervisor记得设置minfds, 避免因为ulimits的问题无法启动进程,如elasticsearch


ansible系统加固
----------------

ansible有个用来加固系统的roles, 建议加上.
包亏一些sysctl配置都是运行linux server需要的.


roles
------

多使用roles, 使用ansible-galaxy查找roles, 每个roles记得查看支持的系统版本,
看看role的源码, 也可适当作出修改.

测试
-----

molecule官方推出的测试roles, playbook的工具, 文档比较少.
基于docker自动跑roles,完成测试.

本地也可以使用vagrant来测试.
