employees = {
    'Emp1': {
        'name':'Todd',
        'age': 24,
        'title': 'programmer',
        'salary': 90000,
        },
    'Emp2': {
        'name':'Bekka',
        'age': 36,
        'title': 'systems analyst',
        'salary': 135000,
        },
    'Emp3': {
        'name':'Devon',
        'age': 21,
        'title': 'intern',
        'salary': 10000,
        },
    'Emp4': {
        'name':'Erica',
        'age': 30,
        'title': 'senior engineer',
        'salary': 145000,
        },        
}
for emp, details in employees.items():
    print(f"\n\tName: {details['name']}")
    age =details['age']
    title = details['title'].title()
    salary = details['salary']

    print(f"\tAge: {age}")
    print(f"\tTitla: {title}")
    print(f"\tSalary: ${salary} annually")