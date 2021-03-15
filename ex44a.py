class Parent(object):

    def __init__(self, age):
        self.age = age

    def hit(self):
        print("Father hits the son.")

    def implicit(self):
        print("Parent implicit()")

class Child(Parent):
    def __init__(self, age, name):
        # Parent.__init__(self, age)
        self.age = age
        self.name = name

dad = Parent(50)
son = Child(22, 'zhang')

print(dad.age)
print(son.age)
son.implicit()
