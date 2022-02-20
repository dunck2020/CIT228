class Employee:
    """A simple employee class"""
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount = 5000):
        self.annual_salary += raise_amount
        print(f'\n{self.first_name} {self.last_name} was awarded a ${raise_amount} raise for a annual salary of ${self.annual_salary}')



