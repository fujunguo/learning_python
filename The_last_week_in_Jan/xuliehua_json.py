import json
d = dict(name='Bob', age=20, score=88)

# write_1
f = open('json.json', 'w')
json.dump(d, f)
f.close()

# write_2
print(json.dumps(d))
print()

# read_1
f = open('json.json', 'r')
r = json.load(f)
f.close()
print(r)
print()

# read_2
json_str = '{"name": "Bob", "age": 20, "score": 88}'
print(json.loads(json_str))
