class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    print("adding new student in database")
    
    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum +=val
        print("hi",self.name,"your avg score:" ,sum/3)
            
s1=Student("Karan Kundara",[98,78,56])
s1.get_avg()

s1.name="Ansh yadav"
s1.get_avg()

#Question 2
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    #debit
    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited")
        print("total balance =",self.get_balance())
        
    #credit
    def credit(self,amount):
        self.balance +=amount
        print("Rs",amount,"was credit")
        print("total balance =",self.get_balance())

    def get_balance(self):
        return self.balance
acc1=Account(10000,1234567)
acc1.debit(1000)
acc1.credit(5000)