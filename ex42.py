## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pets = []

    def add_pet(self, pet):
        if isinstance(pet, Animal):
            print("is animal")
            self.pets.append(pet)
        else:
            print("not a pet")

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee calls Person constructor
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

    def add_pet(self, pet):
        super(Employee, self).add_pet(pet)
        print("The pet's owner is a scrub")

## Fish is-a class of type object
class Fish(object):
    pass

## Salmon is a Fish class
class Salmon(Fish):
    pass

## Halibut is-a Fish class
class Halibut(Fish):
    pass


## rover is-a dog object
rover = Dog("Rover")

## Satan is-a Cat object
satan = Cat("Satan")

## Mary is-a person object
mary = Person("Mary")

## Mary has Satan as a pet
mary.add_pet(satan)

## Frank is-a Employee object
frank = Employee("Frank", 120000)

## Frank has Rover as a pet
frank.add_pet(rover)
frank.add_pet(satan)

## flipper is-a Fish object
flipper = Fish()

## crouse is-a Salmon object
crouse = Salmon()

## harry is-a Halibut object
harry = Halibut()

for pet in frank.pets:
    print(f"{pet.name} is a {type(pet)}")
