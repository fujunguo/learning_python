class A(object):

    def __init__(self, first_name, gender):
        self.namea = 'aaa'
        self.first_name = first_name
        self.gender = gender

    def func_a(self):
        print("Function a: %s" % self.namea)


class B(A):

    def __init__(self, first_name, gender, age):
        A.__init__(self, first_name, gender)
        self.nameb = 'bbb'
        self.namea = 'ccc'
        self.first_name = first_name.upper()
        self.age = age

    def func_b(self):
        print("Function b : %s" % self.nameb)


b = B("lin",'Male', 22)
print(b.nameb)
print(b.namea)
print(b.first_name)
print(b.age)
print(b.gender)
b.func_b()
b.func_a()
