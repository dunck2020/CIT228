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

class Admin(User):
    def __init__(self, first_name, last_name, age, occupation, fav_color, permissions):
        super().__init__(first_name, last_name, age, occupation, fav_color)
        self.privileges = Privileges(permissions)

class Privileges:
    """A class to list privileges for users"""
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f'\nThis user can complete the following tasks:')
        for task in self.privileges:
            print(f'\t-{task.title()}')    

admin_privileges = ['add post', 'delete post', 'ban user', 'delete user']
new_admin = Admin('Jerry', 'Springer', 76, 'Talk Show Host', 'salmon', admin_privileges)
new_admin.greet_user()
new_admin.describe_user()
new_admin.privileges.show_privileges()



