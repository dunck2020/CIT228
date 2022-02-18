def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['ishmael.txt', 'the art of war.txt', 'works of lord byron.txt']
for filename in filenames:
    count_words(filename)

# try it yourself 10-10
def find_words(filename, search_string):
    """search files for given string"""
    try:
        with open (filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        contents = contents.lower()
        search_string = search_string.lower()
        word_count = contents.count(search_string)
        print(f'The word "{search_string}" you are searching for appeared {word_count} times in {filename}')


search_word=input("What common word would you like to search for within the files? ")    
for filename in filenames:
    find_words(filename,search_word)

