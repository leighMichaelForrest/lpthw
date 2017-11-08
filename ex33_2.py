def append(lyst, n, increment=1):
    """Create a list of integers in sequence using a
    while loop."""
    i = 0

    while i < n:
        print(f"At the top i is {i}")
        lyst.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

def append_for(lyst, n, increment=1):
    """Create a list of integers in sequence using a
    for loop."""
    for i in range(0, n, increment):

        print(f"At the top i is {i}")
        lyst.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

numbers = []

append(numbers, 12)

print("The numbers: ")

for num in numbers:
    print(num)
