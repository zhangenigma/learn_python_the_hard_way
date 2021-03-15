# Animal is-a object( yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# is-a
class Dog(Animal):

    def __init__(self, name):
        # has-a
        self.name = name

# is-a
class Cat(Animal):
    def __init__(self, name):
        # has-a
        self.name = name

# is-a
class Person(object):
    def __init__(self, name):
        # has-a
        self.name = name
        # Person has-a pet of some kind
        self.pet = None

# is-a
class Employee(Person):
    def __init__(self, name, salary):
        # super, another type: Person.__init__(self, name)
        super(Employee,self).__init__(name)
        # has-a
        self.salary = salary

# is-a
class Fish(object):
    pass

# is-a
class Salmon(Fish):
    pass

# is-a
class Halibut(Fish):
    pass

# instance
rover = Dog("Rover")

# instance
satan = cat("Satan")

# instance
mary = Person("Mary")

# instance
mary.pet = Satan

# instance
frank = Employee("Frank", 120000)

#attribute
frank.pet = rover

# instance
flipper = Fish()

# instance
crouse = Salmon()

#instance
harry = Halibut()
