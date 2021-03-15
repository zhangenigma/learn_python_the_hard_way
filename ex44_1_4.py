class Parent(object):

    def override(self):
        print("Parent override()")

    def implicit(self):
        print("Parent implicit()")

    def altered(self):
        print("Parent altered()")


class Child(Parent):

    def override(self):
        print("Child override()")

    def altered(self):
        print("Child, Before Parent altered()")
        super(Child, self).altered()
        print("Child, After Parent altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()        
