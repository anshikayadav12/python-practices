# class student:
#     def __init__(self,name):
#         self.name= name
        
# s1 = student("Anshika")
# print(s1.name)
# del s1.name
# print(s1.name)

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def reset_pass(self):
        print(self.acc_pass)
        
acc1=Account("123456","abcd")
print(acc1.acc_no)
# print(acc1.__acc_pass)


#Private attribute & methods
class Person:
    __name = "anonymous" #if want to private our passwords simple give a 2 underscore to attributes and method
    
    def __hello(self):
        print("hello person")
        
    def welcome(self):
        self.__hello()
        
        
p1 = Person()
print(p1.welcome())

#Inheritance   
#Single inheritance
class Car:
    color="blue"
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stopped..")
        
class Toyatocar(Car):
    def __init__(self,name):
        self.name = name
        
car1=Toyatocar("fortuner")
car2=Toyatocar("prlus")

print(car1.name) 
print(car1.start())
print(car1.color)


#multi-level inheritance

class car:
    @staticmethod
    def start():
        print("car started...")
        
    @staticmethod
    def stop():
        print("car stop...")
        
class toyotaCar(car):
    def __init__(self,brand):
        self.brand = brand
        
class fortuner(toyotaCar):
    def __init__(self,type):
        self.type= type
        
car1 =fortuner("diesel")
car1.start()

#Multiple inheritances
class A:
    varA="Welcome to class A"
class B:
    varB="Welcome to Class B"
    
class C(A,B):
    varC="Welcome to class C"

c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)


#Super method
class Car:
    def __init__(self,type):
        self.type =type
        
    @staticmethod
    def start():
        print("car started....")
        
    @staticmethod
    def stop():
        print("car stopped....")
        
class Toyota(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        
car1 =Toyota("prius","electric")
print(car1.type)

#class method
class Person:
    name="anonymous"
    
    # def chnageName(self,name):
    #     #Person.name = name
    #     self.__class__.name = "Rahul kumar"
    
    @classmethod
    def changeName(cls,name):
        cls.name = name
        
p1=Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)


#@property decorator
class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem= chem
        self.math = math
        # self.percentage = str((self.phy+self.chem+self.math)/3 )+ "%"
        
    # def calcpercentage(self):
    #     self.percentage = str((self.phy+self.chem+self.math)/3 )+ "%"
    
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math) / 3)+"%"
        
stu1=Student(98,97,99)
print(stu1.percentage)

stu1.phy=86
#print(stu1.phy)
#stu1.calcpercentage()
print(stu1.percentage)

#polymorphism (operator overloading)
print(1+2)  #3
print("apna"+"college")  #concatenate
print([1,2,3]+[4,5,6]) #merge

#complex number 
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
        
      #dunder function in polymorphism
    def __add__(self,num2):
        newReal=self.real +num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    #dunder function in polymorphism
    def __sub__(self,num3):
        newReal=self.real + num3.real
        newImg = self.img + num3.img
        return Complex(newReal,newImg)
    
    def __mul____(self,num4):
        newReal = self.real + num4.real
        newImg = self.img + num4.img
        return Complex(newReal,newImg)
    
    def __turediv____(self,num5):
        newReal = self.real + num5.real
        newImg =self.img + num5.img
        return Complex(newReal,newImg)
        
    def __mod____(self,num6):
        newReal = self.real + num6.real
        newImg = self.real + num6.img
        return complex(newReal,newImg)
    
    
num = Complex(2,4)
num.showNumber()
  
num1= Complex(1,3)
num1.showNumber()

num2 =Complex(4,6)
num2.showNumber()

num3= num - num2
num3.showNumber()
# num3=num1.add(num2)
# num3.showNumber()

# num4 = num * num3
# num4.showNumber()

# num5 = num /  num3
# num5.showNumber()

# num6 = num + num5
# num6.showNumber()

# num7=num%num6
# num7.showNumber()