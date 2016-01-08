GAE datastore相关
=================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08 15:12:17
:tags: GAE, datastore

about Key
---------

Key is a kind-identifier pairs,
kind default to be the Kind-string,
and can be change be rewrite the model's _get_kind() method.
identifier can be auto and handed by the app

Key can have a sequence of parent, which I'm lookforward to.

| api                    | desc                                         |   |
| ndb.Key(kind, ident)   | get a key object                             |   |
| Entity(..).put()       | create a Entity object and return it keys    |   |
| key.get()              | from the key get the entity object           |   |
| key.kind()             | return the kind string                       |   |
| key.id()               | return the ident string                      |   |
| key.parent()           | return a parent key                          |   |
| key.urlsafe()          | return a url-encode string(using in hte url) |   |
| Key(urlsafe=urlString) | get a key from the urlsafe() string          |   |
|                        |                                              |   |

about Entity
------------

a Entity a key-properties Object
the key can't be change after create.

the Entity can define some hooks-method, for the put or delete and so on

| api                          | desc                                            |                             |
| Entity()                     | new a Entity obj                                |                             |
| Entity().put()               | insert-or-update the Entity and return it's key |                             |
| Entity().key.delete()        | delete a  Entity                                | note the operate on the key |
| Entity().put_multi()         | put multi/return multi                          |                             |
| Entity().delee_multi([keys]) | delete multi                                    |                             |

query
-----

