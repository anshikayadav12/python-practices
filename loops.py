count =1 #itarator
while(count <=5): #iteration
    print("hello")
    count +=1
print(count)


i=1
while i<=10:
    print(i," Hello World")
    i+=1
print(i)

#PRACTICE
#Question 01
j=1
while j<=100:
    print(j)
    j+=1
    
#Question 02
k=100
while k>=1:
    print(k)
    k-=1
    
#Question 03
a = int(input("Enter the number:"))
b=1
while b<=10:
    print(a,"*",b,"=",a*b)
    b+=1
    
    
    
#Question 04
list= [1,4,9,16,25,36,49,64,81,100]
idx=0
while idx < len(list):
    print(list[idx])
    idx+=1
    
#Example
heroes =["ironman","batman","thor","superman"]
index=0
while index < len(heroes):
    print(heroes[index])
    index+=1
    
#Question 5
tuple=(1,2,3,4,5,6,7,7,8,9,0,6)
x=6
i=0 #initailization
while i < len(tuple):
    if(tuple[i] == x):
        print("found at index ",i)
        break
    else:
        print("searching....")
    i+=1

#Break
i=1
while i <= 5:
    print(i)
    if(i==3):
        break
    i +=1
    
#continue
i=1
while i <= 10:
    
    if(i%2 == 0):# odd if(i%2 !== 0)
        i +=1
        continue #skip
    print(i)
    i +=1
    
#For loop
nums = [1,2,3,4,5]
for val in nums:
    print(val)
    
    
str="Anshikayadav"

for char in str:
    if(char == "a"):
        print("a Found")
        break
    print(char)
else:
    print("End")
    
#range
for el in range(5):
    print(el)
    
seq =range(20) #range(stop)
for i in seq:
    print(i)

for i in range(2,10): #range(start,stop)
    print(i)
    
for i in range(2,10,2): #range(start,stop,step)
    print(i)
    
    
#example
for i in range(2,100,2):  #even numbers
    print(i)
    

#pass statement
for i in range(5):
    pass 
print("some useful work")