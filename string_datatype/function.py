# replace(old_value, new_value) 

s = "we are here to learn c++, it is a high level lang"
print(s)

s1=s.replace("c++","python")
s2=s.replace('a','b',2)
s3=s.replace(s,"new")
print(s1)
print(s2)

#Issplit() ---->return value wil get in list by default it split by space
s="we are here to learn c++, it is a high level lang"
s1=s.split()
print(s1)

s2=s.split('a')
print(s2)

s3=s.split("here")
print(s3)


#join() ---> return string (all element will be string otherwise it give error if you want to add something so write in "")
#it also pass tuple
lis = ["apple", "banana","pineapple","orange"]
lis2=["aplle","cherry"]
s=" ".join(lis) + " "+" ".join(lis2)
print(s)


#Q 
s="its now or never"
print(s)

s=s.split()
print(s) #['its', 'now', 'or', 'never']
a=s[0][::-1]
b=s[1][::-1]
c=s[2][::-1]
d=s[3][::-1]
s=[a,b,c,d]
print(s) #['sti', 'won', 'ro', 'reven']











