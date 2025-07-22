# 关键字
# False await	else	import	pass
# None  break	except	in	raise
# True  class	finally	is	return
# and   continue	for	lambda	try
# as    def	from	nonlocal	while
# assert    del	global	not	with
# async elif	if	or	yield


# 普通语句，a，b，c 是 3 个变量，并且被赋值
# a = 1
# b = 2
# c = 3


# 单行语句，用 ; 分隔
# a = 1;b = 2;c = 3


# 多行语句，用 \ 换行，() [] 和 {} 括号包裹，自带换行符
"""
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a) # 45
"""
"""
a = (1 + 2 + 3 +
     4 + 5 + 6 +
     7 + 8 + 9)
print(a) # 45
"""
"""
a = [1, 2, 3,
     4, 5, 6,
     7, 8, 9]
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# 缩进，python 中以缩进来定义代码块结构
"""
a = True
if a:
    print("Hello")
    print("World")
    print("!")
else:
    print("Goodbye")
    print("World")
    print("!")
"""

# 给多个变量赋值
"""
a, b, c = 1, 2.5, "Hello"
print(a, b, c)  # 1 2.5 Hello
print(type(a), type(b), type(c))  # <class 'int'> <class 'float'> <class 'str'>
"""

# 给多个变量赋相同的值
"""
a = b = c = 1
print(a, b, c)  # 1 1 1
"""

# 常量，命名常量时，使用大写字母
# PI = 3.14
# print(PI)  # 3.14


# """ 和 ''' 可以定义多行字符串
# haha = """hello
# world!!!"""
# print(haha)
# hehe = '''hello
# world!!!'''
# print(hehe)
# print(haha == hehe) #  True
# xixi = ("hello "
#         "world!!!")
# print(xixi)
# print(haha == xixi) # False
# keke = 'hello world!!!'
# print(keke)
# print(xixi == keke) # True


# 列表
# fruits = ["apple", "mango", "orange"]  # 列表，索引从 0 开始，定义后可变
# print(fruits)  # ['apple', 'mango', 'orange']
# print(fruits[0]) # apple
# print(fruits[0:2]) # ['apple', 'mango']
# print(fruits[0:]) # ['apple', 'mango', 'orange']
# fruits[0] = "pear" # 定义后可变
# print(fruits) # ['pear', 'mango', 'orange']


# 元组
# numbers = (1, 2, 3)  # 元组，索引从 0 开始，定义后不可变
# print(numbers)  # (1, 2, 3)


# 字典
# alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # 字典，无序集合，可以存储键值对，可以是任意类型
# print(alphabets)  # {'a': 'apple', 'b': 'ball', 'c': 'cat'}


# 集合
# vowels = {'a', 'a', 'e', 'i', 'o', 'u'}  # 集合，无序，输出会自动去重，索引不可用
# print(vowels)  # {'a', 'e', 'i', 'o', 'u'} 或 {'u', 'o', 'i', 'a', 'e'} 顺序不固定，会自动去重


# 布尔
# a = True
# print(a) # True
# print(type(a)) # <class 'bool'>
# print(bool(0)) # False
# print(bool(1)) # True
# print(bool(0.0)) # False
# print(bool(0.1)) # True
# print(bool('')) # False
# print(bool(' ')) # True


# 数值
# a = 10 # 整数
# b = 3.14 # 浮点数
# c = 2 + 3j # 复数
# print(a) # 10
# print(type(a)) # <class 'int'>
# print(int(3.14)) # 3，截断，浮点转整数
# print(float(3)) # 3.0，整数转浮点
# print(float("3")) # 3.0，字符串转浮点
# print(complex(3)) # 3j，整数转复数
# print(hex(255)) # 0xff，整数转十六进制
# print(oct(255)) # 0o377，整数转八进制
# print(bin(255)) # 0b11111111，整数转二进制
# print(abs(-10)) # 10，绝对值
# print(divmod(10, 3)) # (3, 1)，10除3，返回商和余数
# print(pow(2, 3)) # 8，2的3次方
# print(round(3.14)) # 3，3.14四舍五入


