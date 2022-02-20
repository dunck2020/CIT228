import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Unit Tests for the employee class """
    
    def setUp(self):
        first_name = "Niko"
        last_name = "Jefferson"
        annual_salary = 80000
        self.employee = Employee(first_name, last_name, annual_salary)
    
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 85000)

    def test_give_custom_raise(self):
        raise_amount = 23000
        self.employee.give_raise(raise_amount)
        self.assertEqual(self.employee.annual_salary, 103000)

if __name__ == '__main__':
    unittest.main()