from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copy from %s to %s" % (from_file, to_file))

# We could do these two on one line too, how?
indata = open(from_file).read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright, all done.")

out_file.close()
open(from_file).close()
