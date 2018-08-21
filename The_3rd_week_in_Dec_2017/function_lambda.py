f = lambda x: x % 2 == 1

L = list(filter(f, range(1, 20)))
print(L)
