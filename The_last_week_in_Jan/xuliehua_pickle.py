import pickle
d = dict(name='William', age=24, score=88)

# write_1
f = open('pickle.txt', 'wb')
pickle.dump(d, f)
f.close()

# write_2
print(pickle.dumps(d))
print()

# read_1
f = open('pickle.txt', 'rb')
r = pickle.load(f)
f.close()
print(r)
print()

# read_2
pickle_str = b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq' \
             b'\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
print(pickle.loads(pickle_str))

