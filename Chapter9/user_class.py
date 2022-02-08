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

user1 = User('Bob', 'Jones', 43, 'Dish Washer', 'Blue')
user2 = User('Liv', 'Smith', 10, 'Student', 'Lavender')
user3 = User('Monet', 'Monetgomery', 27, 'Programmer', 'Red')
user4 = User('Jack', 'Fishton', 78, 'Comedian', 'Pink')
user5 = User('Flo', 'Stone', 30, 'Rock Climber', 'Orange')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
user4.describe_user()
user4.greet_user()
user5.describe_user()
user5.greet_user()

user_new = User('Hacker', 'Joe', 21, 'Hacker', 'black')
user_new.increment_login_attemps()
user_new.increment_login_attemps()
user_new.increment_login_attemps()
user_new.increment_login_attemps()
user_new.increment_login_attemps()
user_new.increment_login_attemps()
user_new.increment_login_attemps()
user_new.increment_login_attemps()
user_new.increment_login_attemps()
user_new.increment_login_attemps()
user_new.reset_login_attempts()
print(f"\n{user_new.last_name}'s login attemps have been reset, now total attempts are {user_new.login_attemps}.")
print(f'{user_new.first_name} {user_new.last_name} your account is locked... Please contact Admin!')
