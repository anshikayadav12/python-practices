#recursion conditions
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
    
show(5) #5,4,3,2,1

#factorial
def fact(n):
    if(n == 0 or n==1):
        return 1
        return  fact(n-1)* n
print(fact(5))
