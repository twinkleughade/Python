s1 = {1,2,3,3,4,9,11,17}
s2={4,5,9,17,89}

s1.update(s2)
print(s1)

# difference between union and update
#  change in existing set in update and in union it gave another set 

#add function
s1.add(988)
print(s1)

s1.add(2)
print(s1) #it can not add  bcoz it already exsit in 

s1.add((2,3)) # it is tuple so it can add
print(s1)

s1.add([2,3]) # it is list so it can not work in add
print(s1)

s1.update((2,3,56)) # it can add new value not same
print(s1)

s1.update([2,3,56]) # it can add new value not same you can send list in update 
print(s1)

