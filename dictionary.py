dict = {
    "name" :"Anshika",
    "cgpa" : 9.6,
    "marks" : [98,97,95],
    "age" : 35,
    "is_adult" : True
}

null_dict = {}
null_dict["name"] = "apnacollege"
print(null_dict)

print(dict["name"])
dict["name"] = "Shradha" #overwrite
dict["age"] = "19"
print(dict)

#Nested Dictionary
student = {
    "name": "rahul kumar",
    "score" : {
        "chem " : 98,
        "phy" : 97,
        "math" : 95,
    }
}

print(student)
print(student["score"]["math"])