import json

codeGlossary = {
    'if': 'Conditional test which allows you to check any condition',
    'list': 'A collection of items in a particular order',
    'whitespace': 'any nonprinting character, including spaces, tabs and end-of-line symbols',
    'syntax error': 'occurs when python does not recognize a section of code as valid python language',
    'loop': 'method to continually repeat instructions until a condition is met',
    'key': 'item used to access the data in a dictionary key:value pair',
    'comments': 'python comments begin with #',
    'del': 'python command used to delete items from a dictionary',
    'boolean': 'variables that are either true or false',
    'operators': 'mathematical operators for evaluating various entities'
}

def menu():
    selection = int(input("1-create new file:\n2-read existing file:\n3-add to file:\n4-quit:  "))
    while selection!=1 and selection!=2 and selection!=3 and selection!=4:
        print("You made an invalid selection, please try again")
        selection = int(input("1-create new file:\n2-read existing file:\n3-add to file:\n4-quit:  "))
    return selection

# json dump
def create_file(input_data):
    create_new = input('Creating a new file will overwrite and information if already existing, continue: y or n:')
    if create_new == 'y':
        with open("codeGlossary.json", "w") as write_file:
            json.dump(input_data, write_file, indent=4, sort_keys=True)
            print("File codeGlossary.json has been created")

# json read
def read_file():
    try:
        with open("codeGlossary.json") as read_file:
            code_stuff = json.load(read_file)
    except FileNotFoundError:
        print("The file doesn't exist or cannot be found.")
        print("Please make a different menu selection")      
    else: 
        for key, value in code_stuff.items():
            print(f"\n{key} = {value}")
    
# json append
def append_file(new_data):
    with open("codeGlossary.json", "r+") as add_file:
        codeDictionary = json.load(add_file) 
        codeDictionary.update(new_data)
        add_file.seek(0)
        json.dump(codeDictionary, add_file, indent=4, sort_keys=True)
        print("New data has been added to codeGlossary.json")


# get key from user
def get_key():
    key_value = input("Enter the programming term you have information for: ")
    key_input = key_value.split()[0]
    key_input = key_input.lower()
    return key_input

# get value from user
def get_value():
    glossary_info = input("Enter the description of the term: ")
    return glossary_info


user_selection = menu()
while user_selection != 4:
    if user_selection == 1:
        create_file(codeGlossary)
    elif user_selection == 2:
        read_file()
    elif user_selection == 3:
        key = get_key()
        value = get_value()
        new_code_glossary_data = {key:value}
        append_file(new_code_glossary_data)
    else:
        print("The option you selected is not available, please try again")        
    user_selection = menu()