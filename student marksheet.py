class Marksheet:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.sum=0
        self.average=0
    def display(self):
        print("Students Marksheet")
        print("Name:",self.name)
        print("Mark1:",self.mark1)
        print("Mark2:",self.mark2)
        print("Mark3:",self.mark3)
        self.sum=self.mark1+self.mark2+self.mark3
        self.average=self.sum/3
        print("Average Score:",self.average)
        if self.average>=90:
            print("Grade A")
        elif self.average>=80:
            print("Grade B")
        elif self.average>=70:
            print("Grade C")
        elif self.average>=60:
            print("Grade D")
        elif self.average>=50:
            print("Grade E")
        else:
            print("Grade F")
student_name=input("Enter the student name")
mark1=float(input("Enter mark1"))
mark2=float(input("Enter mark2"))
mark3=float(input("Enter mark3"))
m=Marksheet(student_name,mark1,mark2,mark3)
m.display()