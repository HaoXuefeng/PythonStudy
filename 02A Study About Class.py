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
