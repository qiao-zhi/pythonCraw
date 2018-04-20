# 文件IO，读取文件和创建文件
# 1.读取键盘输入
x=input("please input number")
print("您输入的是"+x)

# 2.打开一个文件(open函数相当于创建一个file对象)
fo = open("test.sh", "r+")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)
print("文件位置 : ", fo.tell())

# 3.去读打开的上面的文件进行操作(传负数代表读取所有)
content = fo.read(-1)
print(content)

# 4.向文件中写内容
fo.write("llllllllllllll")
fo.flush()
content1 = fo.read(-1)
print(content1)








