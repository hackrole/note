oauth2
======

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2018-05-03 13:40:09
:status: draft
:tags: oauth2,
:cateory: programming

desc
-----
open authorization

rfc 6749 6750 6819

四种模式
--------

1) 授权码模式(auth code)

2) 简化模式(implicit)

3) 密码模式(resource owner password credentials)

4) 客户端模式(client credentials)


关键参数
--------

1) response_type(code/token)

2) client_id(客户端id)

3) redirect_url

4) scope(权限范围)

5) state(用于传参数)

6) code(授权码)

7) grant_type(authorization_code/password/clientcredentials)

8) access_token/refresh_token/expires_in/scope/token_type


others
------

1) code only once usable.

2) 2 vs 1(token-timeout)

3) four roles

