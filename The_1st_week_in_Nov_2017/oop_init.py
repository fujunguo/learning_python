class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('William')
p.say_hi()

# 获取Person类的属性
# print(dir(Person))
