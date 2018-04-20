# 循环练习题
# 1.本金10000 元存入银行，年利率是千分之三。每过一年，将本金和利息相加作为新的本金。计算五年后，获得的本金是多少。
oriCache=10000
for i in range(5):
    oriCache=oriCache*(1+3/1000)

print(oriCache)

#   2.计算1000以内所有不能被7整除的整数的和
sum = 0
for i in range(1001):
    if i%7 != 0:
        sum=sum+i

print("和为:",sum)


# 3.编写一个程序，最多接受10 个数字，并求出其中所有正数的和。用户可通过输入999终止程序，统计用户输入的正数个数，并显示这些正数的和
count=0
sum1=0
for xx in range(10):
    numstr = input("请输入一个数字:")
    numint=int(numstr)
    if numint==999:
        break
    elif numint >= 0:
        count=count+1
        sum1=sum1+numint
print("正数的个数是:", count)
print("正数的和是:", sum1)


# 4.开发一个标题为“FlipFlop”的游戏应用程序。它从1计数到100，遇到3的倍数就替换为单词“Flip”，5的倍数就替换为单词“Flop”，既为3的倍数又为5的倍数则替换为单词“FlipFlop”。
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FlipFlop')
    elif i % 3 == 0:
        print('Flip')
    elif i % 5 == 0:
        print('Flop')
    else:
        print(i)



# 5.在控制台输出一个用‘*’组成的直角三角形
for out in range(7):
    for inner in range(out+1):
        print("*",end="")
    print("")
# 6、创建一个list，想办法将其用升序排列，此办法要适用于任何长度的list(python直接选择算法)
list3=[1,5,6,9,1,6,8]
for i in range(len(list3)):
    for j in range(i, len(list3)):
        if list3[i] > list3[j]:
            tmp=list3[i];
            list3[i]=list3[j]
            list3[j]=tmp
print(list3)








