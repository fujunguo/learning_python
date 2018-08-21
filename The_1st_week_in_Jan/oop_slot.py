class Student(object):
    __slots__ = ("name", "age")


class NewStudent(Student):
    pass


a = Student()
b = NewStudent()
a.name = "Bart"
# a.score = 55 raise Error

# __slots__定义的属性仅对当前类实例起
# 作用，对继承的子类是不起作用的;
b.score = 55
print(a.name)
print(b.score)
