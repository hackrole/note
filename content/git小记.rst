git小计
=======

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2014-12-12 15:15:38
:status: draft
:tags: git
:summary: 简单记下git使用中碰到的问题和解决思路.
:category: tools


git log使用
-----------

就目前来看git每次 commit都不会被删除,即便是reset --hard.
所有的commit会构成一颗复杂的树形流结构,git log可以用于查看commit列表

显示全部
~~~~~~~~

因为commit不会被删除,即便是reset --hard之后也可以再次reset回去,
不过为了获得commit hash,需要查看所有的commit.

之前一直碰到的一个问题, 就是一直习惯性, git log -a,不会报错,不过也不管用.
应该使用git log --all

不知道能不能只查看莫个branch的所有commit
""""""""""""""""""""""""""""""""""""""""
**TODO**

回退版本
--------

如果出现错误的提交或是bug, 需要把版本回头到上个可用版本.
或是错误的尝试先之后修改的代码完全删除掉.

使用chekcout
~~~~~~~~~~~~

checkout只能修改HEAD的位置,不能通过push等来改变远程库的状态.
因此如果是通过非git pull的方式部署的代码可能会无效(也许可以在部署代码时指定版本).

checkout checksum会将用户切换到一个未名的分支,需要check -b branch来创建分支,用于之后的合并等.

现在的理解是checkout回改变HEAD对应的提交,reset会修改当前分支对应的提交.

使用reset
~~~~~~~~~

reset + push -f 可以解决远程的版本后退.

要考虑的问题是如果是使用merge完成的提交,reset时也许会出现版本混乱无法回退的问题.
不过,本人实际测试中发现可以回退.具体待考察.

使用rebase来合并代码,可以构建更为合理的提交历史线,可以方便的做后退和撤销.

revert
~~~~~~

revert 会生成一个撤销莫次提交的新提交, 可以任意制定撤销那次.

如果commit是无法被删除的,那么这一操作并不推荐,因为每次revert的提交都不能删除,历史会比较混乱,还是推荐reset.
