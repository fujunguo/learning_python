import pickle


# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

# write to the file
f = open(shoplistfile, 'wb')
# Dump the object to a file
pickle.dump(shoplist,f)
f.close()

# destroy the shoplist variable
del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
# load the object from the file
storelist = pickle.load(f)
print(storelist)

