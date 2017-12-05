class Parent(object):

    def override(self):
        print("PARENT override()")

    def talk(self):
        print("Hello")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def talk(self):
        super(Child, self).talk()
        for i in reversed(range(10)):
            print(f"{i + 1}...")

        print("BLASTOFF!!!!!")

dad = Parent()
son = Child()

dad.override()
son.override()

dad.talk()
son.talk()
