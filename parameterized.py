class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:%s\nAge:%d"%(self.name,self.age))
st1=Student("Hasna",20)
print(st1.display())

