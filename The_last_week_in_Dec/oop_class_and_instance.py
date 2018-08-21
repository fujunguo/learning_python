class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"


Lisa = Student('Lisa', 99)
Bart = Student('Bart', 60)
Mike = Student('Mike', 50)

print(Lisa.name, Lisa.get_grade())
print(Bart.name, Bart.get_grade())
print(Mike.name, Mike.get_grade())
