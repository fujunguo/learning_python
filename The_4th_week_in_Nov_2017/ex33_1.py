def list1(x):
    i = 0
    numbers = []
    while i < x:
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + 1
        print("Numbers now:", numbers)
        print("At the bottom i is %d" % i)
        print()
    print("The numbers:")
    for num in numbers:
        print(num)


variable = int(input("Type an integer:"))
list1(variable)
