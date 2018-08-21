def createCounter():
    n = 0

    def counter():
        nonlocal n
        n = n + 1
        return n

    return counter


counterA = createCounter()
counterB = createCounter()
print(counterA(), counterB())
