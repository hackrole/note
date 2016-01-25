django generic-view使用笔记
===========================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2015-06-08 15:32:35
:tags: django, style, python


做了一个django app, 由于数据库使用mongodb, 所以没法使用django-admin. 就自己写了个admin.
起初用的是最简单的一个视图一个函数，forms/generic-view都没用。但是问题很明显，容易出现bug，代码重复度很高。

后来改用django-generic view配合forms, 总的来是开发效率和代码质量确实会有不错的提升，但是相对的，代码逻辑被分散在各处，
即便是自己写的代码，过一段时间回头看都有点看不太懂。

所以这里坐下笔记，整理下django generic-view的功能和流程, 以及自己开发过程中的一些感想，以备后用.

与django-rest-framework的对比
-----------------------------

django-rest-framework里也有类似generic-view的概念。
两者的目的比较相似，都是为了减少重复代码，加快开发速度.

比较大的区别是:  适用目标不同.
django-rest-framework的目标是api接口，所以使用了get/post/delete/put/等method, 设计上就想是对一个model的CURD操作的映射。
django-generic-view的目标是web界面，所以只使用了get/post方法，设计上也不是一眼就能看出每个类的目的。

django-generic-view主要组成
---------------------------

最基础的View/TemplateView/RedirectView/StaticView等
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

listView
~~~~~~~~

提供对象列表视图

detailView
~~~~~~~~~~

单个对象的详情视图

formView/createView/updateView/deleteView
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

用于编辑信息的视图

yearView/monthView等暂时没理解
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

django-generic_view内部流程
---------------------------

listView
~~~~~~~~

实现了默认的get方法，
先调用get_queryset获取queryset, 之后通过paginate_querset对queryset进行分页.
之后通过调用get_context_data获取一些必要的context, 并把view/request放入其中，
之后调用render_to_response返回页面.

1) get_queryset默认返回但强的queryset属性，或者model.objects.all.

2) 可以重写get_queryset来返回特定的查询，结果会被设置到self.object_list.

3) 可以通过分页相关的属性或方法设置分页相关的流程。

4) 通过get_context_data可以获取额外的属性输出到页面.

5) render_to_response使用templateMixin来输出结果.

detailView
~~~~~~~~~~

实现默认的get方法.
先调用get_object方法获取对象,
之后通过get_context_data获取必要的context,
之后返回render_to_response方法

1) get_object默认会调用get_queryset来获取对象.

2) 可以通过定义slug_field等，设置get_object查询条件.

3) 通过定义get_context_data设置额外的页面属性.

formView
~~~~~~~~

实现默认的get方法，
通过get_form_class返回默认的form类，.
通过get_form来获取form实例，其中会调用get_initial(), get_prefix()获取form initial.
然后通过get_context_data获取必要的页面属性
之后通过render_to_response返回页面

1) 可以通过get_form_class这里返回特殊choices的form等.

2) 通过get_initial可以为form表单设置初始化值。

3) get_prefix作用还不明确

4) 通过get_context_data可以设置额外属性,比较enums.choices

实现默认的post方法
前面和get方法类似，通过get_form_class/get_form获取form实例。
之后调用form.is_valid,
如果成功，调用form_valid, 默认的实现会调用form.save()，然后redirect到success_url.
如果失败, 调用form_invalid, 默认实现或返回的form页面，此时form实例会携带错误信息.

1) 需要在页面上输出form的错误信息

2) 需要在form中实现save方法完成保存.

createView/updateview/deleteview
--------------------------------

使用modelForm实现, 暂时没看。
