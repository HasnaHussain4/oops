class Bank:
    def __init__(self,name,acc_no):
        self.name=name
        self.acc_no=acc_no
        self.balance=0
    def display(self):
        print()
        print(".....Account details.....")
        print("Account Holder name :",self.name)
        print("Account Number :",self.acc_no)
        print()
    def deposit(self,deposit):
        self.dp=deposit
        self.balance=self.balance+self.dp
        print("Success")
        print()
    def amount_display(self):
        return self.balance
    def withdraw(self,w):
        if w<self.balance:
            self.balance=self.balance-w
            print("Success")
        else:
            print("No balance")



name=input("Enter the nane:")
acc_no=input("Enter the acc_no")
b=Bank(name,acc_no)
b.display()
print("1.Deposit")
print("2.Withdraw")
print("3.View")
print("4.Exit")
while(True):
    c=int(input("Enter the choice"))
    if c==1:
        deposit=int(input("Amount"))
        b.deposit(deposit)
        print()
    elif c==2:
        wr=int(input("Amount"))
        b.withdraw(wr)
    elif c==3:
        print("Balance",b.amount_display())
    elif c==4:
        break
    else:
        print("Invalid input")


