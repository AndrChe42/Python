class User:

    def __init__(self, first_name, second_name):
        self.user_name = first_name
        self.user_surname = second_name

    def say_name(self):
        print(self.user_name)

    def say_surname(self):
        print(self.user_surname)

    def say_all(self):
        print(self.user_name, self.user_surname)
