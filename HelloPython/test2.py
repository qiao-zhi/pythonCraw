#  正面从0开始，最后从-1开始
#  可变的list集合
list1=['life','is','short','python']
for x in list1:
    if x=='python':
     print("找到的python的下标是:", list1.index(x))

list2=[]
for i in range(5):
    list2[i]=input("请输入第", i+1, "名同学的成绩")

index=int(input("请输入你要查询的同学的编号:")) #输入查询的用户的下标
print("你")






