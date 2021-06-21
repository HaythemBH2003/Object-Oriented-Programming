################ CLASSES #################
''' The Class Methods define how an object  
    interacts with the code.  Methods  are 
    the object's allowed actions.      '''

######      DEFINING  A  CLASS      ######
'''            GENERAL FROM            '''
# class ClassName:
#       ClassName -----> Name of the class
#                        in Camel Case
'''              EXAMPLE               '''  
class Dog:
    def __init__(self):
        #__init__ Method Is Compulsory <!>
        #   IT INITIATES A NEW INSTANCE OF
        #   AN OBJECT WITH ITS  ATTRIBUTES
        # self ---> REFERS TO THE INSTANCE  
        pass

    def bark(self):   # bark -----> METHOD
                      # self -----> OBJECT
        print("BARK BARK BARK")

    def eat(self):    # eat ------> METHOD
                      # self -----> OBJECT
        return "EAT EAT EAT"

    def count(self, x):    
            #  A METHOD CAN TAKE ARGUMENTS
                      # count ----> METHOD
                      # self -----> OBJECT
                      # x ------> ARGUMENT
        return (x + 1)


#####      INITIATING   OBJECTS      #####
new_dog = Dog() 
        # new_dog ---> NEW INSTANCE OF Dog
print(type(new_dog))
        # type of new_dog -----------> Dog
         