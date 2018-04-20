# tuple类似于list，只是一旦创建不可改变
tuple1=('zhangsan', 'lisi', 'wangwu')
print(tuple1)
print(tuple1[1])
print(tuple1[-1])

# 只有一个int型的tuple
tuple2=(1,)
print(tuple2[0])

# tuple中有list的情况，list中的元素可以进行增删改
tuple3=('zhangsan','lisi',['wangwu','zhaoliu'])
print(tuple3)
print(tuple3[-1])
tuple3[-1].append('tianqi') # tuple中的list集合中添加元素
print(tuple3)
tuple3[-1][0]='sunwu' #修改tuple中的list中的元素值
print(tuple3)



# 用多个值接tuple会将tuple的元素分别赋给对应元素的值
tuple4=(1, 2)
x, y = tuple4
print(x, y)



