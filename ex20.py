#from the sys package import the argv module
from sys import argv

#unpack argv into script and input_file variables
script, input_file = argv

#prints the file
def print_all(f):
    print f.read()

#moves to the beginning of the file buffer
def rewind(f):
    f.seek(0)

#prints a line from the file and its line number (this is explicitly handled later in the script)
def print_a_line(line_count, f):
    print line_count, f.readline()

#opens the current file
current_file = open(input_file)

print "First let's print the whole file:\n"

#prints the contents of the file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#resets the cursor to the beginning of the file buffer
rewind(current_file)

print "Let's print three lines:"

#prints the first three lines of the file, with the line number
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

#closes the file object
current_file.close()
