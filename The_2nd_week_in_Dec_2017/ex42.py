# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


##
class Dog(Animal):

    def __init__(self, name):
        ##
        self.name = name


##
class Cat(Animal):

    def __init__(self, name):
        ##
        self.name = name


##
class Person(object):

    def __init__(self, name, gender):
        ##
        self.name = name
        self.gender = gender

    # Person has-a pet of some kind
        self.pet = None


##
class Employee(Person):

    def __init__(self, name, gender, salary):
        ##
        super(Employee, self).__init__(name, gender)
        ##
        self.salary = salary
        print("The salary of {} is {}".format(self.name, self.salary))


##
class Fish(object):
    pass


#
class Salmon(Fish):
    pass


#
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

#
satan = Cat("Satan")

#
# mary = Person("Mary", "Female")

#
Frank = Employee("Frank", "male", 120000)


