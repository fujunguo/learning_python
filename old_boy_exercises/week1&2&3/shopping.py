# __author__: William Kwok
product_list = [
	("iPhone", 5000),
	("iMac", 12000),
	("iPod shuffle", 399)
]
shopping_list = []
salary = input("Enter your salary: ")
if salary.isdigit():
	salary = int(salary)
	while True:
		for index, item in enumerate(product_list):
			print(index, item)
		user_choice = input("选择要买啥？>>>:")
		if user_choice.isdigit():
			user_choice = int(user_choice)
			if -1 < user_choice < len(product_list):
				p_item = product_list[user_choice]
				if p_item[1] <= salary:
					shopping_list.append(p_item[0])
					salary -= p_item[1]
					print("Added {} into shopping cart,your current balance is \033[31;1m{}\033[0m".format(p_item, salary))
				else:
					print("\033[41;1m您的余额为{}，不足以购买。\033[0m".format(salary))
			else:
				print("\033[31;1mThe product is not found.\033[0m")

		elif user_choice == 'q':
			print("Shopping List".center(30, '-'))
			for p in shopping_list:
				print(p)
			print("Your balance is {}".format(salary))
			exit()
		else:
			print("Invalid option")
else:
	print("\033[31;1mPlease enter a number.\033[0m")