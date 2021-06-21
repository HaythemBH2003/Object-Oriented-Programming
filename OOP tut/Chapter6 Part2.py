############## CLASS  ATTRIBUTES ##############

class Person:
    number_of_people = 0  
        # number_of_people ---> CLASS ATTRIBUTE

    def __init__(self, name):
        self.name = name
        ####   CALL & MODIFY  ATTRIBUTES   ####
        Person.number_of_people += 1

p1 = Person("Tim")
print(Person.number_of_people)
p2 = Person("Bill")
print(Person.number_of_people)