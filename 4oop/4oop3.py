class Person:
   origin_country = "USA"

   def __init__(self, name, age, gender):
     self.name = name
     self.age = age
     self.gender = gender

   def speak(self, words):
     print(f"{self.name} speaks: {words}")


class Employee(Person):
   def __init__(self, name, age, gender, salary, job_title):
     super().__init__(name, age, gender)
     self.salary = salary
     self.job_title = job_title

   def display_info(self):
     print(f"Employee {self.name} works as a {self.job_title}")

