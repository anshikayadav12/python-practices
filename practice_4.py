#Question 01
python={} 
print(type(python))
python.update({"table":"a pieceof furniture","table":"list of facts & figures"})
python.update({"cat":"a small animal"})
print(python)

#Question 02
subjects = {
    "python","java","c++","python","javascript","java",
    "python","java","c++","c" 
}
print(len(subjects))

#Question 03
dict ={
    
    
}
b = input("Enter phy marks:")
dict.update({"Phy":b})
b = input("Enter Science marks:")
dict.update({"Science":b})
b = input("Enter Maths marks:")
dict.update({"Maths":b})


print(dict)

#Question 04
set = {9,"9.0"}
set1 = {("float",9.0),("int",9)}
print(set)
print(set1)