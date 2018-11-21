移动开发版本管理相关
====================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08
:tags: tips
:category: design


before or afeter
----------------

做app开发，所有人都是倾向于尽一切可能把逻辑放到后台，
什么提示文字，按钮图标等. 

但是仔细向来这种方式欠缺考虑.

1) 如果提示文字只因app版本有关, 那写在前端更好。避免后台::

        if version == '1':
            message = ''
        elif version == '2':
            messagee = ''

2) 很多时候app版本的负担总是让所有后端苦不堪言，代码日益退化,优化无门.
   究其原因在于后端太重，在c/s开发模式上坚持b/s思路。无视富客户端的发展趋势.

3) 很多东西写在后台是为了灵活，可配置，倒是所有的可配置都意味着必须配置.
