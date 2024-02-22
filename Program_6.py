class student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
        self.calc_grade()
    
    def display(self):
        print(f"{self.name}\t\t{self.score}\t\t{self.grade}\n")
    
    def calc_grade(self):
        if self.score>=90:
            self.grade="A+"
        elif self.score>=80:
            self.grade="A"
        elif self.score>=70:
            self.grade="B+"
        elif self.score>=60:
            self.grade="B"
        elif self.score>=50:
            self.grade="C+"
        elif self.score>=40:
            self.grade="C"
        else:
            self.grade="FAILED"
    
def student_input():
    name = input("Name : ")
    score = int(input("Score : "))
    return name,score

print("-- Student 1 --")
name,score = student_input()
s1 = student(name,score)

print("-- Student 2 --")
name,score = student_input()
s2 = student(name,score)

print("-- Student List --")
print("Name\t\tScore\t\tGrade")
s1.display()
s2.display()