# import argv feature from sys
from sys import argv

# get the script and input_file from the command line arguments
script, input_file = argv

# function that prints the contents of a file to the screen.
#   Takes a file parameter f
def print_all(f):
    # write file to screen
    print(f.read())

# function that returns file reader to start of file.
def rewind(f):
    # go to the start of the file.
    f.seek(0)

# function that prints a line number and line of text from a file.
def print_a_line(line_count, f):
    # print "{line_count} {line_of_file }"
    print(line_count, f.readline())

# open a file and set it to the current_file variable
current_file = open(input_file)

# write "First, let's open the whole file:\n"
print("First, let's open the whole file:\n")

# print contents of entire file.
print_all(current_file)

# write "Now let's rewind, kind of like a tape."
print("Now let's rewind, kind of like a tape.")

# move the file's reader to the beginning of the file.
rewind(current_file)

# write "Let's print three lines:"
print("Let's print three lines:")

# set current_line to one
current_line = 1
# print the current_line  and the text of the current line.
# note: when operation is done, reader stays where it is.
print_a_line(current_line, current_file)

# increment current_line by one
current_line += 1
# display current_line and it's contents.
print_a_line(current_line, current_file)

# increment current_line by one
current_line += 1
# display current_line and it's contents.
print_a_line(current_line, current_file)
