############# CLASS  METHODS #############

class Person:
    number_of_people = 0
    
    def __init__(self, name):
        self.name = name
        Person.add_person()

    #####   DEFINE A  CLASS METHOD   #####
    '''            EXAMPLE 1           '''
    @classmethod
            # @classmethod ----> DECORATOR
            # INDICATES THAT IT IS A CLASS
            #                       METHOD
    def get_number_of_people(cls): 
                        # cls -----> CLASS
        return cls.number_of_people
    
    '''            EXAMPLE 2           '''
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

person1 = Person("Tim")
print(person1.number_of_people)
