a='abc'
b=a
print("a="+a)
print("b="+b)

print("-----华丽的分割线------")

a='ABC'
print("a="+a)
print("b="+b)





print("-----华丽的分割线------")
c=1
d=c
print("c=", c)
print("d=", d)
print("-----华丽的分割线------")

c=2
print("c=", c)
print("d=", d)


# 字符串前面加r代表所有的字符串都是字符串本身，不需要转义
print("-------------华丽的分割线------------")
print(r"sssssss\ \n")

#  三个单引号可以进行多行字符串操作(敲回车相当于加了个\n),多行字符串前面也可以加r表示raw字符串
str1='''
\ w
 wwwwwwww
 wwwwwwww
'''
print(str1)

str2=r'''
SSSSSSSSSSSS \n \t
\t \n
'''
print(str2)

print(r'''
he 
said 
"I'm ok"
''')


# unicode编码集使用
print(u"中国")








