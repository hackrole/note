golang1.5编译失败及gvm安装golang报错
====================================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2015-09-02 15:22:11
:tags: golang, gvm, golang1.5


golang现在使用两套编译安装策略。

golang1.4使用gcc编译。
golang1.5需要使用golang1.4编译

所以需要先下载golang1.4编译安装。然后设置GOROOT_BOOTSTRAP变量为go1.4的主目录。
之后就可以编译golang1.5或是使用gvm安装golang了。

1) gvm使用前需要source ~/.gvm/bin/gvm.

2) gvm使用时最好配置下https代理，不然会很慢.
