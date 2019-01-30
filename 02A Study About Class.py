class A():
    name = "ritian"
    age = 18

    def s(self):
        self.name = "tianhao"
        self.age = 81
        return None


# 此时,A称为类实例
print(A.name)
print(A.age)
print('-' * 30)
# id可以鉴别一个变量和另一个变量是不是同一个变量
print(id(A.name))
print(id(A.age))
print('-' * 30)
a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

# 经过结果可以知道A.name 和a.name 是同一个变量,A.age 和a.age 也是同一个变量
# 所以说明当指定一个变量为类的成员时,并不是复制了类里的所有属性到变量里,而是 在访问变量的属性时 会指向类的属性

a.s()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
# 经过以上执行结果可以知道,当a 的属性被另外赋值之后,a.name 和 a.age 就不会指向类的属性了
# 当然,如果直接在外面对a 的属性赋值也是可以的.例如直接输入 a.name = "zixu"


# 其实也可以在类内部的函数里面直接调用类的成员变量,方法是(__class__.name)  以下是例子
class B():
    name = "sanhuo"
    age = 20

    def x(self):
        print("以下是class B 的属性")
        print(__class__.name)
        print(__class__.age)


b = B()
b.x()


#        注意:  在类中,有self参数的方法(函数)被称为非绑定类函数(PS:可以通过其他变量访问或调用此函数)
#               而没有self参数的方法(函数)被称为绑定类函数(PS: 只能通过类来访问)
# 以上的都是非绑定类函数, 都是在类的外部定义一个变量指向类,再访问类里的函数
# 下面是一个绑定类函数的例子
class C():
    name = "feng"
    age = 24

    @staticmethod
    def say():
        print(__class__.name)
        print(__class__.age)
        print("It's been a long day without you my friend")
        return None


# 调用绑定类的函数需要使用类名来调用
# 如果直接使用 c = C()   c.say()  的话会报错,Type error,因为这样会直接把c作为一个参数扔到函数里,但是绑定类函数是不需要参数的
C.say()


"""
# 为什么定义这个类的时候会显示这个括号是冗余的?
class Stu():
    name = None
    age = 18
    gender = 'male'

    # 注意如果没有self变量可以把括号去掉,或者在定义函数之前先打一行  @staticmethod 声明该函数是静态函数,没有参数可以影响,否则就会有警告
    @staticmethod
    def say():
        print("It's a fine day with you around")

    def fun(self):
        self.name = input("输入学生姓名：")
        self.age = input("学生年龄")
        return None


Ming = Stu()
print("Stu's name is {}".format(Stu.name))
print("Stu is {} yesrs old".format(Stu.age))
print(Stu.gender)
print('-' * 50)
print("Ming's name is {}".format(Ming.name))
print("Ming is {} years old".format(Ming.age))
print(Ming.gender)
Ming.fun()

print('-' * 50)
print("Ming's name is {}".format(Ming.name))
print("Ming is {} years old".format(Ming.age))
print(Ming.gender)
Stu.say()
"""
