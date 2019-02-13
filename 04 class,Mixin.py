"""
Mixin是为了解决多继承的混乱关系而诞生的，Mixin类是只提供某一种   单一的功能  的类，扩充字类的功能
但一定是  单一的功能！！！
如果是多个功能就要创建多个Mixin类来扩充功能
"""


class Person(object):
    def __init__(self):
        self.name = None


class FlyMixin(object):
    def fly(self):
        print("I can fly!")
        return None


class SwimMixin(object):
    def swim(self):
        print("I can swim!")
        return None


class SuperMan(Person, FlyMixin, SwimMixin):
    def __str__(self):
        return "I am very DIAO"


p1 = SuperMan()
print(SuperMan.__name__)
print(p1)
p1.fly()
