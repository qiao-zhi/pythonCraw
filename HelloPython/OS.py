# OS模块处理文件和目录
import os
# 打印当前目录
print(os.getcwd())
# 打印环境变量
print(os.getenv("path"))
# 改变工作目录
path="C:/Users/liqiang/Desktop"
os.chdir(path)
print(os.getcwd())

# 删除目录
os.removedirs("pythonDir")
# 创建目录
os.mkdir("pythonDir")
# 进入当前目录的pythonDir子目录
os.chdir("pythonDir")
print(os.getcwd())
# 创建两个文件
open("test1.txt",'w')
open("test2.txt",'w')
# 列出文件夹下的文件内容
print(os.listdir(os.getcwd()))






