class Stu():
    name = None
    age = 18
    gender = 'male'

    def self(self):
        self.name = input("输入学生姓名：")
        self.age = input("学生年龄")
        return None


Ming = Stu()
print(Stu.name)
print(Stu.age)
print(Stu.gender)
print(id(Stu.name))
print(id(Stu.age))
print(id(Stu.gender))
print('-' * 50)
print(Ming.name)
print(Ming.age)
print(Ming.gender)
print(id(Ming.name))
print(id(Ming.age))
print(id(Ming.gender))
Ming.self()

print('-' * 50)
print(Ming.name)
print(Ming.age)
print(Ming.gender)
print(id(Ming.name))
print(id(Ming.age))
print(id(Ming.gender))
