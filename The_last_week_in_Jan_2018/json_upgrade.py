import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# pickling
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))


# unpickling
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_string = '{"name": "Bob", "age": 20, "score": 88}'

print(json.loads(json_string, object_hook=dict2student))


