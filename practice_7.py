#File I/O
#Question 01
# f=open("practice.txt","w")
# f.write(" Hi everyone\n We are learning fileI/O\n using java\n I like programming in java ")


#Question02
with open("practice.txt","r") as f:
    data=f.read()
    
new_data = data.replace("java","python")
print(new_data)


#question 03
word ="learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")
        
# function
def check_for_word():
    word ="xlearning"
    with open("practice.txt","r") as f:
         data = f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")
        
check_for_word()


#Question 04
def check_for_line():
    word="pyq"
    data=True
    line_no=1
    with open("practice.txt","r")as f:
        while data:
            data=f.readline()        
            if(word in data):
                print(line_no)
                return
            line_no +=1
    return -1

print(check_for_line())

#Question 05
count=0
with open ("practice.txt","r") as f:
    data=f.read()
    print(data)
    
    # num=""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print (int(num))
    #         num=""
    #     else:
    #         num+=data[i]     
    
    nums=data.split(",")
    for val in nums:
        if(int(val)% 2 ==0):     
                count+= 1
print(count)