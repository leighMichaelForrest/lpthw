# initialize cars to 100
cars = 100
# initialize space_in_a_car to 4.0 (a float)
space_in_a_car = 4.0
# initialize drivers to 30
drivers = 30
# initialize passengers to 90
passengers = 90
# initialize cars_not_driven to the difference of cars and drivers
cars_not_driven = cars - drivers
# initialize cars_driven to the value in drivers
cars_driven = drivers
# initialize carpool_capacity to the product of cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# initialize average_passengers_per_car to the quotient of
#     passengers and cars_driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars available.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
    "in each car.")
