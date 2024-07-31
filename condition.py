light="yellow"
if(light =="red"):
    print("Stop")
elif(light =="green"):
    print("Go")
elif(light =="yellow"):
    print("Look")
else:
    print("light is broken")
    
    
    
# Another example
age=14
if(age >=18):
    print("can vote") #indentation
else:
    print("Cannot vote")

#another example

Marks=int(input("Enter Your Marks:"))
if(Marks>=90):
    print("Grade:A")
elif(Marks>=80 and Marks<90):
    print("Grade:B")
elif(Marks>=70 and Marks<80):
    print("Grade=C")
else:
    print("Grade:D")
    
    
#nesting
age=int(input("Enter the age"))
if(age>=18):
    if(age>=80):
        print("Cannot Driven")
    else:
        print("can driven")
else:
    print("Cannot drive")
    