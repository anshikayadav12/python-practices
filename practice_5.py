#Question 01
list = [1,4,9,16,25,36,49,64,81,100]

for int in list:
    print(int)
else:
    print("end")
print(type(list))

#Question 02
tup=(1,4,9,16,25,36,49,81,100)
for int in tup:
    if int == 49:
        print("49 Found")
        break
    print(int)
    
print(type(tup))


#Range Practice Question
#Question 01
for i in range(1,100):
     print(i)
    
#Question 02
for i in range(100,0,-1):
    print(i)
    

#Question 03
n = (input("Enter the Number:"))

for i in range(1,11):
    print(i*n)
    
    
#practice Questions
n = 5
sum = 0
for i in range (n+1):
     sum +=i
print("Total sum =",sum)     


#practice Question 01
n =7 
sum= 0 
j=1
while j <=n:
    sum +=j
    j +=1

# for j in range(1,n+1):
#     sum +=j
    
print("total sum =",sum)



#Question 02
f=5
fact=1
k=f+1
while k<=f:
    sum*= k
    k+=1
print("Factorial",f,":",fact)

#same question withfor loop
n=5
fact =1
for i in range(1,n+1):
    fact*= i
print("Factorial ",fact)