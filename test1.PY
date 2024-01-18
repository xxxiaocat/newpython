#print("test ai")
#this is test word
a = int; a = 100;
b = bool; b=3>a;
c = float; c=123.123;
d = complex; d=1.1+12.2;

if b is True:
    print("is true \n yes")
    #\n是转义
else:
    print(r'is true \n yes')
    #r可以让特殊关键字不转义
    #单引号和双引号，作用一致
word = '123'
word1 = "1231"
word2 = """
123
123
123
123"""
    #三引号，可换行，可当作注释，本质为字段，不影响使用。虽然多行字符串在这里被当作多行注释使用，但它实际上是一个字符串，我们只要不使用它，它不会影响程序的运行。
""""
这些字符串在代码中可以被放置在一些位置，而不引起实际的执行，从而达到注释的效果。
"""

print (word2)
str='123456789'
print (str)
print(str[1])
#打印输出第二位，数组从0开始
print(str[0:-2])
#打印输出第一位到倒数第二位以前（不包含）的位置
print(str[2:6:2])
#打印输出第三位至第七位，且步长为2，即隔一位打印
print(str *2)
#打印两次
print(str + "123")
#打印且连接后续字符串进行打印

import sys;x="xiao";sys.stdout.write(x + "\n" )

print("word" ,word,"\n", end="")
#d打印多内容时，直接使用逗号隔开即可， 但关键词”end“需要在最后

import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
#导入包
from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
#导入特定包，轻量化？

#Python 数据类型转换可以分为两种：
    #隐式类型转换 - 自动完成
    #显式类型转换 - 需要使用类型函数来转换
A = 123;B=123.12
c=A + B;
print(c, type(c))
#a和b的转换，浮点可覆盖整型，为自动完成类型转换

num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("类型转换前，num_str 数据类型为:",type(num_str))

#num_str = int(num_str) 
# 强制转换为整型，如果不调用，则无法进行转换，代码报错
print("类型转换后，num_str 数据类型为:",type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:",num_sum)
print("sum 数据类型为:",type(num_sum))