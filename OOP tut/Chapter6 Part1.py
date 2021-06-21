############## CLASS  ATTRIBUTES ##############
''' CLASS ATTRIBUTES ARE ATTRIBUTES OF THE 
           CLASS NOT OF AN INSTANCE         '''

class Person:
    number_of_people = 0  
        # number_of_people ---> CLASS ATTRIBUTE
          # IT IS NOT DEFINED INSIDE ANY METHOD 
          # =================> DOESN'T USE self
          # DOESN'T HAVE ACCESS TO THE INSTANCE
          # DOESN'T CHANGE FROM ONE INSTANCE TO
          #                         TO AN OTHER

    def __init__(self, name):
        self.name = name

p1 = Person("Tim")
p2 = Person("Bill")

##### GETTING THE ATTRIBUTES ### METHOD 1 #####
print(p1.number_of_people)

##### GETTING THE ATTRIBUTES ### METHOD 2 #####
'''              GENERAL   FORM             '''
# ClassName.ATTRIBUTE
'''                  EXAMPLE                '''
print(Person.number_of_people)

##      MODIFYING THE  CLASS ATTRIBUTES      ##
'''              GENERAL    FORM            '''
# ClassName.ATTRIBUTE = NEW_VALUE
'''                  EXAMPLE                '''
Person.number_of_people = 8
print(p1.number_of_people)
