class Employee(object):
    raise_amount = 1.1
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@kbi.net'

    def full_name(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


emp1 = Employee('구', '본익', 300)
emp2 = Employee('김', '정현', 400)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
