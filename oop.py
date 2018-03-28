class Employee:

    raise_amount = 1.05
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_employees += 1

    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print emp.fullname()

emp_1 = Employee('Bob', 'Williams', 50000)
emp_2 = Employee('Hank', 'Hog', 30000)

dev_1 = Developer('Barry', 'Bonds', 100000, 'Python')
dev_2 = Developer('Tony', 'Gywnn', 90000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 75000, [dev_1])
mgr_1.add_employee(dev_2)
mgr_1.remove_employee(dev_1)

print mgr_1.email
print mgr_1.print_employees()
