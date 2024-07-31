#Question 01
num=int(input("Enter the number:"))
if((num%2)==0):
    print("Even Number -",num)
else:
    print("Odd Number -",num)
    
    
#Question 02
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if(num1>num2 and num1>num3):
    print(num1,"is greater than ",num2,"and",num3)
elif( num2>num3):
    print(num2,"is greater than",num1,"and",num2)
else:
    print(num3,"is grater than",num1,"and",num2)
    
    
#Question 03
num4=int(input("Enter the number:"))
if((num4%7) ==0):
    print("Number is divible of 7")
else:
    print("number is not divisible of 7")