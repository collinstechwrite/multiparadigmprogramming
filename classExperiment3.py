
"""
class Person:
   def __init__(self, name):
       self.name = name

emmy = Person("Emmy")
niels = Person("Niels")

print(emmy.name)
print(niels.name)
"""


"""
class Person:
   def __init__(self, name):
       self.name = name


people = ["Emmy","Niels"]



for item in people:
    a = str(item) + ' = Person("' + str(item) + '")'
    exec(a)

print(Emmy.name)
print(Niels.name)
"""









class Person:
   def __init__(self, name):
       self.name = name


people = ["Emmy","Niels"]

Dictionary1 = {}
for item in people:
    Dictionary1 = { item : Person(item)}



    
print(Dictionary1)
