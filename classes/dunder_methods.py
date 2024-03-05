import datetime

class Employee:
    raise_amount = 1.04

    # most known special method
    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self) -> str:
        return f"{self.first.lower()}.{self.last.lower()}@email.com"

    @property
    def full_name(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        self.pay = int(self.pay * self.raise_amount)

    # an unambiguous representation of the object
    # used for debugging, logging,...
    # meant for the dev
    def __repr__(self) -> str:
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    # used as a display for the end user
    def __str__(self) -> str:
        return f"{self.full_name} - {self.email}"

    # just for the example, because irl
    # it is better to have a more explicit name
    def __add__(self, other) -> int:
        return self.pay + other.pay

    def __len__(self) -> int:
        return len(self.full_name)

if __name__ == "__main__":
    emp_1 = Employee("Corey", "Schafer", 50000)
    emp_2 = Employee("Test", "Employee", 60000)

    # this call the __str__() dunder/special method
    # print(emp_1)
    # print(repr(emp_1))
    # print(str(emp_1))
    # print(emp_1.__repr__())
    print(emp_1 + emp_2)
    print(len(emp_1))