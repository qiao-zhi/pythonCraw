import sys

list1 = ['zhangsan', 'lisi', 'wangyu']
#  直接打印集合
print(list1)

#  c从0开始，类似于java
print(list1[1])

# 负号代表倒着数
print(list1[-1])

#  打印集合长度
print(len(list1))

# 追加元素
list1.append("john")
print(list1)
print(list1[-1])

# 插入到指定位置
list1.insert(1, 'john1')
print(list1)

#  删除元素
#  删除最后一个元素
list1.pop()
print(list1)

#  删除指定位置的元素
del_o = list1.pop(0)  # del_0记录删除的元素
print(list1)
print(del_o)

#  修改(直接覆盖指定位置的值)


# 通过迭代器遍历list的两种方式(for和while)
it = iter(list1)  # 创建迭代器对象
for x in it:
    print(x, end=" ")

it1 = iter(list1)  # 创建迭代器对象
print()
while True:
    try:
        print(next(it1), end='  ')
    except StopIteration:
        sys.exit()
