f = None

try:
    f = open("films.txt", "r")

    for i in f:
        print(i, end="")

except IOError:
    print("Error reading file")

finally:

    if f:
        f.close()
