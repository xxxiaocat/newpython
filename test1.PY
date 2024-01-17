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
    #三引号，可换行
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