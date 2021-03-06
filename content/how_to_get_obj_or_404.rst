get_obj_or_404注意
==================
:author: hackrole
:email: daipeng123456@gmail.com
:date: 2015-06-05 15:22:47
:tags: django
:category: programming


在写get_obj_or_404时的注意事项.

最好使用queryset而不是model，这样有更好的灵活性.
------------------------------------------------

.. code-block:: python

    # object example
    def get_obj_or_404(model, **kw):
        condition = Q(**kw)
        try:
            return model.objects.get(condition)
        except:
            raise NotFound("404, not found")
    # queryset example
    def get_obj_or_404(queryset, **kw):
        condition = Q(**kw)
        try:
            return queryset.get(condition)
        except:
            raise NotFound("404, not found")

exception处理
-------------

1) 对可能的异常要分开处理，如(unfound/multi/others). 上面的例子处理就有问题。

2) 通过re-raise一个特定异常，终断正常流程, 返回None的是很糟糕的设计.
