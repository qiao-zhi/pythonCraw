# 函数部分练习题
# 1.获取三个数字中最大的一个
def fun1(a,b,c):
    if a >=b and a>=c:
        return a
    elif b >= c and b>= a:
        return b
    else:
        return c
print(fun1(1,2,3))

# 2.编写一个函数，将一个集合升序排列
def fun2(list):
    for index2 in range(len(list)):
        for index22 in range(index2+1,len(list)):
            if list[index2] > list[index22]:
                tmp=list[index2]
                list[index2]=list[index22]
                list[index22]=tmp
    return list

print(fun2([1,6,9,8,5,6,96,5]))

# 3.编写函数往集合中插入元素
def fun3(list,element):
    list.append(element)
    return list

print(fun3([1,2],5))


# 4.编写函数，实现从控制台输入一个数字并在控制台打印
def fun4():
    print("您输入的数字是:", input("请输入一个数字"))

fun4()

# 5.编写一个函数，实现将一个集合中的元素反转
def fun5(list):
    tmpList=[]
    index5 = len(list)-1
    while index5>=0:
        tmpList.append(list[index5])
        index5 = index5-1
    return tmpList

print(fun5([5,5,9,6,8,4]))


# 6.编写函数，设置一个整数参数，如果传6，打印如下内容
def fun6(num):
    for i in range(num):
        print(str(i)+"+"+str(num-i)+"="+str(num))
    print(str(num)+"+"+str(num-num)+"="+str(num))

fun6(6)



# 7、编写函数，实现登录验证功能，验证次数最多三次
def fun7(name,password):
    for i in range(3):
        input_name=input("请输入用户名:")
        input_password=input("请输入密码:")
        if input_name == name and input_password==password:
            print("你牛逼")
            return
        else:
            print("输入错误!您还有"+str(2-i)+"次机会")

fun7("n","p")


# 8、编写函数，计算某个数的阶乘(递归函数的用法或者使用循环计算)
def fun8(num):
    if num <1:
        print("请传递正数参数")
        return
    if num==1:
        return 1
    else:
        return num * fun8(num-1)

print(fun8(6))








