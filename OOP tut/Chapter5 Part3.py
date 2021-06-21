############# INHERITANCE #############
'''   BETWEEN TWO SIMILAR CLASSES   '''
# super() ## SUPER  CLASS  ## super() #

class Pet:     # PARENT / GENERAL CLASS
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")

    def speak(self):
        print("I dunno what to say ..")

''' THE CHILD CLASS HAS A NEW ATTRIBUTE
    THAT DOESN'T EXIST IN __init__() OF
    THE PARENT CLASS ( color ATTR ) '''

class Cat(Pet):           # CHILD CLASS
    def __init__(self, name, age, clr):
        # INHERITING name/age ATTRIBUTE
        '''      GENERAL  FORM      '''
        #   super.METHOD(arg1, arg2)
        '''         EXAMPLE         '''
        super().__init__(name, age)
            # super() -> STANDS FOR THE 
            #              PARENT CLASS
            #  THE  __init__()  IS  THE 
            #  PARENT'S METHOD ---> Pet
        self.color = clr

    def show(self): #    DIFFERENT FROM
                    # Pet show() METHOD 
        print(f"My name is {self.name}, I'm {self.age} and my color is {self.color}.")

    def speak(self):
        print("MEOW MEOW MEOW")

class Dog(Pet):           # CHILD CLASS
    def speak(self):
        print("BARK BARK BARK")

dog = Dog("Tim", 3)
cat = Cat("Bill", 4, "white")
dog.show()
dog.speak()
cat.show()
cat.speak()