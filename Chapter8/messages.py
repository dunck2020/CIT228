# Method 1
# import message_activity

# Method 2
# from message_activity import print_texts

# Method 3
# from message_activity import print_texts as pt

# Method 4
# import message_activity as mm

# Method 5
from message_activity import *

print('-----8-9-----')
text_messages = ['Hello', 'LOL', 'When are you getting here?', 'What are you doing?', "How's it going?"]

# message_activity.print_texts(text_messages)
# print_texts(text_messages)
# pt(text_messages)
# mm.print_texts(text_messages)
print_texts(text_messages)

print('\n-----8-10-----')
sent_messages = []
def send_message(messages):
    while messages:
        current_message = messages.pop()
        print(f'Sending: {current_message}')
        sent_messages.append(current_message)
send_message(text_messages)
print(f'Old message list empty: {text_messages}')
print(f'Sent message list: {sent_messages}')

print('\n-----8-11-----')
text_messages = ['Hello', 'LOL', 'When are you getting here?', 'What are you doing?', "How's it going?"]
sent_messages = []
send_message(text_messages[:])
print(f'Old message list saved: {text_messages}')
print(f'Sent message list: {sent_messages}')