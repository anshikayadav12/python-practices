# a= 5
# b=10

# sum =a+b
# print(sum)
#More line of code

def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum

calc_sum(3,6)
calc_sum(5,7)
calc_sum(8,9)
calc_sum(12,34)


#type of writing code
def calc_sub(a,b):
    return a-b

sum =calc_sub(12,6)
print(sum)


#3 type of function work
def multiple(a,b,c):
    multi=a*b*c
    print(multi)
    return multi


multiple(4,5,6)

def print_hello():
    print("Hello")

print_hello()
print_hello()

#Average of 3
def avg_num(a,b,c):
    num=(a+b+c)/3
    print(num)
    return num



avg_num(4,5,6)
avg_num(1,2,3)
avg_num(81,90,78)


#default parameters

def cal_pro(a,b=2):
    print(a*b)
    return a*b

cal_pro(3)

