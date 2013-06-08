from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

if exists(to_file):
    out_file = open(to_file, 'w')
    out_file.write(indata)

out_file.close()
in_file.close()
