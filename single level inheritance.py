class Student :
    def display(self):
        print("hi")
class College(Student):  #inheritance
    def exam(self):
        print("Exam started")
obj=College()
obj.display()
obj.exam()