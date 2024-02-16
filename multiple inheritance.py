class Student1 :
    def display(self):
        print("hi")
class Student2:  #inheritance
    def display1(self):
        print("Exam started")

class College(Student1,Student2):  # inheritance
    def display2(self):
        print("Exam started")
obj=College()
obj.display()
obj.display1()
obj.display2()
