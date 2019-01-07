# __author__: William Kwok
class School(object):
	def __init__(self, school_name, school_addr):
		self.school_name = school_name
		self.school_addr = school_addr
		self.school_students = []
		self.school_teachers = []

	def enroll(self, stu_obj):
		print("为学员{}办理注册手续。".format(stu_obj.name))
		self.school_students.append(stu_obj)

	def hire(self, staff_obj):
		print("雇佣新员工{}。".format(staff_obj.name))
		self.school_teachers.append(staff_obj)


class SchoolMember(object):
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex

	def tell(self):
		pass


class Teacher(SchoolMember):
	def __init__(self, name, age, sex, salary, course):
		super().__init__(name, age, sex)
		self.salary = salary
		self.course = course

	def tell(self):
		print("""
		-----Info of Teacher: {0}-----
		\tName: {0}
		\tAge: {1}
		\tSex: {2}
		\tSalary: {3}
		\tCourse: {4}
		""".format(self.name, self.age, self.sex, self.salary, self.course))

	def teach(self):
		print("{} is teaching course {}.".format(self.name, self.course))


class Student(SchoolMember):
	def __init__(self, name, age, sex, stu_id, grade):
		super().__init__(name, age, sex)
		self.stu_id = stu_id
		self.grade = grade

	def tell(self):
		print("""
		-----Info of Student: {0}-----
		\tName: {0}
		\tAge: {1}
		\tSex: {2}
		\tStu_id: {3}
		\tGrade: {4}
		""".format(self.name, self.age, self.sex, self.stu_id, self.grade))

	def pay_tuition(self, amount):
		print("{} has paid ${} already.".format(self.name, amount))

t1 = Teacher("Oldboy", 33, 'M', 8880, 'Python')
t2 = Teacher("Jackie", 34, 'F', 10000, 'C++')
t1.tell()
t1.teach()

s1 = Student('William', 22, 'M', 122, 4)
s2 = Student('Jane', 24, 'F', 132, 4)
s1.tell()
s1.pay_tuition(2000)
print()

school = School('新东方', '中关村')
school.enroll(s1)
school.enroll(s2)
school.hire(t1)
school.hire(t2)
print()

for teacher in school.school_teachers:
	teacher.teach()

for student in school.school_students:
	student.pay_tuition(20000)
