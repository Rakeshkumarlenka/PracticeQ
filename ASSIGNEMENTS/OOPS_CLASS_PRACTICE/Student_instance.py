class Student:
    def __init__(self,n = '',m=0):
        self.name = n
        self.marks = m

    def display(self):
        print("hi",self.name)
        print("Your marks",self.marks)

    def calculate(self):
        if(self.marks>=600):
            print("FIRST GRADE")
        elif(self.marks>=500):
            print("SECOND GRADE")
        elif (self.marks >= 350):
            print("SECOND GRADE")
        else:
            print("FAIL")

n= int(input("How many students?"))
i = 0
while(i<n):
    name = input("Enter the name:")
    marks =int(input("Enter the marks:"))
    i += 1
s = Student(name,marks)
s.display()
s.calculate()

