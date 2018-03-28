class Employee(object):

    raise_amount = 1.1

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

emp_1 = Employee('Bob', 'Williams', 50000)
emp_2 = Employee('Hank', 'Hog', 30000)

print emp_1.raise_amount
print Employee.raise_amount
print emp_2.raise_amount
