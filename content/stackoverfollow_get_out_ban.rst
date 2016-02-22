如何正确的使用stackoverflow
===========================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08 14:25:23
:tags: stackoverflow,how-to-ask-a-question,ask-for-help

关于屏蔽
--------

stackoverflow会自动屏蔽那些问了太多低质量问题的用户，阻止他们继续提出问题。
具体算法没有公开。但是基本是根据用户问题里的down-voted/zero-voted/deleted-posts量来定。
一两个低质量的问题不会被屏蔽。

被屏蔽后不能提问题，但是不影响其他功能.

如何脱离baned
-------------

只有作出一定的贡献才能脱离baned. baned是永久的，不会超时。

1) 不要问已存在的问题，问之前先试试stackoverflow的搜索功能.

2) 注意问题的语法和单词拼写检查.

3) 适当的格式化代码，保持可读性.

4) 提供及可能多的细节，和已做的努力。

5) 大声读出你的问题，确保能让他人理解你的问题.

良好的提问习惯
--------------

1) search and research. 保持search记录，让其他人知道为什么你的问题与他人的问题有所不同.

2) 写一个好的标题.

   1) 简短准确的概述你的问题，并和其他的问题标题有所不同.

   2) 拼写检查，语法,标点很重要.

   3) 如果你不好总结你的标题，可以在最后处理.

3) 在贴代码和异常前，先描述你的问题。让其他人能更容易理解你的问题.

4) 帮助他人重现你的问题.

   1) 代码要尽可能短小，不包含太多无关内容.

   2) 借助jsfiddle.com等第三方代码分享平台。

5) 添加上所有必要的tag.

6) 提交前仔细检查.

7) 如果发现遗漏内容应该尽快补齐，如果有他人回复应该尽快试验并提供反馈.

**TODO**
http://codeblog.jonskeet.uk/2010/08/29/writing-the-perfect-question/
http://www.catb.org/~esr/faqs/smart-questions.html
https://mikeash.com/getting_answers.html

如何正确的格式化你的问题
------------------------

代码需要用四个空格缩进。
使用``创建行内代码.
如果代码内包含`, 外层可以使用多层`包含
例子如下::

    **TODO image**


行尾增加两个空格，可以加入<br/>换行::

    *斜体* _斜体_ **加粗** __加粗__

使用如下方式添加链接::

    1) [Google](http://www.google.com).

    2) [Google][1].

        [1]: http://www.google.com

    3) [Yahoo!][yahoo].

        [yahoo]: http://www.yahoo.com/

使用如下方式确保naked url输出正常::

    <http://example.com>?


使用如下方式加入section::

    header1
    =======
    header2
    -------

下划线::

    ---

列表::

    - content
    + content
    * content

    1. content
    2. content
    7. content

blockquote::

    > the author is 
    > the way email
    > progmad adad


**TODO**
image

inline-html
tags
Spoilers
code-syntax-highlight
comment
