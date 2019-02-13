
class People(object):
    """用 property 函数来对类中的属性进行统一化操作
        以及类中常用的一些魔法函数举例
    """

    def __init__(self):
        self._name = None
        self._age = None

    # 当对象被当成一个函数使用的时候调用__call__函数，并且执行
    def __call__(self, *args, **kwargs):
        print("I AM CALLED")

    # 当对象被当作是一串字符串输出的时候调用__str__函数，并输出__str__函数的返回值
    def __str__(self):
        return "I'm so diao"

    def fget(self):
        return self._name

    def aget(self):
        return self._age

    def fset(self, name):
        self._name = name.upper()

    def aset(self, age):
        self._age = int(age)

    def fdel(self):
        self._name = "NoName"

    def adel(self):
        self._age = 000

    name = property(fget, fset, fdel, "")
    age = property(aget, aset, adel, "")


p1 = People()
p1.name = "sherlock"
print(p1.name)
p1.age = 22.4
print(p1.age)
print(People.__dict__)
print(People.__doc__)
# 下面是调用__call__函数
p1()
# 下面是调用__str__函数
print(p1)
