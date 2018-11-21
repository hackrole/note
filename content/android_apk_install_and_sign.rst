androiod下如何安装和对apk做sign
===============================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-07
:tags: android,react_native
:category: programming


尝试react-native的时候想把观望的example装到手机上。
但是只能装个debug版本，必须配合react-native server才能运行.
随后实验了下。想安装不需要服务器的release版本大致如下:

http://stackoverflow.com/questions/34630401/how-to-build-a-release-version-of-react-native-examples


1) 把js.bundle和apk文件一起打包.
   把react-native的js.bundle下载到android的asserts目录下.
   可以curl或react-native bundle.具体没研究太透。


2) 去掉调试模式.
   调用 gralde assembleRelease. 而不是gralde installDebug.

3) 之后对apk做签名, 具体如下:
    https://developer.android.com/tools/publishing/app-signing.html
    http://facebook.github.io/react-native/docs/signed-apk-android.html


**TODO** 有时间好好研究下android的签名打包的工具和流程

**TODO** 有时间窒息看下react-native的命令和运行机制