# 数据类型转换，显式类型转换
# print(int(3.14))  # 3，截断，浮点转整数
# print(float(3))  # 3.0，整数转浮点
# print(str(3))  # '3'，整数转字符串
# print(bool(0))  # False，判断非零
# print(complex(3))  # 3j，整数转复数
# print(hex(255))  # 0xff，整数转十六进制
# print(oct(255))  # 0o377，整数转八进制
# print(bin(255))  # 0b11111111，整数转二进制
# print(set([1, 2, 3])) # {1, 2, 3}，序列转换，列表转集合
# print(tuple([1, 2, 3])) # (1, 2, 3)，序列转换，列表转元组
# print(list('abc')) # ['a', 'b', 'c']，序列转换，字符串转列表
# print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]，生成列表
# print(dict([('a', 1), ('b', 2)])) # {'a': 1, 'b': 2}，生成字典


# 数据类型转换，隐式类型转换
# num_int = 123
# num_flo = 1.23
# num_new = num_int + num_flo
# print("num_int的数据类型:", type(num_int))  # num_int的数据类型: <class 'int'>
# print("num_flo的数据类型:", type(num_flo))  # num_flo的数据类型: <class 'float'>
# print("num_new的值:", num_new)  # num_new的值: 124.23
# print("num_new的数据类型:", type(num_new))  # num_new的数据类型: <class 'float'>，为了防止丢失精度，Python会自动将整数转换为浮点数。


# 输出
# print(1, 2, 3, 4) # 1 2 3 4，默认情况下，print()函数会以空格分隔输出的参数，并添加一个换行符。
# print(1, 2, 3, 4, sep='*') # 1*2*3*4，使用sep参数可以指定分隔符。
# print(1, 2, 3, 4, sep='#', end='&') # 1#2#3#4&，使用end参数可以指定输出结束后的分隔符。
# print()
# x = 5; y = 10
# print('x的值为{}，y的值为{}'.format(x,y)) # x的值为5，y的值为10，使用format()函数可以格式化输出。
# print(f'x的值为{x}，y的值为{y}') # x的值为5，y的值为10，使用f-string可以格式化输出。
# print('I love {0} and {1}'.format('bread', 'butter')) # I love bread and butter，使用format()函数可以指定输出的顺序。
# print('I love {1} and {0}'.format('bread', 'butter')) # I love butter and bread
# print('Hello {name}, {greeting}'.format(greeting = 'Good morning', name = 'John')) # Hello John, Good morning，使用format()函数可以指定输出的参数名称。
# a = 12.3456789
# print('a的值为 %3.2f' %a) # a的值为 12.35，使用%-formatting可以格式化输出，%3.2f 中3是宽度，如果结果实际长度<3，会在前面补齐空格。
# print('a的值为 %3.4f' %a)  # a的值为 12.3457，使用%-formatting可以格式化输出。
# print('{0:<10} | {1:^10} | {2:>10}'.format('Left','Center','Right')) # Left       | Center     | Right，使用format()函数可以格式化输出。


# 输入
# num = input('请输入：')


# 导入
# 当我们的程序变得更大时，将其分解为不同的模块是一个好主意。
# 模块是包含Python定义和语句的文件。Python模块具有文件名，并以扩展名 .py 结尾。
# 可以将模块内部的定义导入另一个模块 或 Python中的交互式解释器。我们使用 import 关键字来做到这一点。
# import math
# print(math.sqrt(16)) # 4.0，使用math模块中的sqrt()函数可以求平方根。


# 算术运算符
# print(2 + 3)  # 5，加法
# print(2 - 3)  # -1，减法
# print(2 * 3)  # 6，乘法
# print(2 / 3)  # 0.6666666666666666，除法
# print(2 ** 3)  # 8，乘方
# print(2 // 3) # 0，除法结果取整
# print(2 % 3) # 2，取余


