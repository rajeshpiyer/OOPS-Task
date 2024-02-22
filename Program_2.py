class Students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def printObject(self):
        print(f'\nName : {self.name}\nAge : {self.age}\nGrade : {self.grade}')

def printClassName(object):
    print("\nClass Name : ",type(object).__name__)

st1 = Students("Rajesh",26,"A")
printClassName(st1)
st1.printObject()
