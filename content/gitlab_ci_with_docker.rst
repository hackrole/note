###################
gitlab CI 相关
###################

******************
起步
******************

1) 安装gitlab-runner, 可以使用docker或apt安装,推荐apt安装方便使用。推荐使用清华镜像加速.
    具体参见: qinghua_mirror_site_for_gitlab_runner_

2) 注册gitlab-runner到gitlab.单个项目注册需要有项目admin权限，全局注册需要有gitlab admin权限
    具体参见: gitlab_runner_register_

3) 在项目中添加.gitlab_ci.yml 和Dockerfile(使用docker在ci，方便环境隔离).具体可参考mobile_devices.
    gitlab_ci配置参见: gitlab_ci_job_ref_
    gitlab_dind参见: gitlab_ci_build_docker_ gitlab_ci_docker_executor_

4) 推送项目到远程，查看构建结果. 地址格式: https://git.haomaiyi.com/web/<project_name>/pipelines

******************
杂项
******************

1) 项目需要补齐单元测试，建议统一使用py.test, 可以方便集成coverage和老的unittest.实现可以参考mobile_devices

2) 现在gitlab CI 需要做的事情就是在推送后build一个docker镜像用于调试, 之后在docker中跑单元测试和收集coverage信息.
    后续可以加入staging/test环境自动/手动部署功能

3) gitlab CI 跑起来比较耗时，出问题调试也比较麻烦，所以建议推送前先在本地验证单元测试已通过.可以使用ptw自动监听跑单元测试.

4) gitlab CI如果未能按预期跑,可以使用::

    # 如下方式调试
    # 需要注意的是,本地需要配置一个简单的docker和docker register,以及安装gitlab_runner
    sudo gitlab_runner exec docker <task-name>

    # 另外,gitlab_runner不会使用/etc/gitlab_runner/config.toml配置，会导致build docker没有权限
    ## build docker使用如下方式调试.
    sudo gitlab-runner exec docker --docker-privileged --docker-volumes /var/run/docker.sock:/var/run/docker.sock build_docker

******************
docker相关
******************

1) 这边使用docker在CI, 需要注意docker build很耗时。所以使用将环境和代码全部打包到docker内的方式来构建镜像.

2) 未防止多个代码分支要构建多个镜像, 将代码clone到docker中，并保留了一个有读权限的ssh-key,所以可以在镜像中通过
    git checkout -t $CI_COMMEIT_REF来切换到对应分支做测试.

3) 理论上应该只在必要时构建docker镜像，现在没找到比较好的方式来做.

4) docker构建建议参考dockerfile最佳实践: dockerfile_best_practices_

.. note::

    构建docker镜像时务必使用.dockerignore忽略pyc和__pycache__文件，不过在docker中使用代码时会报错.
    也可以考虑在构建镜像后删除pyc和__pycahce__文件.



.. _qinghua_mirror_site_for_gitlab_runner: https://mirror.tuna.tsinghua.edu.cn/help/gitlab-runner/
.. _gitlab_runner_register: https://docs.gitlab.com/runner/register/
.. _gitlab_ci_job_ref: https://docs.gitlab.com/ee/ci/yaml/
.. _gitlab_ci_build_docker: https://docs.gitlab.com/ce/ci/docker/using_docker_build.html
.. _gitlab_ci_docker_executor: https://docs.gitlab.com/runner/executors/docker.html
.. _dockerfile_best_practices: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
