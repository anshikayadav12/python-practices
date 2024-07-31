#Function practice question
#Question number 01
num=["anshika","Ambar","akash","Indar"]
heroes =["thor","ironman","captain america","shaktiman"]

def length_list(list):
    print(len(list))

length_list(num)
length_list(heroes)

#Question 02

sum=[1,2,3,4,5,6,7,8,9,0]
def element_list(list):
    print(list)
    
element_list(sum)

#Question 03
num=5

def cal_fact (num):
    fact=1
    for i in range(1,num+1):
        fact *=i
    print(fact)
    
cal_fact(5)

#Question 04 
def convert (a):
    USD =83*a
    print("usd_val",a,"INR",USD)
    
    
convert(3)

#HOMEWORK QUESTION
# def odd_even():
    # num=input("Enter the number:")
    # return (num%2)==0
    # print("EVEN")
    # return 
    # print("ODD")    
        
# odd_even()

#REcursive practice question
def calc_sum(n):
    if(n==0):
        return 0
    print(n)
    return calc_sum(n-1) + n
sum=calc_sum(5)
print(sum)


#Question 02
def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits= ["mango","litchi","apple","banana"]

print_list(fruits)