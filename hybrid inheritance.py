class Student1 :
    def display(self):
        print("hi")
class Student2(Student1):  #inheritance
    def display1(self):
        print("hello")
class Student3(Student1):  #inheritance
    def display2(self):
        print(" started")

class College(Student2,Student1):  # inheritance
    def display3(self):
        print("Exam ")
obj=College()
obj.display()
obj.display1()
obj.display3()
