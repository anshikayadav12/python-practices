#f=open("File_name","mode")
# f=open("demo.txt" ,"r")
# data=f.read(10)
# line=f.readline()
# print(data)
# print(line)
# print(type(data))
# f.close()

#Write mode
f=open("demo.txt","a")
data =f.write("I want to some good peoples in my life because no one understand my feels anymore")
f.close()


#Append mode
f=open ("demo.txt","a")
data = f.write("\nI want to know that i am doing anythink wrong with any one of them in my life")
f.close()

#append the sentence start of the sentence overwrite
f = open("demo.txt","r+")
data = f.write("Anshika ")
f.close()

#W+
f = open("demo.txt","w+")
print(f.read())
f.write("Anshika yadav is very bad daughter.")
f.close()

#with syntax
with open("demo.txt","r")as f:
    data=f.read()
    print(data)
    
    
with open("demo.py","w") as f:
    f.write("Anshika is a ugly girl")
    
    
import os
os.remove("demo.txt")
    