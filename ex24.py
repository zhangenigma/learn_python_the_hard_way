print("Let's practice everything.")
print("You'd need to kown 'about escapes with \\ that do：")
print('\n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comparehend passion from intution
and requires an explanation
\n\t\twehere there is none.
"""

print("---------------------")
print(poem)
print("---------------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string
print("With a starting point of ;{}".format(start_point))
#It's just like with an f "" string
print(f"We'd have {beans} beans, {jars}jats, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
#This is an easy way to apply a list to a fotmat starting
print("We'd have {} beans, {} jats, and {} crates.".format(*formula))