# 比较运算符
# print(2 > 3) # False，大于
# print(2 < 3) # True，小于
# print(2 >= 3) # False，大于等于
# print(2 <= 3) # True，小于等于
# print(2 == 3) # False，等于
# print(2 != 3) # True，不等于


# 身份比较运算符
# print(2 is 3) # False，判断两个对象是否相等
# print(2 is not 3) # True，判断两个对象是否不相等
# print((1, 2) != [1, 2]) # True，判断列表、元组、字典、集合等对象是否相等


# 成员运算符
# print(2 in [1, 2, 3]) # True, 判断对象是否在列表中
# print(2 not in [1, 2, 3]) # False, 判断对象是否不在列表中


# 逻辑运算符
# print(2 > 3 and 2 < 3) # False，逻辑与
# print(2 > 3 or 2 < 3) # True，逻辑或
# print(not 2 > 3) # True，逻辑非
# print(2 > 3 ^ 2 < 3) # True，逻辑异或
# print(2 > 3 and 2 < 3 or 2 > 3) # True，逻辑与或
# print(2 > 3 and (2 < 3 or 2 > 3)) # False，括号优先级
# print(2 > 3 and 2 < 3 or 2 > 3 and 2 < 3) # True，逻辑与或
# print(2 > 3 and 2 < 3 or 2 > 3 and 2 < 3) # True，逻辑与或


# 位运算符
# print(2 & 3) # 2，位与
# print(2 | 3) # 3，位或
# print(2 ^ 3) # 1，位异或
# print(~2) # -3，位非
# print(2 << 3) # 16，位左移
# print(2 >> 2) # 0.5，位右移


# 赋值运算符
# a = 1 # 赋值
# a += 1 # a = a + 1
# a -= 1 # a = a - 1
# a *= 1 # a = a * 1
# a /= 1 # a = a / 1
# a %= 1 # a = a % 1
# a **= 1 # a = a ** 1
# a //= 1 # a = a // 1
# a &= 1 # a = a & 1
# a |= 1 # a = a | 1
# a ^= 1 # a = a ^ 1
# a >>= 1 # a = a >> 1
# a <<= 1 # a = a << 1


# if 语句
# a = 1
# if a > 0:
#     print("a > 0")


# if .. else 语句
# a = 1
# if a > 0:
#     print("a > 0")
# else:
#     print("a <= 0")


# if .. elif .. else 语句
# num = float(input("输入数字: "))
# if num > 0:
#     print("正数")
# elif num == 0:
#     print("零")
# else :
#     print("负数")


# for 循环
# 使用索引遍历列表的程序
# genre = ['pop', 'rock', 'jazz']
# # 使用索引遍历列表
# for i in range(len(genre)):
#     print("I like", genre[i])


# for .. else 循环
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # 循环中没有找到任何 divisors
#         print(n, 'is a prime number')


# while 循环
# i = 1
# while i < 6:
#     print(i)
#     i += 1


# while .. else 循环
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print(i, " is no longer less than 6")


# break 语句
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break # 跳出循环
#     i += 1


# continue 语句
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue # 跳过当前循环
#     print(i)


# pass 语句
# sequence = {'p', 'a', 's', 's'}
# for val in sequence:
#     pass # 占位符，什么都不做

# 程序暂停
# while True:
#     pass


# 函数
# def greet(name):
#     """
#     这是一个打招呼的函数，
#     通过name参数传递，
#     要打招呼的人名
#     """
#     print("Hello, " + name + ". Good morning!")
# greet('Paul')
# print(greet.__doc__)


# 带 return 的函数
# def absolute_value(num):
#     """这个函数返回输入数字的绝对值"""
#     if num >= 0:
#         return num
#     else:
#         return -num
# print(absolute_value(2))
# print(absolute_value(-4))


