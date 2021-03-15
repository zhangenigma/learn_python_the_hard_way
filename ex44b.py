# class Parent(object):
#
#     def override(self):
#         print("PRARENT override()")

# class Child(Parent):
#
#     def override(self):
#         print("CHILD override()")

class Parent(object):

    def altered(self):
        print("Parent altered()")


class Child(Parent):

    def altered(self):
        print("Child, Before Parent altered()")
        super(Child, self).altered()
        print("Child, After Parent altered()")

dad = Parent()
son = Child()

# dad.overrride()
# son.override()


dad.altered()
son.altered()
