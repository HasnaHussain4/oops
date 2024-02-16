class Student1 :
    def display(self):
        print("hi")
class Student2(Student1):  #inheritance
    def display1(self):
        print(" started")

class College(Student1):  # inheritance
    def display2(self):
        print("Exam started")
obj=College()
obj.display()
obj.display2()