# 函数参数
# def greet(name, msg):
#     """
#     通过name参数传递，
#     要打招呼的人名
#     """
#     print("Hello, " + name + ". " + msg)
# greet("Sally", "How do you do?")

# 关键字参数
# def greet(name, msg):
#     """
#     :param name:
#     :param msg:
#     :return:
#     """
#     print("Hello, " + name + ". " + msg)
# greet(msg="How do you do?", name="Sally")

# 默认参数
# def greet(name, msg="Good morning!"):
#     """
#     :param name:
#     :param msg:
#     :return:
#     """
#     print("Hello, " + name + ". " + msg)
# greet("Sally")

# 可变参数
# def greet(*names):
#     """
#     :param names:
#     :return:
#     """
#     for name in names:
#         print("Hello, " + name)
# greet("Sally", "Tom", "Kate")

# 关键字参数
# def greet(**names):
#     """
#     :param names:
#     :return:
#     """
#     for name, value in names.items():
#         print("Hello, " + name + ". " + value)
# greet(Sally="Good morning!", Tom="How do you do?", Kate="How are you?")


# 递归函数，默认最大递归深度为1000，超出会报错，结果为RecursionError
# def factorial(n):
#     """
#     整数阶乘的递归函数
#     :param n:
#     :return:
#     """
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# 栈溢出
# def precursor():
#     precursor()
# precursor()


# 匿名函数 Lambda，lambda arguments: expression，arguments 可以是多个，expression 只能一个
# lambda_factorial = lambda n: 1 if n == 1 else n * lambda_factorial(n - 1)
# print(lambda_factorial(5)) # 120

# 程序从列表中过滤出偶数项
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# print(new_list) # [4, 6, 8, 12]


# 全局变量、局部变量、非局变量
# x = 1
# def outer():
#     y = 2
#     def inner():
#         nonlocal y
#     y = 3
#     z = 3
#     print('inner function: nonlocal y =', y)
#     print('outer function: z =', z)
#     inner()
# print('outer function: global x =', x)
# outer()


# global 关键字
# c = 0 # 全局变量
# def add():
#     global c # 用 global 关键字声明 c 为全局变量，否则 c 为局部变量函数内无法修改，只有用 global 才能修改
#     c = c + 2 # increment by 2
#     print("Inside add():", c)
# add()
# print("In main:", c)

# 函数嵌套中的全局变量
# def foo():
#     x = 20
#     def bar():
#         global x # 函数嵌套中的全局变量，只有在全局才能读取
#         x = 25
#     print("在调用bar之前: ", x) # 20
#     print("立即调用bar")
#     bar()
#     print("在调用bar之后: ", x) # 20
# foo()
# print("x在主体内: ", x) # 25


# 模块
# import math # 导入 math 模块
# print(math.sqrt(16))
# from math import pi # 从 math 中只导入 pi
# print(pi)
# from math import * # 从 math 中导入所有
# print(sin(pi/2))
# import sys as system # 导入 sys 并命名为 system
# print(system.argv)

# 重新导入模块
# import imp
# import math
# import.reload(math)
# print(math.sqrt(16))

# 使用dir()函数可以列出模块内所有定义
# import math
# dir(math)


# 包
# 目录必须包含一个名为 __init__.py 的文件，Python才能认为这是一个包。
# 该文件可以保留为空，但是我们通常将该程序包的初始化代码放入此文件中。
# 下面是包的3种引用方式
# import Game.Level.start
# Game.Level.start.select_difficulty(2)
# from Game.Level import start
# start.select_difficulty(2)
# from Game.Level.start import select_difficulty
# select_difficulty(2)


# 闭包
# def outer():
#     x = 1
#     def inner():
#         nonlocal x
#         x = 2
#         print('inner function: x =', x)
#         return x
#     return inner
# print('outer function: global x =', outer())


# 列表推导式
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = [x for x in my_list if x%2 == 0]
# print(new_list)
