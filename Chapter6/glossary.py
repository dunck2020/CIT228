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
print('----------------Try it 6-3------------------- ')
print('If statement:')
print('\t', codeGlossary['if'], '\n')
print('List:')
print('\t', codeGlossary['list'], '\n')
print('Whitespace:')
print('\t', codeGlossary['whitespace'], '\n')
print('Syntax error:')
print('\t', codeGlossary['syntax error'], '\n')
print('Loop:')
print('\t', codeGlossary['loop'], '\n')

print('----------------Try it 6-4------------------ ')
for k,v in codeGlossary.items():
    print(f'{k.title()}:')
    print(f'\t {v.title()}')
