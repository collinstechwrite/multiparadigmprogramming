class Person:
   def __init__(self, name):
       self.name = name


people = ["Emmy","Niels"]

for item in people:
    exec(item = Person(item))

print(Emmy.name)
print(Niels.name)
