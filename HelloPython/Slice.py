# 切片

# ###########         List切片(切出来的还是一个list)         ############
L = ['haha', 'xixi', 'hehe', 'heihei', 'gaga']
# 含头不含尾
# 1.利用整数从前向后切片
# 1.1取index从1到3的，包含1不包含3
print(L[1:3])
# 1.2从0取到3(去掉第一个值默认从0开始取元素)
print(L[:3])


# 2.传入负数代表从最后取值
# 2.1取倒数第三个到倒数第一个(包含倒数第三个不包含倒数第一个)
print(L[-3:-1])
# 2.2从倒数第三个取到末尾
print(L[-3:])


# 3.按指定间隔切片(传入三个参数，第三个参数代表步长)
L1=[0,1,2,3,4,5,6,7,8,9,10]
# 3.1从0到10每2个取一个
print(L1[0:10:2])
# 3.2从头到尾每两个取1个
print(L1[::2])

# ###########         字符串切片(切出来的还是一个字符串)         ############
str='ABCDEFG'
# 下标从0到2
print(str[0:2])
# 从头到尾，每两个取一个
print(str[::2])
# 从第二个到结尾，每两个取一个
print(str[2::2])


# ###########         tuple切片 (切出来的还是一个tuple)        ############
tuple = ('zhangsan','lisi','wangwu','zhaoliu')
# 取下标从1到2的，包含1不包含2
print(tuple[1:2])
# 从开始到下标为2，包含开头不包含2
print(tuple[:2])
# 从头到尾，每两个取一个
print(tuple[::2])
# 到倒数第三个到末尾，每两个取1个
print(tuple[-3::2])












