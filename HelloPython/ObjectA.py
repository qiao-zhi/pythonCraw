# 面向对象练习
class A:
    # 直接定义的类的变量，属于类(通过对象访问的则是对象的变量)
    name = ''
    age = 0
    # 私有成员(类似于java的private，python中私有成员和私有方法用__开头)
    __password = '123456'


    # 无参构造方法
    def __init__(self,height):
        # 类实例才有的属性
        self.height = height
        print("A被创建")


    # 有参构造方法
    def __init__(self,name,age,password,height):
        print("A的有参数的构造方法被调用")
        self.name=name
        self.age=age
        self.__password=password
        # 类实例才有的属性
        self.height = height

    # 成员方法访问私有成员变量
    def getPassword(self):
        return self.__password

    # 重载方法(类似于java的toString()方法)
    def __str__(self):
        return  "name:"+self.name+"\t"+"age:"+str(self.age)

    def getHeight(self):
        return self.height




def test1():
    # 调用有参构造方法创建对象
    aObj=A("zhangsan",25,'123456',195)
    # 打印会调用__str__(self)方法，如果没有重写方法打印的是一串地址
    print(aObj)
    # 访问类实例变量
    print(str(aObj.name)+"\t"+str(aObj.age)+"\t"+str(aObj.getPassword()))
    # 访问类变量
    print(str(A.age))
    #访问类实例才有的属性
    print(aObj.height)

test1()


# B类继承A类
class B(A):
    # 在原有属性的基础上增加的属性
    sex="男"

    # 构造方法
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    # 方法重写(覆盖)
    def getPassword(self):
        # super调用父类的方法
        print(super().getPassword())
        return "这里是B类重写过的方法"


    #重写方法，写完此方法打印对象不会打印地址
    def __str__(self):
        return "name:"+self.name+"\t"+"age:"+str(self.age)+"\tsex:"+self.sex

def test2():
    bObj = B('wangba',99,"女")
    # 打印B实例
    print(bObj)
    # 打印B类的属性
    print("B类的sex属性:"+B.sex)
    # B实例的属性
    print("B实例的sex属性:"+bObj.sex)
    #调用B的getPassword方法
    print(bObj.getPassword())

# test2()


class C(B,A):
    # 属性
    idCode='xxx'


    # 构造方法
    def __init__(self,name,age,sex,idCode):
        self.name=name
        self.age=age
        self.sex=sex
        self.idCode=idCode

def test3():
    cObj = C('ccc',100,"男",'555')
    # 实际是调用B类的__str__方法
    print(cObj)
    # 打印类属性
    print(C.idCode)
    # 实际是调用B类的getPassword方法
    print(cObj.getPassword())


# test3()
