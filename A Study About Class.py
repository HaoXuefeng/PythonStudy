class Stu():
    name = None
    age = 18
    gender = 'male'

    def self(self):
        self.name = input("输入学生姓名：")
        self.age = input("学生年龄")
        self.gender = input("学生性别")
        print("My name is {}".format(self.name))
        print("I'm {} years old".format(self.age))
        return None


Ming = Stu()
Ming.self()
