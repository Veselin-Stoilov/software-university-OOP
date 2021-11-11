from inheriatnce_lab.multiple_inheritance.project.employee import Employee
from inheriatnce_lab.multiple_inheritance.project.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching"

