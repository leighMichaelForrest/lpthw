real_things = ['Beer', 'Bar', 'Cup', 'Bottle', 'Router']

more_stuff = 'Television Can Bike Roller-Skates Bag'
stuff_list = more_stuff.split(' ')

for stuff in stuff_list:
    if stuff == "Roller-Skates":
        stuff = "Roller Skates"
    else:
        pass
    real_things.append(stuff)


print("real_things is: ", real_things)
print(real_things[3:7])
