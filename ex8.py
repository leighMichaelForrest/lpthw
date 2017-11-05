# Set formatter, a string of 4 curly braces.
formatter = "{} {} {} {}"

# print '1, 2, 3, 4' to the screen, in the positions of the curly braces.
print(formatter.format(1, 2, 3, 4))
# print 'one, two, three, four' to screen using the format string.
print(formatter.format("one", "two", "three", "four"))
# print 'True False False True' to the screen.
print(formatter.format(True, False, False, True))
# Print out formatter 4 times, literally.
print(formatter.format(formatter, formatter, formatter, formatter))
# Write out the strings to the format of formatter.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
