python数据分析twitter相关
=========================
:author: hackrole
:email: daipeng123456@gmail.com
:date: 2015-05-26 15:35:14
:tags: python, data_analizer, social_data


twitter提供了一系列的api使得可以通过api来分析twitter数据，获取最热话题等.
主要用于社交化数据分析. python端有python-twitter模块包装了常用的twitter api.

代理问题
--------

国内由于长城网的关系，twitter被屏蔽. python-twitter也没法使用.
所幸最近看issues, 代理问题是否已经有其他的commit解决，并合并.

使用export http_proxy环境变量的方式来使用.

区分twitter/python-twitter的区别
--------------------------------

twitter是官网放出来的包, python-twitter是github上开源的代码。
有时间比较下两者的区别和优劣.
