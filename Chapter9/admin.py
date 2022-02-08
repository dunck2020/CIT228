from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age, occupation, fav_color, permissions):
        super().__init__(first_name, last_name, age, occupation, fav_color)
        self.privileges = Privileges(permissions)