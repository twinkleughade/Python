#------------------             positional argument              -------------------------
# def add (x,y,z):
#     z=x+y+z
#     #print(z)  it give output but also shows None
#     return z   
# p=int(input("enter 1st value"))
# q=int(input("enter 2nd value"))
# r=int(input("enter 3rd value"))
# #x=add(p,q,r,s) it shows there is extra value
# x=add(p,q,r)
# print(x)
 
#-----------------             keyword argument           -----------------------
# def add (x,y,z):
#     z=x+y+z
#     #print(z)  it give output but also shows None
#     return z   
# p=int(input("enter 1st value"))
# q=int(input("enter 2nd value"))
# r=int(input("enter 3rd value"))
# #x=add(p,q,r,s) it shows there is extra value
# x=add(y=r,x=p,z=q)
# print(x)

#----------------------------                 default arguments          ------------------------------
# def square(x=0):
#     print("the square of",x,"is",x*x)
# square(x=4)
# square()

#----------------------------            variable lenght argument (* args)     ------------------------

# def add(*n):
#     print(n)
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
# var=add(10,20,30,40,50,60)
# print(var)

#---------------------------        eval          ---------------------
# x=eval(input("Enter any value"))
# print(type(x))

#------------------------------     keyword variable lenght argument(** kwargs)    -----------------------
# def show(** kwargs):  # we can take different variable replace of kwargs
#     print(kwargs)
#     for i,j in kwargs.items():
#         print(i,"=",j)
# show(name='twinkle', age=26, qualification="BE")

# -------------                         scope         ---------------------
# x=10                           #global  it is a keyword
# def show():
#     global y                   # if we want to show y outside the blck we use global local to global
#     y=20                       #local
#     print(x)
#     print(y)
# show()
# print(x)
# print(y)

# x=10
# def show():
#     x=50
#     print(x)
#     print(globals()['x'])    #globals is a inbult method to take global value in place of local
# show()
# print(x)














