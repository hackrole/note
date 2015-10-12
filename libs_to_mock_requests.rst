=======================
 如何mock requests模块
=======================


requests模块是非常好用的python http处理模块，使用场景很长广。
但是暂时不能自己创建Response导致mock不太方便.

通过搜索发现了两个lib可以处理.

httpretty/responses

httpretty模块是模仿ruby的FakeWeb所写.
responses模块是作者在使用httpretty时遇到问题，最后自己实现的一个less-featury版本.

两个模块亲测都可以使用，而且语法很相似，可以使用decoreate/with-context/start()+stop()语法，
使用很方便.

并且可以对不同的url,设置mock为不同的response,支持url正则语法等.

responses只有几百行代码，有时间可以读读源码.

通过httpretty，知道还有一个新的pip库curding, 具体待研究