import time


def timing_function(some_function):
    """
    Outputs the time a function takes to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return f"Time it took to run the function: {t2 - t1}\n"

    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in range(0, 0b1111111111111111111111):
        num_list.append(num)
    print(f"The sum of all the numbers: {str(sum(num_list))}")

print(my_function())
