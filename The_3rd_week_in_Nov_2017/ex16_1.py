from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file {}:".format(filename))
print(txt.read())