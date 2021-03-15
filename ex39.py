#create a mapping of state to abbreviation
states = {
    'Oregen' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New Youk' : 'NY',
    'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has:", cities['NY'])
print("NY State has:", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Folrida's abbreviation is:", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

# printebery state abbreciation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for accev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safellu get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("sorry, no Texas.")

# get a city with a default value
# city = cities.get('Texas')
#
# if not state:
#     print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
