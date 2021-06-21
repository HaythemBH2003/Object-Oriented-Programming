############# INHERITANCE #############
'''   BETWEEN TWO SIMILAR CLASSES   '''
######## CODE WITH INHERITANCE ########

class Pet:   # Pet -----> GENERAL CLASS
       # CONTAINS COMMON METHODS OF THE
       #                SIMILAR CLASSES
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")

    def speak(self):
        print("I dunno what I say ...")

'''   GENERAL FORM OF INHERITANCE   '''
# class SpecificClass(GeneralClass):
#     def specific_method1(self, args):
#         ....
#     def specific_method2(self, args):
#         ....

'''             EXAMPLE             '''
class Cat(Pet): # Cat INHERITS FROM Pet
            #  Cat INHERITS Pet METHODS
            #  Cat NOW HAS:
                           # __init__()
                           #     show()
    def speak(self):
        print("MEOW MEOW MEOW")

class Dog(Pet): # Dog INHERITS FROM Pet
            #  Dog INHERITS Pet METHODS
            #  Dog NOW HAS:
                           # __init__()
                           #     show()
    def speak(self):
        print("BARK BARK BARK")

class Fish(Pet):
    pass

####     TESTING show() METHOD     ####
pet = Pet("Tim", 5)
pet.show()
cat = Cat("Bill", 3)
cat.show()
dog = Dog("Joe", 6)
dog.show()

####     TESTING speak() METHOD    ####
#<!> BEFORE  ADDING speak() TO Pet <!>#
dog.speak()
cat.speak()

####     TESTING speak() METHOD    ####
# <!> AFTER ADDING speak() TO Pet <!> #
pet.speak() 
dog.speak()    # PRINT "BARK BARK BARK"
cat.speak()    # PRINT "MEOW MEOW MEOW"
''' A SPECIFIC METHOD WILL OVERWRITE A
    METHOD FROM A GENERAL CLASS IF TWO
    METHODS HAVE THE SAME NAME.    '''
fish = Fish("Bubbles", 1)
fish.speak()  # speak() INHERITED FROM
              #              Pet Class


