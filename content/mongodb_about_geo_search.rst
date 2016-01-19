mongodb 地理位置查询tips
========================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2014-05-15 17:29:34
:status: draft
:tags: mongodb, geo-search,


+ geo可以和其他字段生成联合索引

+ find($near)查询无法返回距离.

+ runcommand(geoNear)可以返回距离，不过这个距离不是经纬度计算出来的距离。
   可以考虑通过坐标在查询后完成计算， 如使用python haversine库: https://github.com/hackrole/haversine

+ 使用2d搜应的$near查询只能返回100个文档，无论是count,还是skip都是如此

+ 使用2dsphere索引的查询无此限制,居于球面计算，距离更加精确，是2d索引的取代。

+ 地理位置索引不能和其他的特殊索引一起使用，如:$text

+ 对于分片服务器，不能使用near查询，要换成geonear命令或是$geoNear aggregation stage

+ geoNear只能返回按距离排序的文档，必要时可能需要在内存中排序文档，会导致性能问题，可以考虑用$geowithin取代。

+ 分片服务器中，地理位置索引字段不能做为分片字段使用.
