react起步须知
=============

author: hackrole
email: daipeng123456@gmail.com
date: 2015-12-31
tags: react,browserify-debug,react-get-started
title: react起步须知
summary: 总结react起步需要的内容.

起步须知
--------

1) react当前0.14, react-awesome上很多使用的是0.13的例子，所以要看情况使用.

2) react跑实例的三种方式:

   1) 在浏览器上测试,要引入react/react-dom/babel, 并设置text/babel. 如下
    <script src="libs/react/0.14.5/react.js"></script>
    <script src="libs/react/0.14.5/react-dom.js"></script>
    <script src="libs/babel-core/5.8.23/browser.min.js"></script>

    <script type="text/babel" src="scripts/example.js"></script>
    <script type="text/babel">
    </script>

    这种方式只应该在测试阶段使用.

   2) 使用browserify转化所有文件为一个bundle.js.  文件内要使用require/expects等.如下
      browserify -t [ babelify --presets [react] ] public/scripts/main.js --debug -o public/build/bundle.js

      推荐的方式. 通过添加debug参数方便调试，正式部署要去掉.

   3) 引入react/reactdom, 同时离线使用babel转化jsx.
    <script src="libs/react/0.14.5/react.js"></script>
    <script src="libs/react/0.14.5/react-dom.js"></script>

    <scirpt src="bundle.js"></script>

    babelify --presets react main.js -o bundle.js

3) 要熟悉babelify和browserify的使用。也可以更进一步考虑,grunt/glun工具

4) 了解如何在服务端渲染reactjs.

5) flux为何物？
