# python函数练习
# 1.python自带的一些常见函数的练习
print(abs(-95))
print(hash(-95))
print("sssssssssssssssss"+str(95))


# 2.自定义函数
def my_abs(a):
    if a >= 0:
        return a
    else:
        return -a


# 3.定义不带参数与返回值的函数(无返回值的函数类似于return None,可以简写为return)
def print_star():
    print("***********")


print_star()
x=print_star() #实际返回的为None
print(x)


# 4.多个返回值的函数定义以及使用方法(实际返回的是一个tuple，用多个值获取tuple的时候实际是将每个tuple的元素赋给对应的值)
def twoReturnValue():
    return 'a','b'

x, y = twoReturnValue();
print(x, y)
value=twoReturnValue()
print(value)



# 5.递归函数的用法(自己调用自己的函数)
# 5.1.计算裴波那契数列的第N个数字1 1 2 3 5 8 13 ...
def count(index):
    if index == 1:
        return 1
    if index == 2:
        return 1
    return count(index-1)+count(index-2)

print(count(7))
# 5.2计算N的阶乘
def jiecheng(n):
    if n==1:
        return 1
    else:
        return n*jiecheng(n-1)

print(jiecheng(3))


# 6.默认参数的用法
# 6.1默认参数求n的x次方，如果不传入n的话默认为2
def power(x, n=2):
    s=1
    while n > 0:
        s=s*x
        n=n-1
    return s
print(power(5,3))
print(power(5))

# 可变参数的用法(实际传入的是一个集合)
def fun3(*arg):
    print(len(arg))
    print(arg)
    for ele in arg:
        print(ele)

fun3(1,5,8,5)



# 定义一个空函数(pass关键字是空语句，是为了保持程序结构的完整性)
def fun4():
    pass

fun4()
