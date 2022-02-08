class User:
    """A simple user class"""
    def __init__ (self, first_name, last_name, age, occupation, fav_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.fav_color = fav_color
        self.login_attemps = 0

    def describe_user(self):
        print(f'\nUser {self.first_name} {self.last_name} is {self.age} years old, currently a {self.occupation} their favorite color is {self.fav_color}.')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name} thank you for joining the forum!')
    
    def increment_login_attemps(self):
        self.login_attemps += 1
        print(f'\n{self.last_name} has attempted to login {self.login_attemps} time(s).')
        
    def reset_login_attempts(self):
        self.login_attemps = 0