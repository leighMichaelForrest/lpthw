from sys import argv

script, filename = argv

print("We are going to erase and add new lines to a file.")
print(f"That file's name is {filename}")

txt = open(filename, 'w+')
txt.truncate()

# prompt for three different lines
print("Enter three lines:")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# add the lines into the file
txt.write(line1)
txt.write('\n')
txt.write(line2)
txt.write('\n')
txt.write(line3)
txt.write('\n')

# Go back to the start of file.
txt.seek(0)

# Write out the file.
print(txt.read())
# close the file
txt.close()
