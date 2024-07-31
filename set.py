collection = {1,2,2,2,2,3,4,"hello","hello","world"}

print(collection)
print(type(collection)) #total number of items
print(len(collection))  #length of sets

set = set() #empty dictionary
print(type(set))


#Set Method

#add element
set.add(3)
set.add(6)
set.add(9)
set.add("Anshika")
set.add((1,2,3,4))

#removes the element
set.remove(6)

#empties the set
set.clear()
print(len(set))

#remove a random value
collect = {"hello","college","munisha",1,3,4}
collect.pop()
print(collect)

#combines both values & returns new
set1 = {1,2,3,4}
set2 = {4,5,6,7}
print(set1.union(set2))

#combines common values & returns new 
print(set1.intersection(set2))

