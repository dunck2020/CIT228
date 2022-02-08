from admin import Admin

# These were both imported into admin so we shouldn't have to import them again
# the program runs fine without these two import statements
# from user import User
# from privileges import Privileges

admin_privileges = ['add post', 'delete post', 'ban user', 'delete user']
new_admin = Admin('Jerry', 'Springer', 76, 'Talk Show Host', 'salmon', admin_privileges)
new_admin.greet_user()
new_admin.describe_user()
new_admin.privileges.show_privileges()