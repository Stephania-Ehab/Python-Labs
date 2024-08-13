# class number (1)

class Human:
    species = "Homo sapiens"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        return f"Hi, my name is {self.name}, I am {self.age} years old and I am {self.gender}."
    
    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."

# Example

john = Human("Stephania", 22, "Female")
print(john.introduce())
print(john.celebrate_birthday())



# class number (2)

class Employee:
    company_name = "Tech Corp"
    def __init__(self, name, age, gender, employee_id, position, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.position = position
        self.salary = salary
    
    def work(self):
        return f"{self.name} is working as a {self.position}."
    
    def get_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
        return f"{self.name} got a raise! New salary: ${self.salary:.2f}"

def promote(self, new_position, new_salary=None):
        self.position = new_position
        if new_salary:
            self.salary = new_salary
        return f"Congratulations {self.name}! You have been promoted to {self.position}."

# Example

emma = Employee("Stevy", 22, "Female", "Web Developer", 10000)
print(emma.work())
print(emma.get_raise(10))
print(emma.promote("Senior Web Developer", 15000))

