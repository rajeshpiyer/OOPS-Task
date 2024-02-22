class staff:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def printDetails(self):
        print(f"Role : {self.role}\nDepartment : {self.dept}\nSalary : {self.salary}")
        
class teacher(staff):
    def __init__(self,name,age,role,dept,salary):
        self.name = name
        self.age = age
        super().__init__(role,dept,salary)
    
    def printDetails(self):
        print(f"Name : {self.name}\nAge : {self.age}")
        super().printDetails()

print("Enter the details of the teacher 1 : ")
name = input("Name : ")
age = int(input("Age : "))
role = input("Role : ")
dept = input("Department : ")
salary = int(input("Salary : "))

teacher1 = teacher(name,age,role,dept,salary)
print("\n\nTeacher 1 : ")
teacher1.printDetails()