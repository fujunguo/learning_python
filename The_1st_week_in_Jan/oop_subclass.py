class Animal():
    def run(self):
        print("Animal is running...")


class Dog(Animal):
    # pass
    def run(self):
        print("Dog is running...")


class Cat(Animal):
    pass


dog = Dog()
dog.run()
print(dir(dog))
print()
setattr(dog, 'y', 19)
print(hasattr(dog, 'y'))
print(getattr(dog, 'y'))
