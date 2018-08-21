path = r'C:\Users\mk10569\Desktop\test.txt'
with open(path, 'w') as f:
    f.write('Hello,\nHow\nare\nyou?')

with open(path, 'r') as f:
    print(f.read())
    print()

with open(path, 'r') as f:
    print(f.readline())

with open(path, 'r') as f:
    print(f.readlines())


