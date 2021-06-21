################ CLASS  ATTRIBUTES ################

class Dog:
    ####### ADDING ATTRIBUTES WITH __init__ #######
    '''              GENERAL  FORM              '''
    # def __init__(self, val1, val2, ...):
        # self.att1 = val1
        # self.att2 = val2
    '''                  EXAMPLE                '''
    def __init__(self, name):
            # self -----------> THE INSTANCE ITSELF
            # this_dog_name --> ATTRIBUTE OF OBJECT
        self.this_dog_name = name # STORE ATTRIBUTE
                #  self.ATTRIBUTE = ATTRIBUTE_VALUE

    def bark(self):
        print("BARK BARK BARK")

    def eat(self):
        return "EAT EAT EAT"

    def count(self, x):
        return (x + 1)

    def get_name(self):
        return self.this_dog_name
    
    def set_name(self, new_name):
        self.this_dog_name = new_name 
                # ACCES & MODIFY EXISTING ATTRIBUTE

dog1 = Dog("TIM")

###### GET AN ATTRIBUTE VALUE ##### METHOD 1 ######
######         object.ATTRIBUTE_NAME         ###### 
print(dog1.this_dog_name)

###### GET AN ATTRIBUTE VALUE ##### METHOD 2 ######
###### object.FUNCTION_THAT_RETURNS_THE_ATTR ######
print(dog1.get_name())

###### TEST MODIFYING AN  EXISTING ATTRIBUTE ######
dog1.set_name("BILL")
print(dog1.get_name())
