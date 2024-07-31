dict = {
    "name" :"Anshika",
    "cgpa" : 9.6,
    "marks" : [98,97,95],
    "age" : 35,
    "is_adult" : True
}

print(list(dict.keys())) #return all keys
print(dict.values()) #return all values 
print(dict.items()) # return all(key,val) pairs as tuples

print(dict.get("key")) #returns the key according to value 
dict.update({"city" : "delhi"}) #insert the specific items to the dictionary
print(dict)