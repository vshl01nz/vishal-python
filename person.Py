class Person:
    def __init__(self, name, password):
        self.name = name
        self.password = password


    def greet(self):
        print(f"Hello, {self.name}!")

    def login(self, username, password):
        if username == self.name and password == self.password:
            print("Welcome! You logged in successfully.")
        else:
            print("Your username or password is incorrect.")
vishal = Person(" Vishal ", " 123456")
username = input("enter your username")
password = input("entre your password ")
vishal.login(username , password)