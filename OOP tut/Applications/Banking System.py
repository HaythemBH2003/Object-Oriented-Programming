class Customer:
    def __init__(self, name, age, gender, card_code):
        self.name = name
        self.age = age
        self.gender = gender
        self.card_code = card_code
        self.balance = 0

    def show_customer_info(self):
        print()
        print(f"Name    ** {self.name}")
        print(f"Age     ** {self.age}")
        print(f"Gender  ** {self.gender}")
        print(f"Code    ** {(len(str(self.card_code))-2)* '-'}{(str(self.card_code))[-2:]}")
        print(f"Balance ** {self.balance} DT")
        print()

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            if (str(self.gender)).upper() == "MALE": 
                print(f"Mr {self.name}, your balance is not enough.")
                print()
            else:
                print(f"Mrs {self.name}, your balance is not enough.")
                print()
        else:
            self.balance -= amount

    def transfer(self,receiver, amount):
        if amount <= self.balance:
            self.balance -= amount
            receiver.balance += amount
            print("Transaction executed successfully")
            print("Accounts:")
            print()
            self.show_customer_info()
            receiver.show_customer_info()
        else:
            if (str(self.gender)).upper() == "MALE": 
                print(f"Mr {self.name}, your balance is not enough.")
                print()
            else:
                print(f"Mrs {self.name}, your balance is not enough.")
                print()

class Bank:
    number_of_customers = 0

    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        if customer.age < 18:
            print("You must be at least 18 years old to create a bank account.")
        elif len(str(customer.card_code)) < 3:
            print("Code is too short. Please try again.")
        elif (str(customer.gender)).upper() != "MALE" and (str(customer.gender)).upper() != "FEMALE":
            print("Gender unrecognisable. Please try again.")
        elif len(str(customer.name)) == 0:
            print("Name is missing. Please try again.")
        else:
            (self.customers).append(customer)
            if (str(customer.gender)).upper() == "MALE": 
                print(f"Mr {customer.name} successfully created an account.")
                print()
            else:
                print(f"Mrs {customer.name} successfully created an account.")
                print()

    def show_all(self, customers):
        for customer in customers:
            customer.show_customer_info()

tim = Customer("Tim", 19, "Male", 1234567)
joe = Customer("Joe", 23, "Female", 777777)

bank = Bank("National Agriculture Bank")

bank.add_customer(tim)
bank.add_customer(joe)

tim.deposit(1200)
joe.deposit(900)

tim.withdraw(1500)
joe.withdraw(50)

bank.show_all(bank.customers)

tim.transfer(joe, 200)
