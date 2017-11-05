# initialize a string with a tab in it.
tabby_cat = "\tI'm \'tabbed\' in."
# initialize a string with a newline.
persian_cat = "I'm split\non a line."
# initialize a string with literal backslashes in it
backslash_cat = "I'm \\ a \\ cat."

format_cat = "i'm a \'{}\' kind of kitty\n\twith a {} on top."

# initialize a mult-line string with tabs and a newline.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\t* \Npi
'''

# print tabby_cat string to the screen
print(tabby_cat)
# print persian_cat string to the screen
print(persian_cat)
# print backslash_cat string to the screen
print(backslash_cat)
# print fat_cat string to the screen
print(fat_cat)
print(format_cat.format("cute", "cherry"))
