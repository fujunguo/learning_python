def cheese_and_crackers(chesse_count, boxes_of_crackers):
    print("You have %d cheeses!" % chesse_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party.")
    print("Get a blanket.\n")


# 第一种方式，直接给出参数值。
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


# 第二种方式，定义好变量然后在调用函数时，直接传入定义好的变量
print("Or, we can use variables from our scripts:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# 第三种方式
print("We can even do math inside too:")
# 将逻辑运算后的值作为函数参数代入
cheese_and_crackers(10+20, 5+6)


# 第四种方式
print("And we can combine the two, variables and math:")
# 调用函数时采用参数变量加整形常量的方式代入
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
