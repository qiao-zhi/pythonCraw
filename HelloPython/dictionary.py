# dict类型练习
# 定义一个dict类型
dict1={"zhangsan": 100,"lisi": 999,"wangwu":99}
print(len(dict1))
print(dict1["zhangsan"])
if "tianqi" in dict1:
    print(dict1["tianqi"])
else:
    print("tianqi is not in dict1")

# 更新dict
dict1["zhangsan"]=0
# 追加元素
dict1["tianqi"]=100
# 删除字典元素
del dict1["wangwu"]

# 循环遍历dict
for key in dict1:
    print("key:",key,"value:",dict1[key])



