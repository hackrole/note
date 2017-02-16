 elixir官网教程笔记
====================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2017-02-16 11:35:59
:status: draft
:tags: elixir learn


introduction
------------

1) iex 跑交互

2）elixir 跑脚本或编译

3) elixirc 编译文件

后续使用mix处理项目相关

basic type
----------

type list
~~~~~~~~~

1) integer

2) float 64bit

3) boolean (true/false)

4) atom/symbol (:true)

5) string "elixir"

6) list [1, 2, 3]

7) tuple {ok, "ok"}

8) char-list/Port/Reference/PID

几本运算
~~~~~~~~

div 整除
rem 取余
round 四舍五入
trunc 截整

函数识别
~~~~~~~~

函数名 + 参数个数

is_boolean
is_integer
is_number
is_atom
...

h() iex下帮助命令

atom
~~~~

求值结果为自身

true/false 为atom

strings
~~~~~~~

双引号，单引号为char-list
utf8支持
类似ruby的字符串插值表达式

IO.puts/1 输出

本质为binaries

is_binary
byte_size
String.length utf8-size

String Module utils

匿名函数
~~~~~~~~

add = fn a, b -> a + b end
add.(1, 2)
is_function(add)
is_function(add, 2)o

调用需要加 .(),和命名函数做区分

支持闭包

列表
~~~~

链表实现

length [1, 2, 3]
[1,2] ++ [3]
[1,2,3] -- [3]
hd([1, 2, 3])
tl([1, 2, 3])

可打印列表会打印为char-list

i/1 在iex中获取变量信息

元组
~~~~

连续存储

t = {:ok, "hello"}
tuple_size t
elem(t, 1)
tuple_size(t)
put_tuple(t, 1, "world")

byte_size *_size常数时间
String.length *_length线性时间

基础运算
--------

[1, 2] ++ [3]
[1, 2, 3] -- [3]

"foo" <> "bar"

and/or/not 只接受boolean,短路运算
||/&&/! 接受所有类型值,false/nil外都没true

弱类型
1 == 1.0
1 === 1.0
number < atom < reference < function < port < pid < tuple < map < list < bitstring

模式匹配
--------

= 是模式匹配，不是赋值

只有左边变量会被赋值
1 = x # error

{a, b, c} = {:ok, "world", 42}
{:ok, a} = {:ok, "world"}
[a, b, c] = [1, 2, 3]

# error
{a, b, c} = {:ok, true}
{a, b, c} = [1, 2, 3]

列表hd/tl
[head | tail] = [1, 2, 3]
list = [1, 2]
[0 | list]

变量可以重新binding,和erlang不同. 指定^强制不重新绑定
x = 1
x = 2
^x = 1 # error

_ 和_variable 来避免警告未使用变量

左边不能是函数调用，求值规则限制


case/cond/if
------------
case 可以使用guards
x = 1

case {1, 2, 3} do
  {4, 5, 6} ->
    "not"
  {1, ^x, 3} when x > 0 ->
    "match"
  _ ->
    "always match"
end

guards中可以使用的表达式
比较运算/布尔运算(only and/or/not)/算术运算/<>/in/type_check function/plus some function(bit_size)

用户可以自定义guards, 参考BitWise.
guards出错不会跑异常，支持让guards失败

匿名函数也可以有多case和guards,参数个数需一样

f = fn
  x, y when x > 0 -> x + y
  x, y -> x * y

cond do
  2 + 2 == 5 ->
    "this will not be true"
  2 * 2 == 3 ->
    "not true"
  1 + 1 == 2 ->
    "will"
end

if/unless是宏实现

if true do
  "true"
end
unless true do
  "false"
end

Kernal module文档

do end
~~~~~~

do .. end === do: ...
多行与单行

if true, do: 1 + 1, else: 1+2
if true, do: (
 1 + 1
 1 + 2
)

二进制/字符串/char-list
-----------------------

字符串本质是binaries
is_binary("hello")

bytes(0-255)与code point(utf8 code)
String.codepoints("中国")

?获取code point值
?a
?中

binary与bitstrings
------------------
binary 8bits
bitstrings not 8bits
截断/指定长度/与<<0>>链接

<<0, 1, 2, 3>>
String.valid?(<<238, 191, 191>>)

<<255>>
<<256>> # <<0>>
<<256 :: size(16)>> # <<1, 0>>
<<256 :: utf8>> # utf8 code point
<<256 :: utf8, 0>> # <<196, 128, 0>>

bitstrigns
<<1 :: size(1)>>
<<2 :: size(1) >> <<0 :: size(1)>>
is_bitstring(<<1 :: size(1)>>)
bit_size(<<1 :: size(1)>>) # 1

char-list is codepoint-list
to_charlist "hello"
to_string 'hello'
to_string :hello

keywords and maps
-----------------

keyword-list
list = [a: 1, b: 2]
第一个元素为atom
本身是一个list,有排序
key可以重复
用来给函数传options的手段
Keyword-module

maps key-value store
map = %{:a => 1, 2 => :b}
map[:a]
map[:c] # nil
可以使用任意值做key
无排序
很适合做模式匹配，允许部分匹配
%{:a => a} = %{:a => 1, :b => 2}
Map-module

使用如下语法可更新map,不能add new-key
map = %{:a => 1, 2 => "one"}
%{map  2 => "two"}

如果所有key都是atom,可以如下定义
map = %{a: 1, b: 2}
map.a


使用put_in/update_in／get_update_in来更新嵌套结构
users = [jorn: %{name: "johN"}]
users[:john].name
users = put_in users[:john].name, "John"