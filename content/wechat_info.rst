###################
微信开发相关
###################

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2018-05-04 10:56:35
:status: draft
:tags: wechat,develop

******************
本地调试
******************

现在已在测试环境部署了一个用来调试wechat的环境.使用ssh端口转发,通过nginx代理到ssh端口.

:域名: ngrok.haomaiyi.com
:端口: 8080

使用方式::

    # 本地启动服务, 如果
    python manage.py runserver 0.0.0.0:8000
    # 启动ssh 端口转发
    ssh -vnNT -R 0.0.0.0:8080:localhost:8000 <yourname@121.40.102.202>
    # 之后可以在使用ngrok.haomaiyi.com作为微信回调地址，
    # 请求会被转发到本地,可以方便调试

.. note::

    -R 使用远程端口转发，会在121.40.102.202上开启8080端口（已固定写的nginx转发配置里), 并将对应的请求转发到本地8000(需要和本地服务器端口一致)

    ngrok.haomaiyi.com域名已备案，所以可以用来在正式微信公众号中使用，并调试.


******************
微信开发者工具
******************

微信手机端调试比较麻烦，且浪费时间。
可以参考使用微信官方的开发者工具调试。


微信oauth认证可以使用ipython自行编码一个url,放到开发者工具中调试.
只需按文档凭借url,并替换掉其中redirect_url, 注意redirect_url需要做转码.

实例url::

    https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx4002be6f5b7b5acf&redirect_uri=http%3A%2F%2Fngrok.haomaiyi.com%2Fmobile_devices%2Funionid_login%2F%3Faccount_name%3Dmoda_polso&response_type=code&scope=snsapi_base&state=STATE#wechat_redirect

微信开发者工具: `wechat_devtools <https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1455784140>`_

.. note::

    需注意，需要绑定帐号到公众号才能调试，具体参见上面文档.


******************
微信网页oauth认证
******************

微信oauth有sns_base和sns_userinfo两种授权方式,

我们这边走的是sns_base静默认证,不能直接通过 /sns/userinfo接口获取用户信息.

需要通过oauth认证后获取openid, 再通过 /user/info接口获取用户信息。

1) 如果用户未关注，则获取的信息内容为空.

2) 获取unionid也走此流程，需要将公众号绑定到开放平台.

oauth sns_userinfo获取用户信息接口(未使用): wechat_oauth_sns_userinfo_doc_

获取用户信息或unionid接口: wechat_get_userinfo_doc_

微信开放平台: wechat_open_site_

.. _wechat_oauth_sns_userinfo_doc: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140842
.. _wechat_get_userinfo_doc: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140839
.. _wechat_open_site: https://open.weixin.qq.com/


