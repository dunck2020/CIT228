filename = "learning_python.txt"

# Try it yourself 10-1
with open(filename) as f:
    contents = f.read()
print('--------Output from read()------------------------')
print(contents) 

print('--------Output from for loop inside with.open-----')
with open(filename) as f:
    for line in f:
        print(line)

print('--------Output from readlines()-------------------')
with open(filename) as f:
    all_lines = f.readlines()
for each_line in all_lines:
    print(each_line)

# Try it yourself 10-2
print('---------Replacing "Python" with "c#"-------------\n')
with open(filename) as f:
    for line in f:
        print(f'Original Line: {line}')
        print(f'Modified Line: {line.replace("Python", "c#")}')
        print('-------------------\n')