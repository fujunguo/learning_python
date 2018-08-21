class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


william = Student("William", "male")
if william.get_gender() != "male":
    print("测试失败！")
else:
    william.set_gender("female")
    if william.get_gender() != "female":
        print("测试失败！")
    else:
        print("测试成功！")
