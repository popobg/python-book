import datetime

class Employee:

    # attributes of the class, not the instance
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_employees += 1

    # bind a function to an attribute;
    # allow to access the value without calling the function (no brackets
    @property       # decorator
    def email(self) -> str:
        return f"{self.first.lower()}.{self.last.lower()}@email.com"

    @property
    def full_name(self) -> str:
        return f"{self.first} {self.last}"

    # define a setter for a property method
    @full_name.setter
    def full_name(self, name: str) -> None:
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self) -> None:
        self.first = None
        self.last = None

    # regular method of a class, self = first arg
    # and self.func() to call the function
    def apply_raise(self) -> None:
        self.pay = int(self.pay * self.raise_amount)

    @classmethod    # class method, not instance method
    def set_raise_amount(cls, amount: int) -> None:  # cls refers to the class
        cls.raise_amount = amount   # change the attribute of the class

    # use class method as a constructor
    @classmethod
    def instance_from_string(cls, employee_string: str):
        first, last, pay = employee_string.split("-")
        return cls(first, last, pay)

    # put in the class and called with the class name, but independant.
    # it has a logical connection to the class, without need of its attributes.
    @staticmethod
    def is_workday(day: str) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developper(Employee):
    raise_amount = 1.10

    def __init__(self, first: str, last: str, pay: int, prog_lang: str) -> None:
        super().__init__(first, last, pay)  # == Employee.__init__(self, first, last, pay)
        self.programming_language = prog_lang

class Manager(Employee):

    def __init__(self, first: str, last: str, pay: int, employees=None) -> None:
        super().__init__(first, last, pay)

        if employees is None:   # == if not employees:
            self.num_of_employees = []
        else:
            self.employees = employees

    def add_emp(self, emp: Employee):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp: Employee):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.full_name)


# run this code only if we are running directly this script
if __name__ == "__main__":
    emp_1 = Employee("Corey", "Schafer", 50000)
    # print(emp_1.full_name)

    emp_1.full_name = "Jim Lol"
    emp_2 = Employee("Test", "Employee", 60000)

    emp_3 = Employee.instance_from_string("John-Doe-70000")
    emp_4 = Employee.instance_from_string("Steve-Smith-30000")
    emp_5 = Employee.instance_from_string("Jane-Doe-90000")

    # print(Employee.num_of_employees)

    dev_1 = Developper("Chloe", "Shepperd", 90000, "Python")
    dev_2 = Developper("Clem", "Tchou", 50000, "Java")

    manager = Manager("Tommy", "Bronx", 120000, [dev_1, dev_2])

    # manager.add_emp(emp_3)
    # manager.add_emp(emp_1)
    # manager.print_emps()
    # print("-----------------")
    # manager.remove_emp(emp_1)
    # manager.print_emps()

    # print(isinstance(manager, Manager))
    # print(isinstance(manager, Employee))
    # print(isinstance(manager, Developper))
    print(issubclass(Manager, Employee))
    print(issubclass(Manager, Developper))

    # print(dev_1.pay)
    # dev_1.apply_raise()
    # print(dev_1.pay)
    # print(dev_2.programming_language)

    # Employee.set_raise_amount(1.05)
    # # an instance can also call a class method
    # emp_1.set_raise_amount(1.09)

    # print(Employee.raise_amount)
    # print(emp_1.raise_amount)
    # print(emp_2.raise_amount)
    # print(emp_3.full_name)
    # print(emp_5.email)

    # del emp_1.full_name
    # print(emp_1.full_name)

    # my_date = datetime.date(2023, 7, 11)
    # print(Employee.is_workday(my_date))