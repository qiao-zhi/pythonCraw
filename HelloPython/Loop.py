# -----------------------for循环-----------------------
# 直接遍历list集合读取元素
list1=['zhangsan','lisi','wangwu','zhaoliu','tianqi']
for stu in list1:
    print(stu)

# 利用下标读取list元素
for i in range(len(list1)):
    print(list1[i])

#  含头不含尾(range函数是取开头到结束前一个，如果第一个没有的话是0)
for k in range(5):
    print(k,)

for j in range(2,5):
    print(j)

# -------------------------while循环---------------------------
y=0
while y<10:
    print(y)
    y=y+1



