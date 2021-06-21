class Employee:
    def __init__(self, name):
        self.name = name

    def get_access(self, level, authorisation = False):
        list_of_posts = ['', 'apprentice', 'junior', 'senior', 'supervisor', 'ceo']
        if list_of_posts.index(str(self.post).lower()) < level and authorisation == False:
            print("Unauthorised access: You don't have the privilege of this Department.")
        elif list_of_posts.index(str(self.post).lower()) < level and authorisation == True:
            print("Aurhorised access. Authorisation has been provided by the CEO.")
        else:
            print("Authorised access.")

class CEO(Employee):
    def __init__(self, name, post):
        super().__init__(name)
        self.post = post
    
    def allow_access(self, employee):
        employee.authorisation = True

class Junior(Employee):
    def __init__(self, name, post, authorisation = False):
        super().__init__(name)
        self.post = post
        self.authorisation = authorisation

ceo = CEO("Tim", "Ceo")
junior = Junior("Bill", "junior")

ceo.get_access(2)
junior.get_access(3)

ceo.allow_access(junior)
junior.get_access(4, junior.authorisation)