
#             0             1
#lis = [["ajay", "aman"], (45,56)]
#         0        1       0  1

#print(type(lis))

#lis[1][0] =99  
#lis.pop()
#print(lis)

t = (34,45,[3,4,555])
print(t)
t[2][1]=9999
print(t)
t[2].append(444)
print(t)

lis = [["ajay", "aman"], (45,56,[45,34])]
lis[1][2][0]=24
print(lis)

t = (4, 5, 7, 8 ,9)
a=t.count(5)
print(a)

#sorted()  -----return sorted list

t = (4,89,34,34)
a=sorted(t)
print(a)

#if there is only single element so we have to put , after the object otherwise it will show integer,string etc. typ

#t = (23)  # int
t = (23,)  #tuple
print(type(t))

#t1=("abcd")  #string
t1=("abcd",)  #tuple
print(type(t1))

t2=1,2,3,3,4  #function(tuple)
print(type(t2))

#empty tuple
t = ()
#empty tuple
t1 = tuple()
print(t,t1)

records = ("ajay", 191, 34, 5555232345)
print(records)
records = list(records)   #convert in list
records[3], records[0]=565, "twinkle"   #we can change multiple changes in tuple 
print(records)
records = tuple(records)   #convert in tuple
print(records)

a=3
b=6
print(a,b)
a,b =23,56
print(a,b)


