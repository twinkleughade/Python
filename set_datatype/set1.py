s1 = {1,2,3,3,4,9,11,17}
s2={4,5,9,17,89}
s3={"a","b",1,2,3,88}

print(s1)

#union
r = s1.union(s2)
print(r)
r = s1.intersection(s2)
print(r)
r = s1.union(s2,s3)
print(r)
r=s1.intersection(s2,s3)
print(r)

#symbol - pipeline for union
r = s1|s2|s3  
print(r)

#symbol - & empercent for intersection
r= s1&s2&s3
print(r)


#set difference
r = s1.difference(s2)
print(r)

r = s1 - s2
print(r)

r= s2.difference(s3)
print(r)

r= s1.difference(s2,s3)
print(r)

r = s2 -s1
print(r)
