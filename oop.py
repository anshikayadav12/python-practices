# creating class 
class Student:
    #Contractor
    college_name="ABC College" #class attribute
    
    def __init__(self): #Default contractor
        pass
        
        
    def __init__(self,fullname,marks):  #parameterized constractor
        self.name =fullname #instance attribute
        self.marks=marks
        print("adding new student in database")

# creating object
s1=Student("Karan Kundra",98)
print(s1.name,s1.marks)
s2=Student("Shiva Tiwari",78)
print(s2.name,s2.marks)
print(s2.college_name)


class Car:
    color="blue"
    brand="Maruti Suzuki"
car1=Car()
print(car1.color)
print(car1.brand)

# methods
class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def Welcome(self):
        print("Welcome student",self.name)
    def get_marks(self):
        return self.marks
s1 = Students("karan",98)
s1.Welcome()
print(s1.get_marks())



#static methods
class Students:
    
    @staticmethod
    def hello():
        print("Hello")
        
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def Welcome(self):
        print("Welcome student",self.name)
    def get_marks(self):
        return self.marks
s1 = Students("karan",98)
s1.Welcome()
print(s1.get_marks())
s1.hello()

#abtraction
class car:
    def __init__(self):
        self.acc = False
        self.brk =False
        self.clutch=False
        
    def start (self):
        self.clutch=True
        self.acc = True
        print("car started....")
        
car1=car()
car1.start()

#Encapsulation
