#Question 1
movies=[]
mov1=input("Enter 1st movie:")
mov2=input("Enter 2nd movie:")
mov3=input("Enter 3rd movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#Question 2
pal=[1,2,3,2,1]
copy_pal =pal.copy()
copy_pal.reverse()

if(copy_pal == pal ):
    print("Palindrome")
else:
    print("NOT Palindrome")

#Question 3
list=["C","D","A","A","B","B","A"]

print(list.count("A"))


#Question 4
list.sort()
print(list)