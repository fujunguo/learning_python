try:
    print("try...")
    r = 10 / int('123')
    print("result:", r)

except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

except ValueError as e:
    print("ValueError:", e)

else:
    print("No error!")

finally:
    print("finally...")
print("END")
print()


# 跨越多层调用
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print("END!")


main()

