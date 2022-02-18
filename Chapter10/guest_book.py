import random
import os

"""
# Try it yourself 10-3 & 10-4
filename = "guest.txt"
guest_name = input("What is your name (q to quit)? ")
with open(filename,"a") as f:
    while guest_name !='q':
        print(f"Welcome to emporium {guest_name}. We hope you have a wonderful visit!")
        guest_name +="\n"
        f.write(guest_name)    
        guest_name = input("What is your name (q to quit)? ")
"""
filename = "booked.txt"

# delete file if it exists
if os.path.exists(filename):
    os.remove(filename)

# get user name and assign a room
rooms = []
with open (filename, 'w') as room_file:
    guest = input("Please enter your name (q to quit)?")
    while guest != 'q':
        room_number = random.randint(1,50)
        while room_number in rooms:
            room_number = random.randint(1,50)
        print(f'{guest} you room number will be #{room_number}')
        rooms.append(room_number)
        guest += ' is in room #' + str(room_number) + '\n'
        room_file.write(guest)
        guest = input("Please enter your name (q to quit)?")

# display rooms that are now booked
with open(filename) as room_file:
    print('-----Guest name and room assignment-----')
    for guest_room in room_file:
        print(guest_room)


