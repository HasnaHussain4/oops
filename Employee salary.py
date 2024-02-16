class Employee:
    def __init__(self,name,basic,deduction,allowance):
        self.name=name
        self.basic=basic
        self.deduction=deduction
        self.allowance=allowance
        self.net_salary=0
    def display(self):
        self.net_salary=self.basic+(self.basic*self.allowance/100)-(self.basic*self.deduction/100)
        print("Salary Details")
        print("Name:",self.name)
        print("Basic:",self.basic)
        print("Deduction:",self.deduction)
        print("Allowance:",self.allowance)
        print("Net salary:",self.net_salary)
name=input("Enter the name")
basic=int(input("Enter the basic salary:"))
deduction=int(input("Enter the deduction"))
allowance=int(input("Enter the allowance"))
emp=Employee(name,basic,deduction,allowance)
emp.display()