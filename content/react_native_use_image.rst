react-native中的如何加载图片
============================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-03-02 15:53:58
:status: draft
:tags: reactjs, react-native, ios

如何使用image标签
-----------------

要想使用本地问题，需要把文件放到和index.ios.js相对目录下,
然后使用require来加载, 使用require加载会把文件bundle到ios/imagesets中.
同时可以使用 `@x2 @x3, .ios .android` 等语法来区分平台和尺寸.

似乎默认中的是 .png文件，如果使用.jpg需要制定后缀. 但是估计会有影响.

.. code-block:: javascript

   <Image source={require("a.png")} />

也可以通过uri来制定，此时文件需要自己手动放到ios项目的imagesets目录下.

.. code-block:: javascript

   <Image source={{uri: "a.png"}} />

如果想使用远程文件可以使用如下语法.

.. code-block:: javascript

   <Image source={{uri: http://github.com/tt/tt.jpg}} />

TabBarIOS中的icon
-----------------

icon使用类似image, 可以require或uri.

另外有个systemIcon属性可以用来使用系统自带的图标。有大约10个.
