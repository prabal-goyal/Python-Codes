class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, salary):
       self.first = first
       self.last = last
       self.salary = salary

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('Prabal', 'Goyal', '30000')
emp_2 = Employee('Aditi', 'Goyal', '50000')












# Employee.set_raise_amount(1.08)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)