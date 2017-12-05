# import the argv feature from sys
from sys import argv

# unpack argv into script and filename, respectively
# note: script is THIS FILE!
script, filename = argv

# Get file feature
txt = open(filename)

# Write "Here is your file [filenam]:"
print(f"Here's your file {filename}:")
# Write the contents of the file.
print(txt.read())

# Don't trust user input. Prompting for a file can be bad
#
# Write "Type the filename again" to the screen
print("Type the filename again: ")
# Prompt for a file name
file_again = input("> ")

# Get the file feature for inputted filename
txt_again = open(file_again)

# Print out the contents of the file
print(txt_again.read())

# close the files
txt.close()
txt_again.close()
