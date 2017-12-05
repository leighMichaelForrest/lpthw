# create a mapping of state to abbreviation
states = {
    'Pennsylvania': 'PA',
    'New Jersey': 'NJ',
    'Delaware': 'DE',
}

# create a basic set of states and some cities in them
cities = {
    'PA': 'Philadelphia',
    'NJ': 'Wildwood',
    'DE': 'Wilmington'
}

# print out some cities
print('-' * 10)
print("PA State has: ", cities['PA'])
print("NJ State has: ", cities['NJ'])
print("DE State has: ", cities['DE'])

# print some states
print('-' * 10)
print("Delaware's abbreviation is: ", states['Delaware'])
print("New Jersey's abbreviation is: ", states['New Jersey'])
print("Pennsylvania's abbreviation is: ", states['Pennsylvania'])

# replace 'Wilmington' with 'Pea Patch Island'
cities['DE'] = 'Pea Patch Island'
# do it by using the state then cities dict
print('-' * 10)
print("Pennsylvania has: ", cities[states['Pennsylvania']])
print("New Jersey has: ", cities[states['New Jersey']])
print("Delaware has: ", cities[states['Delaware']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, No Texas")

# get a city with a default  value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
