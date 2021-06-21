###########   STATIC METHODS   ###########
''' STATIC METHODS DO SOMETHING BUT  DON'T 
    CHANGE ANYTHING. THEY DON'T HAVE ACCES
    TO ANY INSTANCE.                   '''

class Math:
    ###  DEFINE A STATIC CLASS METHOD  ###
    '''            EXAMPLE 1           '''
    @staticmethod 
            # @staticmethod ---> DECORATOR
            # INDICATES THAT IT IS  STATIC
    def add5(number):
        return number + 5

print(Math.add5(2))