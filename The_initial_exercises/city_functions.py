# import json
# def get_stored_username():
# 	filename = 'username.json'
# 	try:
# 		with open(filename) as f:
# 			username = json.load(f)
# 	except Exception as e:
# 		return None
# 	else:
# 		return username

# def get_new_username():
# 	username = input('What is your name?')
# 	filename = 'username.json'
# 	with open(filename, 'w') as f:
# 		json.dump(username, f)
# 	return username

# def greet_user():
# 	username = get_stored_username()
# 	right = input('Is {} your name?Type \'yes\' or \'no\' please.'.format(username))
# 	if right == 'yes':
# 		print('Welcome back, '+ username + '!')
# 	else:
# 		username = get_new_username()
# 		print('We\'ll remember you when you come back, '+username+'!')

# greet_user()
def name(city_name, country_name, population=''):
	if population:
		full_name = city_name.title() + ',' + country_name.title() + \
			' - population ' + str(population)
	else:
		full_name = city_name.title() + ',' + country_name.title()
	return full_name