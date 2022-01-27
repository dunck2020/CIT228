current_users = ['elf', 'santa', 'grinch', 'reindeer', 'snowman']
new_users = ['pumpkin', 'bear', 'justice', 'amos', 'Elf']
lower_current_users = []
# 
for user in current_users:
    lower_current_users.append(user.lower())

for user in new_users:
    if user.lower() in lower_current_users:
        print(f'Sorry, but the username {user} has already been used, please select another.')
    else:
        print(f'The username {user} has been accepted, thank you!')