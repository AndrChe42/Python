class User:

    def __init__(self, first_name, second_name):
        self.user_name = first_name
        self.user_surname = second_name
    
    def sayName(self):
        print(self.user_name)

    def saySurname(self):
        print(self.user_surname)
    
    def sayAll(self):
        print(self.user_name, self.user_surname)
        
