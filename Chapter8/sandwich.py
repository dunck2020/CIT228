def make_sandwich(*items):
    print(f'Making a sandwich with the following ingredients:')
    for item in items:
        print(f'- {item}')

make_sandwich('bacon', 'ham', 'cheese')
make_sandwich('provolone')
make_sandwich('peanut butter', 'jelly')