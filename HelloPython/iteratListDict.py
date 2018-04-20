# 迭代list和map的用法
# 1.迭代list
# 使用enumerate方法。
L = ['zhangsan', 'lisi', 'wangwu']
# 使用enumerate方法处理集合后集合变为包含tuple的集合    [(0,'zhangsan'),(1,'lisi'),(2,'wangwu')]
# tuple的特性是:拿一个元素接tuple会将整个tuple赋给此元素，拿与tuple长度相等元素接tuple会将tuple的值依次赋给元素
# 第一种遍历方法
for index,value in enumerate(L):
    print(index, '-', value)

# 第二种方法
for t in enumerate(L):
    print(t[0], '-', value)






# 2.迭代dict
# 2.1 迭代dict的value
# 2.1.1第一种方法 使用dict.value()方法
# dict 对象有一个 values() 方法，这个方法把dict转换成一个包含所有value的list，这样，我们迭代的就是 dict的每一个 value：
dict1={"zhangsan": 100,"lisi": 999,"wangwu":99}
values = dict1.values()
print(values) #[100, 999, 99]
# 遍历value集合
for ele in values:
    print(ele)

# 2.2 迭代dict的key 和 value   使用items方法(会将dict的key和value变成tuple)
# items() 有一个对应的 iteritems()，iteritems() 不把dict转换成list，而是在迭代过程中不断给出 tuple，所以， iteritems() 不占用额外的内存。
print(dict1.items())
# [('zhangsan', 100), ('lisi', 999), ('wangwu', 99)]
# 第一种遍历
for t in dict1.items():
    print(t[0], '-',  t[1])

# 第二种遍历
for key,value in dict1.items():
    print(key, '-', value)


















