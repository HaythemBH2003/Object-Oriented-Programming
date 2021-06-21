from Chapter2 import Dog
new_dog = Dog()

####    OBJECTS & METHODS     ####
''' Attributes of an Object depend 
    on its Class '''

'''       GENERAL FORM         '''
#   var.method(args)
        # var ----------> variable
        # method --> method to use
        # args --------> arguments

#  SOME PREVIOUSLY USED METHODS  #

string = "aaa"
print(string.upper())
    # var.method()
    #   Object 'var' needs to have 
    #           attribute 'method'

#  USING METHODS OF AN INSTANCE  #
'''        GENERAL FORM        '''
# instance.method()
'''          EXAMPLE           '''  
new_dog.bark()
result1 = new_dog.eat()
print(result1)
result2 = new_dog.count(3)
print(result2)            