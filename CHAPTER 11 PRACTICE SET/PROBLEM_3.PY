#Create a class Employee and add salary and increment property to it.

#write a method 'SalaryAfterIncrement' method with a @property decorator with a setter which chnges the value of increment
# based on the salary. 

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        self._increment = 0.10  # Default increment 10%

    @property
    def SalaryAfterIncrement(self):
        """Calculates salary after applying increment."""
        return self._salary + (self._salary * self._increment)

    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, new_salary):
        """
        Setter changes increment percentage based on desired new salary.
        Formula: increment = (new_salary - current_salary) / current_salary
        """
        self._increment = (new_salary - self._salary) / self._salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self._salary}, Increment: {self._increment*100:.1f}%"


# Example usage:
emp = Employee("Bharti", 50000)
print(emp)  # Before increment
print("Salary after increment:", emp.SalaryAfterIncrement)

# Setting a new desired salary → updates increment percentage automatically
emp.SalaryAfterIncrement = 60000
print(emp)  # Increment updated
print("Salary after increment:", emp.SalaryAfterIncrement)

