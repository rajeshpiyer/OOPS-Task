class student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def display(self):
        print(f"{self.name}\t{self.score}")
    
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
print("Name\tScore")
s1.display()
s2.display()