############# INHERITANCE #############
'''   BETWEEN TWO SIMILAR CLASSES   '''
###### CODE  WITHOUT INHERITANCE ######

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("MEOW MEOW MEOW")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("BARK BARK BARK")