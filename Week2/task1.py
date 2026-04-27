from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, emp_id, name, email):
        self.__emp_id = emp_id
        self.__name = name
        self.__email = email

    
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

   
    @abstractmethod
    def calculateSalary(self):
        pass



class RegularEmployee(Employee):
    def __init__(self, emp_id, name, email, base_pay):
        super().__init__(emp_id, name, email)

        if base_pay > 0:
            self.__base_pay = base_pay
        else:
            raise ValueError("Base pay must be > 0")

    def calculateSalary(self):
        return self.__base_pay



class Manager(Employee):
    def __init__(self, emp_id, name, email, base_pay):
        super().__init__(emp_id, name, email)

        if base_pay > 0:
            self.__base_pay = base_pay
        else:
            raise ValueError("Base pay must be > 0")

    def calculateSalary(self):
        return self.__base_pay + (0.2 * self.__base_pay)



class Contractor(Employee):
    def __init__(self, emp_id, name, email, hourly_rate, hours_worked):
        super().__init__(emp_id, name, email)

        if hourly_rate > 0 and hours_worked >= 0:
            self.__hourly_rate = hourly_rate
            self.__hours_worked = hours_worked
        else:
            raise ValueError("Invalid input values")

    def calculateSalary(self):
        return self.__hourly_rate * self.__hours_worked


employees = [
    RegularEmployee(1, "Tarun", "tarun@gmail.com", 30000),
    Manager(2, "Rohit", "rohit@gmail.com", 50000),
    Contractor(3, "Anita", "anita@gmail.com", 500, 40)
]

for emp in employees:
    print(f"ID: {emp.get_emp_id()}, Name: {emp.get_name()}")
    print(f"Salary: {emp.calculateSalary()}")
    print("-" * 30)
